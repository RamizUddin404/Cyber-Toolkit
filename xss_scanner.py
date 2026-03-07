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
        print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[*] XSS Vulnerability Scanner\033[0m")
        url = input("\nEnter URL with param (e.g. http://site.com/search?q=) (or '0' to exit): ")
        if url == '0': break
        payload = "<script>alert('XSS')</script>"
        try:
            if payload in requests.get(url + payload).text:
                print("\033[1;32m[*] ", end=""); print("\033[1;31m[+] VULNERABLE TO XSS!\033[0m")
            else: print("\033[1;32m[*] ", end=""); print("[-] Not vulnerable to simple XSS.")
        except: print("\033[1;32m[*] ", end=""); print("[!] Connection Error.")
        input("\n[Press Enter to Scan Another]")
if __name__ == "__main__": run()
