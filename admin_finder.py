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
        print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[*] Admin Panel Finder\033[0m")
        url = input("\nEnter Website URL (or '0' to exit): ")
        if url == '0': break
        if not url.startswith("http"): url = "http://" + url
        paths = ['admin/', 'login/', 'admin.php', 'wp-admin/', 'manage/', 'controlpanel/']
        for p in paths:
            try:
                r = requests.get(f"{url}/{p}", timeout=3)
                if r.status_code == 200: print("\033[1;32m[*] ", end=""); print(f"[+] Found: {url}/{p}")
            except: pass
        input("\n[Search Finished. Press Enter]")
if __name__ == "__main__": run()
