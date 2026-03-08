# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("QR TOOLKIT (GENERATE/DECODE)")
    print("\033[1;32m[*] Create or Decode QR codes for payloads or info.\033[0m")
    
    if subprocess.call(["which", "qrencode"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        os.system("pkg install qrencode zbar -y")

    while True:
        print("\n[1] Generate QR Code")
        print("[2] Decode QR Code")
        print("[0] Back")
        
        c = input("\nQR > ")
        if c == '0': break
        
        if c == '1':
            data = input("\nEnter Data for QR: ")
            fname = input("Enter Filename (default: qr.png): ") or "qr.png"
            os.system(f"qrencode -o {fname} '{data}'")
            print(f"\n\033[1;32m[+] QR Code saved as {fname}\033[0m")
        elif c == '2':
            img = input("\nEnter Path to QR Image: ")
            if os.path.exists(img):
                print("\n\033[1;32m[*] Decoding...\033[0m")
                os.system(f"zbarimg {img}")
            else:
                print("\033[1;31m[!] File not found!\033[0m")
        
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
