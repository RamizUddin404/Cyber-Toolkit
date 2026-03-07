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
import cyber_deps
cyber_deps.ensure_deps(system_pkgs=["p7zip"])

def run():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[*] Universal Archive Cracker (ZIP/RAR/7Z)\033[0m")
    file = input("Path to Archive: ")
    wordlist = input("Wordlist (Default: rockyou.txt): ") or "rockyou.txt"
    
    if os.path.exists(file) and os.path.exists(wordlist):
        print("\033[1;32m[*] ", end=""); print(f"[*] Cracking {file}...")
        cmd = f"7z x -p'$(cat {wordlist})' {file} -y"
        print("\033[1;32m[*] ", end=""); print("[!] Note: 7z is running. If it fails, the password is not in the list.")
        # Simplified for direct feedback
        os.system(f"for p in $(cat {wordlist}); do 7z x -p$p {file} -aoa >/dev/null 2>&1 && echo '[+] Password Found: '$p && break; done")
    else:
        print("\033[1;32m[*] ", end=""); print("[-] File or Wordlist missing.")
    input("\n[Press Enter]")

if __name__ == "__main__": run()
