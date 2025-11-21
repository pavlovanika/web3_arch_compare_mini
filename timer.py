#!/usr/bin/env python3""
import subprocess
import sys
import time


def main():
    if len(sys.argv) < 2:
        print("Usage: python timer.py <command> [args...]")
        sys.exit(1)

    cmd = sys.argv[1:]
       pretty = " ".join(repr(c) for c in cmd)
    print(f"Running: {pretty}")


    start = time.time()
    result = subprocess.run(cmd)
    end = time.time()

    print(f"\nExit code: {result.returncode}")
    print(f"Elapsed : {end - start:.3f} seconds")


if __name__ == "__main__":
    main()
