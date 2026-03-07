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
cyber_deps.ensure_deps(system_pkgs=["searchsploit"])
import os
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[*] Searchsploit: Official Exploit Database Lookup\033[0m")
        query = input("\nEnter software/vulnerability name (e.g. wordpress 5.0) (or '0' to exit): ")
        if query == '0': break
        os.system(f"searchsploit {query}")
        input("\n[Press Enter to Search Another]")
if __name__ == "__main__": run()
