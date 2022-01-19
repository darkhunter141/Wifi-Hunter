import requests,os
os.system("clear")
database_url = "https://raw.githubusercontent.com/darkhunter141/Database/main/wifihunter_update_value.json"
version_name = requests.get(database_url).json()
v_code = version_name["version"]
print("\033[91m[\033[00m*\033[91m] Checking tools version....\n\033[00m")
with open("version") as version_hunter :
    this_version = int(version_hunter.readline())
    if this_version == v_code:
        print("\033[91m[\033[00m*\033[91m] \033[92mAll files up to date !\n\033[00m")
        print("\033[91m[\033[00m*\033[91m] \033[00mrun python3 main.py\n\033[00m")
    elif this_version != v_code:
        print("\033[91m[\033[00m*\033[91m] \033[95mDownloading files....\n\033[00m")
        
        os.remove("main.py")
        os.remove("version")
        os.system("rm -rf core")
        os.system("wget https://github.com/ashrafiabir01/wifihunter_update_zip/raw/main/wifihunter_update.zip")
        os.system("unzip wifihunter_update.zip")
        os.system("rm -rf wifihunter_update.zip")
        print("\n\033[91m[\033[00m*\033[91m] \033[95mUpdate Done\n\033[00m")
        print("\033[91m[\033[00m*\033[91m] \033[00mrun python3 main.py\n\033[00m")
    else:
        print("\033[91m[\033[00m*\033[91m] \033[91mSomething wrong!\n\033[00m")
        