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
cyber_deps.ensure_deps(python_mods=["pillow"])
from PIL import Image
def run():
    img_path = input("\nEnter Image Path: ")
    if os.path.exists(img_path):
        img = Image.open(img_path)
        img.save("clean_" + img_path)
        print("\033[1;32m[*] ", end=""); print("[+] Metadata Stripped. Saved as clean_" + img_path)
    input("\n[Press Enter]")
if __name__ == "__main__": run()
