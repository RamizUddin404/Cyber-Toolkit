# CREATED BY: RAMIZ UDDIN
import os, cyber_deps
cyber_deps.ensure_deps(system_pkgs=["nmap"])
def run():
    while True:
        os.system("clear")
        print("\033[1;36m" + "="*45)
        print("      ADVANCED NMAP SCANNER")
        print("      CREATED BY: RAMIZ UDDIN")
        print("="*45 + "\033[0m")
        print("\033[1;32m[1] Fast Scan")
        print("[2] OS Detection")
        print("[3] Aggressive Scan")
        print("[99] Uninstall Nmap")
        print("[0] Back\033[0m")
        c = input("\nNmap > ")
        if c == '0': break
        if c == '99': import cyber_deps; cyber_deps.remove_deps(["nmap"]); break
        target = input("\033[1;33mEnter Target IP/URL: \033[0m")
        if c == '1': os.system(f"nmap -F {target}")
        elif c == '2': os.system(f"nmap -O {target}")
        elif c == '3': os.system(f"nmap -A {target}")
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
