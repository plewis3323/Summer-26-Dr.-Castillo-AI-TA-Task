# Stage 2 — Review Round 2

Round 1 closed with `scattering` approved 3/3 and the other three documents unanimously REVISE.
Every blocking issue in round 1 was the same defect class: **a figure or boxed result bisected,
appearing whole in no single segment.**

## Root cause and fix

When a page offered no whitespace valley, `split_tall` fell back to *evenly spaced* cuts, which
land on content by definition. The segmenter was rewritten to:

1. **Cut only in blank gaps between ink bands** — never inside a continuously inked block. A
   band is what a diagram, a boxed result or a bracketed matrix looks like to the profiler.
2. **Keep an oversized but internally gapless block whole** rather than slicing it. Required by
   `rotations` p. 9, where the Euler-angle figure and the text above it form a single
   continuously inked 1252 px block with no blank row anywhere inside — verified at every gap
   threshold from 20 px down to 6 px. Any ceiling below ~2.1× `max_h` forces a cut straight
   through the figure that defines the α/β/γ convention for the next four pages.
3. **Widen the whiteboard column seam** from 140 px to 500 px, and move the column-1/column-2
   boundary to x = 1080.
4. Raise the minimum overlap to 90 px (round 1 had boundaries as thin as 51 px, which one
   reviewer called "luck rather than margin").

Segment counts fell as a result — larger, more atomic segments:
`oscillations` 39 → 27, `rotations` 62 → 48, `comp1015` 20 → 10. `scattering` is unchanged and
keeps its round-1 approval.

Fixes were verified against the crop manifest (`segment_manifest.json`) rather than by eye, and
`tools/check_coverage.py` re-confirmed no page lost handwriting (worst ratio 1.066).

## Verdicts

| Document | R1 | R2 | R3 |
|----------|----|----|----|
| scattering | **APPROVE** (round 1) | **APPROVE** (round 1) | **APPROVE** (round 1) |
| oscillations | pending | pending | **APPROVE** |
| rotations | pending | pending | pending |
| comp1015 | pending | pending | pending |

---

## oscillations — Reviewer 3: APPROVE

**Fix verification**

- p4 double-pendulum figure — **FIXED**, whole in `page04_seg01.png`: hatched ceiling, both rods,
  both masses, φ₁ and φ₂, r̂₁ / ê_φ₁, the blue `+x` arrow **and** the blue downward `−z` arrow
  with its label. The sign convention behind `V = −mgl(2cos φ₁ + cos φ₂)` is recoverable from a
  single crop.
- p1 potential-energy diagrams — **FIXED**, both whole in `page01_seg02.png` including `q_0j`,
  `q_j`, the green `η_j` arrow and label, "EQUILIBRIUM IS HERE!" and "APPROXIMATE BY QUADRATIC".

**Regressions:** none. The reviewer re-checked every boxed result, matrix and figure for new
bisection and lists 16 that are each whole in at least one segment. Minimum overlap is now
121 px (median ~155), up from 51 px.

**New non-blocking findings**

1. **Two segments are fully redundant** — `page05_seg02.png` is contained in
   `page05_seg01 ∪ page05_seg03`, and `page06_seg03.png` in `page06_seg02 ∪ page06_seg04`. Their
   content will therefore be seen three times. Harmless to segmentation, but **the LaTeX stage
   must dedupe by content, not by segment**, or those lines will be transcribed twice.
2. Transcription hazards:
   - `±`/`∓` are pervasive on pp. 5–7 and ambiguous in this hand; the `+` in `2+√2` often reads
     as `H`. Cross-check against the paired `∓` in the same expression.
   - p5 defines `x ≡ ω₀²/ω²`; the plain `x` and the script `𝓍` in `(x−1)²` are the same
     variable. Do not introduce `χ`.
   - p3 alternates `A†` and `Aᵀ` for the same real matrix. Preserve; do not normalise.
   - **Struck-through material is pervasive and must not be transcribed as live:** p1 `+O(η³)`
     and the `f(q₀)` term; p4 the `O(η̇²η²)` and `η⁴/4!` terms; p5 the leading `2ω⁴`; p6 the
     `cos(π/2)` and `sin(π/2)` factors.
   - **Colour carries meaning:** red "LINEAR" (p1), blue axes/annotations (pp. 1, 4), green `η_j`
     (p1 — the only place the small-displacement variable is introduced graphically).
   - p7 carries four **typed** sans-serif annotations overlaid on the handwriting ("Check initial
     condition: At t=0, all sin(…) terms are zero, so we have:"). These are editorial remarks
     added after scanning, not part of the original hand, and must be typeset distinctly.
   - p4 `V = −mgl(2cos φ₁ + cos φ₂)`: the leading `2` reads like an `E`. It is a `2`, confirmed by
     the following `V = mgl·diag(2,1)`.
