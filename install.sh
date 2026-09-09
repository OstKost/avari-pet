#!/usr/bin/env bash
set -e

# Avari Pet v2 Installer for macOS & Linux
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/OstKost/avari-pet/main/install.sh | bash
#   or locally: ./install.sh

PET_ID="avari"
CODEX_DIR="${CODEX_HOME:-$HOME/.codex}"
TARGET_DIR="$CODEX_DIR/pets/$PET_ID"
RAW_BASE_URL="https://raw.githubusercontent.com/OstKost/avari-pet/main/dist"

echo ""
echo -e "\033[1;36m🔮 Avari Pet v2 Installer (macOS / Linux)\033[0m"
echo -e "   White elf companion for ChatGPT / Codex Desktop\n"

echo -e "📁 Target directory: \033[33m$TARGET_DIR\033[0m"
mkdir -p "$TARGET_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" 2>/dev/null)" && pwd 2>/dev/null || echo "")"
LOCAL_DIST="$SCRIPT_DIR/dist"

if [ -d "$LOCAL_DIST" ] && [ -f "$LOCAL_DIST/pet.json" ] && [ -f "$LOCAL_DIST/spritesheet.webp" ]; then
  echo "📦 Installing from local dist/ directory..."
  cp "$LOCAL_DIST/pet.json" "$TARGET_DIR/pet.json"
  cp "$LOCAL_DIST/spritesheet.webp" "$TARGET_DIR/spritesheet.webp"
else
  echo "🌐 Downloading pet assets from GitHub..."
  echo -n "   ⏳ Downloading pet.json... "
  curl -fsSL "$RAW_BASE_URL/pet.json" -o "$TARGET_DIR/pet.json"
  echo -e "\033[32m✔\033[0m"

  echo -n "   ⏳ Downloading spritesheet.webp... "
  curl -fsSL "$RAW_BASE_URL/spritesheet.webp" -o "$TARGET_DIR/spritesheet.webp"
  echo -e "\033[32m✔\033[0m"
fi

SIZE_MB=$(du -m "$TARGET_DIR/spritesheet.webp" | cut -f1)

echo ""
echo -e "\033[1;32m✨ Avari successfully installed into $TARGET_DIR!\033[0m\n"
echo -e "👉 \033[1mNext steps:\033[0m"
echo -e "   1. Restart or reload \033[36mChatGPT Desktop / Codex\033[0m."
echo -e "   2. Select \033[35mAvari\033[0m in your pet selector."
echo -e "   3. Enjoy coding with your magical white elf companion! 🪄✨\n"
