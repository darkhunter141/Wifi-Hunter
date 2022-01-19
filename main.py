import os
import requests
import platform
username = os.getlogin()
# sudo apt install net-tools
if platform.system() == "Linux":
    pass
else:
    print("\033[91m You can't do this here :)")
    exit()
if os.geteuid() == 0:
    pass
else:
    print(
        f"\n\033[91m Hey {username}! You need root permissions to do this :)")
    print("\n \033[00mrun sudo python3 main.py\n\n\n")
    exit()
os.system("clear")
print("\033[91m[\033[00m*\033[91m] Checking tools version\n\033[00m")
database_url = "https://raw.githubusercontent.com/darkhunter141/Database/main/wifihunter_update_value.json"
version_name = requests.get(database_url).json()
v_code = version_name["version"]
with open("version") as version_hunter:
    this_version = int(version_hunter.readline())
    if this_version == v_code:
        pass
    else:
        print("\033[91m[\033[00m*\033[91m] \033[93mUpdate available !\n\033[00m")
        print("\033[91m[\033[00m*\033[91m] \033[00mPlease run python3 updatetools.py\n\n\033[00m")
        exit()
def main_option(no, name):
    print(f"\n\033[91m [\033[00m{no}\033[91m] \033[93m{name}")
from core.banner import banners
banners()
main_option(1, "Install Wireless-tools (beta)")
main_option(2, "Wifi Spam")
main_option(3, "Start monitor mode")
main_option(4, "Stop monitor mode")
main_option(0, "Exit")
option = int(input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > "))
if option == 1:
    os.system("sudo python3 core/menu_install_tools.py")
elif option == 2:
    os.system("sudo python3 core/spam_wifi.py")
elif option == 3:
    banners()
    os.system('clear')
    print('\n\n\033[92m Your interfaces : \n\033[00m')
    os.system('bash core/interface_device.sh')
    print('\n')
    print(
        "\033[91m[\033[00m*\033[91m] Type your wireless interface to start monitor mode\033[00m")
    print("\n")
    interface = input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > ")
    command = "airmon-ng start {} && airmon-ng check kill".format(interface)
    os.system(command)
    print("\n\033[91m Back home (y/n) ")
    option = input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > ")
    if option == "y":
        os.system('python3 main.py')
    else:
        os.system('clear')
        print("\033[91m Wrong try again!")
        print('\033[00m run sudo main.py\n\n\n')
elif option == 4:
    banners()
    os.system('clear')
    print('\n\n\033[92m Your interfaces : \n\033[00m')
    os.system('bash core/interface_device.sh')
    print('\n')
    print(
        "\033[91m[\033[00m*\033[91m] Type your wireless interface to stop monitor mode\033[00m")
    print("\n")
    interface = input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > ")
    command = "airmon-ng stop {} && service network-manager restart && systemctl start NetworkManager".format(
        interface)
    os.system(command)
    print("\n\033[91m Back home (y/n) ")
    option = input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > ")
    if option == "y":
        os.system('python3 main.py')
    else:
        os.system('clear')
        print("\033[91m Wrong try again!")
        print('\033[00m run sudo main.py\n\n\n')

elif option == 0:
    os.system('clear')
    print("\033[91m Wrong try again!")
    print('\033[00m run sudo main.py\n\n\n')
    exit()
else:
    os.system('clear')
    print("\033[91m Wrong try again!")
    print('\033[00m run sudo main.py\n\n\n')
    exit()
