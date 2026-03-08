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
import sys
import shutil
import cyber_deps

def is_installed(cmd):
    return shutil.which(cmd) is not None

def header():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;34m========================================\033[0m")
    print("\033[1;32m[*] ", end=""); print("    FRAMEWORK MANAGER: TOTAL FIX v3.0")
    print("\033[1;32m[*] ", end=""); print("\033[1;34m========================================\033[0m")

def run():
    while True:
        os.system("clear")
        header()
        
        # Status
        msf = "[Installed]" if is_installed("msfconsole") else "[Not Installed]"
        rsf = "[Installed]" if is_installed("rsf") else "[Not Installed]"
        tshark = "[Installed]" if is_installed("tshark") else "[Not Installed]"
        setool = "[Installed]" if os.path.exists("setoolkit/setoolkit") else "[Not Installed]"

        print("\033[1;32m[*] ", end=""); print(f"1. Metasploit Framework      {msf}")
        print("\033[1;32m[*] ", end=""); print(f"2. Routersploit Framework    {rsf}")
        print("\033[1;32m[*] ", end=""); print(f"3. Wireshark (tshark)        {tshark}")
        print("\033[1;32m[*] ", end=""); print(f"4. Social Engineering (SET)  {setool}")
        print("\033[1;32m[*] ", end=""); print("-" * 40)
        print("\033[1;32m[*] ", end=""); print("5. Uninstall Metasploit (Deep)")
        print("\033[1;32m[*] ", end=""); print("6. Uninstall Routersploit (Force)")
        print("\033[1;32m[*] ", end=""); print("7. Uninstall Wireshark (Purge)")
        print("\033[1;32m[*] ", end=""); print("8. Uninstall SET (Delete Folder)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nSelect > ")
        if c == '0': break
        
        if c == '1':
            if not is_installed("msfconsole"): os.system("pkg install metasploit -y || ./metasploit.sh")
            else: os.system("msfconsole")
        elif c == '2':
            if not is_installed("rsf"): os.system("pip install routersploit")
            else: os.system("rsf")
        elif c == '3':
            if not is_installed("tshark"): os.system("pkg install wireshark -y")
            else: os.system("tshark")
        elif c == '4':
            if not os.path.exists("setoolkit/setoolkit"):
                os.system("git clone --depth 1 https://github.com/trustedsec/social-engineer-toolkit setoolkit")
                os.system("cd setoolkit && pip install -r requirements.txt")
            else: os.system("cd setoolkit && python3 setoolkit")
            
        elif c == '5': 
            print("\033[1;32m[*] ", end=""); print("[*] Removing MSF..."); os.system("apt purge metasploit -y >/dev/null 2>&1; rm -rf /data/data/com.termux/files/usr/opt/metasploit-framework")
        elif c == '6': 
            print("\033[1;32m[*] ", end=""); print("[*] Removing RSF..."); os.system("pip uninstall routersploit -y; rm -f $(which rsf)")
        elif c == '7': 
            print("\033[1;32m[*] ", end=""); print("[*] Purging Wireshark..."); os.system("apt purge wireshark -y >/dev/null 2>&1; pkg uninstall wireshark -y >/dev/null 2>&1")
        elif c == '8': 
            print("\033[1;32m[*] ", end=""); print("[*] Removing SET..."); os.system("rm -rf setoolkit")
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
