#!/usr/bin/env python3
"""Convert all PNG images under static/images/ to WebP (q=85).

Also rasterises the two large SVGs to WebP via Pillow (if cairosvg is
unavailable, falls back to a simple Pillow open for any embedded-raster SVGs,
which won't work — in that case we skip and warn).

Usage:
    python3 scripts/convert_images_to_webp.py          # dry-run (default)
    python3 scripts/convert_images_to_webp.py --run     # actually convert
"""
import argparse
import glob
import io
import os
import sys

from PIL import Image

QUALITY = 85
STATIC_IMAGES = os.path.join(os.path.dirname(__file__), "..", "static", "images")
STATIC_IMAGES = os.path.normpath(STATIC_IMAGES)


def convert_png(src: str, *, dry_run: bool) -> int:
    dst = src.rsplit(".", 1)[0] + ".webp"
    img = Image.open(src)
    if img.mode == "RGBA":
        alpha = img.getchannel("A")
        if alpha.getextrema() == (255, 255):
            img = img.convert("RGB")
    elif img.mode != "RGB":
        img = img.convert("RGB")

    buf = io.BytesIO()
    img.save(buf, format="WEBP", quality=QUALITY)
    webp_bytes = buf.tell()

    if not dry_run:
        with open(dst, "wb") as f:
            f.write(buf.getvalue())

    return webp_bytes


def rasterise_svg(src: str, width: int, *, dry_run: bool) -> int:
    try:
        import cairosvg
        png_data = cairosvg.svg2png(url=src, output_width=width)
        img = Image.open(io.BytesIO(png_data)).convert("RGB")
    except (ImportError, OSError):
        print(f"  [WARN] cairosvg not available — skipping SVG: {os.path.basename(src)}")
        print("         Install with: brew install cairo && pip3 install cairosvg")
        return 0

    dst = src.rsplit(".", 1)[0] + ".webp"
    buf = io.BytesIO()
    img.save(buf, format="WEBP", quality=QUALITY)
    webp_bytes = buf.tell()

    if not dry_run:
        with open(dst, "wb") as f:
            f.write(buf.getvalue())

    return webp_bytes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="Actually write files (default is dry-run)")
    args = parser.parse_args()
    dry_run = not args.run

    if dry_run:
        print("=== DRY RUN (pass --run to write files) ===\n")

    pngs = sorted(glob.glob(os.path.join(STATIC_IMAGES, "**", "*.png"), recursive=True))
    print(f"Found {len(pngs)} PNG files under {STATIC_IMAGES}")

    total_orig = 0
    total_webp = 0
    for f in pngs:
        orig = os.path.getsize(f)
        webp = convert_png(f, dry_run=dry_run)
        total_orig += orig
        total_webp += webp

    print(f"PNG total: {total_orig / 1e6:.1f} MB -> WebP total: {total_webp / 1e6:.1f} MB "
          f"({(1 - total_webp / total_orig) * 100:.1f}% smaller)\n")

    svgs = [
        (os.path.join(STATIC_IMAGES, "fig1-webpage.svg"), 1920),
        (os.path.join(STATIC_IMAGES, "hblending-comparison.svg"), 1920),
    ]
    for svg_path, w in svgs:
        if not os.path.isfile(svg_path):
            print(f"  SVG not found: {svg_path}")
            continue
        orig = os.path.getsize(svg_path)
        webp = rasterise_svg(svg_path, w, dry_run=dry_run)
        if webp:
            print(f"  {os.path.basename(svg_path)}: {orig / 1e6:.1f} MB -> {webp / 1e3:.0f} KB WebP")

    if dry_run:
        print("\nNo files written. Re-run with --run to convert.")
    else:
        print("\nDone! WebP files written alongside originals.")


if __name__ == "__main__":
    main()
