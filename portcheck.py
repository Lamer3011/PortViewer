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
"2"--scan all open/listening ports (it will take a long time for its execution)(BETA)
"3"--find out which application is listening on a specific port
"4"--output of all open ports
"5"--to kill any process
"0"--exit
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
        os.system(first)
    elif user == "2":
        os.system(second)
    elif user == "3":
        port = input("Enter port:")
        os.system(thr + port)
    elif user == "4":
        os.system(fou)
    elif user == "5":
        killport = input("Enter port:")
        os.system(fif + killport + ")")
    elif user == "0":
        exit()
    else:
        print("Oops,try again")
########
print(random.choice(welc))
menu()
while 69:
    main()
