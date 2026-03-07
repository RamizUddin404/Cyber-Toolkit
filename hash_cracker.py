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
import os
import cyber_deps
cyber_deps.ensure_deps()

def crack(target_hash, w_path):
    if not os.path.exists(w_path):
        print("\033[1;32m[*] ", end=""); print(f"[*] Wordlist {w_path} not found. Creating a default one...")
        import pass_gen
        pass_gen.generate_wordlist(500, w_path)
    
    print("\033[1;32m[*] ", end=""); print(f"[*] Cracking hash using {w_path}...")
    found = False
    with open(w_path, 'r') as f:
        for line in f:
            word = line.strip()
            if hashlib.sha256(word.encode()).hexdigest() == target_hash:
                print("\033[1;32m[*] ", end=""); print(f"\n\033[1;32m[+] Password Found: {word}\033[0m")
                found = True
                break
    if not found: print("\033[1;32m[*] ", end=""); print("[-] Password not found in list.")

def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[*] Professional Hash Cracker (SHA256)\033[0m")
        h = input("\nEnter Hash (or '0' to exit): ")
        if h == '0': break
        w = input("Wordlist path (Press Enter for auto-default 'pass.txt'): ") or "pass.txt"
        crack(h, w)
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
