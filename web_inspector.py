# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import requests

def check_headers(url):
    if not url.startswith("http"):
        url = "http://" + url
    
    try:
        print("\033[1;32m[*] ", end=""); print(f"[*] Inspecting {url}...")
        response = requests.get(url)
        headers = response.headers
        
        print("\033[1;32m[*] ", end=""); print("\n[ Server Headers ]")
        for key, value in headers.items():
            print("\033[1;32m[*] ", end=""); print(f"{key}: {value}")
            
        print("\033[1;32m[*] ", end=""); print("\n[ Security Check ]")
        security_headers = ["X-Frame-Options", "X-XSS-Protection", "Content-Security-Policy"]
        for h in security_headers:
            if h in headers:
                print("\033[1;32m[*] ", end=""); print(f"[+] {h}: Present")
            else:
                print("\033[1;32m[*] ", end=""); print(f"[-] {h}: Missing (Potential Vulnerability)")
                
    except Exception as e:
        print("\033[1;32m[*] ", end=""); print(f"[!] Error: {e}")

if __name__ == "__main__":
    target = input("Enter Website (e.g. google.com): ")
    check_headers(target)
