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
import platform

def audit():
    print("\033[1;32m[*] ", end=""); print("[*] System Information:")
    print("\033[1;32m[*] ", end=""); print(f"System: {platform.system()}")
    print("\033[1;32m[*] ", end=""); print(f"Release: {platform.release()}")
    print("\033[1;32m[*] ", end=""); print(f"Architecture: {platform.machine()}")
    
    print("\033[1;32m[*] ", end=""); print("\n[*] Checking for Root Access...")
    if os.geteuid() == 0:
        print("\033[1;32m[*] ", end=""); print("[+] Root Access: DETECTED (Dangerous if not careful)")
    else:
        print("\033[1;32m[*] ", end=""); print("[-] Root Access: Not Detected (Safe)")

    print("\033[1;32m[*] ", end=""); print("\n[*] Checking Open Ports (Netstat)...")
    os.system("netstat -tuln 2>/dev/null || echo 'Netstat not available'")

if __name__ == "__main__":
    audit()
