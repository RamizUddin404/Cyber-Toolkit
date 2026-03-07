# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import re

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1
    
    print("\033[1;32m[*] ", end=""); print(f"Password Score: {score}/5")
    if score < 3:
        print("\033[1;32m[*] ", end=""); print("Status: WEAK ❌")
    elif score < 5:
        print("\033[1;32m[*] ", end=""); print("Status: MEDIUM ⚠️")
    else:
        print("\033[1;32m[*] ", end=""); print("Status: STRONG ✅")

if __name__ == "__main__":
    pwd = input("Enter Password to Test: ")
    check_strength(pwd)
