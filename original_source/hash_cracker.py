# CREATED BY: RAMIZ UDDIN
import os, sys, time, hashlib

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("HASH CRACKER (MD5/SHA1/SHA256)")
    print("\033[1;32m[*] Dictionary-based Hash Cracking Tool.\033[0m")
    
    hash_val = input("\n\033[1;33mEnter Target Hash: \033[0m").strip()
    wordlist = input("Enter Path to Wordlist (default: pass.txt): \033[0m") or "pass.txt"
    
    if not os.path.exists(wordlist):
        print("\033[1;31m[!] Wordlist not found!\033[0m")
        input("\n[Press Enter]")
        return
        
    print("\n\033[1;32m[*] Cracking started...\033[0m")
    try:
        with open(wordlist, 'r', errors='ignore') as f:
            for line in f:
                pwd = line.strip()
                # Check MD5, SHA1, SHA256
                if hashlib.md5(pwd.encode()).hexdigest() == hash_val or \
                   hashlib.sha1(pwd.encode()).hexdigest() == hash_val or \
                   hashlib.sha256(pwd.encode()).hexdigest() == hash_val:
                    print(f"\n\033[1;32m[+] SUCCESS! HASH CRACKED: {pwd}\033[0m")
                    input("\n[Press Enter]")
                    return
        print("\n\033[1;31m[!] Hash not found in wordlist.\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Error: {str(e)}\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
