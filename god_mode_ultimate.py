# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("SYSTEM GOD MODE (ULTIMATE CLEAN)")
    print("\033[1;32m[*] Performance Boost: Cleaning and Updating System...")
    print("[*] Works on Root & Non-Root devices.\033[0m")
    
    print("\n\033[1;33m[1/3] Updating Core Packages...\033[0m")
    os.system("pkg update -y && pkg upgrade -y")
    
    print("\n\033[1;33m[2/3] Cleaning Cache and Temp Files...\033[0m")
    os.system("rm -rf $HOME/.cache/*")
    os.system("pkg clean")
    os.system("apt autoremove -y")
    
    print("\n\033[1;33m[3/3] Optimizing Python Environment...\033[0m")
    os.system("find . -name \"*.pyc\" -delete")
    os.system("find . -name \"__pycache__\" -delete")
    
    print("\n\033[1;32m[+] GOD MODE FINISH! Your System is now optimized.\033[0m")
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
