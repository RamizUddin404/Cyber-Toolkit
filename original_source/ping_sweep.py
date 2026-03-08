# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import os
def run():
    print("\033[1;32m[*] ", end=""); print("\n[*] Ping Sweep")
    base = input("Subnet (e.g. 192.168.1): ")
    if base=="99": import cyber_deps; cyber_deps.remove_deps(); return
    print("\033[1;32m[*] ", end=""); print("Scanning...")
    for i in range(1, 20):
        ip = f"{base}.{i}"
        res = os.system(f"ping -c 1 -W 1 {ip} >/dev/null")
        if res == 0: print("\033[1;32m[*] ", end=""); print(f"[+] {ip} is UP")
    input("[Enter]")
if __name__=="__main__": run()