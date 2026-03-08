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
import subprocess
import requests
import string
import random
import cyber_deps

cyber_deps.ensure_deps(system_pkgs=["p7zip", "wget"], python_mods=["requests"])

MASTER_LIST = "rockyou.txt"

def download_master():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] Downloading FULL RockYou Database (14 Million Passwords)...\033[0m")
    print("\033[1;32m[*] ", end=""); print("[!] This is 130MB. It will take 1-3 minutes. Please wait...")
    url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
    try:
        subprocess.call(["wget", "-O", MASTER_LIST, url])
        print("\033[1;32m[*] ", end=""); print(f"\n\033[1;32m[+] SUCCESS! 14 Million Passwords Ready in {MASTER_LIST}\033[0m")
    except Exception as e:
        print("\033[1;32m[*] ", end=""); print(f"[!] Download failed: {e}")

def run_crack(z_path, w_path):
    if not os.path.exists(z_path):
        print("\033[1;32m[*] ", end=""); print(f"\033[1;31m[!] ZIP file not found!\033[0m")
        return
    
    print("\033[1;32m[*] ", end=""); print(f"\n\033[1;32m[*] Launching Attack on: {os.path.basename(z_path)}\033[0m")
    print("\033[1;32m[*] ", end=""); print(f"[*] Wordlist: {w_path}")
    print("\033[1;32m[*] ", end=""); print("-" * 55)
    
    try:
        with open(w_path, 'r', errors='ignore') as f:
            for count, line in enumerate(f, 1):
                pwd = line.strip()
                if not pwd: continue
                if count % 1000 == 0: print("\033[1;32m[*] ", end=""); print(f"\r[*] Tested {count} passwords...", end="")
                
                # Check password
                cmd = f"7z t -p'{pwd}' '{z_path}'"
                res = subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                if res == 0:
                    print("\033[1;32m[*] ", end=""); print(f"\n\n\033[1;32m[###################################]\033[0m")
                    print("\033[1;32m[*] ", end=""); print(f"\033[1;32m[+] MATCH FOUND: {pwd}\033[0m")
                    print("\033[1;32m[*] ", end=""); print(f"\033[1;32m[###################################]\033[0m")
                    return
            print("\033[1;32m[*] ", end=""); print("\n\n\033[1;31m[-] NO MATCH FOUND IN THIS LIST.\033[0m")
    except Exception as e: print("\033[1;32m[*] ", end=""); print(f"\n[!] Error: {e}")

def run():
    while True:
        os.system('clear')
        print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[!] ULTIMATE 14-MILLION PASS & ZIP ENGINE [!]\033[0m")
        print("\033[1;32m[*] ", end=""); print("-" * 60)
        print("\033[1;32m[*] ", end=""); print("1. Download FULL Master Database (14,000,000 Passwords)")
        print("\033[1;32m[*] ", end=""); print("2. Smart Profiler (Personal Info)")
        print("\033[1;32m[*] ", end=""); print("3. Generate PINs (0000-9999)")
        print("\033[1;32m[*] ", end=""); print("4. AUTO ZIP CRACK (Generate & Crack)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nEngine > ")
        if c == '0': break
        
        if c == '1': download_master()
        elif c == '2': 
            print("\033[1;32m[*] ", end=""); print("\n[*] Smart Profiler Launched...")
            # Simple inline profiler for stability
            name = input("Target Name: ").lower()
            dob = input("Birth Year: ")
            with open("target_pass.txt", "w") as f:
                f.write(f"{name}\n{name}{dob}\n{name}123\n{name}@123\n{name.capitalize()}{dob}\n")
            print("\033[1;32m[*] ", end=""); print("[+] Profiled wordlist saved to target_pass.txt")
        elif c == '3':
            with open("pins.txt", "w") as f:
                for i in range(10000): f.write(f"{i:04d}\n")
            print("\033[1;32m[*] ", end=""); print("[+] Generated pins.txt")
        elif c == '4':
            z = input("\nEnter ZIP Path: ")
            print("\033[1;32m[*] ", end=""); print("\nSelect Wordlist:")
            print("\033[1;32m[*] ", end=""); print("1. FULL RockYou Master DB (14M passes - RECOMMENDED)")
            print("\033[1;32m[*] ", end=""); print("2. Smart Profiler (Personal/Targeted Info)")
            print("\033[1;32m[*] ", end=""); print("3. PINs (0000-9999)")
            
            wc = input("Choice > ")
            w_path = MASTER_LIST
            if wc == '1' and not os.path.exists(MASTER_LIST): download_master()
            elif wc == '2': w_path = "target_pass.txt"
            elif wc == '3': w_path = "pins.txt"
            
            run_crack(z, w_path)
            
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
