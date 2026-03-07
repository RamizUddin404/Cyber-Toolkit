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
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;34m[*] Professional Google Dorking Helper\033[0m")
        print("\033[1;32m[*] ", end=""); print("1. Find Login Pages")
        print("\033[1;32m[*] ", end=""); print("2. Find Exposed DB Files (.sql, .db)")
        print("\033[1;32m[*] ", end=""); print("3. Find PDF/Sensitive Docs")
        print("\033[1;32m[*] ", end=""); print("4. Custom Dork Search")
        print("\033[1;32m[*] ", end=""); print("99. Uninstall This Tool (Remove Packages)")
        print("\033[1;32m[*] ", end=""); print("0. Back")
        
        choice = input("\nDork > ")
        if choice == '0': break
        domain = input("Enter Target Domain (e.g. site.com): ")
        
        dorks = {
            '1': f"site:{domain} inurl:login",
            '2': f"site:{domain} ext:sql | ext:db | ext:config",
            '3': f"site:{domain} ext:pdf | ext:doc | ext:docx",
            '4': input("Enter your custom dork: ")
        }
        
        if choice in dorks:
            query = dorks[choice].replace(" ", "+")
            url = f"https://www.google.com/search?q={query}"
            print("\033[1;32m[*] ", end=""); print(f"\n[+] Copy this URL to your browser:\n\033[1;32m{url}\033[0m")
        
        input("\n[Press Enter to Continue]")
if __name__ == "__main__": run()
