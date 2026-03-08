# CREATED BY: RAMIZ UDDIN
import os, sys, time, base64

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    while True:
        tool_header("BASE64 PRO (ENCODE/DECODE)")
        print("\033[1;32m[1] Encode Text to Base64")
        print("[2] Decode Base64 to Text")
        print("[0] Back\033[0m")
        
        c = input("\nBase64 > ")
        if c == '0': break
        
        data = input("\nEnter Data: ")
        try:
            if c == '1':
                res = base64.b64encode(data.encode()).decode()
                print(f"\n\033[1;32m[+] ENCODED: {res}\033[0m")
            elif c == '2':
                res = base64.b64decode(data.encode()).decode()
                print(f"\n\033[1;32m[+] DECODED: {res}\033[0m")
        except Exception as e:
            print(f"\n\033[1;31m[!] Error: {str(e)}\033[0m")
        
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
