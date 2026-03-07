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
import cyber_deps
# pyzbar needs zbar system library
cyber_deps.ensure_deps(system_pkgs=["zbar"], python_mods=["qrcode", "pillow", "pyzbar"])
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;34m[*] QR Code Toolkit (Hacker Style)\033[0m")
        print("\033[1;32m[*] ", end=""); print("-" * 40)
        print("\033[1;32m[*] ", end=""); print("1. Create QR Code (Link/Text)")
        print("\033[1;32m[*] ", end=""); print("2. Scan/Decode QR Image (Read Content)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nQR > ")
        if c == '0': break
        
        if c == '1':
            data = input("Enter Data/URL: ")
            name = input("Enter output name (e.g. hack.png): ") or "qr.png"
            img = qrcode.make(data)
            img.save(name)
            print("\033[1;32m[*] ", end=""); print(f"\033[1;32m[+] QR Saved as {name}\033[0m")
            
        elif c == '2':
            img_path = input("Enter QR Image Path (e.g. /sdcard/qr.png): ")
            if os.path.exists(img_path):
                print("\033[1;32m[*] ", end=""); print(f"[*] Scanning {img_path}...")
                try:
                    detected = decode(Image.open(img_path))
                    if detected:
                        print("\033[1;32m[*] ", end=""); print(f"\n\033[1;32m[+] DECODED CONTENT: {detected[0].data.decode('utf-8')}\033[0m")
                    else:
                        print("\033[1;32m[*] ", end=""); print("\033[1;31m[-] No QR Code found in this image.\033[0m")
                except Exception as e:
                    print("\033[1;32m[*] ", end=""); print(f"[!] Error decoding: {e}")
            else:
                print("\033[1;32m[*] ", end=""); print("[!] File not found!")
                
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
