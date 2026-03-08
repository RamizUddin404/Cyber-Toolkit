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
    if input("Check IP? ") == "99": import cyber_deps; cyber_deps.remove_deps(); return
    os.system("curl ifconfig.me")
    input("[Enter]")
if __name__=="__main__": run()