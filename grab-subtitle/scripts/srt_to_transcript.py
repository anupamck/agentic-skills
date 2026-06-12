#!/usr/bin/env python3
"""Convert an SRT subtitle file into a clean timestamped transcript."""

import re
import sys

PARAGRAPH_GAP_SECONDS = 30


def parse_srt(path):
    with open(path, encoding="utf-8-sig") as f:
        content = f.read()

    blocks = re.split(r"\n\s*\n", content.strip())
    entries = []
    for block in blocks:
        lines = block.strip().splitlines()
        if len(lines) < 3:
            continue
        match = re.match(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})", lines[1])
        if not match:
            continue
        h, m, s, _ = match.groups()
        total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
        text = " ".join(lines[2:])
        text = re.sub(r"<[^>]+>", "", text).strip()
        if text:
            entries.append((total_seconds, text))
    return entries


def format_timestamp(seconds):
    m, s = divmod(seconds, 60)
    return f"[{m}:{s:02d}]"


def group_paragraphs(entries):
    if not entries:
        return []

    paragraphs = []
    current_ts = entries[0][0]
    current_texts = []

    for ts, text in entries:
        if current_texts and ts - current_ts >= PARAGRAPH_GAP_SECONDS:
            paragraphs.append((current_ts, " ".join(current_texts)))
            current_ts = ts
            current_texts = []
        current_texts.append(text)

    if current_texts:
        paragraphs.append((current_ts, " ".join(current_texts)))

    return paragraphs


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input.srt> <output.txt>", file=sys.stderr)
        sys.exit(1)

    srt_path = sys.argv[1]
    out_path = sys.argv[2]

    entries = parse_srt(srt_path)
    paragraphs = group_paragraphs(entries)

    with open(out_path, "w", encoding="utf-8") as f:
        for i, (ts, text) in enumerate(paragraphs):
            if i > 0:
                f.write("\n")
            f.write(f"{format_timestamp(ts)} {text}\n")

    print(f"Wrote {len(paragraphs)} paragraphs to {out_path}")


if __name__ == "__main__":
    main()
