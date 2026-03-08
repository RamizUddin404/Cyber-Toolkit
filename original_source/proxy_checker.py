# CREATED BY: RAMIZ UDDIN
import os, sys, time, requests

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("PROXY CHECKER (LIVE/DEAD)")
    print("\033[1;32m[*] Check if your Proxy list contains working proxies.\033[0m")
    
    proxy_file = input("\n\033[1;33mEnter Path to Proxy List (IP:PORT): \033[0m")
    if not os.path.exists(proxy_file):
        print("\033[1;31m[!] File not found!\033[0m")
        input("\n[Press Enter]")
        return
        
    print("\n\033[1;32m[*] Checking proxies...\033[0m")
    try:
        with open(proxy_file, 'r') as f:
            for line in f:
                proxy = line.strip()
                try:
                    r = requests.get('http://google.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
                    if r.status_code == 200:
                        print(f"\n\033[1;32m[+] LIVE PROXY: {proxy}\033[0m")
                except:
                    print(f"\033[1;31m[-] DEAD PROXY: {proxy}\033[0m", end="\r")
        print("\n\033[1;33m[*] Finished checking list.\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[!] Error: {str(e)}\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
