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
import time
def run():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[*] SMS Bomber PRO\033[0m")
    num = input("Target Number: ")
    cnt = int(input("Amount: ") or 10)
    for i in range(1, cnt+1):
        print("\033[1;32m[*] ", end=""); print(f"[+] Sending {i}/{cnt}...", end="\r")
        time.sleep(0.1)
    print("\033[1;32m[*] ", end=""); print("\n[+] Finish.")
    input("\n[Press Enter]")
if __name__ == "__main__": run()
