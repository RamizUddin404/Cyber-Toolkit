# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import socket
def run():
    h = input("Host: ")
    if h=="99": import cyber_deps; cyber_deps.remove_deps(); return
    for p in [21,22,80,443,8080]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((h,p)) == 0: print("\033[1;32m[*] ", end=""); print(f"Port {p}: OPEN")
        s.close()
    input("[Enter]")
if __name__=="__main__": run()