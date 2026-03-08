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
cyber_deps.ensure_deps(system_pkgs=["nikto"])

def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] Web Vulnerability Scanner (Nikto)\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Start Scan")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall Nikto (Remove)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nNikto > ")
        if c == '0': break
        if c == '99':
            cyber_deps.remove_deps(system_pkgs=["nikto"])
            break
        
        target = input("Enter Website (URL): ")
        if target: os.system(f"nikto -h {target}")
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
