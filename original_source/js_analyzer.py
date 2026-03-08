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
import cyber_deps
def run():
    print("\033[1;32m[*] ", end=""); print("\n\033[1;33m[*] JS Analyzer (Hidden Endpoint Finder)\033[0m")
    url = input("Enter JS URL: ")
    if url: os.system(f"curl -s {url} | grep -oE '(http|https)://[^\" ]+'")
    input("\n[Press Enter]")
if __name__ == "__main__": run()
