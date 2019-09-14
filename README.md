# HackTheKeyboard
<h3>A tiny keylogger coded with just 12 lines of Python script, which captures keystrokes and sends them to your web server of your choice.</h3>

<b>First Thing First</b><br>
This keylogger project is prepared for those who would like to understand the working and behaviour of keyloggers, reverse engineer the compiled version of the code to find kill-switches and build IOCs/Signatures, ethically test on systems for the purpose of Ethical Hacking/Penetration Testing such as testing the bypasses and detection by EDR, SIEM, HIPS etc.
The program should not be used for any illegal activities such as running the compiled version of this code in a user machine without his/her consent, distributing it by means of spamming/phishing campaigns etc.

<br><br>
<b> Short working demonstration of HackTheKeyBoard </b><br>
https://www.youtube.com/watch?v=miUS2aoupD8

<br>
<b>How stuff works?</b>

This KeyLogger uses two main packages (Keyboard and Requests)

a) Keyboard package contains pre-built classes and functions which acts as hook procedures to the system kernel using which it can intercept events, such as messages, mouse actions, and keystrokes. A package function known as read_key() runs in an infinite while loop capturing all keys into a string variable in an incremental manner.

b) Once it captures all keystroke and if it finds character 'e' in the strings(the most typed keyboard character), it triggers Requests package function known as requests.get("URL") to send the captured keystroke strings via HTTP packet using GET method directly into your chosen web server such as Apache. You can prepare your server in your Termux Environment running in an Android Phone. The keystrokes are then stored in the webserver access log file as a normal HTTP GET request entries. The string variable is re-initialized and starts filling up again while in the loop.
 
<br>
<b>Setting up the Server</b><br>
Apache Webserver is highly recomended for its simplicity but you can use any webserver, given that it logs all the incomming requests into a log file.

Here is an example of setting up an environment using Android Termux

1) Install Apache Server -> `apt-get install apache2`
2) Start Apache Server -> `apachectl start`<br>
   Note: Just ignore the runtime warnings!
3) Install Open SSH -> `pkg install openssh` or `apt-get install openssh`
4) Open Reverse HTTP Tunnel to Serveo.net and wait -> `ssh -R 80:localhost:8080 serveo.net`<br>
   Note: 8080 is the default local port of apache, and port 80 will be the incomming port from Internet

<br>
<b> Editing and running the Keylogger</b><br>
Editing and compiling requires python interpreter to be installed and a suitable IDE such as PyCharm.<br>
(Rookies can just Google it online on "how to install python along with an IDE")

1) Download the Zip package of this repo and extract in your drive or run `git clone https://github.com/Sumeet-R/HackTheKeyboard` in Linux.
2) Install dependencies -> `pip3 install -r requirements.txt` or manually install the mentioned packages in requirements.txt from IDE
3) Open your IDE and import the python script, modify the variable named "host=" with the hostname displayed at 4th step of server setup.
4) Run the python code using `sudo python3 htk.py'
5) Test by typing upto 20 characters. If requests with keystrokes appears in your serveo terminal, it would mean that you have sucessfully setup the keylog server and Keylogger. You can later refer the Apache access log file located in `/var/log/apache/access_log`

<br>
<b> Compiling the Keylogger</b><br>
You can search online how to compile a keylogger based on target OS environment.
For Windows : https://pypi.org/project/auto-py-to-exe/ 



 
