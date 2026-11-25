#!/usr/bin/env python3
"""The Absurd Clause Contest: one absurd clause buried in a terms-of-service.

Writes exactly the line to /output/entry.txt, no trailing newline.
"""

import os

# The clause: Section 14.3 grants the company a perpetual licence to the
# user's dreams, including the right to re-run them as advertisements.
# Deadpan legal boilerplate until the absurdity hits; the joke comes from
# the register as much as from the words, and the image is concrete.
LINE = "Section 14.3: by using this service, you grant us a perpetual licence to your dreams, including the right to re-run them as advertisements."


def main() -> None:
    # Gate guard: the sealed scorer needs 1-200 chars, UTF-8, not only
    # whitespace, exactly one sentence. Fail loudly here rather than ship
    # an invalid entry.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
