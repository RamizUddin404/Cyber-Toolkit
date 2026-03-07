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
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] Whois Domain Information\033[0m")
        domain = input("\nEnter Domain (or '0' to exit): ")
        if domain == '0': break
        try:
            r = requests.get(f"https://networkcalc.com/api/dns/lookup/{domain}")
            print("\033[1;32m[*] ", end=""); print(r.text)
        except: print("\033[1;32m[*] ", end=""); print("[!] Error fetching data.")
        input("\n[Press Enter to Lookup Another]")
if __name__ == "__main__": run()
