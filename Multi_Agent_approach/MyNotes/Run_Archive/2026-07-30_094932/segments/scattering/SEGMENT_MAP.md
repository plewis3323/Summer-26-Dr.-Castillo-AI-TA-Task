# SEGMENT MAP — `scattering`

Source PDF: `Input/Lecture-scattering-Hamiltonian_241022-forward.pdf`
Pages rendered at 200 DPI, 1700 x 2200 px each (`pages/page-N.png`).
Geometry is ImageMagick `-crop WxH+X+Y` on the corresponding page PNG.
All segments are full page width (1700 px); neighbours overlap by 60–110 px
(round-2 re-crops raised the two 50 px joins and widened three segments).
Subject: graduate classical mechanics — scattering by a central potential, Rutherford
cross section, and the start of Hamiltonian mechanics (Goldstein Ch. 3 / Ch. 8).

---

## Page 1 — Scattering by a central potential (Oct 22 2024) — 6 segments

| Segment | Geometry | Content |
|---|---|---|
| `page01_seg01.png` | `1700x570+0+0` | Title + date; incident energy `E = (m/2)v0^2`, incident velocity `v0 = sqrt(2E/m)`, angular momentum `l = s m v0 = s sqrt(2mE)`, `s = l/sqrt(2mE)`; scattering-geometry diagram (impact parameter `s`, apsidal point, `r_<`, deflection angle `theta`, scattered ring); `d^3r = r^2 dr dphi sin(theta) dtheta`, solid angle `dOmega = 2 pi sin(theta) dtheta`, azimuthal symmetry remark, `s(theta,E)`. |
| `page01_seg02.png` | `1700x490+0+510` | Definition of incident intensity `I`; definition of the differential cross section `sigma(Omega) dOmega`; the flux-matching chain `I(2 pi s)|ds| = I sigma(theta) 2 pi sin(theta)|dtheta|`; boxed result `sigma(theta) = (s/sin theta)|ds/dtheta|`; boxed total cross section `sigma_T = int dOmega sigma(Omega)`. |
| `page01_seg03.png` | `1700x460+0+940` | Repulsive case (`pi = theta + 2 psi`) and attractive case (`pi = 2 psi - theta`) with ray diagrams and apsidal points; boxed universal relation `theta = |pi - 2 psi|`; heading "Computing s(theta,E) (universal method)". |
| `page01_seg04.png` | `1700x350+0+1330` | Universal method setup: energy `E = (m/2) rdot^2 + V(r) + l^2/(2 m r^2)`, `rdot = [ (2/m)(E - V - l^2/2mr^2) ]^{1/2}`, `dt = dr/rdot`; `l = m r^2 thetadot` and reduction of `dtheta` to the radial integrand with `l/sqrt(2mE) = s`. |
| `page01_seg05.png` | `1700x330+0+1570` | Apsidal-angle integral `psi = int_0^psi dpsi = int_{theta_m}^{pi} dtheta = int_{r_m}^{inf} s r^{-2} dr / [1 - V(r) - s^2/r^2]^{1/2}` **[SOURCE ERROR — the source omits `/E` on the `V(r)` term, making it dimensionally inconsistent; the boxed result to its right has it correctly. Transcribe verbatim, do not correct]**; substitution `u = 1/r`, `du = r^{-2} dr` **[SOURCE ERROR — sign dropped; correct is `du = -r^{-2} dr`. Transcribe verbatim, do not correct]**, `u_m = 1/r_m`; boxed final result `theta(s) = |pi - 2 int_0^{u_m} s du / [1 - V(1/u)/E - s^2 u^2]^{1/2}|`. |
| `page01_seg06.png` | `1700x370+0+1830` | Closing prescription: invert to get `|ds/dtheta| = 1/|dtheta/ds|` and feed into `sigma(theta) = (s/sin theta)|ds/dtheta|`; remark that everything up to here holds for ANY central potential `V(r)`. (Bottom of written content y=2087, measured.) |

## Page 2 — Coulomb scattering: repulsive and attractive orbits — 7 segments

| Segment | Geometry | Content |
|---|---|---|
| `page02_seg01.png` | `1700x540+0+0` | Heading "Coulomb Scattering"; boxed conic classification (E>0 hyperbolic, E=0 parabolic, E<0 elliptic, only for `V = -k/r`); force `f = Z Z' e^2 / r^2`, `f = -k/r^2`, `V = -k/r`, `k = -Z Z' e^2`; orbit `1/r = C[1 + eps cos(thetatilde - thetatilde')]` with `C = mk/l^2`; eccentricity `eps = [1 + 2El^2/(mk^2)]^{1/2} = [1 + (2sE/ZZ'e^2)^2]^{1/2} > 1`; `l = s m v0 = s sqrt(2mE)`. |
| `page02_seg02.png` | `1700x480+0+480` | Two situations: (i) repulsive `ZZ' > 0 => k < 0`, (ii) attractive `ZZ' < 0 => k > 0` (also gravity `k = G m1 m2`); start of case (i) with `C = mk/l^2 < 0` and the positivity chain `1/r > 0 <=> cos(thetatilde - thetatilde') < -1/eps`. |
| `page02_seg03.png` | `1700x300+0+890` | Prose argument for the repulsive branch: cosine must be negative and larger in magnitude than `1/eps`; `thetatilde = thetatilde'` is unphysical (gives `1/r = C[1+eps] < 0`); it lies in the inaccessible region of the hyperbola, so periapsis is at `thetatilde = thetatilde' ± pi` and one chooses `thetatilde' = pi`. |
| `page02_seg04.png` | `1700x290+0+1130` | `cos(thetatilde - pi) = -cos thetatilde`; resulting orbit `1/r = (m Z Z' e^2/l^2)[eps cos thetatilde - 1]`; maximum at `thetatilde = 0`, minimum radius `1/r_m = (m Z Z' e^2/l^2)(eps - 1)`. |
| `page02_seg05.png` | `1700x360+0+1360` | Apsidal angle in the repulsive case is `thetatilde = 0`; need `psi = thetatilde(r -> inf)`; bracketed reminder `theta = pi - 2 psi => psi = (pi - theta)/2`; solve `0 = eps cos psi - 1` giving `1/eps = cos((pi-theta)/2) = sin(theta/2)`. |
| `page02_seg06.png` | `1700x350+0+1650` | Case (ii) attractive, `k > 0`, `C = km/l^2 > 0`; take `thetatilde' = 0`, `1/r = C[1+eps]`; max at `thetatilde = 0`, minimum radius `1/r_m = C[1+eps]`; apsidal point also at `thetatilde = 0`; bracketed reminder `theta = 2 psi - pi => psi = (pi + theta)/2`. |
| `page02_seg07.png` | `1700x300+0+1900` | Attractive-case condition `0 = 1 + eps cos psi` giving `-1/eps = cos((pi+theta)/2) = -sin(theta/2)`. (Bottom of written content y=2111, measured.) |

## Page 3 — Rutherford cross section, total cross section, screening caveat — 8 segments

| Segment | Geometry | Content |
|---|---|---|
| `page03_seg01.png` | `1700x250+0+0` | Typed lead-in "We now combine both cases"; the identity chain `cot^2(theta/2) = 1/sin^2(theta/2) - 1 = eps^2 - 1 = (2sE/ZZ'e^2)^2`; boxed impact parameter `s = s(theta,E) = |Z Z' e^2 / 2E| cot(theta/2)`. |
| `page03_seg02.png` | `1700x220+0+190` | Differentiation `ds/dtheta = -|Z Z' e^2/4E| (1/sin^2(theta/2))`; assembly of `sigma(theta) = (s/sin theta)|ds/dtheta|` with the `sin(theta/2) cos(theta/2)` cancellations. |
| `page03_seg03.png` | `1700x230+0+350` | Boxed Rutherford scattering cross section `sigma(theta) = (1/4)(Z Z' e^2 / 2E)^2 csc^4(theta/2)`, labelled "Rutherford scattering cross section (for Coulomb forces)". |
| `page03_seg04.png` | `1700x300+0+520` | Typed Remarks 1–4: same for repulsive and attractive (goes as `(zz')^2`); diverges like `E^{-2}` at low energy; diverges like `theta^{-4}` at small angles; identical to the quantum-mechanical result. |
| `page03_seg05.png` | `1700x330+0+750` | Heading "Total scattering cross section"; `sigma_T = int sigma(Omega) dOmega`; `sigma(theta) = const / sin^4(theta/2)`; notation table (Goldstein `sigma(Omega)` vs. others `dsigma/dOmega`; `sigma_T` vs. `sigma`). |
| `page03_seg06.png` | `1700x300+0+1010` | `dOmega = 2 pi sin theta dtheta = 4 pi sin(theta/2) cos(theta/2) dtheta`; `sigma_T = (4 pi/4)(Z Z' e^2/2E)^2 int_0^pi ... dtheta`; small-angle estimate `~ int_0 dtheta/(theta/2)^3 = 8 theta^{-2}/(-2)| -> +inf`, labelled "strongly divergent". |
| `page03_seg07.png` | `1700x360+0+1250` | Angular range `0 < theta < pi` annotated on a scattering diagram (impact parameter `s`, scattering center, angle `theta`); classical: `sigma_T = +inf` for any long-range potential; quantum: `sigma_T = +inf` for some long-range potentials where `V(r)` does not decay fast enough as `r -> inf`. |
| `page03_seg08.png` | `1700x340+0+1510` | "Scattering center" label; CAVEAT — in a dense conducting material `V = -k/r` becomes the screened Coulomb ("Yukawa") potential `V^screen(r) = -(k/r) e^{-r/lambda}`; parenthetical note that in non-conducting materials the screened form differs but still vanishes much faster than `1/r`. (Bottom of written content y=1820, measured; remainder of page is blank — probe-verified.) |

## Page 4 — Chapter 8: Hamiltonian and Hamilton's equations of motion — 7 segments

| Segment | Geometry | Content |
|---|---|---|
| `page04_seg01.png` | `1700x520+0+0` | Chapter 8 heading; Lagrangian `L = T - V = L(q_1..q_n, qdot_1..qdot_n, t)`; Euler–Lagrange equation `0 = d/dt(dL/dqdot_i) - dL/dq_i`; canonical momentum `p_i = dL/dqdot_i`; boxed "MIDTERM REMARK" on polar coordinates (`dL/dthetadot = p_theta = l_z`) with a struck-through (red X) attempt `L = L(r, rdot, p_theta)`. |
| `page04_seg02.png` | `1700x240+0+460` | Legendre transformation statement: `(q_1..q_n, qdot_1..qdot_n) -> (q_1..q_n, p_1..p_n)`; `f(x,y) => df = (df/dx)dx + (df/dy)dy`. |
| `page04_seg03.png` | `1700x360+0+640` | Thermodynamic analogy: 1st law `dU = dQ + dW = T dS - p dV`, `U = U(S,V)` internal energy (fluid at constant N); want `T, V` as variables; introduce `F = A = U - TS`, Helmholtz free energy. |
| `page04_seg04.png` | `1700x320+0+940` | `dA = dU - d(TS) = -S dT - p dV => A = A(T,V)`; general Legendre setup `f(x,y) = u dx + v dy` **[SOURCE ERROR — should be `df = u dx + v dy`; `page04_seg05` uses `df` correctly. Transcribe verbatim, do not correct]** with `u = df/dx`, `v = df/dy`, transformation `(x,y) -> (u,y)`. |
| `page04_seg05.png` | `1700x250+0+1200` | `g = f - ux => dg = -x du + v dy`, hence `g = g(u,y)`. |
| `page04_seg06.png` | `1700x370+0+1390` | Apply to `L(q_1..q_n, qdot_1..qdot_n)` with circled `p_i = dL/dqdot_i`; define `H = -(L - sum_i p_i qdot_i)`; expand `dH = -dL + sum_i d(p_i qdot_i)` showing the `dqdot_i` terms cancel. Note the **interlinear insertion** `-∂L/∂t +` written above the main `dH` line — it is a PARTIAL derivative, not `dL/dt`. |
| `page04_seg07.png` | `1700x500+0+1700` | `dH = -(∂L/∂t) + sum_i (qdot_i dp_i - (dL/dq_i) dq_i) => H = H(p_1..p_n, q_1..q_n, t)`; boxed canonical equations of motion `dH/dp_i = qdot_i`, `dH/dq_i = -dL/dq_i = -pdot_i` (via Lagrange's equation), `∂H/∂t = -∂L/∂t` (partial derivatives — the source's first term also omits its `dt`, a SOURCE ERROR; transcribe verbatim), labelled "canonical eqs of motion". (Bottom of written content y=2186, measured.) |

---

## Round-2 revision record (Stage 2 review loop)

Reviewers 2 and 3 returned REVISE on round 1; Reviewer 1 returned APPROVE. Changes applied:

| Segment | Was | Now | Reason |
|---|---|---|---|
| `page01_seg04.png` | `1700x310+0+1330` | `1700x350+0+1330` | **Blocking.** The two underbrace identifications `= l/sqrt(2mE) = s` and `= s^2` fell outside the segment; `= s^2` was in NO segment together with the equation it annotates. |
| `page03_seg07.png` | `1700x320+0+1250` | `1700x360+0+1250` | **Blocking.** The caption `SCATTERING CENTER` was bisected mid-glyph, and the neighbouring segment carried the caption without its diagram. |
| `page02_seg05.png` | `1700x340+0+1360` | `1700x360+0+1360` | Overlap with seg06 was 50 px, below the 60 px floor. Now 70 px. |
| `page03_seg04.png` | `1700x280+0+520` | `1700x300+0+520` | Overlap with seg05 was 50 px. Now 70 px. |
| `page02_seg07.png` | `1700x270+0+1930` | `1700x300+0+1900` | The bracketed premise `theta = 2 psi - pi => psi = (pi+theta)/2` was only half-height at the segment's top edge. |

Documentation corrections: measured bottom-of-content values replaced the estimates; three
SOURCE ERROR markers were added so the transcription stage reproduces the notes faithfully
instead of silently "fixing" the lecturer's slips; the `dL/dt` vs `∂L/∂t` distinction on page 4
was disambiguated.

### Transcription hazards carried forward (not segmentation defects)

- **Retracted material:** `page04_seg01` contains `L = L(r, rdot, p_theta)` struck through with a heavy red X. It is an explicitly rejected attempt and must never be rendered as a valid result.
- **Notational collision:** page 1 uses `theta` for BOTH the orbital polar angle and the deflection angle; page 2 disambiguates with `thetatilde`. Do not silently unify them.
- **Glyph hazards:** `Z` reads as `2` (so `ZZ'e^2` looks like `22'e^2`); `eps` is written lunate and must not become `\in`; `psi` reads as the digit `4`; `delta` reads as `6`; the `thetatilde` tilde is faint and drops out; `s` vs `S` (normalize the boxed `S = S(theta,E)` to lowercase `s`).
- **Verified-correct-but-odd:** the repulsive branch `1/r = (-mk/l^2)[-1 - eps cos(...)]` and the `d/dtheta cot(theta/2)` expansion both look like slips but are algebraically right. Transcribe verbatim.
