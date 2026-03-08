# CREATED BY: RAMIZ UDDIN
import os, time, re

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("PASSWORD STRENGTH CHECKER")
    print("\033[1;32m[*] Analyze your password security level.\033[0m")
    
    password = input("\n\033[1;33mEnter Password to Test: \033[0m")
    if password:
        score = 0
        if len(password) >= 8: score += 1
        if re.search(r"[A-Z]", password): score += 1
        if re.search(r"[a-z]", password): score += 1
        if re.search(r"\d", password): score += 1
        if re.search(r"[!@#$%^&*]", password): score += 1
        
        print("\n\033[1;36m" + "─" * 45)
        print(f"  Security Score: {score}/5")
        if score < 3:
            print("  Status        : \033[1;31mWEAK ❌\033[0m")
        elif score < 5:
            print("  Status        : \033[1;33mMEDIUM ⚠️\033[0m")
        else:
            print("  Status        : \033[1;32mSTRONG ✅\033[0m")
        print("─" * 45 + "\033[0m")
        
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
