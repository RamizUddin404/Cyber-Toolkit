#!/usr/bin/env python3
"""Show basic local system and Python information without changing the device."""
import os
import platform
import sys
from pathlib import Path


def main():
    print("Local System Information")
    print(f"Operating system: {platform.system()} {platform.release()}")
    print(f"Machine:          {platform.machine() or 'unknown'}")
    print(f"Python:           {platform.python_version()}")
    print(f"Executable:       {sys.executable}")
    print(f"Working folder:   {Path.cwd()}")
    print(f"Process ID:       {os.getpid()}")
    print(f"CPU count:        {os.cpu_count() or 'unknown'}")


if __name__ == "__main__":
    main()
