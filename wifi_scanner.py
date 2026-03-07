# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import os
import cyber_deps
# airmon-ng is part of aircrack-ng
cyber_deps.ensure_deps(system_pkgs=["aircrack-ng"])

def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[*] WiFi Security Scanner (Root Required)\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Check Monitor Mode")
        print("\033[1;32m[*] ", end=""); print("2. Scan Networks (airodump)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall WiFi Tools")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nWiFi > ")
        if c == '0': break
        if c == '99':
            cyber_deps.remove_deps(system_pkgs=["aircrack-ng"])
            break
        if c == '1': os.system("sudo airmon-ng")
        elif c == '2': os.system("sudo airodump-ng wlan0")
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
