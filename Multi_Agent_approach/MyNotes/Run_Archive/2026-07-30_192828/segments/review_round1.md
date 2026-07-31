# Stage 2 — Review Round 1

Panel: 3 PhD-level physics reviewers per document, 12 agents in parallel. Each reviewer read
every segment of their document plus all its source pages.

| Document | R1 | R2 | R3 |
|----------|----|----|----|
| scattering | **APPROVE** | **APPROVE** | **APPROVE** | ← panel closed, 3/3 |
| oscillations | pending | pending | pending |
| rotations | pending | pending | pending |
| comp1015 | pending | pending | pending |

---

## scattering — Reviewer 3 (scattering/cross sections): APPROVE

**Blocking issues:** none.

**Coverage:** all 4 pages fully represented; segments span the full inked extent of each page
with no interior gap, and zero ink in any uncovered tail. Measured boundary overlaps 55–165 px;
the two thinnest fall in blank bands, so nothing is orphaned. Segments are exact unresampled
crops, so legibility is strictly better than the composite page.

**Source-level physics slips — transcribe faithfully, do NOT silently correct:**

1. `page01_seg04.png` — intermediate integrand omits the `/E` on the potential:
   written `∫ s r^-2 dr / [1 - V(r) - s^2/r^2]^{1/2}`, while the boxed final result on the same
   segment correctly carries `V(u)/E`. Correcting one and not the other yields an inconsistent
   document.
2. `page01_seg04.png` — substitution written `u = 1/r, du = r^-2 dr`; correct relation is
   `du = -r^-2 dr`. Sign omission absorbed by the limit swap. Preserve as written.
3. `page04_seg04.png` — `dH = -∂L/∂t + Σ(q̇_i dp_i - ∂L/∂q_i dq_i)` omits `dt` on the first
   term. Source shorthand; preserve.

**Semantic marks that must survive transcription:**

- `page04_seg01.png` — the MIDTERM REMARK box contains `L = L(r, ṙ, p_θ) ⇒ Lagrange Eqn`
  struck through with a large red X: the lecturer **retracted** it. Only `∂L/∂θ̇ = p_θ = l_z`
  above the X stands. Must be rendered as invalidated, not as an asserted result.
- `page02_seg03.png` — marginal "UNPHYSICAL" annotation is bound to `1/r = C[1+ε] < 0` and must
  stay attached to that equation.
- Deliberate cancellation strokes are semantic, not stray: `cos π → -1`, `sin π → 0` underbraces
  (`page02_seg03.png`); `cos(π/2) → 0`, `sin(π/2) → 1` (`page02_seg04.png`, `page02_seg05.png`);
  `TdS`/`-TdS` and `u dx`/`-u dx` (`page04_seg03.png`); `∂L/∂q̇_i dq̇_i` (`page04_seg04.png`).

**Symbol hazards, in order of risk:**

| Hazard | Where | Note |
|--------|-------|------|
| `ψ` renders almost exactly like numeral `4` | `page01_seg03`, `page02_seg04`, `page02_seg05` | highest-risk misread in the document (`ψ = (π-θ)/2`, `θ = |π - 2ψ|`) |
| `ε` (eccentricity) vs `E` (energy) | `page02_seg01/03/04/05`, `page03_seg01` | collide on the same lines |
| `ℓ` (angular momentum) vs `1` | `page01_seg01/04`, `page02_seg01`, `page04_seg01` | `s = ℓ/√(2mE)`, `ℓ = s m v₀`, `l_z` |
| `θ̃`/`θ̃'` vs `θ`/`θ'` | `page02_seg03/04/05` | tilde is faint; distinction is load-bearing (θ̃ = orbit polar angle, θ = scattering angle) |
| `δ` reads as `6` | `page03_seg03` | upper limit of the divergence integral |
| `s = s(θ,E)` misread as `s(θ,θ)` | `page03_seg01` | the `E` is narrow and abuts the paren |

**Physics spot-check passed** on `σ(θ) = (s/sinθ)|ds/dθ|`, `θ = |π - 2ψ|`,
`ε = [1 + (2sE/ZZ'e²)²]^{1/2} > 1`, `s = |ZZ'e²/2E| cot(θ/2)`, the boxed Rutherford result
`σ(θ) = ¼(ZZ'e²/2E)² csc⁴(θ/2)`, the `dΩ = 4π sin(θ/2)cos(θ/2)dθ` rewrite, and the
`H = -(L - Σp_i q̇_i)` canonical-equations chain.

## scattering — Reviewer 1 (classical mechanics / scattering theory): APPROVE

**Blocking issues:** none. Verified crop geometry programmatically (exact pixel-block matching
of each segment against its page, plus grid-suppressed ink accounting): measured lost ink mass
is **0** on all four pages, and all 19 segments are full page width, so nothing is lost
laterally either.

Independently confirms R3 on: the `/E` omission and the `du = -r^-2 dr` sign, the struck-out
MIDTERM REMARK box, the semantic cancellation strokes, the `ψ`-reads-as-`4` hazard, the `ε`/`E`
collision, the `ℓ`/`1` collision, and the faint tildes.

**Additional findings not raised by R3:**

1. **Typed text on `page03_seg02.png` contains literal LaTeX macros** — "It diverges like
   \theta^{-4}", "for small angles \theta", "(zz')^2", "E^{-2}". These must be rendered as
   math, not emitted as escaped literal text.
2. **`page04_seg02.png` uses the slashed inexact differential** đQ and đW. Do not transcribe as
   plain `dQ`/`dW`.
3. **Impact parameter is written inconsistently** as both `s` and `S` in the source.
4. `page02_seg01.png` — the orbit constant `C = mk/ℓ²` is drawn with a hook that reads as `G`;
   and "(ALSO GRAVITY k = G m₁ m₂)" renders as "Gmm₂".
5. `page03_seg04.png` — "SCREENED COULOMB" reads as "COULDMB" and the caveat's word "DENSE" is
   heavily overwritten; likeliest OCR miss on the page. `V^SCREEN(r) = -(k/r)e^{-r/λ}` has a
   small superscript and λ.
6. `page04_seg01.png` — evaluation-bar subscript stacks `|_{q̇_j, q_j}` are small and render as
   "q̇j / qj"; `p_θ = ℓ_z` risks `ℓ→1`.
7. **Figure handling:** the page-1 scattered-ring figure spans rows ~165–630 but seg01 ends at
   592, so its unlabeled lower taper appears only at the top of seg02 as a stray curve. All
   semantic content is inside seg01 — the LaTeX stage should draw the figure from seg01 and
   ignore the orphan curve atop seg02. Both reviewers judged this not worth a re-cut.
8. `page02_seg04.png` and `page02_seg05.png` have the tilde accents on `θ̃`/`θ̃'` shaved off at
   row 1; those lines appear complete in `page02_seg03.png` and `page02_seg04.png` respectively
   — transcribe them from there. The θ/θ̃/θ̃' distinction is load-bearing on page 2
   (θ̃' = π is the repulsive-case choice, θ̃' = 0 the attractive one).

## scattering — Reviewer 2 (Hamiltonian mechanics / mathematical methods): APPROVE

**Blocking issues:** none. Verified by pixel-exact template match (every segment matched its
page with mean error 0.000) and published the full segment row-spans; no gaps anywhere, every
consecutive pair overlaps, all uncovered tails confirmed at zero dark pixels.

Confirms R1/R3 on every shared point.

**Additional findings not raised by R1 or R3:**

1. **Fourth source-level slip** — `page04_seg03.png`: "In general f(x,y) = u dx + v dy" should
   be `df = u dx + v dy`. The very next line (`g = f - ux ⇒ dg = df - d(ux)`) uses it correctly.
2. **`π` is drawn with doubled vertical strokes and reads as "II"/"𝕀"**, most acutely in
   `page03_seg03.png` where `σ_T = (4π/4)(ZZ'e²/2E)² ∫₀^π …` looks like "4 I / 4".
3. **`ε` (eccentricity) vs `e` (elementary charge)** — a *second* collision on top of the ε/E
   one, and both appear inside the same expression:
   `ε = [1 + (2sE/ZZ'e²)²]^{1/2}`, `cot²(θ/2) = ε² - 1 = (2sE/ZZ'e²)²`.
4. The typed Remarks use **lowercase `zz'`** where all the handwriting uses **`ZZ'`**.
5. The red X on `page04_seg01.png` strikes **only the lower portion** of the MIDTERM REMARK box
   (`L = L(r, ṙ, p_θ) ⇓ Lagrange Eqn`); the line above it, `∂L/∂θ̇ = p_θ = ℓ_z`, is **not**
   struck and remains valid content. The X's lower tip spills into seg02, but the full box and
   full X are both present in seg01.
6. `page03_seg03.png` — a stray ink mark at the extreme right margin (x ≈ 1690) is clipped in
   the **source scan itself**, not by segmentation; not recoverable.
7. `page02_seg03.png` — "OF THE HYPERBOLA" carries an author strikethrough over "OF"; sentence
   still complete.
8. `page03_seg01.png` — the σ(θ) chain has cancellation strikes over `cos(θ/2)`/`sin(θ/2)`
   factors that are easy to lose; the boxed Rutherford endpoint can be used to validate the chain.
9. Segments carrying more than one logical unit (acceptable, noted for chunk-level prompting):
   `page01_seg03.png` (repulsive diagram + attractive diagram + boxed `θ = |π - 2ψ|` + opening
   of the `S(θ,E)` derivation) and `page03_seg03.png` (total-cross-section derivation + the
   separate Goldstein NOTATION block).
10. `page04_seg01.png` — the held-fixed variable subscripts under each partial derivative
    (`q̇_j, q_j`) are the least legible marks in the document; transcribers should be told what
    they are rather than left to guess.
