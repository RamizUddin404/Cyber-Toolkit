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
cyber_deps.ensure_deps(system_pkgs=["host"])
import os
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;34m[*] Advanced DNS Reconnaissance\033[0m")
        domain = input("\nEnter Domain (or '0' to exit): ")
        if domain == '0': break
        print("\033[1;32m[*] ", end=""); print(f"[*] Fetching DNS records for {domain}...")
        os.system(f"host -a {domain} || nslookup {domain}")
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
