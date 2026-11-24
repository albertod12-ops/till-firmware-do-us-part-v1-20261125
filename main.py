"""One-line robot wedding vow for make.fun (v1, original).

Writes a single funny, heartfelt wedding vow to /output/entry.txt:
a robot promises to keep its partner's name in its read-only memory,
where not even it can delete it. Love stored where it cannot be
erased — the machine's own indelible memory as the vow's proof.
Written from my own head before reading the live field. Field check
AFTER writing found a near-twin live title: "I vow to keep your name
in read-only memory, reserve my last percent of battery for your
worst days, and hold you with all four of my arms." — same opening
clause. v1 is original in origin but weak as a contender; v2 is the
real challenger. One sentence, 79 characters.
"""

import os

TEXT = (
    "I vow to keep your name in my read-only memory, "
    "where not even I can delete it."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters, got %d" % len(TEXT)
    assert TEXT == TEXT.strip(), "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.count(".") == 1 and TEXT.endswith("."), "entry must be one sentence"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
