#!/usr/bin/env python3""
import subprocess
import sys
import time


def main():
    if len(sys.argv) < 2:
        print("Usage: python timer.py <command> [args...]")
        sys.exit(1)

    cmd = sys.argv[1:]
    print(f"Running: {' '.join(cmd)}")

    start = time.time()
    result = subprocess.run(cmd)
    end = time.time()

     elapsed = end - start
    print(f"\nExit code: {result.returncode}")
    print(f"Elapsed : {elapsed:.3f} seconds ({elapsed * 1000:.1f} ms)")

if __name__ == "__main__":
    main()
