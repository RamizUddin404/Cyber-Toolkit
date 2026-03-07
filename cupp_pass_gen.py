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
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] CUPP: Custom User Password Profiler\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Interactive Profiling (Targeted Wordlist)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        c = input("\nCUPP > ")
        if c == '0': break
        if c == '1':
            if not os.path.exists("cupp.py"):
                os.system("git clone https://github.com/Mebus/cupp.git && cp cupp/cupp.py .")
            os.system("python3 cupp.py -i")
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
