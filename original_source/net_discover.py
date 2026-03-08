# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import cyber_deps
cyber_deps.ensure_deps(system_pkgs=["netdiscover"])
import os
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] Network Host Discovery (Netdiscover)\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Scan Local Network")
        print("\033[1;32m[*] ", end=""); print("2. Scan Specific Range")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nNetdiscover > ")
        if c == '0': break
        
        if c == '1': os.system("sudo netdiscover" if os.geteuid() != 0 else "netdiscover")
        elif c == '2':
            r = input("Enter Range (e.g. 192.168.1.0/24): ")
            os.system(f"sudo netdiscover -r {r}" if os.geteuid() != 0 else f"netdiscover -r {r}")
        
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
