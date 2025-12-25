#!/usr/bin/env python3
"""
Run a set of predefined privacy/soundness/performance presets
against app.py (web3_arch_compare_mini) for quick comparison.
"""
import subprocess
import sys
from pathlib import Path
from typing import TypedDict


class Preset(TypedDict):
    label: str
    privacy: int
    soundness: int
    performance: int


PRESETS = [
    {
        "label": "Privacy-heavy Aztec-style (high privacy, strong soundness, moderate performance)",
        "privacy": 9,
        "soundness": 8,
        "performance": 6,
    },
    {
        "label": "FHE-style Zama profile (very high privacy & soundness, lower performance priority)",
        "privacy": 10,
        "soundness": 9,
        "performance": 4,
    },
    {
        "label": "High-throughput protocol (medium privacy, strict soundness, high performance)",
        "privacy": 5,
        "soundness": 9,
        "performance": 9,
    },
]
VERSION = "1.0.0"


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    app_path = repo_root / "app.py"

    if not app_path.is_file():
        print("ERROR: app.py not found next to run_presets.py", file=sys.stderr)
        sys.exit(1)

    if not app_path.suffix == ".py":
        print(f"ERROR: expected a Python file at {app_path}", file=sys.stderr)
        sys.exit(1)

    for idx, preset in enumerate(PRESETS, start=1):
        print("=" * 80)
        print(f"[{idx}] {preset['label']}")
        print(f"    privacy    = {preset['privacy']}")
        print(f"    soundness  = {preset['soundness']}")
        print(f"    performance= {preset['performance']}")
        print("-" * 80)
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print script version and exit."
    )

        cmd = [
            sys.executable,
            str(app_path),
            "--privacy",
            str(preset["privacy"]),
            "--soundness",
            str(preset["soundness"]),
            "--performance",
            str(preset["performance"]),
        ]

                print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, text=True, capture_output=True)


        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            print("[stderr]", result.stderr.strip(), file=sys.stderr)

        print()  # blank line between presets

    print("=" * 80)
    print("Done running all presets.")


if __name__ == "__main__":
    main()
