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

def run():
    while True:
        os.system("clear")
        print("\033[1;32m[*] ", end=""); print("\n\033[1;36m[*] ADB & FASTBOOT PRO MANAGER\033[0m")
        adb_status = "[Installed]" if cyber_deps.is_installed("adb") else "[Missing]"
        print("\033[1;32m[*] ", end=""); print(f"1. ADB/Fastboot Tools {adb_status}")
        print("\033[1;32m[*] ", end=""); print("2. ADB Shell Access")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall ADB/Fastboot Packages")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nADB Pro > ")
        if c == '0': break
        
        if c == '1':
            if not cyber_deps.is_installed("adb"): os.system("pkg install adb -y")
            os.system("adb devices")
        elif c == '2':
            os.system("adb shell")
        elif c == '99':
            print("\033[1;32m[*] ", end=""); print("[*] Removing ADB/Fastboot..."); os.system("pkg uninstall adb -y")
            
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
