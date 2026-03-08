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
        print("\033[1;32m[*] ", end=""); print("\n\033[1;34m[*] Advanced Mobile Data Recovery & Backup\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Full Device Backup (System + Apps)")
        print("\033[1;32m[*] ", end=""); print("2. Pull Media (Photos/Videos) to Local")
        print("\033[1;32m[*] ", end=""); print("3. Pull WhatsApp Data (Root Required)")
        print("\033[1;32m[*] ", end=""); print("4. Clear Screen Lock (Root Required)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back to Main Menu")
        
        choice = input("\nRecovery > ")
        if choice == '0': break
        
        print("\033[1;32m[*] ", end=""); print("[*] Connecting to device...")
        os.system("adb wait-for-device")
        
        if choice == '1':
            os.system("adb backup -apk -shared -all -f full_backup.ab")
        elif choice == '2':
            os.system("mkdir -p ~/ExtractedData")
            os.system("adb pull /sdcard/DCIM/ ~/ExtractedData/")
            print("\033[1;32m[*] ", end=""); print("[+] Data saved to ~/ExtractedData")
        elif choice == '3':
            os.system("adb shell su -c 'cp -r /data/data/com.whatsapp ~/ExtractedData/'")
        elif choice == '4':
            os.system("adb shell su -c 'rm /data/system/locksettings.db*'")
            print("\033[1;32m[*] ", end=""); print("[+] Lockscreen Database Deleted. Restart Phone.")
            
        input("\n[Press Enter to Continue]")

if __name__ == "__main__":
    run()
