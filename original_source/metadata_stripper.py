# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("METADATA STRIPPER (EXIF REMOVER)")
    print("\033[1;32m[*] Remove personal metadata (GPS, Device Info) from images.\033[0m")
    
    # Check for exiftool
    if subprocess.call(["which", "exiftool"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        print("\n\033[1;31m[!] Exiftool not found. Installing...\033[0m")
        os.system("pkg install perl wget -y && wget https://github.com/exiftool/exiftool/archive/master.zip && unzip master.zip && mv exiftool-master/exiftool $PREFIX/bin/ && chmod +x $PREFIX/bin/exiftool")

    file_path = input("\n\033[1;33mEnter Path to Image: \033[0m")
    if os.path.exists(file_path):
        print("\n\033[1;32m[*] Stripping Metadata...\033[0m")
        os.system(f"exiftool -all= {file_path}")
        print("\n\033[1;32m[+] Success! Metadata removed from original file.\033[0m")
    else:
        print("\033[1;31m[!] File not found!\033[0m")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__": run()
