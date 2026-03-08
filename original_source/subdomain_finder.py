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
        print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[*] Subdomain Finder (Recon)\033[0m")
        domain = input("\nEnter Domain (e.g. google.com) (or '0' to exit): ")
        if domain == '0': break
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        try:
            data = requests.get(url).json()
            subs = sorted(set([entry['name_value'] for entry in data]))
            print("\033[1;32m[*] ", end=""); print(f"\n[+] Found {len(subs)} Subdomains:")
            for s in subs: print("\033[1;32m[*] ", end=""); print(f" - {s}")
        except: print("\033[1;32m[*] ", end=""); print("[-] No subdomains found or API error.")
        input("\n[Press Enter to Search Another]")
if __name__ == "__main__": run()
