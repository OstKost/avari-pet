# AGENTS.md — Guidelines for AI Agents in avari-pet

This repository builds, validates, and packages **Avari**, an animated desktop assistant pet compliant with the **Codex Pet v2** standard (`spriteVersionNumber: 2`).

---

## 1. Token Hygiene & Context Conservation (MANDATORY)

To keep context windows clean, minimize latency, and prevent token exhaustion:

1. **Cap Terminal Output**:
   - Never run unbounded commands (`cat`, `find`, `ls -R`, `git log`).
   - Always pipe or restrict output: `| head -n 25`, `| tail -n 25`, `grep -E '...'`, or `jq -c '.'`.
   - For file listings, use `find . -maxdepth 2` or check count first: `ls -1 dir/ | wc -l`.
2. **Targeted File Reading**:
   - Do NOT load entire large markdown/json files (>80 lines) into context unless strictly required.
   - Use line-range slicing (`StartLine`/`EndLine`) or ripgrep/grep to look up specific keys or sections.
3. **Zero Raw Image / Base64 Dumps**:
   - Never dump Base64, raw binary bytes, or extensive ASCII art into context.
   - Rely on deterministic JSON logs (`asset_fit.json`, `review.json`, `validation-extended.json`) to confirm image geometry, palette, and bounding boxes.
   - Inspect visual contact sheets only at designated milestone checkpoints.
4. **Subagent / Worker Handoffs**:
   - Subagents/workers must return **only** a compact key-value summary (max 5–8 lines):
     ```text
     status: PASS | FAIL
     job: <row_name>
     output_path: <path>
     frames_valid: <count>
     issues: <none | short summary>
     ```
   - Do NOT echo back full generation prompts, image logs, or execution traces.
5. **Surgical Edits Over Rewrites**:
   - Use patch/diff tools (`replace_file_content`) rather than rewriting whole files.

---

## 2. Multi-Model Strategy & Playbook

Tasks in this repository are partitioned by model capability to optimize speed, cost, and reliability:

| Task Type | Recommended Model Tier | Responsibility & Behavior |
|---|---|---|
| **Script Execution & Frame Processing** | **Fast / Light**<br>*(Gemini Flash, Haiku, GPT-4o-mini)* | Run extraction, compose atlases, execute Python validation scripts, move files. Strictly follow exact command templates; do not invent arguments. |
| **Manifest & JSON Updates** | **Fast / Light**<br>*(Gemini Flash, Haiku, GPT-4o-mini)* | Update `progress.md`, `images.md`, or metadata files with targeted edits. |
| **Prompt Crafting & Visual QA** | **Reasoning / Frontier**<br>*(Gemini Pro, Claude Sonnet, GPT-4o, o3-mini)* | Author state-specific prompts for `$imagegen`, evaluate visual character adherence, review motion continuity, resolve chroma despill artifacts. |
| **Troubleshooting & Architecture** | **Reasoning / Frontier**<br>*(Gemini Pro, Claude Sonnet, GPT-4o, o3-mini)* | Debug layout coordinate drift, frame clipping, non-deterministic regressions. |

### Model Guardrails
- **If you are a Fast/Light model**: If any script returns a non-zero exit code or validation fails with `ok: false`, **halt immediately**. Do not hallucinate fixes or bypass checks; report the first 3 lines of stderr.
- **If you are a Frontier model**: Respect the established pipeline and existing scripts. Do not write custom ad-hoc image slicers if standard `hatch-pet` scripts exist.

---

## 3. Core Technical Invariants (Codex Pet v2)

Every agent must respect these non-negotiable standards:

- **Atlas Geometry**:
  - Total Dimensions: **1536 × 2288 px** (8 columns × 11 rows).
  - Cell Size: **192 × 208 px** (stride-aligned).
  - Version: `spriteVersionNumber: 2` in `pet.json`.
- **Row Mapping**:
  - `Row 0`: `idle` (6 frames)
  - `Row 1`: `running-right` (8 frames)
  - `Row 2`: `running-left` (8 frames)
  - `Row 3`: `waving` (4 frames)
  - `Row 4`: `jumping` (5 frames)
  - `Row 5`: `failed` (8 frames)
  - `Row 6`: `waiting` (6 frames)
  - `Row 7`: `running` (6 frames — coding magic inside orb, NOT sprinting)
  - `Row 8`: `review` (6 frames)
  - `Row 9`: `look-row-9` (8 frames: `000°` up to `157.5°` clockwise)
  - `Row 10`: `look-row-10` (8 frames: `180°` down to `337.5°` clockwise)
- **Visual Identity (Avari)**:
  - Long white hair (`#F2F0E8` / shadow `#A8B4B7`), pointed elf ears, adult serene expression.
  - Deep sapphire eyes (`#123B80`).
  - Midnight teal-navy cloak (`#06141B`, `#0A1D26`, `#102833`) with muted old gold trim (`#D9B96E`).
  - **Magic Artifact**: exactly **one solid bluish glass sphere** held in hands, with glowing gold code `{<>}` inside.
  - **Strict Avoidances**: no floating particles outside the sphere, no runes in mid-air, no pixel art, no shadows on the ground, flat `#FF00FF` magenta chroma background.

---

## 4. Directory Structure & Working Boundaries

```text
avari-pet/
├── DESIGN.md              # Canonical visual specification (read-only reference)
├── actions.md             # Motion & state definitions (read-only reference)
├── plan_260909_full.md    # Active release checklist & punch list
├── progress.md            # High-level tracking status
├── images.md              # Image generation audit log
├── run/                   # BASELINE RUN (READ-ONLY ARCHIVE — DO NOT OVERWRITE)
└── run_260909/            # ACTIVE RUN DIRECTORY (perform all current operations here)
    ├── decoded/           # Despilled/extracted strip assets
    ├── final/             # Final assembled spritesheet & validation JSONs
    ├── frames/            # Extracted individual frame directories per row
    ├── prompts/           # Row-specific prompt definitions
    ├── qa/                # QA review sheets, contact sheets, blind QA verdicts
    └── references/        # Layout guides and canonical base references
```

---

## 5. Tooling & Execution Cheat Sheet

### Environment Setup
Always activate the local virtual environment or use the Python runtime containing `Pillow`:
```bash
source .venv/bin/activate
# Verify Pillow is present
python3 -c "import PIL; print('Pillow OK')"
```

### Hatch-Pet Script Suite
Scripts are installed at:
`/Applications/ChatGPT.app/Contents/Resources/skills/skills/.curated/hatch-pet/scripts`

Store the path in a variable:
```bash
HATCH_SCRIPTS="/Applications/ChatGPT.app/Contents/Resources/skills/skills/.curated/hatch-pet/scripts"
```

### Common Commands

1. **Extract frames from a row strip**:
   ```bash
   python3 "$HATCH_SCRIPTS/extract_strip_frames.py" \
     --strip-image run_260909/decoded/<row_name>.png \
     --output-dir run_260909/frames/<row_name>/ \
     --frame-count <N> --cell-width 192 --cell-height 208
   ```

2. **Despill magenta chroma edges**:
   ```bash
   python3 "$HATCH_SCRIPTS/despill_chroma_edges.py" \
     --input-image <raw_chroma.png> \
     --output-image <despilled.png> \
     --chroma-key "#FF00FF"
   ```

3. **Assemble full 8×11 v2 atlas**:
   ```bash
   python3 "$HATCH_SCRIPTS/assemble_extended_atlas.py" \
     --config run_260909/atlas-config.json \
     --output-dir run_260909/final/
   ```

4. **Validate atlas (Hard Release Gate)**:
   ```bash
   python3 "$HATCH_SCRIPTS/validate_atlas.py" \
     --atlas-image run_260909/final/spritesheet.png \
     --require-v2 \
     --cell-width 192 --cell-height 208 \
     --output-json run_260909/final/validation-extended.json
   ```

5. **Generate animation previews & contact sheets**:
   ```bash
   python3 "$HATCH_SCRIPTS/render_animation_previews.py" \
     --frames-manifest run_260909/frames/frames-manifest.json \
     --output-dir run_260909/qa/
   ```

---

## 6. Golden Rules & Prohibitions

1. **No Single-Cell Patchwork**: Never replace an individual cell in an 8-frame row with a cell from a different generation run. Rows must maintain uniform lighting, scale, and motion registration.
2. **No Baseline Pollution**: Never touch or delete `run/`. All new outputs go into `run_260909/`.
3. **No Intermediate Releases**: Never distribute or install an 8×9 atlas as a v2 pet. Release requires all 11 rows and passing `--require-v2` validation.
4. **Atomic Installation**: When deploying to `~/.codex/pets/avari/`, back up any existing installation first and write new files atomically.
