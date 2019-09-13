# HackTheKeyboard
<h3>A tiny keylogger coded with just 15 lines of Python script, which captures keystrokes and sends them to your web server of your choice even in your Android phone with Termux.</h3>

<b>Make a Note</b>: This keylogger project is prepared for those who would like to understand the working and behaviour of keyloggers, reverse engineering the compiled version of the code to find kill-switches and build IOCs/Signatures, ethically test on systems for the purpose of Ethical Hacking/Penetration Testing such as testing the bypasses and detection by EDR, SIEM, HIPS etc.
The program should not be used for any illegal activities such as running the compiled version of this code in a user machine without his/her consent, distributing it by means of spamming/phishing campaigns etc.

<b>How stuff works?</b>

This KeyLogger uses two main packages (Keyboard and Requests)

a) Keyboard package contains pre-built classes and functions which acts as hook procedures to the system kernal using which it can intercept events, such as messages, mouse actions, and keystrokes. A package function known as read_key() runs in an infinite while loop capturing all keys into a string variable in an increamental manner upto 20 characters.

b) Once it captures all 20 keystrokes, it uses Requests package function requests.get("URL") to send the captured keystrokes string in HTTP packet using GET method into your chosen web server such as Apache. The keystrokes are stored in the webserver log as a normal HTTP GET request. The string variable is re-initialized and starts filling up again while in the loop.
 

<b>Setting up the Server</b>



<b> Editing and Compiling the Keylogger Python file</b>



 
