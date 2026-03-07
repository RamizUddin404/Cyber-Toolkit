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
cyber_deps.ensure_deps(system_pkgs=["wget"])
import os
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;36m[*] Website Cloner (Downloader)\033[0m")
        url = input("\nEnter Website URL (or '0' to exit): ")
        if url == '0': break
        print("\033[1;32m[*] ", end=""); print(f"[*] Cloning {url}...")
        os.system(f"wget --mirror --convert-links --adjust-extension --page-requisites --no-parent {url}")
        print("\033[1;32m[*] ", end=""); print("[+] Cloning complete.")
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
