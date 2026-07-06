# Multi-Agent Pipeline: Handwritten Notes → LaTeX PDF

## Project Goal

Build a reusable multi-agent framework that converts handwritten notes (paper, whiteboard, or chalkboard photos/scans in PDF form) into legible, well-segmented, LaTeX-compiled PDF outputs.

This document is the master plan for the first pass. It is written to be **agent-readable**: an orchestrating agent should be able to read this file and execute the pipeline stages in order. It is also meant to be **edited and reused** — swap in your own input files, agent counts, or output conventions as needed.

---

## Agents

| Agent | Role |
|-------|------|
| **Prime Agent** (orchestrator) | Runs the pipeline end to end: ingests input PDFs, performs segmentation, submits work for review, applies feedback, assembles final outputs. |
| **Reviewer Agents ×3** (physics-PhD-level experts) | Independently inspect the segmented PNG outputs for legibility, correct segmentation, and faithful capture of the physics/math content. Each returns explicit feedback and an APPROVE / REVISE verdict. |
| **Final Review Agents ×5** (physics-PhD-level experts) | Independently inspect the compiled LaTeX PDF from Stage 5 for correctness, legibility, and fidelity to the source notes. Each returns abundant, scrutinized feedback until all five approve. |

---

## Pipeline Stages

### Stage 0 — Ingest
Feed the handwritten / board-written PDF files into the framework.

- **Input:** one or more source PDFs (handwritten pages, whiteboard/chalkboard photos).
- **Action:** register the files, verify they are readable, and stage them for segmentation.

### Stage 1 — Segment to PNG
Create (or invoke) a **segmentation skill/extension** that splits each page into legible, readable PNG files.

- Segment by logical unit (equation block, diagram, paragraph of notes) so each PNG is independently readable.
- **Overlap is allowed and encouraged** where it improves readability — adjacent segments may share content rather than cutting a figure or equation in half.
- **Output:** a set of PNG files per source page, with a naming scheme that preserves page order and segment order (e.g. `page03_seg02.png`).

### Stage 2 — Expert Review Loop
The Prime Agent's PNG output is scrutinized by the **3 physics-PhD-level reviewer agents**.

- Each reviewer examines every PNG for legibility, segmentation quality, and content fidelity, and returns concrete feedback.
- Reviewers must be PhD-level physics experts and act as heavily strict, serious critics — scrutinizing the segmentation, the underlying physics, and the logic of the material.
- Reviewers also check that segment overlap is used correctly: enough overlap to avoid losing information at segment boundaries, without being excessive.
- **Loop condition:** Stages 1 ↔ 2 repeat — the Prime Agent re-segments per the feedback — until **all reviewers approve**. Only then does the pipeline advance.
- Keep a short log of each review round (round number, feedback given, changes made) so the loop is auditable.

### Stage 3 — Assemble Reviewed PDF
Paste the approved PNGs, in order, into a single compiled PDF.

- **Output:** one PDF containing all approved segments in reading order.

### Stage 4 — Mathpix-Ready Staging (Alternate Path A)
Copy the final pictures and the assembled PDF into a directory named **`mathpix_ready/`** (create it if it does not exist).

- **Verify** the contents actually meet Mathpix input requirements (supported formats, resolution, file sizes) — don't just copy blindly.
- **Alternate path:** these files can be sent to Mathpix to produce a `.tex` document, which a separate AI agent then cleans up/fixes and compiles to PDF. This branch is optional and runs outside this pipeline.

### Stage 5 — Direct LaTeX Compilation (Primary Path B)
Instead of (or in addition to) the Mathpix route: take the final PDF / pictures and produce a **LaTeX-compiled PDF** directly.

- Transcribe the approved content into a `.tex` document, compile it, and confirm it builds cleanly.
- Once compiled, **5 physics-PhD-level agents** heavily scrutinize the result and give abundant, rigorous feedback.
- **Loop condition:** if any expert requests changes, the pipeline is re-run from the appropriate earlier stage until **all 5 experts agree** the compiled PDF is correct.
- Between rounds, the Prime Agent revises by re-reading the original notes and consulting the web or its training data on the underlying physics — to better understand the content and resolve the experts' feedback before the next review pass.
- Place the `.tex` source and compiled PDF into **`Final_Product_Ready/`** (create it if it does not exist).

---

## Directory Conventions

```
project_root/
├── input/                 # Stage 0: source handwritten/board PDFs
├── segments/              # Stage 1–2: segmented PNGs (per review round)
├── assembled/             # Stage 3: reviewed, assembled PDF
├── mathpix_ready/         # Stage 4: verified Mathpix-ready files (alt path)
└── Final_Product_Ready/   # Stage 5: final .tex + compiled LaTeX PDF
```

(Only `mathpix_ready/` and `Final_Product_Ready/` are required names from the original plan; the rest are suggested and may be renamed.)

---

## Success Criteria

1. Every source page is represented by legible, well-segmented PNGs.
2. All 3 reviewer agents have approved the segments (review loop closed).
3. An assembled PDF of approved segments exists.
4. `mathpix_ready/` contains verified, Mathpix-compatible copies of the final assets.
5. `Final_Product_Ready/` contains a `.tex` source and a cleanly compiled LaTeX PDF.
6. All 5 final-review agents have approved the compiled LaTeX PDF (Stage 5 loop closed).

---

## Reuse Notes

- This outline is a **rough-draft template**: anyone should be able to reuse it by pointing Stage 0 at their own PDFs and re-running the pipeline.
- The segmentation skill (Stage 1), the reviewer agent prompts (Stage 2), and the assembly/compilation steps (Stages 3–5) should each be built as separable, reusable components so the process works universally across courses, note styles, and subjects.
- The number and specialty of reviewer agents (default: 3 × physics PhD) is configurable — adjust to match the subject matter of the notes.
