#!/usr/bin/env python3
"""Audit image pages for an A4 industrial brochure delivery package."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image


A4_RATIO = 210 / 297
A4_WIDTH_IN = 210 / 25.4
A4_HEIGHT_IN = 297 / 25.4


def page_number(path: Path) -> int | None:
    match = re.fullmatch(r"P(\d+)\.(png|jpg|jpeg|tif|tiff)", path.name, re.I)
    if not match:
        return None
    return int(match.group(1))


def audit(folder: Path, expected_pages: int | None) -> int:
    files: list[tuple[int, Path]] = []
    for path in folder.iterdir():
        if not path.is_file():
            continue
        number = page_number(path)
        if number is not None:
            files.append((number, path))

    files.sort(key=lambda item: item[0])
    found = {number for number, _ in files}

    missing = []
    if expected_pages:
        missing = [n for n in range(1, expected_pages + 1) if n not in found]

    print(f"Folder: {folder}")
    print(f"Pages found: {len(files)}")
    if expected_pages:
        print(f"Expected pages: {expected_pages}")
    if missing:
        print("Missing pages:", ", ".join(f"P{n}" for n in missing))

    print()
    print("Page\tFile\tPixels\tRatio\tApprox A4 DPI\tSize MB")

    warnings: list[str] = []
    for number, path in files:
        with Image.open(path) as img:
            width, height = img.size
        ratio = width / height
        dpi = min(width / A4_WIDTH_IN, height / A4_HEIGHT_IN)
        mb = path.stat().st_size / 1024 / 1024
        print(f"P{number}\t{path.name}\t{width}x{height}\t{ratio:.4f}\t{dpi:.0f}\t{mb:.2f}")

        if abs(ratio - A4_RATIO) > 0.01:
            warnings.append(f"P{number}: ratio {ratio:.4f} is not close to A4 {A4_RATIO:.4f}")
        if dpi < 240:
            warnings.append(f"P{number}: approximate A4 DPI is low ({dpi:.0f})")

    if warnings:
        print()
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
        return 1

    print()
    print("Audit passed: page images are present and close to A4 print requirements.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Folder containing P1.png, P2.png, ...")
    parser.add_argument("--expected-pages", type=int, default=None)
    args = parser.parse_args()

    if not args.folder.exists() or not args.folder.is_dir():
        parser.error(f"Folder does not exist: {args.folder}")

    return audit(args.folder, args.expected_pages)


if __name__ == "__main__":
    raise SystemExit(main())
