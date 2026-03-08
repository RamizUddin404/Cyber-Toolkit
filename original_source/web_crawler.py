# CREATED BY: RAMIZ UDDIN
import os, sys, time, subprocess

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

def run():
    tool_header("WEB CRAWLER (LINK EXTRACTOR)")
    print("\033[1;32m[*] Extract all unique links from a webpage URL.\033[0m")
    
    url = input("\n\033[1;33mEnter Target URL (e.g. http://example.com): \033[0m").strip()
    if not url.startswith('http'):
        url = 'http://' + url
        
    print(f"\n\033[1;32m[*] Crawling {url}...\033[0m")
    time.sleep(1)
    
    try:
        # Use curl to get HTML and grep to extract links
        # Simplified regex for extracting href
        cmd = f'curl -s "{url}" | grep -oE "href=\\\"([^\\\"]+)\\\"" | cut -d\'"\' -f2 | sort -u'
        print("\033[1;36m" + "─" * 45)
        print("  FOUND LINKS:")
        print("─" * 45 + "\033[0m")
        os.system(cmd)
        print("\033[1;36m" + "─" * 45 + "\033[0m")
        
    except Exception as e:
        print(f"\n\033[1;31m[!] Error: {str(e)}\033[0m")
        
    input("\n[Press Enter to Return]")

if __name__ == "__main__":
    run()
