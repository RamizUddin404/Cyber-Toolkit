# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import os
import time
import cyber_deps
cyber_deps.ensure_deps(python_mods=["requests"])

def run():
    while True:
        os.system("clear")
        print("\033[1;32m[*] ", end=""); print("\n\033[1;35m[*] DARK WEB SEARCH ENGINE (.onion)\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Search Ahmia (Onion Search)")
        print("\033[1;32m[*] ", end=""); print("2. Common Onion Links List")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall Dark Search")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nDarkWeb > ")
        if c == '0': break
        if c == '99': cyber_deps.remove_deps(); break
        
        if c == '1':
            query = input("Enter Search Query: ")
            print("\033[1;32m[*] ", end=""); print(f"[*] Searching for '{query}' on Dark Web...")
            # Using a public gateway for safety simulation
            url = f"https://ahmia.fi/search/?q={query}"
            print("\033[1;32m[*] ", end=""); print(f"[+] Open this link in Tor Browser: \n{url}")
            os.system(f"termux-open-url '{url}'")
        elif c == '2':
            print("\033[1;32m[*] ", end=""); print("\n[ POPULAR ONION LINKS ]")
            print("\033[1;32m[*] ", end=""); print("1. Hidden Wiki: http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion")
            print("\033[1;32m[*] ", end=""); print("2. Facebook Tor: https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion")
            print("\033[1;32m[*] ", end=""); print("3. DuckDuckGo: https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion")
        
        input("\n[Press Enter]")

if __name__ == "__main__": run()
