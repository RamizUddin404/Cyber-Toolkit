# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import re
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] Hash Type Identifier\033[0m")
        h = input("\nEnter Hash (or '0' to exit): ")
        if h == '0': break
        if len(h) == 32: print("\033[1;32m[*] ", end=""); print("[+] Possible Hash: MD5")
        elif len(h) == 40: print("\033[1;32m[*] ", end=""); print("[+] Possible Hash: SHA-1")
        elif len(h) == 64: print("\033[1;32m[*] ", end=""); print("[+] Possible Hash: SHA-256")
        elif len(h) == 128: print("\033[1;32m[*] ", end=""); print("[+] Possible Hash: SHA-512")
        else: print("\033[1;32m[*] ", end=""); print("[-] Unknown Hash Type.")
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
