# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import base64, os
def run():
    print("\033[1;32m[*] ", end=""); print("\n[*] Base64 Tool")
    print("\033[1;32m[*] ", end=""); print("1. Encode  2. Decode  99. Uninstall")
    c = input("Select: ")
    if c=="99": import cyber_deps; cyber_deps.remove_deps(); return
    t = input("Text: ")
    if c=="1": print("\033[1;32m[*] ", end=""); print(f"Encoded: {base64.b64encode(t.encode()).decode()}")
    elif c=="2": print("\033[1;32m[*] ", end=""); print(f"Decoded: {base64.b64decode(t.encode()).decode()}")
    input("[Enter]")
if __name__=="__main__": run()