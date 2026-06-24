---
name: physics-notes-organizer
description: Organize disorganized graduate-level physics handwritten notes into AI-readable OrganizedNotes packages with segmented blocks, metadata, and preserved handwriting. Use when converting professor lecture notes, whiteboard photos, or scan sets into structured output for Mathpix or LaTeX conversion.
---

# Physics Notes Organizer

Transform raw handwritten physics notes (paper, whiteboard, scans) into an **OrganizedNotes** package that an AI can process reliably while preserving the professor's original handwriting.

## When to use

- User has disorganized or partially organized physics lecture notes (images/scans)
- User wants Step 1 of the pipeline: structured, AI-readable organization before LaTeX/PDF
- User mentions segmenting notes, block metadata, manifest files, or preparing notes for Mathpix

## Output location

Create packages under:

```
OrganizedNotes/<lecture_id>/
├── manifest.yaml
├── source/                 # original scans, unmodified
└── blocks/
    └── block_NNN/
        ├── image.png       # cropped handwritten segment
        └── meta.yaml
```

Schema reference: [Main_Project/schemas/organized_notes_schema.yaml](../../Main_Project/schemas/organized_notes_schema.yaml)

Example: [Main_Project/examples/sample_lecture/](../../Main_Project/examples/sample_lecture/)

## Workflow

### 1. Ingest

- Collect all source images (photos of paper, whiteboard, PDF exports).
- Copy originals unchanged into `OrganizedNotes/<lecture_id>/source/`.
- Name pages consistently: `page_01.jpg`, `page_02.jpg`, etc.

### 2. Segment into blocks

Split notes on **graduate-physics semantics**, not arbitrary page breaks:

| Split when you see | content_type |
|--------------------|--------------|
| Named definition or term | `definition` |
| Stated result without full proof | `theorem` |
| Multi-step mathematical argument | `derivation` |
| Standalone or key displayed equation | `equation` |
| Sketch, graph, or figure | `diagram` |
| Worked problem or numeric instance | `example` |
| Side note, reminder, or aside | `remark` |
| Illegible or ambiguous content | `unclear` |

**When ambiguous:** keep the block intact, set `confidence: low`, add `review_notes`. Do not merge unrelated content or split mid-derivation without a clear boundary.

### 3. Preserve handwriting

- Each block gets a cropped `image.png` showing the professor's handwriting for that segment.
- Set `handwriting_preserved: true` on every block (required invariant).
- Never replace handwriting with transcription-only output at this stage.

### 4. Write metadata

**manifest.yaml** — lecture level:

```yaml
lecture_id: phys6801_2026-01-15_lagrangian
course: PHYS 6801 — Classical Mechanics
topic: Lagrangian mechanics and the principle of least action
date: "2026-01-15"
source_pages:
  - page_01.jpg
reading_order:
  - block_001
  - block_002
sections:
  - id: action_principle
    title: Principle of least action
    block_ids: [block_001, block_002]
physics_context:
  prerequisites: [Newtonian mechanics, variational calculus]
  notation: ["S for action", "L for Lagrangian"]
conversion_path_hint: mathpix
```

**blocks/block_NNN/meta.yaml** — per block:

```yaml
block_id: block_001
section: action_principle
reading_order: 1
content_type: definition
source_ref:
  page: page_01.jpg
  region: top half of page
ai_summary: Defines the action S as the time integral of the Lagrangian L.
handwriting_preserved: true
equations_detected:
  - "S = integral of L dt"
confidence: high
```

Optional fields: `extracted_text_guess`, `depends_on`, `review_notes`.

### 5. Validate

Before finishing, check:

- [ ] Every source page appears in at least one block's `source_ref.page`
- [ ] `reading_order` in manifest lists every block exactly once
- [ ] `reading_order` integers in block meta match manifest order
- [ ] Every block has `image.png` and `meta.yaml`
- [ ] Low-confidence blocks are flagged, not silently merged or dropped
- [ ] No block was dropped (margin notes → `remark` or `unclear`)

## Downstream handoff

**Path 3a — Mathpix:** Batch OCR each `blocks/block_NNN/image.png` → raw `.tex` per block → merge in `reading_order`.

**Path 3b — Direct LaTeX agent:** Feed `manifest.yaml`, all `meta.yaml` files, and block images. Use summaries as hints; **images remain authoritative** for math content.

## Graduate physics tagging tips

- A derivation that states a theorem mid-stream: use `derivation`; reference the theorem block in `depends_on`.
- Multiple equations on one line about the same idea: one `equation` block unless they are clearly separate topics.
- Whiteboard erasures or overwritten text: keep visible content, note ambiguity in `review_notes`.
- Non-linear board layout: use `reading_order` to impose narrative order; ignore spatial left-to-right if the professor jumped around.

## Standalone prompts

For manual use outside Cursor, see:

- [Original_Prompts_Precontext_files/organize_notes_system_prompt.md](../../Original_Prompts_Precontext_files/organize_notes_system_prompt.md)
- [Original_Prompts_Precontext_files/organize_notes_user_template.md](../../Original_Prompts_Precontext_files/organize_notes_user_template.md)
