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
        "--repeat",
        type=int,
        default=1,
        help="Run the command this many times and report average time.",
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

    last_result = None
    total_elapsed = 0.0
    for i in range(args.repeat):
        if args.repeat > 1:
            print(f"\nRun {i+1}/{args.repeat}...")
        start = time.monotonic()
        last_result = subprocess.run(cmd, shell=False)
        end = time.monotonic()
        total_elapsed += (end - start)

    avg = total_elapsed / args.repeat

    from datetime import datetime

    start_ts = datetime.now().isoformat(timespec="seconds")
    end_ts = datetime.now().isoformat(timespec="seconds")
    print(f"Started at: {start_ts}")
    print(f"Finished at: {end_ts}")

    print(f"\nExit code: {last_result.returncode if last_result else 'N/A'}")
    if args.repeat == 1:
        print(f"Elapsed : {avg:.3f} seconds ({avg * 1000:.1f} ms)")
    else:
        print(f"Average elapsed over {args.repeat} runs: {avg:.3f} seconds ({avg * 1000:.1f} ms)")


if __name__ == "__main__":
    main()
