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
import subprocess
import shutil

# List of packages that we usually install via cyber_deps
PKG_LIST = [
    "termux-api", "bluez", "wireshark", "metasploit", "p7zip", 
    "nmap", "hydra", "sqlmap", "nikto", "proxychains-ng", 
    "tor", "jq", "zbar", "adb", "fastboot", "sherlock", "dsniff"
]

# List of python modules
PY_MODS = ["requests", "pillow", "scapy", "beautifulsoup4", "colorama"]

def header():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;35m========================================\033[0m")
    print("\033[1;32m[*] ", end=""); print("      MASTER UNINSTALLER & OPTIMIZER")
    print("\033[1;32m[*] ", end=""); print("\033[1;35m========================================\033[0m")

def uninstall_pkgs():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[*] Uninstalling System Packages...\033[0m")
    for pkg in PKG_LIST:
        print("\033[1;32m[*] ", end=""); print(f"[-] Removing {pkg}...", end="\r")
        os.system(f"pkg uninstall {pkg} -y > /dev/null 2>&1")
    print("\033[1;32m[*] ", end=""); print("\n[+] All system packages removed.")

def uninstall_python():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[*] Uninstalling Python Modules...\033[0m")
    for mod in PY_MODS:
        print("\033[1;32m[*] ", end=""); print(f"[-] Removing {mod}...", end="\r")
        os.system(f"pip uninstall {mod} -y > /dev/null 2>&1")
    print("\033[1;32m[*] ", end=""); print("\n[+] All python modules removed.")

def remove_tools():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[*] Removing Cloned Tools & Folders...\033[0m")
    folders = ["setoolkit", "nikto", "__pycache__"]
    for folder in folders:
        path = os.path.join(os.path.expanduser("~"), folder)
        if os.path.exists(path):
            print("\033[1;32m[*] ", end=""); print(f"[-] Deleting {path}...")
            shutil.rmtree(path, ignore_errors=True)
        # Also check current dir
        if os.path.exists(folder):
            shutil.rmtree(folder, ignore_errors=True)
    print("\033[1;32m[*] ", end=""); print("[+] Cloned tools removed.")

def run():
    while True:
        os.system("clear")
        header()
        print("\033[1;32m[*] ", end=""); print("1. Optimize Termux (Clean Cache/Temp)")
        print("\033[1;32m[*] ", end=""); print("2. Uninstall All System Packages (Un-hack)")
        print("\033[1;32m[*] ", end=""); print("3. Uninstall All Python Modules")
        print("\033[1;32m[*] ", end=""); print("4. Remove Cloned Folders (SET, Nikto, etc.)")
        print("\033[1;32m[*] ", end=""); print("5. FULL CLEANUP (Reset All)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nManager > ")
        if c == '0': break
        
        if c == '1':
            print("\033[1;32m[*] ", end=""); print("[*] Cleaning up...")
            os.system("pkg clean && apt autoremove -y")
            os.system("rm -rf ~/.cache/*")
            print("\033[1;32m[*] ", end=""); print("[+] Storage optimized.")
        elif c == '2':
            if input("[!] Confirm Package Removal? (y/n): ") == 'y':
                uninstall_pkgs()
        elif c == '3':
            if input("[!] Confirm Python Module Removal? (y/n): ") == 'y':
                uninstall_python()
        elif c == '4':
            remove_tools()
        elif c == '5':
            if input("\033[1;31m[!!!] WARNING: This will remove EVERYTHING. Continue? (y/n): \033[0m") == 'y':
                uninstall_pkgs()
                uninstall_python()
                remove_tools()
                print("\033[1;32m[*] ", end=""); print("\n[+] System is now Clean.")
                
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
