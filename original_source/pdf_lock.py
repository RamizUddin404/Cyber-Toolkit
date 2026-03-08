# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("PDF LOCKER (PASSWORD PROTECTOR)")
    print("\033[1;32m[*] Lock your PDF file with a strong password.\033[0m")
    
    # Check for pdftk or qpdf
    if subprocess.call(["which", "qpdf"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        os.system("pkg install qpdf -y")

    file_path = input("\n\033[1;33mEnter Path to PDF: \033[0m")
    password = input("Enter Password to set: \033[0m")
    out_file = input("Enter Output Filename (default: locked.pdf): ") or "locked.pdf"
    
    if os.path.exists(file_path):
        print("\n\033[1;32m[*] Locking PDF...\033[0m")
        # qpdf --encrypt [user-pwd] [owner-pwd] [key-len] -- input-file output-file
        os.system(f"qpdf --encrypt {password} {password} 256 -- {file_path} {out_file}")
        print(f"\n\033[1;32m[+] SUCCESS! File saved as {out_file}\033[0m")
    else:
        print("\033[1;31m[!] File not found!\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
