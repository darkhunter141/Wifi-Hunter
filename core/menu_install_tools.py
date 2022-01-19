import os
from banner import banners
def option(option_name, option_no):
    custom_option = f"\n\033[91m [\033[00m{option_no}\033[91m] \033[93m{option_name}"
    print(custom_option)


def menu():
    print("\n\n\033[91m Choose an option : ")
    option('Wifte', 1)
    option('Aircrack-ng', 2)
    option('Reaver', 3)
    option('Pixiewps', 4)
    option('Wireshark', 5)
    option('Wash', 6)
    option("Macchanger", 7)
    option("Cowpatty", 8)
    option("Bully", 9)
    option("Mdk3", 10)


def choice_intall_tools():
    option = input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > ")
    print()
    if option == "y":
        print("\033[91m[\033[00m*\033[91m] apt update...\033[00m")
        os.system("sudo apt-get update")
        print("\033[91m[\033[00m*\033[91m] Installing pixiewps...\033[00m")
        os.system("sudo apt-get install -y pixiewps")
        print("\033[91m[\033[00m*\033[91m] Installing reaver...\033[00m")
        os.system("sudo apt install reaver -y")
        print("\033[91m[\033[00m*\033[91m]Installing wifite...\033[00m")
        os.system("sudo apt install wifite -y")
        print("\033[91m[\033[00m*\033[91m] Installing aircrack-ng...\033[00m")
        os.system("sudo apt install aircrack-ng -y")
        print("\033[91m[\033[00m*\033[91m] Installing wireshark...\033[00m")
        os.system("sudo apt install wireshark -y")
        print("\033[91m[\033[00m*\033[91m] Installing macchanger...\033[00m")
        os.system("sudo apt install macchanger")
        print("\033[91m[\033[00m*\033[91m] Installing cowpatty...\033[00m")
        os.system("sudo apt-get install cowpatty")
        print("\033[91m[\033[00m*\033[91m] Installing bully...\033[00m")
        os.system("sudo apt-get install bully")
        print("\033[91m[\033[00m*\033[91m] Installing mdk3..\033[00m")
        os.system("sudo apt-get install mdk3")
        os.system("sudo apt install net-tools")
        print("\n\n Done")
        print("\n\033[91m Back home (y/n) ")
        option = input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > ")
        if option == "y":
            os.system('python3 main.py')
        else:
            print("\033[91m Wrong try again!")
            print('\033[00m run sudo main.py\n\n\n')

    else:
        os.system("clear")
        print("\033[91m Wrong try again!")
        print('\033[00m run sudo main.py\n\n\n')


banners()
menu()
print("\n\033[91m[\033[00m*\033[91m]\033[91m Install all tools (y/n) ")
choice_intall_tools()
