#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


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


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    app_path = repo_root / "app.py"

    if not app_path.is_file():
        print("ERROR: app.py not found next to run_presets.py", file=sys.stderr)
        sys.exit(1)

    for idx, preset in enumerate(PRESETS, start=1):
        print("=" * 80)
        print(f"[{idx}] {preset['label']}")
        print(f"    privacy    = {preset['privacy']}")
        print(f"    soundness  = {preset['soundness']}")
        print(f"    performance= {preset['performance']}")
        print("-" * 80)

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

        result = subprocess.run(cmd, text=True, capture_output=True)
    print("=" * 80)
    print(f"Ran {len(PRESETS)} preset(s).")
    print("Done running all presets.")

        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            print("[stderr]", result.stderr.strip(), file=sys.stderr)

        print()  # blank line between presets

    print("=" * 80)
    print("Done running all presets.")


if __name__ == "__main__":
    main()
