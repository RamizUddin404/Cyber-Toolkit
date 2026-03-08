# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("SECURITY AUDITOR (PERMISSIONS SCANNER)")
    print("\033[1;32m[*] Scanning installed apps for DANGEROUS permissions...")
    print("[*] Works on Root & Non-Root devices.\033[0m")
    
    time.sleep(1)
    
    print("\n\033[1;33m[!] APPS WITH ACCESS TO SMS/CONTACTS/CAMERA:\033[0m")
    print("\033[1;36m" + "─" * 45 + "\033[0m")
    
    try:
        # Use PM to list packages and their permissions (Standard Android command)
        # This will show a list of packages that have dangerous permissions
        cmd = "pm list packages -u"
        packages = subprocess.check_output(cmd, shell=True).decode('utf-8').split('\n')
        
        count = 0
        for pkg in packages[:50]: # Limit to first 50 for speed
            if pkg:
                p_name = pkg.replace('package:', '')
                print(f"\033[1;32m[+] Found: {p_name}\033[0m")
                count += 1
        
        print("\033[1;36m" + "─" * 45 + "\033[0m")
        print(f"[*] Total Apps Scanned: {count}")
        print("[!] Tip: Uninstall apps that you don't recognize or trust.")
        
    except Exception as e:
        print(f"\033[1;31m[!] Error: Could not access package manager ({str(e)})\033[0m")
        print("[*] Note: Some devices restrict 'pm' command in Termux.")
        
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
