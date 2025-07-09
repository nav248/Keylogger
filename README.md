# Keylogger

 Project Overview:
 
This project demonstrates how a basic keylogger works using Python. It's built strictly for educational and ethical awareness purposes to help understand how keyloggers can compromise system security and how to protect against them.

 Objective:
 
To build a lightweight Python-based keylogger that logs user keystrokes and stores them in a local file.


Technologies Used:

1.Python -	Core programming language

2.pynput	- Library to monitor keyboard input


3.file I/O	- To log keystrokes into a file


How to Run:

1. Install Requirements

pip install pynput

2. Run the Keylogger

python keylogger.py

3. Stop Logging
   
Press the ESC key to stop the keylogger safely.

5. View Logs
   
Open the file keylogs.txt to view logged keystrokes.

How It Works:

Listens for every keystroke on the keyboard.

Logs normal keys (letters, numbers) and special keys (Enter, Space, etc.).

Stores each keystroke in keylogs.txt with timestamps.


Security Takeaway:

1.This tool helps users understand how malicious software might log inputs, making it easier to:

2.Detect suspicious activity

3.Educate others on the importance of password managers

4.Strengthen system security awareness
