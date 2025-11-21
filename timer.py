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
        "--quiet",
        action="store_true",
        help="Do not print the 'Running:' line.",
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
  if not args.quiet:
        pretty = " ".join(repr(c) for c in cmd)
        print(f"Running: {pretty}")
    cmd = args.command

    cmd = sys.argv[1:]
    print(f"Running: {' '.join(cmd)}")

    start = time.time()
    result = subprocess.run(cmd)
    end = time.time()
    from datetime import datetime

    start_ts = datetime.now().isoformat(timespec="seconds")
    end_ts = datetime.now().isoformat(timespec="seconds")
    print(f"Started at: {start_ts}")
    print(f"Finished at: {end_ts}")

    print(f"\nExit code: {result.returncode}")
    print(f"Elapsed : {end - start:.3f} seconds")


if __name__ == "__main__":
    main()
