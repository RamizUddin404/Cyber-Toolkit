# CREATED BY: RAMIZ UDDIN
import os
import time
import cyber_deps

# Ensure necessary downloaders and proot
cyber_deps.ensure_deps(system_pkgs=["wget", "proot", "tar"])

def tool_header():
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print("      KALI NETHUNTER INSTALLER (ROOTLESS)")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header()
    print("\033[1;33m[!] WARNING: This requires ~2GB free storage & good internet.\033[0m")
    print("1. Install Kali Nethunter (Full)")
    print("2. Launch Nethunter (If installed)")
    print("3. Repair/Fix Installation")
    print("99. Uninstall Nethunter")
    print("0. Back")
    
    c = input("\nNethunter > ")
    if c == '0': return
    
    if c == '1':
        print("\n\033[1;32m[*] Downloading Official Installer...\033[0m")
        # Using the official URL from Offensive Security
        cmd = "wget -O install-nethunter-termux https://offsec.ing/nh-termux"
        os.system(cmd)
        
        print("\n\033[1;32m[*] Starting Installation Process...\033[0m")
        print("[!] Select '1' when asked for image type (Full/Minimal).")
        time.sleep(3)
        os.system("chmod +x install-nethunter-termux")
        os.system("./install-nethunter-termux")
        
    elif c == '2':
        if os.path.exists("/data/data/com.termux/files/usr/bin/nethunter"):
            print("[*] Launching Kali Linux...")
            os.system("nethunter")
        else:
            print("\033[1;31m[-] Nethunter is not installed yet. Use Option 1.\033[0m")
            
    elif c == '3':
        print("[*] Fixing permissions...")
        os.system("chmod +x install-nethunter-termux")
        print("[+] Try installing again.")
        
    elif c == '99':
        print("[*] Removing Nethunter...")
        os.system("rm -rf kali-arm64 install-nethunter-termux")
        print("[+] Cleanup complete.")
        
    input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
