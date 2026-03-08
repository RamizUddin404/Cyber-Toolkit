# CREATED BY: RAMIZ UDDIN
import os, sys, time, requests

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("EMAIL SPOOF CHECKER (DNS AUDIT)")
    print("\033[1;32m[*] Check if a domain's SPF/DMARC records are misconfigured (Spoofable).\033[0m")
    
    domain = input("\n\033[1;33mEnter Domain Name (e.g. apple.com): \033[0m").strip()
    
    print("\n\033[1;32m[*] Checking DNS Records...\033[0m")
    try:
        # Check SPF
        print(f"\n\033[1;36m[*] Checking SPF Record for {domain}...\033[0m")
        os.system(f"host -t TXT {domain} | grep spf")
        
        # Check DMARC
        print(f"\n\033[1;36m[*] Checking DMARC Record for _dmarc.{domain}...\033[0m")
        os.system(f"host -t TXT _dmarc.{domain}")
        
        print("\n\033[1;33m[!] Analyze: If No SPF or DMARC is found, the domain is likely SPOOFABLE.\033[0m")
        
    except Exception as e:
        print(f"\033[1;31m[!] Error: {str(e)}\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
