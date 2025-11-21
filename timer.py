#!/usr/bin/env python3""
import argparse
import subprocess
import sys
import time


def main() -> None:
    """Parse arguments, run the given command, and print timing."""
    parser = argparse.ArgumentParser(description="Time how long a command takes to run.")
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print script version and exit."
    )
    parser.add_argument(
        "command",
        nargs=argparse.REMAINDER,
        help="Command and arguments to run."
    )
    args = parser.parse_args()

    if args.version:
        print(f"timer.py version {__version__}")
        return

    if not args.command:
        print("Usage: timer.py <command> [args...]", file=sys.stderr)
        sys.exit(1)

    cmd = args.command

    cmd = sys.argv[1:]
    print(f"Running: {' '.join(cmd)}")

    start = time.time()
    result = subprocess.run(cmd)
    end = time.time()

    print(f"\nExit code: {result.returncode}")
    print(f"Elapsed : {end - start:.3f} seconds")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.", file=sys.stderr)
        sys.exit(130)

