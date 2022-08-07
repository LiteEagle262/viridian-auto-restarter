import json,os,ctypes
from time import sleep

with open('settings.json') as f:
    config = json.load(f)

timer = config.get('restart_interval') # timer is in seconds

def restart():
    os.remove("players.txt")
    os.startfile("Viridian.ConsoleApp.exe")
    sleep(1)
    os.system(f"TASKKILL /F /IM Viridian.ConsoleApp.exe")
    print("Restarted")
    clear()

def clear():
    os.system('cls')
    banner()
    sleep(timer)
    restart()

def banner():
    ctypes.windll.kernel32.SetConsoleTitleW("Made by LiteEagle262 | liteeagle.me")
    print(f"""
            ██████╗ ███████╗███████╗████████╗ █████╗ ██████╗ ████████╗███████╗██████╗ 
            ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
            ██████╔╝█████╗  ███████╗   ██║   ███████║██████╔╝   ██║   █████╗  ██████╔╝
            ██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
            ██║  ██║███████╗███████║   ██║   ██║  ██║██║  ██║   ██║   ███████╗██║  ██║
            ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                        
                    https://github.com/LiteEagle262/viridian-auto-restarter        
                                 Timer Set to: {timer} Seconds
        """)

clear()