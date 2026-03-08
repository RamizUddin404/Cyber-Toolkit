# FIXED BY GEMINI CLI
import os
import sys
import time
import subprocess
import shutil

def tool_header(name):
    os.system('clear')
    print('\x1b[1;36m=============================================')
    print(f'      {name.upper()}')
    print('      CREATED BY: RAMIZ UDDIN')
    print('=============================================\x1b[0m')

def run():
    tool_header('METADATA STRIPPER (EXIF REMOVER)')
    print('\x1b[1;32m[*] Remove personal metadata (GPS, Device Info) from images.\x1b[0m')
    
    if shutil.which('exiftool') is None:
        print('\n\x1b[1;31m[!] Exiftool not found. Installing...\x1b[0m')
        os.system('pkg install perl wget -y && wget https://github.com/exiftool/exiftool/archive/master.zip && unzip master.zip && mv exiftool-master/exiftool $PREFIX/bin/ && chmod +x $PREFIX/bin/exiftool')
    
    file_path = input('\n\x1b[1;33mEnter Path to Image: \x1b[0m')
    if os.path.exists(file_path):
        print('\n\x1b[1;32m[*] Stripping Metadata...\x1b[0m')
        os.system(f'exiftool -all= "{file_path}"')
        print('\n\x1b[1;32m[+] Success! Metadata removed from original file.\x1b[0m')
    else:
        print('\x1b[1;31m[!] File not found!\x1b[0m')
    
    input('\n[Press Enter to Return]')

if __name__ == '__main__':
    run()
