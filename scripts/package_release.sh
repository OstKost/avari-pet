#!/usr/bin/env bash
set -e

# Packages Avari Pet v2 into a clean release ZIP for GitHub Releases
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$REPO_ROOT/dist"
STAGE_DIR="/tmp/avari-release-stage"
ZIP_NAME="avari-v2.0.0.zip"
ZIP_PATH="$DIST_DIR/$ZIP_NAME"

echo "📦 Packaging Avari v2 release archive..."

# 1. Ensure dist is built
python3 "$REPO_ROOT/scripts/build_dist.py"

# 2. Stage files
rm -rf "$STAGE_DIR"
mkdir -p "$STAGE_DIR/avari"
cp "$DIST_DIR/pet.json" "$STAGE_DIR/avari/"
cp "$DIST_DIR/spritesheet.webp" "$STAGE_DIR/avari/"

# 3. Create zip
rm -f "$ZIP_PATH"
(cd "$STAGE_DIR" && zip -r "$ZIP_PATH" avari)

rm -rf "$STAGE_DIR"

ZIP_SIZE_MB=$(du -m "$ZIP_PATH" | cut -f1)
echo "✅ Created release zip: $ZIP_PATH (~${ZIP_SIZE_MB} MB)"
