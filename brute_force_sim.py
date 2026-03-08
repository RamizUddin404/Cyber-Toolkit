# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("BRUTE FORCE SIMULATOR")
    print("\033[1;32m[*] Educational simulation of a brute force attack.\033[0m")
    
    target_pass = input("\n\033[1;33mSet a Target Password to crack: \033[0m")
    wordlist_str = input("Enter dummy wordlist (comma separated): \033[0m") or "123456,password,qwerty,admin,root"
    wordlist = wordlist_str.split(',')
    
    print(f"\n\033[1;32m[*] Starting Brute Force against '{target_pass}'...\033[0m")
    time.sleep(1)
    
    found = False
    for pwd in wordlist:
        pwd = pwd.strip()
        print(f"\033[1;36m[#] Trying: {pwd}...", end="\r")
        time.sleep(0.3)
        if pwd == target_pass:
            print(f"\n\n\033[1;32m[+] SUCCESS! Password Found: {pwd}\033[0m")
            found = True
            break
            
    if not found:
        print("\n\n\033[1;31m[-] Password not in wordlist.\033[0m")
        
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
