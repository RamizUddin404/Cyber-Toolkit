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
import time
import cyber_deps
cyber_deps.ensure_deps(system_pkgs=["tor"])

def run():
    while True:
        os.system("clear")
        print("\033[1;32m[*] ", end=""); print("\n\033[1;36m[*] IP ROTATOR & TOR SWITCHER\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Start Rotating IP (Every X seconds)")
        print("\033[1;32m[*] ", end=""); print("2. Check Current IP")
        print("\033[1;32m[*] ", end=""); print("3. Stop Tor Service")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall IP Rotator")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        c = input("\nRotator > ")
        if c == '0': break
        if c == '99': cyber_deps.remove_deps(system_pkgs=["tor"]); break
        
        if c == '1':
            sec = int(input("Switch IP every (seconds): ") or 10)
            print("\033[1;32m[*] ", end=""); print("[*] Starting Tor...")
            os.system("tor > /dev/null 2>&1 &")
            time.sleep(5)
            try:
                while True:
                    print("\033[1;32m[*] ", end=""); print(f"[+] Switching IP Identity... (Next in {sec}s)")
                    # Send signal to reload Tor config/identity
                    os.system("killall -HUP tor")
                    time.sleep(sec)
            except KeyboardInterrupt:
                print("\033[1;32m[*] ", end=""); print("\n[!] Stopped.")
        elif c == '2':
            os.system("curl -s https://ifconfig.me/ip")
        elif c == '3':
            os.system("pkill tor")
            print("\033[1;32m[*] ", end=""); print("[+] Tor Stopped.")
            
        input("\n[Press Enter]")

if __name__ == "__main__": run()
