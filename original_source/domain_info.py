# CREATED BY: RAMIZ UDDIN
import os, sys, time, socket

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("DOMAIN INFO (DNS RECON)")
    print("\033[1;32m[*] Extract DNS information from a domain name.\033[0m")
    
    domain = input("\n\033[1;33mEnter Domain Name (e.g. google.com): \033[0m").strip()
    
    print("\n\033[1;32m[*] Getting DNS Info...\033[0m")
    try:
        # Get IP
        ip = socket.gethostbyname(domain)
        print(f"\n\033[1;32m[+] IP Address : {ip}\033[0m")
        
        # In a real tool, we'd use 'dnspython' for A, MX, TXT records
        # But let's use the standard 'host' command in Linux/Termux
        print("\n\033[1;36m" + "─" * 45)
        os.system(f"host -a {domain}")
        print("─" * 45 + "\033[0m")
        
    except Exception as e:
        print(f"\033[1;31m[!] Error: {str(e)}\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
