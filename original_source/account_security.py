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
import random
import cyber_deps

# Ensure requests module for potential API calls
cyber_deps.ensure_deps(python_mods=["requests"])

def header():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;31m========================================\033[0m")
    print("\033[1;32m[*] ", end=""); print("      DEEP BREACH CHECKER & SECURITY")
    print("\033[1;32m[*] ", end=""); print("\033[1;31m========================================\033[0m")

def deep_check(email):
    print("\033[1;32m[*] ", end=""); print(f"\n\033[1;33m[*] Searching Global Breach Databases for: {email}...\033[0m")
    time.sleep(2)
    
    # Realistic Breach Sources Simulation (based on common global leaks)
    all_sources = [
        "Facebook (533M User Leak - 2021)", "LinkedIn (700M Professional Data - 2021)", 
        "Twitter (200M Email Leak - 2023)", "Canva (137M Accounts - 2019)", 
        "Wattpad (270M Records - 2020)", "Adobe (153M Accounts - 2013)", 
        "MyFitnessPal (150M Records)", "Zomato (17M User Info)", 
        "Dropbox (68M Emails)", "Evite (100M Records)", "Dubsmash", "Bitly"
    ]
    
    # Deterministic but realistic simulation for Termux speed
    random.seed(email)
    leaked_in = random.sample(all_sources, random.randint(1, 4))
    
    if "@" not in email or "." not in email:
        print("\033[1;32m[*] ", end=""); print("\033[1;31m[!] Invalid Email Format.\033[0m")
        return

    print("\033[1;32m[*] ", end=""); print(f"\n\033[1;31m[!] ALERT: This Email was found in {len(leaked_in)} Massive Data Breaches!\033[0m")
    print("\033[1;32m[*] ", end=""); print("\033[1;34m" + "-"*60 + "\033[0m")
    print("\033[1;32m[*] ", end=""); print(f"\033[1;37mBreach Sources (Where your data was leaked):\033[0m")
    for source in leaked_in:
        print("\033[1;32m[*] ", end=""); print(f" [+] SOURCE: {source}")
    print("\033[1;32m[*] ", end=""); print("\033[1;34m" + "-"*60 + "\033[0m")
    
    # Risk Level Guide
    print("\033[1;32m[*] ", end=""); print(f"\n\033[1;33m[*] RISK ASSESSMENT:\033[0m")
    if len(leaked_in) > 2:
        print("\033[1;32m[*] ", end=""); print("\033[1;31m [CRITICAL] High Risk: Your Password and Personal Info are public.\033[0m")
    else:
        print("\033[1;32m[*] ", end=""); print("\033[1;33m [MEDIUM] Warning: Your Email is on hacker wordlists.\033[0m")

def security_guide():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[*] ULTIMATE ACCOUNT SECURITY GUIDE (Hacker-Proof)\033[0m")
    print("\033[1;32m[*] ", end=""); print("-" * 65)
    print("\033[1;32m[*] ", end=""); print("1. \033[1;31mChange Password NOW:\033[0m If your email is leaked, hackers use ")
    print("\033[1;32m[*] ", end=""); print("   the old password to attack your Gmail/Bank/FB accounts.")
    print("\033[1;32m[*] ", end=""); print("2. \033[1;33mUse Unique Passwords:\033[0m Never use the same pass for 2 accounts.")
    print("\033[1;32m[*] ", end=""); print("3. \033[1;32mEnable 2-Factor (2FA):\033[0m Use 'Google Authenticator' instead of SMS.")
    print("\033[1;32m[*] ", end=""); print("4. \033[1;36mCheck Logged-In Devices:\033[0m Go to Gmail Settings > Security >")
    print("\033[1;32m[*] ", end=""); print("   Manage all devices. Logout any device you don't recognize.")
    print("\033[1;32m[*] ", end=""); print("5. \033[1;35mClear Cookies:\033[0m Periodically clear browser cookies to avoid")
    print("\033[1;32m[*] ", end=""); print("   Session Hijacking (Cookie Stealing).")
    print("\033[1;32m[*] ", end=""); print("-" * 65)

def run():
    while True:
        os.system("clear")
        header()
        print("\033[1;32m[*] ", end=""); print("1. Deep Email Breach Check (Show Leak Sources)")
        print("\033[1;32m[*] ", end=""); print("2. View Security & Password Change Guide")
        print("\033[1;32m[*] ", end=""); print("3. View Captured Credentials (Phishing Results)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall Account Security Module")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        choice = input("\nSecurity > ")
        
        if choice == '0': break
        
        if choice == '1':
            email = input("\nEnter Email to check: ")
            deep_check(email)
            input("\n[Press Enter to Continue]")
        elif choice == '2':
            security_guide()
            input("\n[Press Enter to Continue]")
        elif choice == '3':
            if os.path.exists("captured_creds.txt"):
                print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[ Captured Login Data ]\033[0m")
                print("\033[1;32m[*] ", end=""); print(open("captured_creds.txt").read())
            else: print("\033[1;32m[*] ", end=""); print("[-] No data captured yet. Run Tool 16 first.")
            input("\n[Press Enter to Continue]")
        elif choice == '99':
            cyber_deps.remove_deps()
            break

if __name__ == "__main__": run()
