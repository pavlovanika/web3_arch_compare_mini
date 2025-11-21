#!/usr/bin/env python3
import platform
import sys
import os
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Print quick system & Python info.")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print raw sys.argv for debugging."
    )
    args = parser.parse_args()

    if args.debug:
        print(f"argv           : {sys.argv}")

    if args.version:
        print(f"quick_info version {__version__}")
        return

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
