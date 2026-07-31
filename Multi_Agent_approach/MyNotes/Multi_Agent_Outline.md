# Multi-Agent Pipeline: Handwritten Notes → LaTeX PDF

## Project Goal

Build a reusable multi-agent framework that converts handwritten notes (paper, whiteboard, or chalkboard photos/scans in PDF form) into legible, well-segmented, LaTeX-compiled PDF outputs.

This document is the master plan for the first pass. It is written to be **agent-readable**: an orchestrating agent should be able to read this file and execute the pipeline stages in order. It is also meant to be **edited and reused** — swap in your own input files, agent counts, or output conventions as needed.

---

## Operating Principles

These apply to every stage of the pipeline:

1. **Speed with precision.** The job should run relatively fast without sacrificing quality. Parallelize wherever stages or inputs are independent; reserve careful sequential work for the steps that actually need it (review loops, final compilation).
2. **Batch inputs, parallel subagents.** The pipeline accepts **multiple input PDFs at a time**. The Prime Agent should spawn **as many subagents as needed** to run the process chain concurrently across inputs (e.g., segment/review each source PDF in parallel), keeping the run both fast and high-quality.
3. **Archive before you run.** If directories from old or previous jobs exist (`segments/`, `assembled/`, `Final_Product_Ready/`, etc.), **archive them first** (e.g., move into a timestamped `Run_Archive/` folder), then execute the whole process fresh.
4. **Source content dominates.** The final LaTeX PDF is **overwhelmingly the content of the source notes themselves** — every equation, derivation step, diagram, and remark that appears in the source must appear in the output. Material not present in the source is added **only when it is genuinely needed** to make a step followable, and when added it must be **very concise** (a clause or a single short sentence). If a passage can stand without the addition, leave the addition out.
5. **No meta-introduction.** The final notes document must **not** open with an intro describing what the agents did or how the pipeline works — it gets right into the notes.
6. **Self-contained voice — never reference the source medium.** The document must read as a standalone physics text. It must **never** refer to where the material came from. Phrases such as *"in the original notes,"* *"on the board,"* *"as written in the notes,"* *"the notes show,"* *"from the lecture,"* *"the handwritten page,"* *"as drawn above in the notes,"* or any equivalent are **forbidden** anywhere in the output — body text, figure captions, footnotes, and section titles alike. Describe the physics directly ("The trajectory is sketched in Fig. 2"), not its provenance.
7. **One output document per input document.** Each source PDF is a distinct topic and gets its **own** end-to-end chain and its **own** final `.tex` + compiled PDF. Three input PDFs covering three topics produce three output documents — never one merged document, never a split of one input across several. The mapping is strictly 1:1.

---

## Agents

| Agent | Role |
|-------|------|
| **Prime Agent** (orchestrator) | Runs the pipeline end to end: ingests input PDFs, performs segmentation, submits work for review, applies feedback, assembles final outputs. |
| **Reviewer Agents ×3** (physics-PhD-level experts) | Independently inspect the segmented PNG outputs for legibility, correct segmentation, and faithful capture of the physics/math content. Each returns explicit feedback and an APPROVE / REVISE verdict. |
| **Final Review Agents ×5** (physics-PhD-level experts) | Independently inspect **each** compiled LaTeX PDF from Stage 4 for correctness, legibility, and fidelity to the source. They also act as journal/publisher referees: they heavily scrutinize whether the document follows the notation conventions of the reference textbook chosen in Stage 4 and whether its typesetting is **publication-ready by a major physics publisher's standard** — while confirming the content is drawn from the source with only sparse, very concise additions, contains **no reference to notes/boards/lectures/pages**, and opens directly with the content, with no agent/pipeline introduction. Each returns abundant, scrutinized feedback until all five approve. |

---

## Pipeline Stages

### Stage 0 — Ingest
Feed the handwritten / board-written PDF files into the framework.

- **Input:** one or more source PDFs (handwritten pages, whiteboard/chalkboard photos). Multiple inputs may be submitted in a single run and processed in parallel.
- **Pre-flight:** if working directories from a previous job exist, archive them (timestamped `Run_Archive/` folder) before starting, so the new run begins clean.
- **Action:** register the files, verify they are readable, and stage them for segmentation. Assign each input to its own subagent chain so independent inputs move through the pipeline concurrently.
- **One chain per input.** Give each source PDF a short topic slug (e.g. `oscillations`, `rotations`, `scattering`) derived from its subject matter, and carry that slug through every stage: its own segment directory, its own assembled PDF, its own `.tex`, its own compiled PDF. Inputs are **never merged** into a shared document, and a single input is **never split** across multiple documents.
- **Manifest:** the Prime Agent records the input → slug → output-document mapping up front and verifies at the end that the count of final PDFs equals the count of input PDFs.

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
Paste the approved PNGs, in order, into a compiled PDF — **one per input document**.

- **Output:** for each source PDF, one assembled PDF containing that input's approved segments in reading order. Assembled PDFs from different inputs are never combined.

### Stage 4 — Direct LaTeX Compilation
Take the final PDF / pictures and produce a **LaTeX-compiled PDF** directly.

**Step 4a — Choose the reference textbook convention (before writing any LaTeX):**

- The Prime Agent first identifies the standard physics textbook(s) whose subject matter **best matches the content of the class notes** (e.g., Griffiths for E&M or QM, Taylor for classical mechanics, Jackson for graduate E&M, Sakurai for graduate QM, Kittel/Ashcroft & Mermin for solid state).
- **The textbook serves two purposes only:** (1) **context** — it helps the agents learn and understand the material in the notes; and (2) **notation conventions** — it fixes the symbols, vector/tensor notation, unit system (SI vs. Gaussian), and equation-formatting style used when transcribing. It is **not** a license to rewrite the notes in the textbook's voice or structure — the content itself stays faithful to the original notes.
- This choice must itself be **heavily scrutinized**: the Prime Agent must state which textbook(s) it chose, why they best match the notes, and the reviewer agents must challenge that choice before transcription begins.

**Step 4b — Transcribe and compile in that convention:**

- **One `.tex` per input document.** Each source PDF is transcribed into its own `.tex` file and compiled to its own PDF, named with that input's topic slug. Do not merge topics into a combined document.
- Transcribe the approved content into a `.tex` document using the chosen textbook's **notation conventions**, keeping the material **as close to the original notes as possible**. Do not restructure, expand, or rewrite the notes into textbook prose.
- **The body is the source content.** Transcribe what is actually there — every equation, intermediate step, diagram, label, and marginal remark. Do not drop steps because they seem obvious, and do not import textbook material the source does not cover.
- **Additions are the exception, not the rule.** Add a clarifying line only when a step is otherwise unfollowable (e.g. an unstated substitution or an undefined symbol). When you do, keep it to a clause or one short sentence, in the same notation, and place it adjacent to the step it serves. Prefer a shorter addition over a longer one; prefer no addition over a short one. A reader should not be able to tell added lines from transcribed ones by their length or tone.
- **Never reference the source medium.** The prose must not mention notes, boards, lectures, pages, scans, or handwriting — see Operating Principle 6. Write about the physics directly. Cross-references point to the document's own numbered equations and figures ("substituting into Eq. (12)", "see Fig. 3"), never to the source material or to its physical layout ("the box at the bottom of the page", "the sketch on the right").
- The document must **start directly with the notes content** — no introduction describing what the agents did, how the pipeline works, or how the document was produced.
- Compile it and confirm it builds cleanly (no errors, no unresolved references, no overfull-box sloppiness in the final PDF).
- **Self-check before review:** grep the `.tex` for banned provenance wording (`original notes`, `the notes`, `on the board`, `blackboard`, `whiteboard`, `handwritten`, `the lecture`, `the lecturer`, `as shown above in the`, `the page`, `the scan`) and rewrite every hit before handing off to the reviewers.

**Step 4c — Publication-readiness review:**

- Once compiled, **5 physics-PhD-level agents** heavily scrutinize the result and give abundant, rigorous feedback.
- The evaluation bar is explicit and strict: the final product must be judged **publication-ready by the standard of a major physics publisher** (e.g., Springer, Cambridge University Press, Pearson, APS journals) **in typesetting quality** — typography, notation consistency, and physical correctness — while the **content remains a faithful rendering of the original notes**, not a textbook rewrite.
- Each reviewer must explicitly verify and report on **all five**:
  1. **Coverage and fidelity** — the document tracks the source closely: nothing in the source is missing, and nothing is restructured or rewritten into textbook prose.
  2. **Restraint in additions** — any material not in the source is genuinely necessary and very concise. A reviewer who finds padding, generic textbook exposition, or an added paragraph where a clause would do must call it out and issue REVISE.
  3. **No provenance language** — the document nowhere refers to notes, boards, lectures, pages, scans, or handwriting. Reviewers scan the text (including captions and footnotes) for this and treat **any** occurrence as an automatic REVISE.
  4. **Convention and typesetting** — adherence to the reference textbook's notation conventions and publisher-grade typesetting quality.
  5. **No meta-introduction** — the document opens directly with the content, with nothing about the agents or the pipeline.
- Reviewers evaluate **each output document separately** and also confirm the 1:1 mapping: one final PDF per input PDF, with no topics merged and none split.
- **Loop condition:** if any expert requests changes, the pipeline is re-run from the appropriate earlier stage until **all 5 experts agree** the compiled PDF is correct **and publication-ready**.
- Between rounds, the Prime Agent revises by re-reading the original notes and consulting the web or its training data on the underlying physics — to better understand the content and resolve the experts' feedback before the next review pass.
- Place the `.tex` source and compiled PDF into **`Final_Product_Ready/`** (create it if it does not exist).

---

## Directory Conventions

```
project_root/
├── input/                 # Stage 0: source handwritten/board PDFs (one per topic)
├── segments/
│   ├── <slug-a>/          # Stage 1–2: segmented PNGs for input A
│   └── <slug-b>/          #            ... for input B
├── assembled/             # Stage 3: one assembled PDF per input (<slug>.pdf)
├── Final_Product_Ready/   # Stage 4: one .tex + one compiled PDF per input
└── Run_Archive/           # Pre-flight: archived directories from previous jobs (timestamped)
```

Everything downstream of Stage 0 is **partitioned by input slug** — segments, assembled PDFs, and final documents each carry the slug of the input they came from, so the 1:1 input→output mapping is visible in the file tree.

(Only `Final_Product_Ready/` is a required name from the original plan; the rest are suggested and may be renamed.)

---

## Success Criteria

1. Any directories left over from previous jobs were archived before the run started.
2. Every source page is represented by legible, well-segmented PNGs.
3. All 3 reviewer agents have approved the segments (review loop closed).
4. An assembled PDF of approved segments exists **for each input**.
5. `Final_Product_Ready/` contains a `.tex` source and a cleanly compiled LaTeX PDF **for each input**.
6. **The input→output mapping is 1:1:** the number of final PDFs equals the number of input PDFs, no two inputs were merged into one document, and no single input was split across documents.
7. The `.tex` document uses the notation conventions of an explicitly named reference textbook that best matches the notes' subject matter (Stage 4a), the textbook was used for context and notation only, and that choice was reviewed and justified.
8. The final PDF is predominantly the source content, with additions only where a step would otherwise be unfollowable and each addition kept very concise.
9. **No output document contains any reference to notes, boards, lectures, pages, scans, or handwriting** — in body text, captions, footnotes, or headings.
10. Each final PDF opens directly with the content — no introduction about the agents or pipeline.
11. All 5 final-review agents have approved every compiled LaTeX PDF as **publication-ready by a major physics publisher's standard** in typesetting quality (Stage 4 loop closed).
12. When multiple input PDFs were supplied, they were processed in parallel by subagent chains without loss of quality.

---

## Reuse Notes

- This outline is a **rough-draft template**: anyone should be able to reuse it by pointing Stage 0 at their own PDFs and re-running the pipeline.
- The segmentation skill (Stage 1), the reviewer agent prompts (Stage 2), and the assembly/compilation steps (Stages 3–4) should each be built as separable, reusable components so the process works universally across courses, note styles, and subjects.
- The number and specialty of reviewer agents (default: 3 × physics PhD) is configurable — adjust to match the subject matter of the notes.
- The 1:1 input→output rule is what makes the pipeline scale: drop *n* topic PDFs into `input/`, get *n* self-contained documents back. Batching topics into one file is never the right call, even when the topics are related.
- The reference-textbook convention (Stage 4a) generalizes too: for non-physics notes, match against the standard textbook of that field and hold the final PDF to the same publication-ready bar from that field's major publishers.
