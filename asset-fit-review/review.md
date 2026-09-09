# Production Base Fit Review

Status: **FAIL**
Image: `/Volumes/KingstonM2/Projects/avari-pet/production-base.png`
Source size: `1254x1254`
Cell bbox: `[49, 19, 134, 189]`
Cell coverage: `0.2435`
Edge density: `0.5165`
Palette estimate: `128`

## Failures
- palette and shading are too complex for a small desktop pet sprite

## Warnings
- source image is large; this is acceptable only if the sprite is already simplified

## Recommendations
- Regenerate a production_base image instead of using the high-detail confirmation image.
- Keep the strongest identity cues, but simplify hair strands, textures, shadows, fingers, and small accessories.
- Use a transparent background or one flat chroma color that does not appear inside the sprite.
- Center the complete sprite inside one 192x208 cell with safe padding.

## User Check

Show `cell-preview.png` to the user before hatch-pet handoff.
Only continue after the user confirms the character still reads clearly at 192x208.
