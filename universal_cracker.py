# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("UNIVERSAL ARCHIVE CRACKER (ZIP/RAR/7Z)")
    print("\033[1;32m[*] Brute-force password protected archives.\033[0m")
    
    # Check for fcrackzip
    if subprocess.call(["which", "fcrackzip"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        os.system("pkg install fcrackzip -y")

    file_path = input("\n\033[1;33mEnter Path to Archive: \033[0m")
    wordlist = input("Enter Path to Wordlist (default: pass.txt): \033[0m") or "pass.txt"
    
    if os.path.exists(file_path) and os.path.exists(wordlist):
        print("\n\033[1;32m[*] Cracking Archive...\033[0m")
        # fcrackzip works for ZIP files
        if file_path.endswith('.zip'):
            os.system(f"fcrackzip -u -D -p {wordlist} {file_path}")
        else:
            print("\n\033[1;33m[*] Only ZIP supported via internal fcrackzip.\033[0m")
            print("[*] For others, try john/hashcat manually.")
    else:
        print("\033[1;31m[!] File or Wordlist not found!\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
