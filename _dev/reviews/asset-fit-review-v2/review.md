# Production Base Fit Review

Status: **FAIL**
Image: `/Volumes/KingstonM2/Projects/avari-pet/production-base-v2.png`
Source size: `1205x1305`
Cell bbox: `[44, 17, 138, 195]`
Cell coverage: `0.2844`
Edge density: `0.4911`
Palette estimate: `128`

## Failures
- sprite is too tall or too close to the 192x208 cell edge
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
