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
import cyber_deps
cyber_deps.ensure_deps(system_pkgs=["tor", "proxychains-ng"])

def run():
    while True:
        os.system("clear")
        print("\033[1;32m[*] ", end=""); print("\n\033[1;35m========================================\033[0m")
        print("\033[1;32m[*] ", end=""); print("      TOR & ANONYMITY TUNNEL (GHOST)")
        print("\033[1;32m[*] ", end=""); print("\033[1;35m========================================\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Start Tor Service (Hidden IP)")
        print("\033[1;32m[*] ", end=""); print("2. Configure Proxychains (Termux)")
        print("\033[1;32m[*] ", end=""); print("3. Check My Current IP (Public)")
        print("\033[1;32m[*] ", end=""); print("4. Stop All Services")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nGhost > ")
        if c == '0': break
        
        if c == '1':
            print("\033[1;32m[*] ", end=""); print("[*] Starting Tor in background...")
            os.system("tor > /dev/null 2>&1 &")
            time.sleep(3)
            print("\033[1;32m[*] ", end=""); print("[+] Tor is now RUNNING. Use 'proxychains4' before any command.")
        elif c == '2':
            print("\033[1;32m[*] ", end=""); print("[*] Setting up Proxychains configuration...")
            # Simple setup for local tor
            os.system("echo 'socks5 127.0.0.1 9050' > ~/.proxychains.conf")
            print("\033[1;32m[*] ", end=""); print("[+] Configured: ~/proxychains.conf")
        elif c == '3':
            print("\033[1;32m[*] ", end=""); print("[*] Fetching Public IP...")
            os.system("curl -s https://ifconfig.me/ip")
        elif c == '4':
            os.system("pkill tor")
            print("\033[1;32m[*] ", end=""); print("[+] All anonymity services stopped.")
            
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
