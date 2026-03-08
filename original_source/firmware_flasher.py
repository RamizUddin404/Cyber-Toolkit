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
        print("\033[1;32m[*] ", end=""); print("\n\033[1;35m[*] Professional Mobile Firmware Flasher\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Flash Boot (boot.img)")
        print("\033[1;32m[*] ", end=""); print("2. Flash Recovery (recovery.img)")
        print("\033[1;32m[*] ", end=""); print("3. Flash System (system.img)")
        print("\033[1;32m[*] ", end=""); print("4. Flash VBMETA (vbmeta.img)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back to Main Menu")
        
        choice = input("\nFlash > ")
        if choice == '0': break
        
        img_path = input("Enter path to .img file: ")
        if not os.path.exists(img_path):
            print("\033[1;32m[*] ", end=""); print("[!] File not found! Please check the path.")
            continue
            
        print("\033[1;32m[*] ", end=""); print("[*] Waiting for device in Fastboot mode...")
        os.system("fastboot wait-for-device")
        
        if choice == '1': os.system(f"fastboot flash boot {img_path}")
        elif choice == '2': os.system(f"fastboot flash recovery {img_path}")
        elif choice == '3': os.system(f"fastboot flash system {img_path}")
        elif choice == '4': os.system(f"fastboot flash vbmeta --disable-verity --disable-verification {img_path}")
        
        print("\033[1;32m[*] ", end=""); print("\n[+] Operation Finished.")
        input("[Press Enter to Continue]")

if __name__ == "__main__":
    run()
