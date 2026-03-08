# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import cyber_deps
cyber_deps.ensure_deps(python_mods=["requests"])
import requests
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[*] Social Media Recon (OSINT Tool)\033[0m")
        user = input("\nEnter Username to Search (or '0' to exit): ")
        if user == '0': break
        
        platforms = {
            "Facebook": f"https://www.facebook.com/{user}",
            "Instagram": f"https://www.instagram.com/{user}",
            "Twitter": f"https://twitter.com/{user}",
            "GitHub": f"https://github.com/{user}",
            "TikTok": f"https://www.tiktok.com/@{user}"
        }
        for name, url in platforms.items():
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200: print("\033[1;32m[*] ", end=""); print(f"[+] {name}: Found! -> {url}")
                else: print("\033[1;32m[*] ", end=""); print(f"[-] {name}: Not Found")
            except: print("\033[1;32m[*] ", end=""); print(f"[!] {name}: Error checking")
        input("\n[Press Enter to Search Again]")
if __name__ == "__main__": run()
