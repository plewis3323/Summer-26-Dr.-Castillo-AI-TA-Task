# mathpix_ready/ — Stage 4 staging (alternate path, unused beyond staging)

Contents: 20 approved segment PNGs (run 2, independent segmentation — see
`../segments/review_log.md`) + the Stage 3 assembled PDF
(`hc6001_2024-10-22_scattering_hamiltonian_assembled.pdf`).

## Mathpix compatibility check
- **Format:** all 20 images are PNG; the assembled file is a standard PDF. Both are
  natively supported Mathpix input formats.
- **Resolution:** all segments are 1700px wide (200dpi page render width), heights
  range 300–900px. Well within Mathpix's supported image dimension range
  (it accepts roughly 30px–10000px per side) — high enough for legible OCR of
  handwritten math, not so large as to be rejected or throttled.
- **File size:** each PNG is well under 250KB; the assembled PDF is ~3.4MB. Both are
  far under Mathpix's per-file size limits (PNGs: single-digit MB; PDFs: tens of MB).
- **Page count:** the assembled PDF has 20 pages (one segment per page), consistent
  with the 20 approved segments.

All checks pass — this directory is Mathpix-ready. Per `Multi_Agent_Outline.md` Stage 4,
this branch is optional and was not pursued further in this run; the primary deliverable
is the direct-LaTeX path in `../Final_Product_Ready/`.
