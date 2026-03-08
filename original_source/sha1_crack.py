# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import hashlib
def run():
    print("\033[1;32m[*] ", end=""); print("[*] SHA1 Cracker")
    t = input("Hash: ")
    if t=="99": import cyber_deps; cyber_deps.remove_deps(); return
    w = input("Wordlist: ") or "pass.txt"
    try:
        with open(w, "r") as f:
            for l in f:
                if hashlib.sha1(l.strip().encode()).hexdigest() == t:
                    print("\033[1;32m[*] ", end=""); print(f"Found: {l.strip()}"); break
    except: print("\033[1;32m[*] ", end=""); print("Error")
    input("[Enter]")
if __name__=="__main__": run()