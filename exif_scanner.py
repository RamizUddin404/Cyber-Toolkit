# CREATED BY: RAMIZ UDDIN
import os, time

def tool_header(name):
    os.system("clear")
    print("\033[1;36m" + "="*45)
    print(f"      {name.upper()}")
    print("      CREATED BY: RAMIZ UDDIN")
    print("="*45 + "\033[0m")

# CREATED BY: RAMIZ UDDIN
import cyber_deps
cyber_deps.ensure_deps(system_pkgs=["exiftool"])
import os
def run():
    while True:
        print("\033[1;32m[*] ", end=""); print("\n\033[1;32m[*] Digital Forensics: Image Exif Scanner\033[0m")
        img_path = input("\nEnter Image Path (or '0' to exit): ")
        if img_path == '0': break
        if not os.path.exists(img_path): print("\033[1;32m[*] ", end=""); print("[!] File not found."); continue
        # Simple use of exiftool if installed
        os.system(f"exiftool {img_path} || echo '[!] Please install exiftool (pkg install exiftool)'")
        input("\n[Press Enter to Scan Another]")
if __name__ == "__main__": run()
