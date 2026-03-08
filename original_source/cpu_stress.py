# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import time
def run():
    print("\033[1;32m[*] ", end=""); print("[*] CPU Stress Test (5s)")
    if input("Start? ") == "99": import cyber_deps; cyber_deps.remove_deps(); return
    t = time.time() + 5
    while time.time() < t: x = 2**2
    print("\033[1;32m[*] ", end=""); print("Done")
    input("[Enter]")
if __name__=="__main__": run()