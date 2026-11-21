# SPDX-License-Identifier: MIT
"""Write a one-line joke about working beside AI coding agents to entry.txt."""

import os
from pathlib import Path

JOKE = "The AI agent's one-line fix touched 61 files; the bug was in the 62nd."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
