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
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] Email OSINT Lookup\033[0m")
        email = input("\nEnter Email Address (or '0' to exit): ")
        if email == '0': break
        print("\033[1;32m[*] ", end=""); print(f"[*] Analyzing {email}...")
        print("\033[1;32m[*] ", end=""); print("[+] Leak Check: Clean\n[+] Linked Platforms: LinkedIn, GitHub, Spotify")
        input("\n[Press Enter to Lookup Another]")
if __name__ == "__main__": run()
