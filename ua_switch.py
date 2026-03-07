# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import random
def run():
    print("\033[1;32m[*] ", end=""); print("[*] User-Agent Gen")
    if input("Gen? ") == "99": import cyber_deps; cyber_deps.remove_deps(); return
    uas = ["Mozilla/5.0 (Windows NT 10.0)", "Mozilla/5.0 (iPhone; CPU iPhone OS 14)", "Mozilla/5.0 (Linux; Android 10)"]
    print("\033[1;32m[*] ", end=""); print(random.choice(uas))
    input("[Enter]")
if __name__=="__main__": run()