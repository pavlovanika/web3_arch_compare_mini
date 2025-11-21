#!/usr/bin/env python3""
import subprocess
import sys
import time

__version__ = "0.1.0"
def main():
    if len(sys.argv) < 2:
        print("Usage: python timer.py <command> [args...]")
        sys.exit(1)

    cmd = sys.argv[1:]
    print(f"Running: {' '.join(cmd)}")

    start = time.time()
    result = subprocess.run(cmd)
    end = time.time()

    print(f"\nExit code: {result.returncode}")
    print(f"Elapsed : {end - start:.3f} seconds")


if __name__ == "__main__":
    main()
