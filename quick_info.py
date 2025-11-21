#!/usr/bin/env python3
import platform
import sys
import os
import argparse

def main() -> None:
    """Print quick diagnostic information about the current environment."""
    parser = argparse.ArgumentParser(description="Print quick system & Python info.")
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print script version and exit."
    )
    args = parser.parse_args()
    if args.version:
        print(f"quick_info version {__version__}")
        return

    print("=== QUICK INFO ===")
    print(f"Python version : {sys.version.split()[0]}")
    print(f"Platform       : {platform.system()} {platform.release()}")
      print(f"Machine        : {platform.machine()}")
    print(f"Python exe     : {sys.executable}")
    print(f"Working dir    : {os.getcwd()}")
    print("\nEnvironment variables (selected):")
    for key in ["PATH", "HOME", "USER", "SHELL"]:
        print(f"  {key}: {os.getenv(key)}")

if __name__ == "__main__":
    main()
