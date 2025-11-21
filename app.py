#!/usr/bin/env python3
import argparse
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Profile:
    key: str
    name: str
    privacy: float      # 0–1
    soundness: float    # 0–1
    performance: float  # 0–1
    note: str


PROFILES: Dict[str, Profile] = {
    "aztec": Profile(
        key="aztec",
        name="Aztec-style zk Rollup",
        privacy=0.95,
        soundness=0.80,
        performance=0.55,
        note="Strong privacy with zk circuits over Ethereum.",
    ),
    "zama": Profile(
        key="zama",
        name="Zama-style FHE System",
        privacy=0.90,
        soundness=0.86,
        performance=0.40,
        note="Encrypted compute with fully homomorphic encryption.",
    ),
    "soundness": Profile(
        key="soundness",
        name="Soundness-first Protocol",
        privacy=0.50,
        soundness=0.98,
        performance=0.70,
        note="Formally specified, proof-driven protocol engineering.",
    ),
}


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def score_profile(p: Profile, need_priv: int, need_snd: int, need_perf: int) -> float:
    priv_need = clamp01(need_priv / 10.0)
    snd_need = clamp01(need_snd / 10.0)
    perf_need = clamp01(need_perf / 10.0)

    priv_match = 1.0 - abs(priv_need - p.privacy)
    snd_match = 1.0 - abs(snd_need - p.soundness)
    perf_match = 1.0 - abs(perf_need - p.performance)

    # Weighted average
    return clamp01(0.4 * snd_match + 0.35 * priv_match + 0.25 * perf_match)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="web3_arch_compare_mini",
        description="Tiny comparator for Aztec, Zama, and soundness-first Web3 styles.",
    )
    parser.add_argument("--privacy", type=int, default=8, help="Privacy importance 0–10 (default 8).")
    parser.add_argument("--soundness", type=int, default=7, help="Soundness importance 0–10 (default 7).")
    parser.add_argument("--performance", type=int, default=6, help="Performance importance 0–10 (default 6).")
    return parser.parse_args()


def label_fit(score: float) -> str:
    if score >= 0.8:
        return "excellent"
    if score >= 0.65:
        return "good"
    if score >= 0.5:
        return "fair"
    return "weak"


def main() -> None:
    args = parse_args()

    need_priv = max(0, min(10, args.privacy))
    need_snd = max(0, min(10, args.soundness))
    need_perf = max(0, min(10, args.performance))

    results: List[tuple[str, float]] = []
    for key, p in PROFILES.items():
        s = score_profile(p, need_priv, need_snd, need_perf)
        results.append((key, s))

    results.sort(key=lambda x: x[1], reverse=True)

       print("🔎 web3_arch_compare_mini")
    print(f"Needs  -> privacy: {need_priv}/10  soundness: {need_snd}/10  performance: {need_perf}/10")
    print("-" * 60)
    print("Fit scores (best first):")
    for key, s in results:
        p = PROFILES[key]
        bar = "█" * int(s * 20)
        print(f"- {p.name:25s} ({key}): {s:.3f} [{label_fit(s)}] {bar}")
        print(f"  {p.note}")
    best_key, best_score = results[0]
    best = PROFILES[best_key]
    print("")
    print(f"Recommended direction: {best.name} ({best.key}) with score {best_score:.3f}")


if __name__ == "__main__":
    main()
