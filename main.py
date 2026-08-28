#!/usr/bin/env python3
import os

def main():
    # Change current working directory to 'core' so internal imports/paths work
    core_path = os.path.join(os.getcwd(), 'core')
    if os.path.isdir(core_path):
        os.chdir(core_path)
        # Execute the original main.py
        if os.path.exists('main.py'):
            os.system('python3 main.py')
        else:
            print("[!] Critical Error: 'core/main.py' not found.")
    else:
        print("[!] Error: 'core' directory not found. Please reinstall the toolkit.")

if __name__ == "__main__":
    main()
