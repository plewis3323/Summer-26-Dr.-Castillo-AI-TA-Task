# Stage 2 review log — `central_potential`

Input: `Input/Lecture-241015_comp.pdf` (one board photo, 2356×932 native).
Panel: 3 independent physics-PhD reviewer agents per round. Loop condition:
advance only when all three APPROVE.

## Round 1 — 20 segments — REVISE ×3

Cut: five vertical column windows (x 5:600, 565:990, 950:1495, 1380:1860,
1845:2340), each split horizontally at whitespace valleys.

All three reviewers independently reached the same root cause: **the board's
lower band is written as lines running horizontally across columns 1–3**, and a
vertical column grid slices them. Consequences they each found:

- **Blocking, all three:** the boxed generic equation of trajectory
  `−(ℓ²/μ)u² d²u/dφ² = F(1/u) + (ℓ²/μ)u³` was cut at the column-1/2 seam so that
  its leading minus sign and `ℓ²/μ` prefactor appeared in **no** segment. A
  transcriber reading the crop alone would have emitted a sign-wrong,
  prefactor-less equation — and had no cue anything was missing, because the box
  border was outside the crop too.
- The `LHS:` chain-rule expansion, the `⇒ RHS` identity, the `u = 1/r`
  substitution, the `LHS=RHS` header and the caption were each split across the
  40 px column-2/3 seam, whole in no segment.
- The closing parenthesis of the radial equation of motion sat at x ≈ 1006,
  outside the x = 990 crop edge.
- `du/dφ = 0 ⟺ MAX OR MIN r POINT` was cut at x = 1495.
- Left-edge clipping of the `LHS:` label and adjacent glyphs at x = 565.

Coverage itself was complete — nothing fell in a gap. Every defect was of one
class: **an object sliced so that no single segment shows it whole.**

**Change:** segmentation rebuilt around explicit region rectangles
(`tools/segment_regions.py`, `regions.json`) instead of column windows — column
windows above the band, full-width band windows through it.

## Round 2 — 23 segments — APPROVE ×1, REVISE ×2

All ten round-1 defects verified fixed by all three reviewers, at pixel level.
Two new defects, both raised independently by the two dissenting reviewers:

- **Blocking:** the apsidal-point ellipse in column 4 was split across the
  seg18/seg19 seam — one crop held the upper arc, the other the lower — so the
  figure was whole in no segment. The same wholeness violation as round 1,
  transplanted from an equation onto a figure. The third reviewer, who had
  approved, had checked equations but not drawn objects.
- The lower band's segment order presented the **conclusion** of the LHS
  reduction before its **setup**: the lecturer ran out of room in column 2 and
  finished that computation in the spare space at the bottom-left of column 1,
  so the column-major numbering inverted the derivation. Both halves open with
  the token `LHS:`, inviting a transcriber to emit them as two unrelated blocks.

Also noted: a 12 px band seam shaving the tops of tall grouping parentheses, and
a near-empty sliver crop in `colC-bottom`.

**Changes:**
- Added an `atomic` region flag — emit as one crop, never subdivide. A
  whitespace-valley finder reads a diagram as a tall inked block and cuts it
  wherever the arithmetic lands; naming the rectangle is the only reliable
  guarantee that a figure survives whole.
- New atomic region `colD-figure` (x 1350–1875, y 596–830) holding the ellipse
  entire, laid over the seg18/19 seam.
- `band-low` split into two atomic regions so the band reads in derivation
  order: `band-mid` → `band-low-chain` → `band-A` (the continuation) →
  `band-low-box` (the conclusion). Seam widened 12 px → 40 px.
- `colC-bottom` made atomic, removing the sliver.
- `SEGMENT_MAP.md` gained a "Reading the lower band" section stating that
  segment 13 continues segment 12.

## Round 3 — 24 segments — APPROVE ×3 ✅

All four round-2 fixes verified. All three reviewers ran mechanical checks
rather than relying on inspection: connected-component wholeness tests against
every crop rectangle, and pixel-coverage differencing of the crop union against
the ink mask. Results agreed — **0 uncovered ink pixels**; the only uncovered
board area is a 5 px strip of blank frame at x 0–5. Every equation, box border,
bracket, brace, label and drawn figure was confirmed whole in at least one
segment. No new defects.

Reviewer minor items applied to the documentation (no re-crop): segment 12's
role no longer claims to contain the `LHS=RHS` header, which is clipped there
and whole in segment 14; the board's own spelling `(ABSIDAL POINTS)` is
preserved; a note ties segment 20's figure back to the apsidal condition in
segment 15; and two further genuine source limitations were recorded — the final
eccentricity box was written against the physical bottom edge of the board and
never given a bottom rule, and column 3 writes `[u + du/dφ²]` on one line and
`[u + d²u/dφ²]` on the next, which must not be silently normalised.

**Stage 2 closed.** 24 approved segments → Stage 3.

## What the loop bought

Round 1's blocking defect was a genuine physics error in waiting: a boxed result
transcribed with the wrong sign and a missing prefactor, undetectable downstream
because the evidence of the omission was cropped away with it. Round 2's was the
same failure mode on a figure, and it survived one reviewer's approval — the
panel of three is what caught it.
