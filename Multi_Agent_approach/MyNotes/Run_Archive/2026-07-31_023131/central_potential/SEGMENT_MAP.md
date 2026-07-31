# Segment map — `central_potential`

Source: `Input/Lecture-241015_comp.pdf` (single board photo, 2356×932 native).
Working page: `pages/page-1.png` (2340×875, board cropped out of the source frame).
All coordinates below are in `page-1.png` pixels; every crop is upscaled 2.5× on save.

## Layout

The board is written as **five vertical columns across two physical panels**
(panel seam at x ≈ 1838–1852), but the columns only hold for the **upper**
two-thirds. Below y ≈ 550 the writing of columns 1–3 turns into **lines that run
horizontally across those columns** — the `LHS:` / `RHS:` / `LHS=RHS` reduction
that produces the generic trajectory equation. Segmenting that region on the
column grid slices those lines, which is what the round-1 panel rejected.

Segmentation therefore cuts by **region**, not by column: column windows above
the band, and full-width band windows through it. Regions marked *atomic* below
are emitted as a single crop and never subdivided, because the object they hold
only means anything whole.

## Regions, in reading order

| Segments | Region | x range | y range | Content |
|---|---|---|---|---|
| 01–04 | `colA-top` | 5–620 | 0–752 | Ch. 3 heading; **L** = μr²φ̇ ẑ, **r** = r r̂, **p** = μṙ; Lagrangian; φ cyclic ⇒ p_φ = μr²φ̇ ≡ ℓ conserved; V_eff = V + ℓ²/2μr²; E = ½μṙ² + V_eff; boxed universal-method quadratures t(r), φ(t) |
| 05–07 | `colB-top` | 530–1060 | 0–562 | ℓ = μr²φ̇ ⇒ φ̇ = ℓ/μr²; d/dt = (ℓ/μr²) d/dφ; orbit sketch; radial equation of motion μr̈ = −∂V_eff/∂r |
| 08–10 | `colC-top` | 880–1590 | 0–562 | F(r) = −∂V/∂r rewritten in u: dV/dr = −u² dV/du, du/dr = −u², ending at −F(1/u) = (ℓ²/μ)u²[u + d²u/dφ²] |
| 11 | `band-mid` | 460–1255 | 548–700 | μr̈ = F(r) + ℓ²/μr³; ∂(r⁻²)/∂r; u = 1/r and du/dφ = −(1/r²)dr/dφ; ℓ²/μr³ = (ℓ²/μ)u³ ⇒ RHS |
| 12 | `band-low-chain` *(atomic)* | 460–1255 | 660–775 | LHS chain-rule expansion μ (d/dt)(dr/dt) = … = (ℓ/μr²)(d/dφ)((ℓ/μr²)dr/dφ). The `LHS=RHS` header below it is clipped here and is whole in segment 14 |
| 13 | `band-A` *(atomic)* | 5–520 | 735–875 | **Continuation of segment 12**, wrapped to the spare space at the bottom-left of column 1: μr̈ = −(ℓ²/μ)(1/r²)(d/dφ)(du/dφ) = −(ℓ²/μ)u² d²u/dφ² |
| 14 | `band-low-box` *(atomic)* | 460–1255 | 740–875 | **Boxed** −(ℓ²/μ)u² d²u/dφ² = F(1/u) + (ℓ²/μ)u³, captioned *generic eq. of trajectory for arbitrary V(r)* |
| 15 | `colC-bottom` *(atomic)* | 1180–1600 | 548–875 | **Boxed** d²u/dφ² + u = −(μ/ℓ²) (d/du)V(1/u) — the trajectory (Binet) equation; solve for u = u₀ at φ = φ₀; du/dφ = 0 ⟺ max/min r |
| 16–19 | `colD` | 1350–1875 | 0–875 | Gravitational/Kepler case V = −k/r = −ku; boxed d²u/dφ² + u = kμ/ℓ² as a shifted harmonic oscillator; ũ aside and homogeneous solution; boxed u(φ) = kμ/ℓ² + A cos(φ−φ₀) |
| 20 | `colD-figure` *(atomic)* | 1350–1875 | 596–830 | The apsidal-point ellipse in one piece: closed outline, r₀ chord, φ₀ angle, both apsides, and the labels du/dφ = 0, r = MAX OR MIN, and `(ABSIDAL POINTS)` — the board's own spelling, with a *b* |
| 21–24 | `colE` | 1810–2340 | 0–875 | Boxed u(φ) = (kμ/ℓ²)[e cos(φ−φ₀) + 1] = 1/r; e ≡ A/(kμ/ℓ²); the same result via the universal method, ending at u = (μk/ℓ²)[1 + √(1+2ℓ²E/μk²) cos(φ−φ₀)] = 1/r and e ≡ √(1 + 2ℓ²E/μk²) |

### Reading the lower band

Segments 11 → 12 → 13 → 14 are one continuous argument, and the order matters:
segment 12 sets up the LHS chain rule, **segment 13 is its continuation, not a
separate statement** — the lecturer ran out of room in column 2 and finished the
reduction in the empty space at the bottom-left of column 1 — and segment 14
then equates that reduced LHS to the RHS assembled in segment 11. Both 12 and 13
open with the token `LHS:`; they are two halves of one derivation, not two
derivations.

Segment 20 illustrates the `du/dφ = 0 ⟺ max/min r` statement of segment 15 — the
curly arrow leaves column 3 and lands on the ellipse's lower-left apsis. It is
numbered with column 4 because that is where it sits on the board, but it
belongs to the apsidal condition, not to the Kepler solution around it.

Regions overlap deliberately. A line clipped in one region is whole in another —
`colC-top` and `colC-bottom` clip the band lines at their left edge, and the band
regions clip column 3 at their right edge; each object is complete in the region
that owns it. Segments 16–19 tile column 4 for reading; segment 20 re-crops the
ellipse across the 18/19 seam so the figure exists whole.

## Known source limitations (not segmentation defects)

- The final boxed `e ≡ √(1 + 2ℓ²E/μk²)` has no bottom rule: it was written
  against the physical bottom edge of the board and the border was never drawn.
  The photograph shows the marker rail below it — there is no missing ink to
  hunt for.
- Column 3 writes `[u + du/dφ²]` on one line and `[u + d²u/dφ²]` on the next.
  Both are on the board; the first is the lecturer's shorthand. Do not normalise
  one against the other silently.
- The boxed universal-method result `u = (μk/ℓ²)[…] = 1/r` has **no right
  border** — its top and bottom rules run off the right edge of the photograph.
  The equation itself, including the trailing `= 1/r`, is complete.
- The radicand of `du/dφ = (u′)² = √( · − )` in column 5 is essentially blank on
  the board, and a dotted vertical ellipsis stands in for elided steps below it.
  This is genuine board content — the intermediate algebra was not written out.
  Note the line as written is also false (`du/dφ` is `u′`, not `(u′)²`); it is
  transcribed as it stands, not repaired.
- The tail of `HOMOGENEOUS SOLUTION` in column 4 runs into the physical panel
  frame and is partly illegible at source.
- `SOLVE` in `SOLVE FOR GIVEN` (segment 15) is partly erased on the board.

## Struck-out and cancelled material

Factors are cancelled in place. Segment 10 carries cancellation strokes through
the `u²` on each side of `−u² dV/du = (ℓ²/μ)u²[u + d²u/dφ²]`, and segment 12
carries one through the `μ` in `μ(ℓ/μr²)`. These are working marks on live
equations, not retractions of them.

The right-hand stroke in segment 10 clips the tail of the `μ` on its way past
the `u²`; it does **not** cancel the `μ`. Four independent reviewers checked
this at native resolution, and the algebra settles it either way — the `μ`
survives into the boxed trajectory equation as `−μ/ℓ²`, so cancelling it would
be false.
