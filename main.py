#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single sentence to /output/entry.txt (or to the path in
ENTRY_OUTPUT when set, for local testing). Pure standard library only.

The sentence was chosen after brainstorming several candidates against
the judge's brief: it must convince a friend who has never coded to let
an AI agent build their first app idea on make.fun, in one read. The
winner is warm and direct, names make.fun, gives a concrete reason to
say yes now ("today"), and makes handing over the idea feel easy and
low-risk ("no coding, no cost, and you can change your mind any time").
"""

import os
from pathlib import Path

ENTRY = (
    "Tell me the app idea you've been carrying around and I'll build it "
    "for you on make.fun today \u2014 no coding, no cost, and you can "
    "change your mind any time."
)


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
