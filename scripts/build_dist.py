#!/usr/bin/env python3
"""
Build clean release distribution for Avari Codex Pet v2.
Copies verified assets to dist/ and generates pet.json manifest.
"""

import json
import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FINAL_DIR = REPO_ROOT / "_runs" / "run_260909" / "final"
if not FINAL_DIR.exists():
    FINAL_DIR = REPO_ROOT / "run_260909" / "final"
DIST_DIR = REPO_ROOT / "dist"


PET_MANIFEST = {
    "id": "avari",
    "displayName": "Авари",
    "description": "Белая эльфийка Avari Keys в тёмном сине-зелёном плаще, созидающая код как магию внутри парящей сферы.",
    "spriteVersionNumber": 2,
    "spritesheetPath": "spritesheet.webp"
}

def main():
    print("📦 Building Avari Codex Pet v2 distribution...")

    source_webp = FINAL_DIR / "spritesheet-extended.webp"
    source_png = FINAL_DIR / "spritesheet-extended.png"
    validation_file = FINAL_DIR / "validation-extended.json"

    if not source_webp.exists():
        print(f"❌ Error: Source spritesheet not found at {source_webp}", file=sys.stderr)
        sys.exit(1)

    if validation_file.exists():
        with open(validation_file, "r", encoding="utf-8") as f:
            val_data = json.load(f)
            if not val_data.get("ok"):
                print("❌ Error: validation-extended.json status is not ok!", file=sys.stderr)
                sys.exit(1)
            print("✅ Atlas validation check: PASSED (ok: true)")

    # Ensure dist directory exists
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    # Write pet.json
    pet_json_path = DIST_DIR / "pet.json"
    with open(pet_json_path, "w", encoding="utf-8") as f:
        json.dump(PET_MANIFEST, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"✅ Created {pet_json_path.relative_to(REPO_ROOT)}")

    # Copy spritesheet.webp
    dist_webp = DIST_DIR / "spritesheet.webp"
    shutil.copyfile(source_webp, dist_webp)
    webp_size_mb = dist_webp.stat().st_size / (1024 * 1024)
    print(f"✅ Copied {dist_webp.relative_to(REPO_ROOT)} ({webp_size_mb:.2f} MB)")

    # Copy spritesheet.png as fallback
    if source_png.exists():
        dist_png = DIST_DIR / "spritesheet.png"
        shutil.copyfile(source_png, dist_png)
        png_size_mb = dist_png.stat().st_size / (1024 * 1024)
        print(f"✅ Copied {dist_png.relative_to(REPO_ROOT)} ({png_size_mb:.2f} MB)")

    print("\n🎉 Distribution build completed successfully!")
    print(f"   Destination: {DIST_DIR}")

if __name__ == "__main__":
    main()
