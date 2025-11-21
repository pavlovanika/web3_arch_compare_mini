#!/usr/bin/env python3
import platform
import sys
import os
import textwrap

def main():
       print("=== QUICK INFO ===")
    print(f"Python version : {sys.version.split()[0]}")
    print(f"Platform       : {platform.system()} {platform.release()}")
    print(f"Machine        : {platform.machine()}")
    print(f"Working dir    : {os.getcwd()}")
    print("\nEnvironment variables (selected):")
    for key in ["PATH", "HOME", "USER", "SHELL"]:
        print(f"  {key}: {os.getenv(key)}")

if __name__ == "__main__":
    main()
