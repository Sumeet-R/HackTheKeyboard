# HackTheKeyboard
<h3>A tiny keylogger coded with just 15 lines of Python script, which captures keystrokes and sends them to your web server.</h3>

<b>Warning</b>: This keylogger project is prepared for those who would like to understand working and behaviour of keyloggers, ethically test on systems for the purpose of Ethical Hacking/Penetration Testing such as testing the end-point security, SIEM, HIPS bypasses and detection etc. The program should be not be used for any illegal activities such as running the compiled version of this code in a user machine without his/her consent, distributing it by means of spamming/phishing campaigns etc.

<b>How stuff works?</b>
This KeyLogger uses two main packages (Keyboard and Requests)
Keyboard package contains pre-built classes and functions which acts as hook procedures to the system kernal using which it can intercept events, such as messages, mouse actions, and keystrokes. 
A package function known as read_key() runs in a infinite while loop capturing all keys into a string variable in an increamental manner upto 20 characters.

Once it captures the 20 keystrokes, it uses Requests package function requests.get("URL") to send the captured keystrokes string in HTTP packet using GET method towards your chosen web server such as Apache. The keystrokes are stored in the webserver log as a normal HTTP GET request.
 
 




 
