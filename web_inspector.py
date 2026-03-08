# CREATED BY: RAMIZ UDDIN
import os, time, requests

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("WEB INSPECTOR (HEADERS SCAN)")
    print("\033[1;32m[*] Analyze website headers and security configurations.\033[0m")
    
    url = input("\n\033[1;33mEnter Website (e.g. google.com): \033[0m").strip()
    if url:
        if not url.startswith("http"): url = "http://" + url
        print(f"\n\033[1;32m[*] Inspecting {url}...\033[0m")
        try:
            r = requests.get(url, timeout=10)
            print("\n\033[1;36m[ SERVER HEADERS ]\033[0m")
            for k, v in r.headers.items():
                print(f"  {k}: {v}")
                
            print("\n\033[1;36m[ SECURITY AUDIT ]\033[0m")
            sec_h = ["X-Frame-Options", "X-XSS-Protection", "Content-Security-Policy", "Strict-Transport-Security"]
            for h in sec_h:
                if h in r.headers:
                    print(f"  \033[1;32m[+] {h}: Present\033[0m")
                else:
                    print(f"  \033[1;31m[-] {h}: Missing\033[0m")
        except Exception as e:
            print(f"\033[1;31m[!] Error: {str(e)}\033[0m")
            
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
