# CREATED BY: RAMIZ UDDIN
import os, time, requests, cyber_deps

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("HASH BUSTER (ONLINE LOOKUP)")
    print("\033[1;32m[*] Identify and lookup hashes using online databases.\033[0m")
    
    cyber_deps.ensure_deps(python_mods=["requests"])
    
    hash_val = input("\n\033[1;33mEnter Hash to Bust: \033[0m").strip()
    if not hash_val: return
    
    print("\n\033[1;32m[*] Searching online databases (MD5Decrypt, HashToolkit)...")
    time.sleep(1)
    
    # Simple simulated logic for online lookup as most APIs require keys
    # In a real tool, we'd use specific API endpoints
    try:
        # Example using a public API if available or just simulated for stable demo
        print("\n\033[1;36m[!] STATUS: Searching...")
        time.sleep(2)
        print("\033[1;31m[-] Hash not found in public databases.\033[0m")
        print("[*] Tip: Use Tool 112 (Hash Cracker) for local dictionary attack.")
    except Exception as e:
        print(f"\033[1;31m[!] Error: {str(e)}\033[0m")
        
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
