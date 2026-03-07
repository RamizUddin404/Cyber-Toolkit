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
cyber_deps.ensure_deps(system_pkgs=["dirsearch"])
import os
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;34m[*] Directory & URL Fuzzer (Dirsearch)\033[0m")
        target = input("\nEnter Target URL (or '0' to exit): ")
        if target == '0': break
        # Requires dirsearch (pkg install dirsearch)
        os.system(f"dirsearch -u {target}")
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
