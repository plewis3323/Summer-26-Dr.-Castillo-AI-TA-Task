# Segment Map — `oscillations`

Source PDF: `Input/Lecture-Oscillations-241119_241114.pdf`
Page PNGs: `segments/oscillations/pages/page-N.png` (1700x2200 px, 200 DPI)
Subject: Graduate classical mechanics — Small Oscillations (Goldstein Ch. 6)

Crop geometry is ImageMagick `WxH+X+Y` against the parent page PNG. All segments are
full page width (1700 px); vertical neighbours overlap by 60–300 px.

**7 pages → 44 segments.**

---

## Page 1 — 1D equilibrium, multi-DOF setup, Taylor expansion of V, T and V matrices

| Segment | Geometry | Content |
|---|---|---|
| `page01_seg01.png` | `1700x400+0+0` | Title "SMALL OSCILLATIONS (Chapter 6 Goldstein)"; 1D case q̈ = f(q); equilibrium condition 0 = f(q₀) at q = q₀; motivation for small displacement; q = q₀ + η with η "small". |
| `page01_seg02.png` | `1700x460+0+340` | (q₀+η)¨ = η̈; Taylor expansion f(q₀+η) = f(q₀) + η f′(q₀) + …; linearised EOM η̈ ≈ f′(q₀)η; note that EOM is linear in small deviations; oscillation vs. instability criteria f′(q₀) ≶ 0 with ω = √(−f′(q₀)), λ = √(f′(q₀)) and the two solution forms. |
| `page01_seg03.png` | `1700x420+0+740` | Section rule; "More than one degree of freedom", simplification V = V(q₁…qₙ, t); L = T − V; equilibrium ⇔ generalized forces Q_j = −∂V/∂q_j |_{q⃗=q⃗₀} = 0. |
| `page01_seg04.png` | `1700x480+0+1100` | Both V(q_j) plots side by side, intact with labels: left plot (V axis, "EQUILIBRIUM IS HERE!", q₀ⱼ) and right plot (blue "APPROXIMATE BY QUADRATIC", equilibrium arrow, green η_j displacement). |
| `page01_seg05.png` | `1700x450+0+1480` | "TAYLOR EXPAND V TO 2ⁿᵈ ORDER IN η"; full expansion V(q₁…qₙ) = V(q₀₁…q₀ₙ) + Σ ∂V/∂q_j η_j + ½ Σ ∂²V/∂q_i∂q_j η_i η_j; annotations CONSTANT ⇒ no worries, first-order term = 0; definition ≡ V_ij, n×n matrix, symmetry V_ij = V_ji. |
| `page01_seg06.png` | `1700x340+0+1860` | Kinetic energy: T = ½ Σ ∂²T/∂q̇_i∂q̇_j |_{q̇=0, q=q₀} η̇_i η̇_j ≡ T_ij, symmetry T_ij = T_ji; boxed T = Σ_P (m_P/2)(ṙ⃗_P)² with ṙ⃗_P = Σ_j ∂r⃗_P/∂q_j q̇_j + ∂r⃗_P/∂t (last term struck out — "ASSUME" scleronomic). |

## Page 2 — Quadratic Lagrangian, Lagrange equations, generalized eigenvalue problem, KE aside

| Segment | Geometry | Content |
|---|---|---|
| `page02_seg01.png` | `1700x340+0+0` | Boxed quadratic Lagrangian L = ½ Σ_{ij}(T_ij η̇_i η̇_j − V_ij η_i η_j); explicit 2-DOF differentiation ∂/∂η₂ of the V-terms showing V₁₂ = V₂₁ symmetry. |
| `page02_seg02.png` | `1700x420+0+280` | Remark that the ½ prefactor cancels the factor 2 from the derivative; boxed SIMPLE CASE sanity check T = (m/2)η̇², V = (k/2)η² ⇒ mη̈ = −kη; general results ∂L/∂η_i = −Σ V_ij η_j and p_i = ∂L/∂η̇_i = Σ T_ij η̇_j; start of the boxed Lagrange equations. |
| `page02_seg03.png` | `1700x360+0+640` | Boxed coupled equations 0 = Σ_j (−V_ij η_j − T_ij η̈_j), i = 1…n; ansatz η_j = η_{j0} cos(ωt + δ_j) ⇒ η̈_j = −ω²η_j; substitution giving 0 = Σ_j (V_ij − ω²T_ij) η_{j0} cos(ωt + δ_j). |
| `page02_seg04.png` | `1700x520+0+940` | Since cos(ωt+φ_j) ≠ 0 generically: boxed generalized eigenvalue problem 0 = Σ_j (V_ij − ω²T_ij) η_{j0}; annotations identifying eigenvalue ω (normal mode frequency) and eigenvector η_{j0} (normal mode); boxed secular equation Det[V_ij − ω²T_ij] = 0 for nontrivial solutions. |
| `page02_seg05.png` | `1700x440+0+1400` | ASIDE — more details on the kinetic energy: T = Σ_P (m_P/2)(ṙ⃗_P)² expanded as a double sum over ∂r⃗_P/∂q_i q̇_i + ∂r⃗_P/∂t; ṙ⃗_P from r⃗_P = r⃗_P(q₁…qₙ, t). |
| `page02_seg06.png` | `1700x420+0+1780` | Decomposition T = T₂ + T₁ + T₀ with T₂ = ½ Σ m_ij q̇_i q̇_j, T₁ = Σ π_j q̇_j, T₀ = Σ_P (m_P/2)(∂r⃗_P/∂t)²; definitions m_ij = Σ_P m_P ∂r⃗_P/∂q_i · ∂r⃗_P/∂q_j and π_j = Σ_P m_P ∂r⃗_P/∂q_j · ∂r⃗_P/∂t; note that m_ij depends on the q's. |
| |

## Page 3 — T_ij derivation, eigenvector matrix A, normal modes example, normal coordinates

| Segment | Geometry | Content |
|---|---|---|
| `page03_seg01.png` | `1700x420+0+0` | Assuming ∂r⃗_P/∂t = 0 and expanding about q_j = q_{0j} + η_j: T = T₂ = ½ Σ (m_ij|_{q₀} + Σ_k ∂m_ij/∂q_k η_k + …)(q̇₀ᵢ+η̇ᵢ)(q̇₀ⱼ+η̇ⱼ); note (q₀ᵢ+ηᵢ)˙ = η̇ᵢ and that η_k η̇_i η̇_j ∝ η³ is higher order. |
| `page03_seg02.png` | `1700x340+0+360` | "THEREFORE, up to quadratic order in η, η̇": boxed T = ½ Σ T_ij η̇_i η̇_j with T_ij = m_ij|_{q⃗=q⃗₀}; section rule. |
| `page03_seg03.png` | `1700x370+0+640` | Secular equation Det[V_ij − ω_k²T_ij] = 0 and matrix form [V − ω_k²T] a⃗_k = 0⃗, k = 1…n (n = # degrees of freedom); "General solution is linear combination": η_i = Σ_k C_k a_{ik} cos(ω_k t + δ_k) and vector form η⃗ = Σ_k C_k a⃗_k cos(ω_k t + δ_k). |
| `page03_seg04.png` | `1700x340+0+950` | Definition (A)_ij ≡ a_ij, A = (a⃗₁ a⃗₂ … a⃗ₙ); orthonormality property 1 = AᵀTA ⇒ A⁻¹ = AᵀT; diagonalization AᵀVA = diag(ω₁²…ωₙ²); label "Matrix of eigenvectors / normal modes". |
| `page03_seg05.png` | `1700x390+0+1230` | "Normal modes example" with the 3-mass / 2-spring chain diagram (masses 1, 2, 3); mode a⃗₁ = (1, 0, −1)ᵀ with its motion arrows and ω₁; mode a⃗₂ = (−1, 2, −1)ᵀ with its motion arrows and ω₂. |
| `page03_seg06.png` | `1700x340+0+1560` | Zero-frequency translation mode a⃗₃ = (1, 1, 1)ᵀ with ω₃ = 0; general solution (η₁ η₂ η₃)ᵀ = C₁a⃗₁cos(ω₁t+δ₁) + C₂a⃗₂cos(ω₂t+δ₂) + C₃a⃗₃cos(ω₃t+δ₃); rule and "Normal coordinates ξ" heading. |
| `page03_seg07.png` | `1700x360+0+1840` | Normal coordinates: η⃗ = Aξ⃗, η_i = Σ_k ξ_k a_ik, ξ_k = C_k cos(ω_k t + δ_k), ξ⃗ = A⁻¹η⃗ = AᵀTη⃗; Lagrangian rewritten L = ½[η̇⃗ᵀTη̇⃗ − η⃗ᵀVη⃗] = ½[ξ̇⃗ᵀAᵀTAξ̇⃗ − ξ⃗ᵀAᵀVAξ⃗] ⇒ boxed decoupled L = ½ Σ_k (ξ̇_k² − ω_k² ξ_k²). |

## Page 4 — Double pendulum example: geometry, T and V, quadratic-order T and V matrices

| Segment | Geometry | Content |
|---|---|---|
| `page04_seg01.png` | `1700x700+0+0` | Title "Example: Oscillations of a double pendulum"; complete labelled double-pendulum diagram (pivot hatching, +x / −z axes, ℓ, φ₁, φ₂, both masses m, r̂₁); transformation equations r⃗₁ = ℓ(sinφ₁x̂ − cosφ₁ẑ) = ℓr̂₁, r⃗₂ = ℓ(r̂₁ + r̂₂₁), with r̂₁ and r̂₂₁ defined; start of "Velocities". |
| `page04_seg02.png` | `1700x480+0+400` | Velocities: r̂̇₁ = φ̇₁ ∂r̂₁/∂φ₁, r̂̇₂₁ = φ̇₂ ∂r̂₂₁/∂φ₂; unit vectors ∂r̂₁/∂φ₁ = ê_{φ₁} = cosφ₁x̂ + sinφ₁ẑ (and the φ₂ analogue); resulting ṙ⃗₁ and ṙ⃗₂ in Cartesian components. (Lower part of the pendulum diagram repeats here for context.) |
| `page04_seg03.png` | `1700x380+0+820` | T = (m/2)[(ṙ⃗₁)² + (ṙ⃗₂)²] reduced to T = (mℓ²/2)[2φ̇₁² + φ̇₂² + 2φ̇₁φ̇₂cos(φ₂−φ₁)] using ê_{φ₁}·ê_{φ₂} = cos(φ₂−φ₁); potential V = −mgℓ(2cosφ₁ + cosφ₂); full Lagrangian L = T − V. |
| `page04_seg04.png` | `1700x360+0+1140` | Verification that φ₁ = φ₂ = 0 is an equilibrium: ∂V/∂φ₁ = mgℓ sinφ₁ = 0 and ∂V/∂φ₂ = mgℓ sinφ₂ = 0 at φ = 0; V is an absolute minimum ⇒ equilibrium is STABLE. |
| `page04_seg05.png` | `1700x360+0+1440` | Expansion of T and V to quadratic order in η_i = φ_i − φ_i⁰ = φ_i: φ̇₁φ̇₂cos(φ₂−φ₁) ≈ η̇₁η̇₂ + O(η̇²η²); cos φ_i = cos η_i ≈ 1 − η_i²/2 (quartic term struck out). |
| `page04_seg06.png` | `1700x460+0+1740` | Quadratic-order results: V = −mgℓ[3 − η₁²/2 − η₂²/2] ⇒ V-matrix V = mgℓ (2 0; 0 1); T = (mℓ²/2)[2η̇₁² + η̇₂² + 2η̇₁η̇₂] ⇒ T-matrix T = mℓ²(2 1; 1 1); explicit row-vector·matrix·column-vector CHECK of both, plus the general form T = ½(q̇₁…q̇ₙ)T(q̇). |

## Page 5 — Eigenfrequencies, eigenvectors, normalization, modal matrix

| Segment | Geometry | Content |
|---|---|---|
| `page05_seg01.png` | `1700x360+0+0` | Notation mgℓ = mℓ²(g/ℓ), ω₀² ≡ g/ℓ; eigenvalue equation 0 = Det[V − ω²T] = Det(mℓ²[2g/ℓ − 2ω², −ω²; −ω², g/ℓ − ω²]); first expansion to ω⁴ − 4ω₀²ω² + 2ω₀⁴. |
| `page05_seg02.png` | `1700x360+0+300` | Completing the square: 0 = (ω² − 2ω₀²)² − 2ω₀⁴ ⇒ ω² = (2 ± √2)ω₀²; boxed eigenfrequencies ω₊ = √(2+√2) ω₀, ω₋ = √(2−√2) ω₀; start of "Eigenvectors". |
| `page05_seg03.png` | `1700x340+0+600` | Eigenvector equations (0,0)ᵀ = (2ω₀²−2ω², −ω²; −ω², ω₀²−ω²)(a₁, a₂)ᵀ, giving a₂/a₁ = 2(ω₀²/ω² − 1) and the reciprocal form; SIDE NOTE showing the two equations are equivalent, 1 = 2(ω₀²/ω² − 1)². |
| `page05_seg04.png` | `1700x420+0+880` | Completion of the side note: ω⁴ = 2(ω₀²−ω²)(ω₀²−ω²) ⇔ 0 = Det(V − ω²T) ✓; "So we can take either equation together with normalization to get a⃗"; proposal a⃗ = N(1, 2(ω₀²/ω² − 1))ᵀ, N = normalization constant, x ≡ ω₀²/ω². |
| `page05_seg05.png` | `1700x440+0+1240` | Normalization 1 = a⃗ᵀT a⃗ worked out in x: 1 = N²mℓ²[2x + 2(x−1)(2x−1)] = 2N²mℓ²[2x² − 2x + 1] = 4N²mℓ² ω₀²/ω² ⇒ boxed N_± = (1/√(4m))(ω_±/ℓω₀) = ((2±√2)/(4mℓ²))^{1/2}. |
| `page05_seg06.png` | `1700x390+0+1560` | Supporting algebra ((x−1)² identities, ω⁴[2(x−1)²−1] = 0 check); evaluation ω₀²/ω_±² = 1/(2±√2) = 1 ∓ 1/√2 so 2(ω₀²/ω_±² − 1) = ∓√2; boxed normalized eigenvectors a⃗_± = ((2±√2)/(4mℓ²))^{1/2}(1, ∓√2)ᵀ and boxed ω_± = (2±√2)^{1/2}√(g/ℓ). |
| `page05_seg07.png` | `1700x320+0+1880` | Boxed modal matrix A = (a⃗₊ a⃗₋) = (4mℓ²)^{−1/2}(a b; c d) with the entries a = (2+√2)^{1/2}, b = (2−√2)^{1/2}, c = −√2 a, d = +√2 b. |

## Page 6 — Mode pictures, normal coordinates ξ_±, decoupled Lagrangian, initial conditions

| Segment | Geometry | Content |
|---|---|---|
| `page06_seg01.png` | `1700x340+0+0` | "Graphical representation" of the two modes: a⃗₊ picture (high frequency ω₊, masses out of phase) and a⃗₋ picture (lower frequency ω₋, masses in phase), with the note |η₂| = √2|η₁| > |η₁| in both modes; "Normal coordinates" heading; start of the right-hand column of a, b, c, d algebra. |
| `page06_seg02.png` | `1700x380+0+280` | ξ⃗ = AᵀTη⃗ = Aᵀ mℓ²(2 1; 1 1)(η₁, η₂)ᵀ evaluated to (mℓ²/4)^{1/2}((2a+c)η₁ + (a+c)η₂, (2b+d)η₁ + (b+d)η₂)ᵀ; right-hand column evaluating 2a+c, a+c, 2b+d, b+d in terms of (√2∓1)^{1/2}, plus the (mℓ²/4)^{1/2} simplifications. |
| `page06_seg03.png` | `1700x300+0+600` | Boxed normal coordinates ξ₊(t) = m^{1/2}ℓ((√2−1)/(2√2))^{1/2}[√2 η₁(t) − η₂(t)] and ξ₋(t) = m^{1/2}ℓ((√2+1)/(2√2))^{1/2}[√2 η₁(t) + η₂(t)]; boxed alternative forms ξ_±(t) = f_± cos(ω_± t + δ_±). |
| `page06_seg04.png` | `1700x340+0+860` | Boxed time derivatives ξ̇₊(t), ξ̇₋(t) in terms of η̇₁, η̇₂; boxed ξ̇_±(t) = −f_± ω_± sin(ω_± t + δ_±); heading "Lagrangian in terms of the normal coordinates". |
| `page06_seg05.png` | `1700x380+0+1140` | Decoupled Lagrangian L = ½ Σ_α (ξ̇_α² − ω_α² ξ_α²) written out for the ± modes, then L = ½[(ξ̇₊² − (2+√2)(g/ℓ)ξ₊²) + (ξ̇₋² − (2−√2)(g/ℓ)ξ₋²)]; statement of the initial condition at t = 0: φ₁ = φ₂ = 0, φ̇₁ = −φ̇₂ = v > 0. |
| `page06_seg06.png` | `1700x290+0+1460` | "Get φ₁(t), φ₂(t)"; first phase condition f₊cos(δ₊) = ξ₊(0) = 0 ⇒ δ₊ = ±π/2, ±3π/2, …; supporting simplification m^{1/2}ℓ((√2±1)/(2√2))^{1/2}(√2±1)v = √(2±√2) m^{1/2}ℓv/2. |
| `page06_seg07.png` | `1700x510+0+1690` | Second phase condition f₋cos(δ₋) = 0; velocity conditions −f_±ω_± sin(δ_±) = ξ̇_±(0) = √(2±√2) m^{1/2}ℓv/2; choice δ₊ = δ₋ = −π/2 ⇒ boxed amplitudes f_± = (v/2)[mℓ³/g]^{1/2}; the identity cos(ωt − π/2) = sin ωt. |

## Page 7 — Explicit φ₁(t), φ₂(t), initial-condition checks, QM analogy

| Segment | Geometry | Content |
|---|---|---|
| `page07_seg01.png` | `1700x340+0+0` | ξ_±(t) = f_± cos(ω_± t − π/2) = f_± sin(ω_± t); boxed ξ_±(t) = (v/2)[mℓ³/g]^{1/2} sin([(2±√2)g/ℓ]^{1/2} t); right column collecting a, b, c, d, f₊a, f₋b and (4mℓ²)^{−1/2}(v/2)(mℓ³/g)^{1/2} = v/(4√(g/ℓ)); heading "In terms of the original coordinates". |
| `page07_seg02.png` | `1700x460+0+280` | η⃗(t) = Aξ⃗(t) = (4mℓ²)^{−1/2}(a b; c d)(ξ₊, ξ₋)ᵀ; boxed final solutions φ₁(t) = η₁(t) and φ₂(t) = η₂(t) as sums of the two sine modes with coefficients (2±√2)^{1/2}; typed margin check that at t = 0 all sines vanish so φ₁ = φ₂ = 0 ✓. |
| `page07_seg03.png` | `1700x380+0+680` | Boxed angular velocities φ̇₁(t) = η̇₁(t) and φ̇₂(t) = η̇₂(t) as cosine sums; typed margin check that at t = 0 the cosines are 1 giving φ̇₁ = v ✓ and φ̇₂ = −v ✓; heading "COMPARISON WITH QUANTUM MECHANICS". |
| `page07_seg04.png` | `1700x430+0+1020` | Comparison table, upper half: QM column |ψ(0)⟩ → {c_α} → |ψ(t)⟩ ← c_α e^{−iE_α t/ħ}; Small-osc column η⃗(0), η̇⃗(0) → ξ⃗(0), ξ̇⃗(0) with the downward evolution arrow. |
| `page07_seg05.png` | `1700x520+0+1380` | Comparison table, lower half: |ψ(0)⟩ = Σ_α c_α|φ_α⟩ with c_α = ⟨φ_α|ψ(0)⟩, |ψ(t)⟩ = Σ_α c_α e^{−iE_α t/ħ}|φ_α⟩; small-osc counterparts η⃗(t), η̇⃗(t) ← ξ⃗(t), ξ̇⃗(t) with η⃗(t) = Aξ⃗(t) and ξ⃗(t) = AᵀTη⃗(t). This is the last written content on the page (blank below y ≈ 1750). |

---

## Notes on legibility

- All 44 segments were visually re-checked after cropping; every one is independently readable.
- Page 4 was originally cropped so that the double-pendulum diagram was split; seg01/seg02
  were re-cropped (seg01 extended to 700 px tall) so the diagram is intact in seg01.
- Page 5 seg05 was re-cropped (440 px instead of 380 px) so the boxed N_± result is not clipped.
- Marginal / harder-to-read content:
  - Page 6 seg01–seg02 right-hand column (the 2a+c, a+c, 2b+d, b+d algebra with nested
    (√2∓1)^{1/2} factors) is written small and dense; radicals and signs there are the least
    certain text on the whole document.
  - Page 5 seg06 lower-left supporting algebra ((x−1)² manipulations) is small but legible.
  - Page 1 seg06 has a circled inset "q̇ = 0, q⃗ = q⃗₀" with an arrow into the T_ij underbrace;
    the inset is rotated/cramped.
  - Page 7 contains two typed (non-handwritten) margin annotations checking the initial
    conditions — these are digital text overlaid on the scan, not handwriting.
