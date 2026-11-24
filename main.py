#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — winning meme entry.

The picture is pre-rendered and stored in this repository as entry.png
(1024x1024 PNG, under the 1 MiB cap). This script only copies it to the
output path, using nothing but the Python standard library: no network,
no clock, no randomness, so a second run writes byte-identical output.
It works the same in a bare Python container with no image libraries or
fonts installed, and it never writes into the repository itself.
"""

import os
import shutil

SRC_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    if not os.path.isfile(src):
        raise SystemExit(f"missing pre-rendered picture: {src}")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, SRC_NAME)
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    if size > 1_048_576:
        raise SystemExit(f"output over the 1 MiB gate: {size} bytes")
    print(f"wrote {dst} ({size} bytes)")


if __name__ == "__main__":
    main()
