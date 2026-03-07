# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import requests, os, cyber_deps
cyber_deps.ensure_deps(python_mods=["requests"])
def run():
    print("\033[1;32m[*] ", end=""); print("\n[*] HTTP Header Analyzer")
    u = input("URL: ")
    if u=="99": import cyber_deps; cyber_deps.remove_deps(); return
    try: 
        r = requests.get(u)
        for k,v in r.headers.items(): print("\033[1;32m[*] ", end=""); print(f"{k}: {v}")
    except: print("\033[1;32m[*] ", end=""); print("Error")
    input("[Enter]")
if __name__=="__main__": run()