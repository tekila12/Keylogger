# Keylogger



A keylogger  built for educational purposes to demonstrate system programming, networking, and ethical hacking. Runs invisibly on Windows, captures keystrokes in real-time, and logs all activity to a Linux listener. Developed as part of a cybersecurity portfolio, showcasing skills honed through Hack The Box challenges.

**⚠️ Ethical Disclaimer**: For educational use only in authorized environments (e.g., personal VMs). Unauthorized use is illegal and unethical. Use responsibly to learn cybersecurity concepts.

## Demo Video
Watch the keylogger in action: [Demo Video](https://drive.google.com/file/d/1Y6MSUbnZyN2-xrn3Nvh0S-c0WZszP5kR/view?usp=sharing).
## Features
- **Silent Execution**: Runs without a console window on Windows using `ctypes`.
- **System-Wide Keylogging**: Captures all keystrokes (requires admin privileges).
- **Real-Time Logging**: Sends keystrokes instantly to the Linux listener via TCP socket.
- **Command Support**: Handles `get_logs` for full keystroke history, `dir`, `whoami`, and `exit`.
- **No Local Logs**: Stores data in memory for stealth, with no files saved on the target.
- **Persistent Logging**: Saves all keystrokes and command outputs to `~/keylogger_received_logs.txt` on the listener.
- **Packaged Executable**: Bundles `keyboard` module in a password-protected `keylogger.exe`.

## Files
- `keylogger.py`: Windows keylogger script (captures and sends keystrokes).
- `listener.py`: Linux listener script (receives and logs data).
- `keylogger_icon.png`: Portfolio icon (keyboard with network signal).


## Process
1. **Setup**:
   - **Windows VM (`x.x.x.x`)**:
     - Install dependencies: `pip install keyboard pyinstaller`.
     - Update `LISTENER_IP` in `keylogger.py` to `x.x.x.x`.
     - Compile: `pyinstaller --onefile --noconsole keylogger.py`.
   - **Linux VM (`x.x.x.x`)**:
     - Install Python: `sudo apt install python3`.
     - Save `listener.py`.
2. **Execution**:
   - Start listener: `python3 listener.py` (listens on `0.0.0.0:4444`).
   - Run keylogger as admin: `Start-Process .\dist\keylogger.exe -Verb runAs`.
   - Type in any app (e.g., Notepad, “who”).
   - Listener displays `KEYSTROKE: [2025-08-07 07:45:23] w`, etc., and logs to `~/keylogger_received_logs.txt`.
3. **Commands**:
   - Send `dir` or `whoami` to execute shell commands.
   - Send `get_logs` to retrieve all keystrokes.
   - Send `exit` or press `Ctrl+C` to close.
4. **Output**:
   - Logs (`~/keylogger_received_logs.txt`) include connection events, keystrokes, command outputs, and sent commands, without duplicates from `get_logs`.

## Installation
1. **Windows VM**:
   ```bash
   pip install keyboard pyinstaller
   ```
2. **Linux VM**:
   ```bash
   sudo apt install python3
   ```
3. Update `LISTENER_IP` in `keylogger.py` to your Linux VM IP (e.g., `x.x.x.x`).

## Packaging
```bash
pyinstaller --onefile --noconsole keylogger.py
```


## Usage
1. Start listener on Linux:
   ```bash
   python3 listener.py
   ```
2. Run keylogger on Windows:
   ```bash
   .\dist\keylogger.exe 
   ```
3. Type in any app; keystrokes are logged in real-time to `~/keylogger_received_logs.txt`.
4. Send commands (`whoami`, `dir`, `get_logs`, `exit`).
5. Exit with `Ctrl+C` or `exit` command.

## Example Output
```
Listening on 0.0.0.0:4444...
Connection from ('x.x.x.x', 50499)
[*] Connected from Windows
KEYSTROKE: [2025-08-07 07:45:23] w
KEYSTROKE: [2025-08-07 07:45:24] h
KEYSTROKE: [2025-08-07 07:45:24] o
> dir
Sent command: dir
Volume in drive C has no label...
> whoami
Sent command: whoami
desktop-3ckfkt3\ajnur
> get_logs
Sent command: get_logs
[*] Logs:
LOG: [2025-08-07 07:45:23] w
LOG: [2025-08-07 07:45:24] h
LOG: [2025-08-07 07:45:24] o
> exit
Sent command: exit
Connection closed from ('x.x.x.x', 50499)
```
Logs in `~/keylogger_received_logs.txt`:
```
[2025-08-07 07:45:00] Listening on 0.0.0.0:4444
[2025-08-07 07:45:01] Connection from ('x.x.x.x', 50499)
[2025-08-07 07:45:01] [*] Connected from Windows
[2025-08-07 07:45:23] KEYSTROKE: [2025-08-07 07:45:23] w
[2025-08-07 07:45:24] KEYSTROKE: [2025-08-07 07:45:24] h
[2025-08-07 07:45:24] KEYSTROKE: [2025-08-07 07:45:24] o
[2025-08-07 07:45:30] Sent command: dir
[2025-08-07 07:45:30] Volume in drive C has no label...
[2025-08-07 07:45:35] Sent command: whoami
[2025-08-07 07:45:35] desktop-3ckfkt3\ajnur
[2025-08-07 07:45:40] Sent command: get_logs
[2025-08-07 07:45:45] Sent command: exit
[2025-08-07 07:45:45] Connection closed from ('x.x.x.x', 50499)
```

## Notes

- `keyboard` module is bundled in `keylogger.exe`.
- Video demonstrates setup, execution, and logging.

