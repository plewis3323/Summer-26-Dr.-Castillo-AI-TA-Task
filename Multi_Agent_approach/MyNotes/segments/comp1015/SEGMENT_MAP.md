# Segment Map — comp1015, page 1

Source PDF: `Input/Lecture-241015_comp.pdf`
Page render: `segments/comp1015/pages/page-1.png` (1651 x 2335 px, 200 DPI)

The page is almost entirely blank white margin. The whiteboard photograph occupies a
single landscape band:

- **Board bounding box (page px): x = 25 .. 1640, y = 850 .. 1480** (approx. 1615 x 630)
  - Main whiteboard panel: x = 25 .. 1296
  - Separate right-hand board panel: x = 1310 .. 1640
  - Everything outside this band is empty margin and was discarded.

Because the board is wide and short, segmentation is **column-first** (5 vertical
columns following the board's own visual divisions), then each column is split into a
top and a bottom row. Neighbouring segments overlap by 60–110 px (pre-upscale) so no
equation is bisected. All segments are cropped from `pages/page-1.png` and upscaled
**250%** for legibility.

Geometry is given as ImageMagick `WxH+X+Y` in original page pixels.

| # | File | Crop geometry | Output px | Content |
|---|------|---------------|-----------|---------|
| 01 | `page01_seg01.png` | `405x352+25+848` | 1013x880 | Col A top — "Chapter 3: Motion in central potential V(r)"; angular momentum L = μr²φ̇ ẑ as const. of motion, r⃗ = r r̂, p⃗ = μ ṙ⃗; Lagrangian L = T − V = (μ/2)(ṙ² + r²φ̇²) − V(r); φ cyclic ⇒ p_φ = ∂L/∂φ̇ = μr²φ̇ ≡ ℓ conserved; V_eff(r) = V(r) + ℓ²/2μr²; energy E = T + V = (μ/2)ṙ² + V_eff(r) |
| 02 | `page01_seg02.png` | `405x342+25+1140` | 1013x855 | Col A bottom — repeats the E = T + V line, then "Universal method ⇒ complete solution": boxed quadrature t = ∫ dr′/√((2/μ)(E − V(r) − ℓ²/2μr²)) giving t = t(r), and φ = φ₀ + ∫ ℓ/(μr²(t′)) dt′ giving φ = φ(t); below, LHS: μr̈ = −(ℓ²/μ)(1/r²) (d/dφ)(du/dφ) = −(ℓ²/μ) u² d²u/dφ² |
| 03 | `page01_seg03.png` | `520x352+370+848` | 1300x880 | Col B top — "Diff. eqn for r = r(φ)": ℓ = μr²φ̇ ⇒ φ̇ = ℓ/μr² = dφ/dt; chain rule dF/dt = (dF/dφ)(dφ/dt) = (ℓ/μr²) dF/dφ; sketch of an elliptical orbit with radius vector and angle φ; label "Radial Eq. of Motion"; −∂V/∂r = F(r) |
| 04 | `page01_seg04.png` | `520x342+370+1140` | 1300x855 | Col B bottom — radial equation μr̈ = −∂V_eff/∂r = −(∂/∂r)(V(r) + ℓ²/2μr²) = F(r) + ℓ²/μr³; substitution u = 1/r, du/dφ = (du/dr)(dr/dφ) = −(1/r²) dr/dφ; ∂/∂r(r⁻²) = −2r⁻³, ℓ²/μr³ = (ℓ²/μ)u³ ⇒ RHS: F(1/u) + (ℓ²/μ)u³; full LHS chain μ (d/dt)(dr/dt) = …; boxed **generic equation of trajectory for arbitrary V(r)**: −(ℓ²/μ) u² d²u/dφ² = F(1/u) + (ℓ²/μ) u³ |
| 05 | `page01_seg05.png` | `350x352+660+848` | 875x880 | Col C top — F(r) = −∂V/∂r; dV/dr = (dV/du)(du/dr) = −u² dV/du; du/dr = −1/r² = −u²; F(u) = F(r) = −dV/dr = u² dV(1/u)/du; −F(1/u) = (ℓ²/μ) u² [u + d²u/dφ²] |
| 06 | `page01_seg06.png` | `470x342+660+1140` | 1175x855 | Col C bottom — rearrangement −u² dV/du = (ℓ²/μ) u² [u + d²u/dφ²]; boxed **equation for the trajectory r(φ)**: d²u/dφ² + u = −(μ/ℓ²) (d/du) V(1/u); "solve for given u = u₀ for φ = φ₀"; du/dφ = 0 ⟺ max or min r point. (Also carries the tail of col B's generic-trajectory box for overlap.) |
| 07 | `page01_seg07.png` | `360x352+950+848` | 900x880 | Col D top — green header "Gravitational case / **Kepler problem**": V = −k/r = −ku, dV/du = −k; boxed d²u/dφ² + u = kμ/ℓ² — "harmonic oscillator with shifted origin"; "Aside" box: ũ = u − kμ/ℓ², boxed d²ũ/dφ² + ũ = 0; homogeneous solution ũ(φ) = A cos(φ − φ₀), ũ′(φ) = −A sin(φ − φ₀) |
| 08 | `page01_seg08.png` | `360x342+950+1140` | 900x855 | Col D bottom — ũ″(φ) = −A cos(φ − φ₀) = −ũ(φ); boxed general solution **u(φ) = kμ/ℓ² + A cos(φ − φ₀)**; u₀ = 1/r₀; hand-drawn ellipse with r₀ and φ₀ marked, du/dφ = 0 at r = max or min, labelled "(abs[c]idal) points" |
| 09 | `page01_seg09.png` | `353x352+1295+848` | 883x880 | Col E (right panel) top — boxed **u(φ) = (kμ/ℓ²)[e cos(φ − φ₀) + 1] = 1/r**; "e constant", e ≡ A/(kμ/ℓ²); "Using the universal method": u″ = −u + kμ/ℓ², multiply by u′(φ) ⇒ du/dφ = (u′)² = √(…) |
| 10 | `page01_seg10.png` | `353x342+1295+1140` | 883x855 | Col E (right panel) bottom — dφ = du/u′, ⋮ (steps elided on the board), boxed final orbit **u = (μk/ℓ²)[1 + √(1 + 2ℓ²E/μk²) cos(φ − φ₀)] = 1/r**, and boxed eccentricity **e ≡ √(1 + 2ℓ²E/μk²)** |

## Reading order

Left-to-right across the board by column, top-to-bottom within each column:
seg01 → seg02 (col A) → seg03 → seg04 (col B) → seg05 → seg06 (col C) →
seg07 → seg08 (col D) → seg09 → seg10 (col E, right panel).

## Known low-confidence content

- **seg09**: the square root on the last line, `du/dφ = (u′)² = √( . − )`, is genuinely
  blank/erased on the board — the radicand was never written out.
- **seg10**: the vertical dotted ellipsis between `dφ = du/u′` and the boxed final
  result marks omitted algebra on the board itself, not a segmentation gap.
- **seg08**: the parenthetical label reads "(ABSIDAL) POINTS" as written; the intended
  term is *apsidal* points.
- **seg05/seg06**: a couple of lightly-written intermediate lines (`−F(u) = −u² dV(1/u)/du`)
  are faint on the original photo but readable at 250%.
