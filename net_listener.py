# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import os, cyber_deps
cyber_deps.ensure_deps(system_pkgs=["netcat"])
def run():
    print("\033[1;32m[*] ", end=""); print("\n[*] Port Listener (Netcat)")
    p = input("Port: ")
    if p=="99": import cyber_deps; cyber_deps.remove_deps(); return
    os.system(f"nc -lvp {p}")
if __name__=="__main__": run()