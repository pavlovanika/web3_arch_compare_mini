# web3_arch_compare_mini

A tiny CLI script that compares three conceptual Web3 architectural styles and tells you which one best matches your priorities:

- Aztec-style zk rollup (privacy-heavy)
- Zama-style FHE system (encrypted compute)
- Soundness-first protocol (formal verification and correctness)


Repository contents

This repository intentionally has only two files:

- app.py
- README.md


What it does

You provide three numbers from 0 to 10:

- how important privacy is
- how important soundness (formal guarantees, proofs) is
- how important performance (throughput / latency) is

The script has built-in profiles for:

- Aztec-style zk rollup
- Zama-style FHE compute stack
- Soundness-first protocol lab

Each profile has a privacy, soundness, and performance focus between 0 and 1. The script computes how close your needs are to each profile and prints a ranked list of scores, plus a simple recommendation.


Installation

Requirements:

- Python 3.8 or newer

Steps:

1. Create a new GitHub repository with any name.
2. Place app.py and this README.md at the root of the repo.
3. Ensure the python command is available on your system.
4. No external libraries are required; only the Python standard library is used.


Usage

From the root of the repository:

Example 1: high privacy, strong soundness, moderate performance

python app.py --privacy 9 --soundness 8 --performance 6

Example 2: FHE-heavy use case with very high privacy and soundness, lower performance priority

python app.py --privacy 10 --soundness 9 --performance 4

Example 3: high throughput protocol with medium privacy but strict soundness

python app.py --privacy 5 --soundness 9 --performance 9


Output

The script prints:

- your stated needs for privacy, soundness, and performance
- each profile with:
  - name and key
  - fitScore (0.0–1.0)
  - label: excellent, good, fair, weak
  - a short note about that style
- a final “recommended direction” line pointing at the highest scoring profile

There is no JSON mode and no network access. The script is intentionally minimal.


Notes

- All numbers and weights are illustrative and designed for discussion, not for rigorous system design.
- The tool does not call any RPCs, does not read keys, and does not touch the blockchain.
- You can easily extend app.py to add more profiles or change the scoring logic to better match your view of Aztec-like, Zama-like, or soundness-first architectures.
