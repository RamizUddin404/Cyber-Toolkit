# CREATED BY: RAMIZ UDDIN
import os, sys, time, requests

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("XSS VULN SCANNER")
    print("\033[1;32m[*] Simple XSS vulnerability testing tool.\033[0m")
    
    url = input("\n\033[1;33mEnter Target URL (e.g. site.com/search?q=): \033[0m").strip()
    if not url.startswith('http'): url = 'http://' + url
    
    payload = "<script>alert('RAMIZ_UDDIN_XSS')</script>"
    
    print("\n\033[1;32m[*] Testing payload...\033[0m")
    try:
        r = requests.get(url + payload, timeout=10)
        if payload in r.text:
            print(f"\033[1;31m[!] POTENTIAL XSS DETECTED! Payload reflected in response.\033[0m")
        else:
            print("\033[1;32m[-] Not vulnerable (Reflection failed).\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Error: {str(e)}\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
