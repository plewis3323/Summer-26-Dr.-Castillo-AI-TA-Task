# Stage 4a — Reference Convention Record

Reviewed by two independent referees (one auditing the proposal, one attempting to refute it).
Verdicts: **ACCEPT WITH AMENDMENTS** and **SURVIVES WITH AMENDMENTS**. The amendments below are
mandatory and are authoritative over anything in the reference texts.

## Reference texts

| Text | Scope |
|------|-------|
| **Goldstein, Poole & Safko, *Classical Mechanics*, 3rd ed.** | Primary for `scattering`, `oscillations`, `comp1015`, and the opening (CM-separation, inertia-tensor) material of `rotations`. |
| **Fetter & Walecka, *Theoretical Mechanics of Particles and Continua*, Ch. 5** | **Co-primary for `rotations` from the Euler angles onward.** Cited by the lecturer himself. |
| ~~Taylor, *Classical Mechanics*~~ | **Struck.** See Amendment 2. |

### Why Goldstein — evidence from the notes themselves

- `scattering` p. 3 carries an explicit two-column box headed **"NOTATION: Goldstein | Others"**,
  mapping σ(Ω) ↔ dσ/dΩ and σ_T ↔ σ — the lecturer names Goldstein and takes his side.
- `oscillations` p. 1, underlined top line: **"SMALL OSCILLATIONS (Chapter 6 Goldstein)"**.
- `comp1015` opens **"CHAPTER 3 — MOTION IN CENTRAL POTENTIAL V(r)"** (Goldstein Ch. 3);
  `scattering` p. 4 opens **"Chapter 8 — Hamiltonian and Hamilton's Eqns of Motion"** (Goldstein Ch. 8),
  and reproduces Goldstein §8.1's thermodynamic Legendre-transform motivation — a pedagogical
  move specific to Goldstein.
- `scattering` p. 1 uses **s** for the impact parameter (Goldstein-specific; nearly every other
  text uses `b`), with `I`, `σ(Ω)dΩ`, `σ(θ) = (s/sinθ)|ds/dθ|`, apsidal angle **Ψ**, `Θ = |π−2Ψ|`.
  That symbol combination occurs in Goldstein and essentially nowhere else.
- **Gaussian units** confirmed: `f = ZZ'e²/r²`, `k = −ZZ'e²`, no `4πε₀`.

### Amendment 1 (mandatory) — `rotations` follows Fetter & Walecka, not Goldstein Ch. 4–5

The original proposal claimed `rotations` covers "Goldstein Ch. 4–5". **Refuted.**
`segments/rotations/pages/page-09.png`, mid-page, in the lecturer's own hand:

> **"Following Ch5 F&W (Skipping a lot)"**

and immediately after: **"WE CHOOSE EULER ANGLES: α, β, γ"**.

The consequences are not cosmetic:

- Euler angles are **α, β, γ**, not Goldstein's φ, θ, ψ, sustained through p. 12 (`p_β`,
  `α̇cosβ = I₃ω₃/I₁`, `ω⃗ = α̇ê₃⁰ + γ̇ê₃`), with conjugate momenta named after them in a
  numbered-equation chain.
- Space axes are **ê₁⁰, ê₂⁰, ê₃⁰** and body axes **ê₁, ê₂, ê₃**. Goldstein uses unprimed for
  space and *primed* for body — **the reverse sense**. Importing Goldstein's convention here
  would **invert every equation in the segment.**
- Line of nodes is **ê_β**, not Goldstein's ξ-axis.

`rotations` is therefore **hybrid**: Goldstein-compatible for the CM-separation (p. 1, matching
Goldstein §1.2 exactly) and inertia-tensor (p. 5, §5.3-compatible) material, F&W from the Euler
angles onward.

### Amendment 2 (mandatory) — drop Taylor

There is no undergraduate-level passage in this batch. `oscillations` p. 2 carries the full
`T = T₂ + T₁ + T₀` decomposition with `m_ij = Σ_p m_p (∂r⃗_p/∂q_i)·(∂r⃗_p/∂q_j)`; `scattering`
derives the cross section from the apsidal quadrature for *arbitrary* V(r); the Hamiltonian is
built by Legendre transform. **None of this is in Taylor**, which also has no T₀/T₁/T₂ split and
uses SI — invoking it would push `b` for the impact parameter and insert `4πε₀`.

Alternatives weighed and rejected: Landau & Lifshitz (uses `M`, `ρ`, `χ` — none appear),
Marion & Thornton (SI, `b`), José & Saletan and Arnold (too geometric, no T_ij/V_ij formulation).

## Scope — the limit both referees imposed

The reference texts govern **terminology, equation style, and structural vocabulary only.**
They are **not** authoritative over symbols. The four lectures are each internally consistent and
**mutually inconsistent by design** — the lecturer reused letters across weeks. Where the notes
and a textbook disagree, **the notes win.**

> Compared symbol by symbol, the notes agree with Goldstein about 70% of the time, and at every
> point of disagreement the notes are the *clearer, less overloaded* choice. There is no case in
> this batch where a textbook symbol should displace the lecturer's.

This ruling already caught a live defect: the first draft of `goldsteinnotes.sty` defined
`\reduced` = μ and `\lang` = ℓ as shared macros. Applied to `scattering`, that would have silently
turned the notes' **m** into **μ**; applied to `oscillations`/`rotations`, it would have merged
angular momentum with the *lengths* those lectures write as `l`. Both macros were removed; the
style file now defines no macro binding a quantity to a letter.

---

## Per-lecture symbol table — AUTHORITATIVE

Where a row differs across columns, that is intentional. Do **not** harmonise.

| Quantity | `scattering` | `oscillations` | `rotations` | `comp1015` | Textbook | Ruling |
|---|---|---|---|---|---|---|
| Orbiting / reduced mass | **m** | — | — | **μ** | m | per-lecture; never convert m→μ |
| Angular momentum (central force) | **ℓ** | — | — | **ℓ** | l | typeset `\ell`; never promote to `L` |
| System / rigid-body ang. mom. | — | — | **L⃗, L_i = I_iω_i** | — | L, L_i | match; keep uppercase vector |
| Eccentricity | **ε** | — | — | **e** | e | hard carve-out — in `scattering` **e is the elementary charge** (k = −ZZ′e²); writing eccentricity as `e` there gives the literal collision e = [1+(2sE/ZZ′e²)²]^½ |
| Orbit polar angle | **θ̃, θ̃′** | — | — | **φ** | θ | tilde is load-bearing and is the lecturer's own disambiguation device (θ̃′ = π repulsive, θ̃′ = 0 attractive); no textbook counterpart |
| Scattering angle | **θ** (lowercase) | — | — | — | Θ (capital) | **notes' lowercase θ**; do not import capital Θ |
| Apsidal angle | **Ψ** | — | — | — | Ψ | match; drawn like a `4` — see hazards |
| Impact parameter | **s** | — | — | — | s | exact match; **never `b`** |
| Differential cross section | **σ(Ω)**, σ(θ) for the s-form | — | — | — | σ(Ω) | match — **do NOT rewrite as dσ/dΩ** |
| Total cross section | **σ_T = ∫dΩ σ(Ω)** | — | — | — | σ_T | match |
| Effective potential | — | — | — | **V_eff(r)** | V′ | **notes' V_eff**; explicitly labelled |
| Hamiltonian | **H = −(L − Σp_i q̇_i)** | — | — | — | H = Σq̇_ip_i − L | keep the notes' parenthesised form — written that way to expose the Legendre structure |
| Small displacement | — | **η, η_j; q_j = q_{0j} + η_j** | — | — | η_i, q_{0i} | exact match |
| Normal-mode ampl./phase | — | **η_{j0}, δ_j** | — | — | C a_j, δ | **notes**; Goldstein's a_j never appears — do not introduce it |
| Kinetic/potential matrices | — | **T_ij, V_ij** | — | — | T_ij, V_ij | exact match |
| General mass matrix | — | **m_ij, π_j, T₀/T₁/T₂** | — | — | m_jk | match; keep π_j |
| Inertia tensor | — | — | **I_ij = Σ_p m_p[δ_ij r_p² − r_{pi}r_{pj}]** | — | I_jk = Σ_i m_i(…) | **notes** — they reserve **p for the particle index** and i,j for components where Goldstein overloads i. Strictly clearer, and consistent with `oscillations` (m_p, r⃗_p) |
| Principal moments | — | — | **I₁, I₂, I₃; I_ij = I_iδ_ij** | — | I₁,I₂,I₃ | match |
| Parallel-axis theorem | — | — | **I = Ī + Ma²** | — | I = I_cm + Ma² | **notes — keep the overbar Ī** |
| **Euler angles** | — | — | **α, β, γ** | — | φ, θ, ψ | **NON-NEGOTIABLE — see Amendment 1** |
| **Space vs body axes** | — | — | **ê_i⁰ space / ê_i body** | — | unprimed space / primed body | **notes — Goldstein's sense is REVERSED; importing it inverts every equation** |
| Line of nodes | — | — | **ê_β** | — | ξ-axis | notes |
| `l` (roman ell) | ang. momentum | **a length** (mgl, ω₀²≡g/l) | **a length** (Mgl, l₁ = l + k̄²/l) | ang. momentum | — | two distinct meanings; never merge |
| `k` | force const. (V = −k/r) | **mode index** k = 1…n | **radius of gyration** (I ≡ Mk²) | force const. | — | three meanings; no textbook ruling exists for the radius of gyration |
| `I` | **beam intensity** | identity 𝟙 = ÃTA | **inertia tensor** | — | both | Goldstein overloads it too; leave both, rename neither |
| `Ω` | **solid angle** | — | ang.-velocity **matrix** Ω_ij; pendulum **frequency** Ω_Q; top **precession rate** Ω | — | — | four meanings — **no bare `\Omega` macro** |
| `L` | Lagrangian | Lagrangian | Lagrangian **and** L_i, L⃗ | Lagrangian | both | on `rotations` pp. 5/10/12 the bold/arrow distinction must be applied deliberately per occurrence |
| `A` | Helmholtz free energy | **modal matrix** A ≡ (a⃗₁…a⃗ₙ) | — | orbit amplitude | — | different lectures; low risk |
| `T`, `V` | T = temperature, V = volume (p. 4) **and** kinetic/potential (pp. 1–3) | T_ij, V_ij | T = period | — | — | the lecturer accepted this collision **within** one lecture; do not "fix" it |
| Generalized force | — | **Q_j = −∂V/∂q_j** | — | — | Q_i | match |
| Kepler constant | **k = −ZZ′e², k = Gm₁m₂** | — | — | V = −k/r | k | match |
| Units | **Gaussian** | — | — | — | Gaussian | match — **never insert 4πε₀**, and never *attribute* the choice (guard-rail 7) |

---

## Guard-rails for transcription

1. **Do not normalise the Euler angles**, and do not invert the space/body axis convention.
2. **Do not import Goldstein's Ch. 4–5 apparatus into `rotations`** — no A = BCD matrix
   factorisation, no Cayley–Klein parameters, no Euler's theorem. The lecturer wrote
   **"Skipping a lot"**: that phrase is an explicit instruction that the omissions are
   intentional. **Transcribe the gaps as gaps.**
3. **Do not renumber.** `rotations` carries the lecturer's own hand-numbered equations **(1)–(53)**
   with explicit back-references ("Eq (27) is the special case of Eq (4) in the CM Frame";
   "(2)+(40) ⇒ (52)"). Preserve his numbers verbatim; LaTeX auto-numbering would break the
   cross-references.
4. **Do not restructure `oscillations` into Goldstein's §6.1/§6.2 order.** The notes deliberately
   open with a 1-D warm-up (q̈ = f(q), η̈ ≈ f′(q₀)η, oscillation vs. instability,
   ω = √(−f′(q₀)) vs. λ = √(f′(q₀))) that Goldstein does not have. It stays first and stays intact.
5. **Do not promote the "ASIDE" on `oscillations` p. 2 into a main section.** The lecturer marked
   it `ASIDE:` and set it off by a rule; Goldstein presents that T₀/T₁/T₂ material inline.
   Preserve the subordination.
6. **Do not complete truncated numerical coefficients.** `rotations` p. 5 has `I₃ ~ ⧸#⧸ Ma²` and
   `I₁ ~ ⧸#⧸ Mb²` with the coefficient **struck out** — the lecturer asserts only the scaling.
   Do not substitute 1/2, 2/5 or 1/12 from a textbook table.
7. **Do not attribute the notes' own conventions to a textbook in prose.** The previous run's
   output claimed the chapter was typeset "in the notation and equation conventions of Goldstein"
   and called Gaussian units "following Goldstein's convention". Both are transcriber inventions —
   the lecturer never says this, and Gaussian units are simply what he wrote. **This is precisely
   the scope violation to prevent.** The reference text is a decoding aid, not a citation to
   assert on the lecturer's behalf.
8. **Do not add explanatory notation remarks that are not in the notes.** The previous run added a
   `\begin{remark}[Notation]` block explaining that "other references commonly write dσ/dΩ";
   nothing on the page says this. Any genuinely useful editorial note must be visually distinct
   from lecture content, never presented as it.
9. **Do not "correct" the lecturer's loose statements.** `rotations` p. 5 reads
   `I_ij = I_ji = I*_ji ⇒ HERMITIAN ⇒ CAN BE DIAGONALIZED`; for a real tensor this is redundant.
   Transcribe as written.
10. **Preserve struck-out material as retracted** — never deleted, never silently restored. Use
    `\retracted{}`. This covers the red X on `scattering` p. 4 (which strikes **only** the lower
    part of the MIDTERM REMARK box — the line above it is *not* struck and remains valid), the
    struck coefficients on `rotations` p. 5, and the semantic cancellation strokes catalogued in
    `segments/review_round1.md`.
11. **Preserve the lecturer's own asides and marginalia** — the "AWFUL MESS / THUMBTACK" remark
    closing `rotations` p. 12, the "UNPHYSICAL" note bound to `1/r = C[1+ε] < 0` in `scattering`
    p. 2, and the "UP TO HERE" caveat on `scattering` p. 1.
12. **No cross-lecture consistency pass.** Any QA step that diffs symbols *between* documents will
    flag μ/m, e/ε, φ/θ̃, α/φ as errors and try to unify them. They are correct as they stand.
    Fidelity is per-page.
13. **Reproduce the source's own slips**, flagged rather than fixed — see `segments/review_round1.md`.
