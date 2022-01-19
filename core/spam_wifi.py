import os
from banner import banners
banners()
print('\n\n\033[92m Your interfaces : \n\033[00m')
os.system('bash core/interface_device.sh')
print("\n\n")


def main_option(no, name):
    print(f"\n\033[91m [\033[00m{no}\033[91m] \033[93m{name}")


main_option(1, "Use Random SSIDS (slow)")
main_option(2, "Use custom SSIDS")
main_option(3, "Use default SSIDS")
main_option(0, "Exit")
print("\n\n\033[91m Choose an option : ")
option = int(input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > "))
print("\n\n\033[91m[\033[00m*\033[91m] Type your wireless interface name : \033[00m")
option2 = input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > ")
print("\n\n\033[91m[\033[00m*\033[91m] Turning on monitor mode\033[00m")
os.system(f"macchanger -p {option2} >> /dev/null 2>&1")
os.system("sudo airmon-ng check kill")
os.system(f"sudo airmon-ng start {option2}")
print("\n\033[91m[\033[00m*\033[91m] Starting process...\033[00m")
if option == 1:
    os.system(f"sudo mdk3 {option2} b -100 DH141")
elif option == 2:
    print("\n\n\033[91m Type File Location  : ")
    filename = input("\n\n\033[92m ͟w͟i͟f͟i͟-͟h͟u͟n͟t͟e͟r͟ > ")
    os.system(f"sudo mdk3 {option2} b -c 1 -f {filename}")
elif option == 3:
    os.system(f"sudo mdk3 {option2} b -c 1 -f core/ssid.txt")
else:
    exit()