import random, os

welc = ['''
______          _   _   _ _
| ___ \        | | | | | (_)
| |_/ ___  _ __| |_| | | |_  _____      _____ _ __
|  __/ _ \| '__| __| | | | |/ _ \ \ /\ / / _ | '__|
| | | (_) | |  | |_\ \_/ | |  __/\ V  V |  __| |
\_|  \___/|_|   \__|\___/|_|\___| \_/\_/ \___|_|
''',
'''
   ___           _         _
  / _ \___  _ __| |_/\   /(_) _____      _____ _ __
 / /_)/ _ \| '__| __\ \ / | |/ _ \ \ /\ / / _ | '__|
/ ___| (_) | |  | |_ \ V /| |  __/\ V  V |  __| |
\/    \___/|_|   \__| \_/ |_|\___| \_/\_/ \___|_|
''',
'''
 _____         _   _____ _
|  _  |___ ___| |_|  |  |_|___ _ _ _ ___ ___
|   __| . |  _|  _|  |  | | -_| | | | -_|  _|
|__|  |___|_| |_|  \___/|_|___|_____|___|_|
''',
'''
██████╗ ██████╗██████╗██████████╗   █████████████╗    ███████████████╗
██╔══████╔═══████╔══██╚══██╔══██║   ██████╔════██║    ████╔════██╔══██╗
██████╔██║   ████████╔╝  ██║  ██║   █████████╗ ██║ █╗ ███████╗ ██████╔╝
██╔═══╝██║   ████╔══██╗  ██║  ╚██╗ ██╔████╔══╝ ██║███╗████╔══╝ ██╔══██╗
██║    ╚██████╔██║  ██║  ██║   ╚████╔╝█████████╚███╔███╔█████████║  ██║
╚═╝     ╚═════╝╚═╝  ╚═╝  ╚═╝    ╚═══╝ ╚═╚══════╝╚══╝╚══╝╚══════╚═╝  ╚═╝
''',
'''
 ______            __   ___ ___ __
|   __ .-----.----|  |_|   |   |__.-----.--.--.--.-----.----.
|    __|  _  |   _|   _|   |   |  |  -__|  |  |  |  -__|   _|
|___|  |_____|__| |____|\_____/|__|_____|________|_____|__|
''',
'''
 ___             _   _   _
(  _`\          ( )_( ) ( )_
| |_) ) _   _ __| ,_| | | (_)  __  _   _   _   __  _ __
| ,__//'_`\( '__| | | | | | |/'__`( ) ( ) ( )/'__`( '__)
| |  ( (_) | |  | |_| \_/ | (  ___| \_/ \_/ (  ___| |
(_)  `\___/(_)  `\__`\___/(_`\____`\___x___/`\____(_)
''']

def menu():
    print('''
"1"--displays all ports listening TCP and UDP connections in numerical format
"2"--scan all open/listening ports (it will take a long time for its execution)(Linux)
"3"--find out which application is listening on a specific port
"4"--output of all open ports
"5"--to kill any process
"6"-- +extra options(For windows)
"0"--exit
    ''')

def menu_2():
    print('''
"7"--open port for server(Minecraft(recommended))
"9"--go back
    ''')

first = 'sudo ss -lntu'
second = 'sudo nmap -n -PN -sT -sU -p- localhost'
thr = 'sudo lsof -i :'
fou = 'sudo netstat -ltup'
fif = 'kill $(lsof -t -i:'
########
def main():
    user  = input(">>")
    if user == "1":
        try:
            os.system('netstat -an |find /i "listening"')
        except:
            os.system(first)
    elif user == "2":
        try:
            os.system('netstat /a /o')
        except:
            os.system(second)
    elif user == "3":
        port = input("Enter port:")
        try:
            os.system('netstat -ano | findstr :' + port)
        except:
            os.system(thr + port)
    elif user == "4":
        try:
            os.system('netstat -a')
        except:
            os.system(fou)
    elif user == "5":
        killport = input("Enter port:")
        try:
            os.system('taskkill /PID ' + killport + ' /F')
        except:
            os.system(fif + killport + ")")
    ###########
    elif user == "6":
        menu_2()
        while 7:
            userplus = input(">>>")
            if userplus == "7":
                minecraftport = input("Enter port:")
                os.system('netsh advfirewall firewall add rule name=L2TP_TCP protocol=TCP localport=' + minecraftport + ' action=allow dir=IN')
            elif userplus == "9":
                os.system('cls')
                start()
            else:
                print("Oops,try again")
    ############
    elif user == "0":
        exit()
    else:
        print("Oops,try again")
########
def start():
    menu()
    while 69:
        main()

print(random.choice(welc))
start()
