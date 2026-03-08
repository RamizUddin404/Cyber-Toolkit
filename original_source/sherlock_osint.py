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
cyber_deps.ensure_deps(system_pkgs=["sherlock"])

def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;34m[*] Sherlock OSINT (Username Tracker)\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Search Username")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall Sherlock")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nSherlock > ")
        if c == '0': break
        if c == '99':
            cyber_deps.remove_deps(system_pkgs=["sherlock"])
            break
        
        user = input("Enter Username: ")
        if user: os.system(f"sherlock {user}")
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
