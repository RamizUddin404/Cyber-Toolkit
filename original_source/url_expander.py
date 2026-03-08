# CREATED BY: RAMIZ UDDIN
import os, sys, time, requests

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("URL EXPANDER (ANTI-PHISH)")
    print("\033[1;32m[*] Reveal the real destination of shortened links safely.\033[0m")
    
    url = input("\n\033[1;33mEnter Shortened URL: \033[0m")
    if not url.startswith('http'): url = 'http://' + url
    
    print("\n\033[1;32m[*] Expanding URL...\033[0m")
    try:
        r = requests.head(url, allow_redirects=True, timeout=10)
        print("\033[1;36m" + "─" * 45)
        print(f"  Short URL  : {url}")
        print(f"  Destination: {r.url}")
        print(f"  Status Code: {r.status_code}")
        print("─" * 45 + "\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Error: {str(e)}\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
