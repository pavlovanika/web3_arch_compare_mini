#!/usr/bin/env python3
import argparse
from collections import Counter
import sys


def parse_args():
    p = argparse.ArgumentParser(description="Small log analysis script.")
    p.add_argument("--file", required=True, help="Path to log file")
        p.add_argument(
        "--min-count",
        type=int,
        default=1,
        help="Only show lines that occur at least this many times.",
    )
    p.add_argument("--top", type=int, default=5, help="Show N most common lines")
    p.add_argument("--filter", help="Only count lines containing this keyword")
    return p.parse_args()


def main():
    args = parse_args()

    try:
        with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"ERROR: Could not read {args.file}: {e}", file=sys.stderr)
        sys.exit(1)

    if args.filter:
        lines = [l for l in lines if args.filter in l]

    total = len(lines)
    errors = sum(1 for l in lines if "error" in l.lower())
    warnings = sum(1 for l in lines if "warn" in l.lower())

    print("=== LOG STATS ===")
    print(f"File        : {args.file}")
    print(f"Total lines : {total}")
    print(f"Errors      : {errors}")
    print(f"Warnings    : {warnings}")

    if total == 0:
        print("\n(No lines to analyze.)")
        return

    counter = Counter(lines)
    top = counter.most_common(args.top)

        print(f"\nTop {args.top} most common lines (min count = {args.min_count}):")
    shown = 0
    for line, count in top:
        if count < args.min_count:
            continue
        shown += 1
        print(f"{shown}. ({count}x) {line.strip()}")

    if shown == 0:
        print("No lines met the minimum count threshold.")


if __name__ == "__main__":
    main()
