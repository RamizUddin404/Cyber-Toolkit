# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import base64
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;35m[*] Cryptography Tool\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Encrypt (Base64)")
        print("\033[1;32m[*] ", end=""); print("2. Decrypt (Base64)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        action = input("\nCrypto > ")
        if action == '0': break
        
        text = input("Enter Text: ")
        if action == '1':
            print("\033[1;32m[*] ", end=""); print(f"Result: {base64.b64encode(text.encode()).decode()}")
        elif action == '2':
            try: print("\033[1;32m[*] ", end=""); print(f"Result: {base64.b64decode(text).decode()}")
            except: print("\033[1;32m[*] ", end=""); print("[!] Invalid Hash")

if __name__ == "__main__":
    run()
