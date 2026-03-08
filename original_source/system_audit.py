# CREATED BY: RAMIZ UDDIN
import os, time, platform

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("SYSTEM AUDIT & INFO")
    print("\033[1;32m[*] Extracting System Information...\033[0m")
    
    print(f"\n  \033[1;36mOS Type      : {platform.system()}")
    print(f"  Release      : {platform.release()}")
    print(f"  Architecture : {platform.machine()}")
    print(f"  Processor    : {platform.processor()}\033[0m")
    
    print("\n\033[1;32m[*] Checking for Root Access...\033[0m")
    if os.getuid() == 0:
        print("  \033[1;31m[!] Status: ROOTED (Full Access)\033[0m")
    else:
        print("  \033[1;32m[+] Status: NON-ROOT (User Access)\033[0m")

    print("\n\033[1;32m[*] Checking Network Interfaces...\033[0m")
    os.system("ip addr | grep 'state UP' -A2 || echo 'Could not fetch interface info'")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
