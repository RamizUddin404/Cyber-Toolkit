# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import cyber_deps
cyber_deps.ensure_deps(system_pkgs=["steghide"])
import os
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;35m[*] Steganography: Hide/Extract Data in Images\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Embed (Hide) File in Image")
        print("\033[1;32m[*] ", end=""); print("2. Extract (Find) Hidden File")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nStegano > ")
        if c == '0': break
        
        img = input("Enter Image Path: ")
        if c == '1':
            secret = input("Enter Secret File Path: ")
            os.system(f"steghide embed -cf {img} -ef {secret}")
        elif c == '2':
            os.system(f"steghide extract -sf {img}")
        
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
