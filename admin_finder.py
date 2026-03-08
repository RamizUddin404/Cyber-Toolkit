# CREATED BY: RAMIZ UDDIN
import os, sys, time, requests

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("ADMIN PANEL FINDER (WEB SCAN)")
    print("\033[1;32m[*] Scanning website for common Admin Login paths.\033[0m")
    
    url = input("\n\033[1;33mEnter Target Website (e.g. example.com): \033[0m").strip()
    if not url.startswith('http'): url = 'http://' + url
    if not url.endswith('/'): url = url + '/'
    
    paths = ['admin/', 'administrator/', 'login/', 'wp-login.php', 'admin.php', 'user/login/', 'controlpanel/', 'panel/']
    
    print("\n\033[1;32m[*] Scanning...\033[0m")
    try:
        found = False
        for path in paths:
            target = url + path
            print(f"\033[1;36m[*] Checking: {target}...", end="\r")
            r = requests.get(target, timeout=5)
            if r.status_code == 200:
                print(f"\n\033[1;32m[+] FOUND: {target}\033[0m")
                found = True
        if not found: print("\n\033[1;31m[-] No common paths found.\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[!] Error: {str(e)}\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
