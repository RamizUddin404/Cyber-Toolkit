# CREATED BY: RAMIZ UDDIN
import os, time, cyber_deps

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("SQLMAP INJECTION TOOL")
    print("\033[1;32m[*] Advanced SQL Injection Scanner via SQLMap.\033[0m")
    
    cyber_deps.ensure_deps(system_pkgs=["sqlmap"])
    
    target = input("\n\033[1;33mEnter Target URL (e.g. site.com/php?id=1): \033[0m").strip()
    if target:
        print(f"\n\033[1;32m[*] Starting SQLMap Scan on {target}...\033[0m")
        print("[!] Using --batch and --random-agent for efficiency.")
        time.sleep(1)
        os.system(f"sqlmap -u '{target}' --batch --random-agent --level=1 --risk=1")
    
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
