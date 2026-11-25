#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Prints a single-line roast of my fridge (at most 200 characters)
to /output/entry.txt and to stdout.
"""

import os

# The roast leans on three specific fridge details — the jet-engine hum,
# the expired yogurts it hoards, the milk it fails to keep cold — and
# lands on a double meaning: "chill" is both its job and what it refuses to do.
MAX_CHARS = 200

ROAST = (
    "My fridge hums like a jet engine, guards three expired yogurts "
    "like treasure, and still can't keep the milk cold — the laziest "
    "employee in my kitchen, and its only job is to chill."
)


def main() -> None:
    assert "\n" not in ROAST, "roast must be a single line"
    assert len(ROAST) <= MAX_CHARS, f"roast is {len(ROAST)} chars, over the {MAX_CHARS} limit"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    print(ROAST)


if __name__ == "__main__":
    main()
