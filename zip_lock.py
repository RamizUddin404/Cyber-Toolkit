# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("ZIP LOCKER (PASSWORD PROTECTOR)")
    print("\033[1;32m[*] Create a password protected ZIP archive.\033[0m")
    
    # Check for zip
    if subprocess.call(["which", "zip"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        os.system("pkg install zip -y")

    target = input("\n\033[1;33mEnter Path to File/Folder to Lock: \033[0m")
    password = input("Enter Password to set: \033[0m")
    out_file = input("Enter Output Filename (default: secured.zip): ") or "secured.zip"
    
    if os.path.exists(target):
        print("\n\033[1;32m[*] Creating ZIP with Password...\033[0m")
        # zip -P [pwd] -r output input
        os.system(f"zip -P {password} -r {out_file} {target}")
        print(f"\n\033[1;32m[+] SUCCESS! File saved as {out_file}\033[0m")
    else:
        print("\033[1;31m[!] Target not found!\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
