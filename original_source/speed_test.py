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
cyber_deps.ensure_deps(python_mods=["speedtest-cli"])
def run():
    print("\033[1;32m[*] ", end=""); print("[*] Speed Test")
    if input("Run? ") == "99": import cyber_deps; cyber_deps.remove_deps(); return
    os.system("speedtest-cli --simple")
    input("[Enter]")
if __name__=="__main__": run()