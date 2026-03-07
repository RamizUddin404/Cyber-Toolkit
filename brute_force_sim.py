# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import time

def brute_force(target_pass, wordlist):
    print("\033[1;32m[*] ", end=""); print(f"[*] Starting Brute Force against target...")
    for password in wordlist:
        print("\033[1;32m[*] ", end=""); print(f"[#] Trying: {password}")
        time.sleep(0.2)
        if password == target_pass:
            print("\033[1;32m[*] ", end=""); print(f"\n[+] SUCCESS! Password Found: {password}")
            return
    print("\033[1;32m[*] ", end=""); print("[-] Password not in wordlist.")

if __name__ == "__main__":
    target = "admin123"
    words = ["123456", "password", "qwerty", "admin123", "root"]
    brute_force(target, words)
