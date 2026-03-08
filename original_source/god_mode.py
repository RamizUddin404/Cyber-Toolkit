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
import time

def run():
    while True:
        os.system("clear")
        print("\033[1;32m[*] ", end=""); print("\033[1;31m" + "="*45)
        print("\033[1;32m[*] ", end=""); print("      THE GOD MODE: MASTER CONTROL")
        print("\033[1;32m[*] ", end=""); print("      BRANDED FOR: RAMIZ UDDIN")
        print("\033[1;32m[*] ", end=""); print("="*45 + "\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. FULL SYSTEM UPGRADE (APT/PKG)")
        print("\033[1;32m[*] ", end=""); print("2. CLEAN ALL TEMP & CACHE FILES")
        print("\033[1;32m[*] ", end=""); print("3. PUSH UPDATES TO GITHUB (AUTO)")
        print("\033[1;32m[*] ", end=""); print("4. SYSTEM MONITOR (CPU/RAM)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall God Mode")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nGOD > ")
        if c == '0': break
        
        if c == '1':
            print("\033[1;32m[*] ", end=""); print("[*] Upgrading everything...")
            os.system("pkg update && pkg upgrade -y")
        elif c == '2':
            print("\033[1;32m[*] ", end=""); print("[*] Cleaning storage...")
            os.system("pkg clean && apt autoremove -y")
        elif c == '3':
            print("\033[1;32m[*] ", end=""); print("[*] Syncing with GitHub...")
            os.system("git add . && git commit -m 'System Update via GOD MODE' && git push origin main")
        elif c == '4':
            os.system("top -n 1")
        elif c == '99':
            print("\033[1;32m[*] ", end=""); print("[!] Removing God Mode...")
            os.remove("god_mode.py")
            break
            
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
