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
        print("\033[1;32m[*] ", end=""); print("\n\033[1;36m[*] Advanced IP Geolocation Lookup\033[0m")
        ip = input("\nEnter IP Address (or '0' to exit): ")
        if ip == '0': break
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}")
            data = r.json()
            if data['status'] == 'fail': print("\033[1;32m[*] ", end=""); print("[-] Invalid IP."); continue
            for k, v in data.items(): print("\033[1;32m[*] ", end=""); print(f"[+] {k.capitalize()}: {v}")
            print("\033[1;32m[*] ", end=""); print(f"[+] Maps: https://www.google.com/maps/place/{data['lat']},{data['lon']}")
        except: print("\033[1;32m[*] ", end=""); print("[!] Connection Error.")
        input("\n[Press Enter to Lookup Again]")
if __name__ == "__main__": run()
