#!/usr/bin/env python3
"""
Root entry point for Cyber-Toolkit
Launches the main application from core directory
"""

import os
import sys
import subprocess

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    core_path = os.path.join(script_dir, 'core')
    core_main = os.path.join(core_path, 'main.py')
    
    # Check if core directory exists
    if not os.path.isdir(core_path):
        print("[!] Error: 'core' directory not found!")
        print("[!] Please reinstall the toolkit.")
        sys.exit(1)
    
    # Check if core/main.py exists
    if not os.path.exists(core_main):
        print("[!] Error: 'core/main.py' not found!")
        print("[!] Please reinstall the toolkit.")
        sys.exit(1)
    
    # Run the core main.py
    try:
        result = subprocess.run(['python3', core_main], cwd=core_path)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\n[!] Program interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error running core/main.py: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
