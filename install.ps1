# Avari Pet v2 Installer for Windows (PowerShell)
# Usage:
#   irm https://raw.githubusercontent.com/OstKost/avari-pet/main/install.ps1 | iex
#   or locally: .\install.ps1

$ErrorActionPreference = "Stop"

$PET_ID = "avari"
$CODEX_DIR = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$TARGET_DIR = Join-Path $CODEX_DIR (Join-Path "pets" $PET_ID)
$RAW_BASE_URL = "https://raw.githubusercontent.com/OstKost/avari-pet/main/dist"

Write-Host ""
Write-Host "🔮 Avari Pet v2 Installer (Windows)" -ForegroundColor Cyan
Write-Host "   White elf companion for ChatGPT / Codex Desktop`n"

Write-Host "📁 Target directory: $TARGET_DIR" -ForegroundColor Yellow

if (-not (Test-Path $TARGET_DIR)) {
    New-Item -ItemType Directory -Path $TARGET_DIR -Force | Out-Null
}

$LOCAL_DIST = Join-Path $PSScriptRoot "dist"

if ((Test-Path $LOCAL_DIST) -and (Test-Path (Join-Path $LOCAL_DIST "pet.json")) -and (Test-Path (Join-Path $LOCAL_DIST "spritesheet.webp"))) {
    Write-Host "📦 Installing from local dist/ directory..."
    Copy-Item (Join-Path $LOCAL_DIST "pet.json") (Join-Path $TARGET_DIR "pet.json") -Force
    Copy-Item (Join-Path $LOCAL_DIST "spritesheet.webp") (Join-Path $TARGET_DIR "spritesheet.webp") -Force
} else {
    Write-Host "🌐 Downloading pet assets from GitHub..."
    Write-Host -NoNewline "   ⏳ Downloading pet.json... "
    Invoke-WebRequest -Uri "$RAW_BASE_URL/pet.json" -OutFile (Join-Path $TARGET_DIR "pet.json")
    Write-Host "✔" -ForegroundColor Green

    Write-Host -NoNewline "   ⏳ Downloading spritesheet.webp... "
    Invoke-WebRequest -Uri "$RAW_BASE_URL/spritesheet.webp" -OutFile (Join-Path $TARGET_DIR "spritesheet.webp")
    Write-Host "✔" -ForegroundColor Green
}

Write-Host ""
Write-Host "✨ Avari successfully installed into $TARGET_DIR!" -ForegroundColor Green
Write-Host ""
Write-Host "👉 Next steps:"
Write-Host "   1. Restart or reload ChatGPT Desktop / Codex."
Write-Host "   2. Select Avari in your pet selector."
Write-Host "   3. Enjoy coding with your magical white elf companion! 🪄✨`n"
