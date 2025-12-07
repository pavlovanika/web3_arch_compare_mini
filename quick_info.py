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
        parser.add_argument(
        "--short",
        action="store_true",
        help="Print only Python version and platform.",
    )

    args = parser.parse_args()
    if args.short:
        print(f"Python {sys.version.split()[0]} on {platform.system()} {platform.release()}")
        return
    if args.version:
        print(f"quick_info version {__version__}")
        return

    print("=== QUICK INFO ===")
    print(f"Python version : {sys.version.split()[0]}")
    print(f"Platform       : {platform.system()} {platform.release()}")
    print(f"Machine        : {platform.machine()}")
       print(f"Working dir    : {Path.cwd()}")
    print("\nEnvironment variables (selected):")
    for key in ["PATH", "HOME", "USER", "SHELL"]:
        print(f"  {key}: {os.getenv(key)}")

if __name__ == "__main__":
    main()
