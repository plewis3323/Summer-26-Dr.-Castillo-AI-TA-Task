# Pipeline run — 2026-07-30

Input: `Input/Lecture-241015_comp.pdf` — one whiteboard photograph, Goldstein
Ch. 3, motion in a central potential and the Kepler problem.
Slug: `central_potential`. One input → one output document.

## Stage 0 — Ingest

`segments/`, `assembled/` and `Final_Product_Ready/` from the previous job were
archived to `Run_Archive/2026-07-30_192828/` before anything ran. The reusable
`goldsteinnotes.sty` preamble was carried forward; everything else started clean.

The source PDF wraps a single 2356×932 JPEG. Rendering the page would have
resampled it, so the embedded image was extracted at native resolution and
cropped to the board (`segments/central_potential/pages/page-1.png`, 2340×875).
Segment crops are upscaled 2.5× on save, which is where the legibility comes
from — there is no more detail in the source than that.

## Stage 1–2 — Segmentation and the 3-reviewer loop

Three rounds. Full audit trail in `segments/review_log.md`; the region model is
documented in `segments/central_potential/SEGMENT_MAP.md`.

The board is written in five columns across two panels, **but only in its upper
two-thirds**. Below y ≈ 550 the writing of columns 1–3 becomes lines running
horizontally *across* those columns. Round 1 imposed a column grid on the whole
board and all three reviewers independently rejected it for the same reason: the
grid sliced those lines. The worst case was the boxed generic trajectory
equation, cut so that its leading minus sign and `ℓ²/μ` prefactor appeared in no
crop at all — a transcriber would have emitted a sign-wrong, prefactor-less
equation with nothing to signal the loss.

That drove a rewrite of the segmenter. `tools/segment_regions.py` cuts by
explicit region rectangles instead of column windows, and supports an `atomic`
flag meaning "emit as one crop, never subdivide". The flag exists because a
whitespace-valley finder reads a diagram as a tall inked block and will cut it
wherever the arithmetic lands — which is exactly how round 2 lost the apsidal
ellipse across a seam, the same wholeness failure as round 1 applied to a figure
rather than an equation. Naming the rectangle is the only reliable guarantee.

Round 3 passed 3/3. All three reviewers ran mechanical checks rather than
inspection — connected-component wholeness tests against every crop rectangle,
and pixel-differencing the crop union against the ink mask — and agreed: zero
uncovered ink, every equation, box border, bracket, label and figure whole in at
least one of the 24 segments.

## Stage 3 — Assembly

`assembled/central_potential_approved.pdf`, 24 approved segments in reading
order.

## Stage 4a — Reference convention

**Goldstein, Poole & Safko, _Classical Mechanics_, 3rd ed., Ch. 3.** Put to an
adversarial challenge, which argued the case against at full force before
conceding: the board's two most frequent symbols, φ and μ, both disagree with
Goldstein's chapter text (θ and m), and Taylor ch. 8 matches φ, μ and ℓ with no
relabelling at all.

The challenge failed on the observation that symbol names carry no structural
information, while everything a reference convention actually buys is
Goldstein's and uniquely his: the Binet equation in the potential-derivative
form `u'' + u = −(μ/ℓ²) d/du V(1/u)` (Taylor and Marion & Thornton both write the
force form); the intermediate `−F(1/u) = (ℓ²/μ)u²[u + u'']` that Goldstein passes
through to reach it; V rather than U for the potential; `V = −k/r` with k the
attractive constant; `e ≡ √(1 + 2ℓ²E/μk²)` symbol-for-symbol; the shifted-oscillator
route; and "apsidal" as vocabulary. The board reproduces the derivation's shape,
not just its endpoint.

The ruling that governed transcription: **the lecturer's symbol wins wherever it
differs.** φ not θ, μ not m, capital F, A for the oscillator amplitude, ũ for the
shifted variable, "absidal" with a *b*, the `= 1/r` tag appended to both boxed
orbit solutions, `μk` in the last box against `kμ` elsewhere left unnormalised,
the shorthand `[u + du/dφ²]` standing beside `[u + d²u/dφ²]`, and "universal
method" as the name for the quadrature pair.

## Stage 4b–4c — Transcription and the 5-referee loop

`Final_Product_Ready/hc6001_2024-10-15_central_potential_kepler.{tex,pdf}` —
4 pages, 35 numbered equations, 2 figures, clean compile with no overfull or
underfull boxes and no unresolved references.

Four rounds, five referees each, unanimous approval only at round 4.

**Round 1 (0/5).** All five found the same blocking defect: equation (33) had
silently dropped `du/dφ =` from the source line. The board writes
`du/dφ = (u′)² = √( · − )`, which is mathematically false as written — and the
transcription had resolved the lecturer's slip by deleting it. A correction
disguised as an omission, and precisely the drift the panel exists to catch. The
line was restored as written. Also: both figures were geometrically wrong, two
source labels were printed twice, and the captions had imported vocabulary
("turning points", "reference direction") the board never uses.

**Round 2 (1/5).** Four referees caught a TikZ regression — a `\node[rotate=-17]`
added to "compensate" for the picture's canvas rotation, which TikZ never applies
to node text, so the compensation itself sheared the labels. One referee went
further and showed Figure 2 was drawing `r₀` as the apsis-to-apsis major axis
with the angle vertex sitting *on* the ellipse, where the board puts the vertex
at an interior point and `r₀` is a radius out to the apsis. Since `r₀ = 1/u₀` is
a radial distance, the figure contradicted the equation it illustrated. That was
a single dissenting voice and it was right.

**Round 3 (0/5).** Two defects, both found by measurement rather than inspection.
The redrawn figure still marked no angle — a straight arrow left the vertex at
10° while `r₀` left it at 19°, so the arrow ended in white space. And the strut
added in round 2 to separate a fraction rule from a radical vinculum was proven
**inert**: two referees deleted it and rendered a pixel-identical PDF. It was
raised until it engaged, and the result measured at 300 dpi (7.9 pt of clear
separation, against 1.7 pt with the strut removed) rather than eyeballed.

**Round 4 (5/5).** Approved. Referees verified the figure geometry analytically
from the TikZ coordinates, repeated the strut-deletion test, re-derived every
boxed result from scratch, and confirmed zero provenance language in the
rendered document.

## Success criteria

| # | Criterion | Status |
|---|---|---|
| 1 | Previous job archived before the run | `Run_Archive/2026-07-30_192828/` |
| 2 | Every source region legibly segmented | 24 segments, 0 uncovered ink |
| 3 | All 3 segmentation reviewers approved | round 3, 3/3 |
| 4 | Assembled PDF per input | `assembled/central_potential_approved.pdf` |
| 5 | `.tex` + compiled PDF per input | both present, clean compile |
| 6 | 1:1 input→output mapping | 1 input PDF → 1 output PDF |
| 7 | Reference textbook named, justified, challenged | Goldstein Ch. 3, endorsed after adversarial review |
| 8 | Predominantly source content, additions minimal | additions are connectives and two float citations |
| 9 | No provenance language anywhere | verified by grep and by reading all rendered pages |
| 10 | Opens directly with the content | title → §3.1 → Eq. (3.1) |
| 11 | All 5 final referees approved | round 4, 5/5 |
| 12 | Parallel subagent chains where inputs allow | single input this run; no parallel chains needed |

## What the review loops bought

Every blocking defect across both loops was of one kind: **something was lost or
misrepresented in a way the downstream stage could not have detected.** A boxed
equation cropped so the missing sign and prefactor were cropped away with it. A
figure sliced across a seam. A false line in the source quietly repaired. A
figure asserting a geometry that contradicted its own equation. A typographic
fix that changed nothing at all.

Three of those survived at least one reviewer's approval, and two were caught by
a single dissenting voice against four. The panel size is what did the work.
