# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import cyber_deps
cyber_deps.ensure_deps(system_pkgs=["apktool", "java"])
import os
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[*] Professional APK Analyzer\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Decompile APK (Source Code)")
        print("\033[1;32m[*] ", end=""); print("2. Rebuild APK")
        print("\033[1;32m[*] ", end=""); print("3. Sign APK")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back to Main Menu")
        
        choice = input("\nAPK > ")
        if choice == '0': break
        
        path = input("Enter path to APK/Folder: ")
        if not os.path.exists(path):
            print("\033[1;32m[*] ", end=""); print("[!] Path not found.")
            continue
            
        if choice == '1': os.system(f"apktool d {path}")
        elif choice == '2': os.system(f"apktool b {path}")
        elif choice == '3': os.system(f"apksigner sign --key key.pk8 --cert cert.x509.pem {path}")
        
        input("\n[Press Enter to Continue]")

if __name__ == "__main__":
    run()
