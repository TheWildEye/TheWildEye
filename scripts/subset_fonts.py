#!/usr/bin/env python3
"""
Subset the embedded fonts to only the characters the artwork actually uses.

The five WOFFs in fonts/ are already subset builds, but they still carry a lot of
glyphs we never draw. Re-subsetting to the exact character set cuts ~80 KB of
base64 out of cards/page.svg. Run this whenever the artwork's text changes:

    python scripts/subset_fonts.py

Originals are kept in fonts/full/ so the subset can always be regenerated.
"""
import glob
import os
import re
import shutil

from fontTools import subset

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
FONTS = os.path.join(ROOT, "fonts")
FULL = os.path.join(FONTS, "full")

# ASCII printable + every non-ASCII glyph the artwork draws.
CHARS = "".join(chr(c) for c in range(32, 127)) + "\u00b7\u00d7\u2013\u2014\u2019\u2018\u201c\u201d\u2713\u2605\u25b8\u2197\u2192"


def used_chars():
    src = os.path.join(ROOT, "cards", "page.svg")
    if os.path.exists(src):
        text = re.sub(r"<[^>]+>", "", open(src, encoding="utf-8").read())
        return set(text) | set(CHARS)
    return set(CHARS)


def main():
    os.makedirs(FULL, exist_ok=True)
    for f in glob.glob(os.path.join(FONTS, "*.woff")):
        dst = os.path.join(FULL, os.path.basename(f))
        if not os.path.exists(dst):
            shutil.copy2(f, dst)

    unicodes = sorted(ord(c) for c in used_chars() if c.strip())
    opts = subset.Options()
    opts.flavor = "woff"
    opts.desubroutinize = True
    opts.notdef_outline = True
    opts.recalc_bounds = True

    for f in glob.glob(os.path.join(FULL, "*.woff")):
        name = os.path.basename(f)
        font = subset.load_font(f, opts)
        ss = subset.Subsetter(options=opts)
        ss.populate(unicodes=unicodes)
        ss.subset(font)
        out = os.path.join(FONTS, name)
        subset.save_font(font, out, opts)
        print(f"{name}: {os.path.getsize(f)} -> {os.path.getsize(out)} bytes")


if __name__ == "__main__":
    main()
