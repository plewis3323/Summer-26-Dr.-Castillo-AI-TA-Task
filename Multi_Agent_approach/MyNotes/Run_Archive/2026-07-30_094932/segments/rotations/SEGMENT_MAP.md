# Segment Map — `rotations`

Source PDF: `Input/Lecture-Rotations-Rigid-241031.pdf`
Page PNGs: `segments/rotations/pages/page-01.png` … `page-12.png` (200 DPI, 1700x2200 each)
Segments: `segments/rotations/pageNN_segMM.png` — full page width (1700 px), horizontal cuts only.
Geometry column is the ImageMagick crop string `WxH+X+Y` applied to the parent page PNG.
Adjacent segments overlap by ~60–320 px so no equation, box, or diagram is bisected.
Equation numbers are the marginal numbers written in the notes; **note the numbering restarts** —
pages 1 uses (1)–(27), pages 9–12 restart at (1) and run to (53). Pages 2–8 are largely unnumbered.

Total: **76 segments** over 12 pages.

---

## Page 01 — Summary on elementary rotations (8 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page01_seg01.png` | `1700x240+0+0` | Title "SUMMARY ON ELEMENTARY ROTATIONS"; L_z = Iω_z, N = r×F, T = ½Iω² = ω_z L_z/2; dL/dt = N^(e) with inertial-frame / CM-frame conditions | (1)(2)(3)(4) |
| `page01_seg02.png` | `1700x400+0+180` | Rolling-without-slipping condition v_CMx + ω_z R = 0, sign convention ω_z<0 for clockwise; rolling-disk diagram with ground hatching and +x/+y axes | (5)(6) |
| `page01_seg03.png` | `1700x300+0+500` | Parallel axis theorem I = Ī + Ma²; definitions of Ī (M of I about CM) and a (axis-to-CM distance); blob diagram with axis of rotation and CM | (7)(8)(9) |
| `page01_seg04.png` | `1700x400+0+720` | Separating CM motion: L and T decomposition, M = Σm_j, R = Σm_j r_j / M, r'_j = r_j − R; 3D vector diagram (red r'_i vectors relative to CM) | (10)(11)(12)(13)(14) |
| `page01_seg05.png` | `1700x300+0+1050` | Rigid body rotating with ω_z about CM: L_z = (R×MṘ)_z + Iω_z and T = (M/2)|Ṙ|² + ½Iω_z² | (16)(17) |
| `page01_seg06.png` | `1700x290+0+1290` | PROOFS — changing to the CM system: L = Σ r_i×m_i ṙ_i expanded into CM + relative + cross terms; boxed substitution r_i = R + r'_i | (18)(19) |
| `page01_seg07.png` | `1700x310+0+1490` | Cross-terms vanish: both Σ r'_i×m_i R̈ and Σ R×m_i ṙ'_i reduce to [MR − MR]×Ṙ = 0; start of boxed result "THEN" | (20)(21)(22) |
| `page01_seg08.png` | `1700x460+0+1740` | Boxed L = R×MṘ + Σ r'_i×m_i ṙ'_i, its time derivative, dL/dt = N^(e) = Σ r_i×F_i^(e), Newton's 2nd law for a particle system, boxed dL'/dt = Σ r'_i×F_i^(e); closing remark that Eq (27) is the CM-frame special case of Eq (4) | (22)(23)(24)(25)(26)(27) |

## Page 02 — Rotations, non-inertial systems, rigid body motion (7 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page02_seg01.png` | `1700x440+0+0` | Title; circular motion in a plane, v = ω×r, v⊥r, r·ṙ = 0, two orientation diagrams; right column: x̂×ŷ = ẑ cyclic set, ê_1 ≡ x̂ etc. | — |
| `page02_seg02.png` | `1700x400+0+380` | Orthonormality ê_i·ê_j = δ_ij; rotating coordinate system, 0 = dδ_ij/dt branches for i=j and i≠j; right column: Levi-Civita symbol definition | — |
| `page02_seg03.png` | `1700x340+0+720` | {ê_j} is a basis ⇒ boxed dê_i/dt = Σ_j Ω_ij ê_j with Ω_ij = ê_j·dê_i/dt, plus the "USE THAT" projection identity; right column: ε values and ê_i×ê_j = Σ_ℓ ε_ijℓ ê_ℓ | — |
| `page02_seg04.png` | `1700x400+0+1000` | Dirac-notation projection analogy; antisymmetry Ω_ji = −Ω_ij and Ω_ii = 0; the 3×3 antisymmetric Ω matrix; identification ω_1 ≡ Ω_23, ω_2 = Ω_31, ω_3 = Ω_12 | — |
| `page02_seg05.png` | `1700x340+0+1340` | dê_1/dt = Ω_12 ê_2 + Ω_13 ê_3 = ω×ê_1, verified against the explicit cross product | — |
| `page02_seg06.png` | `1700x340+0+1600` | dê_2/dt = ω×ê_2, verified likewise; helper cross products ê_1×ê_2 = ê_3, ê_3×ê_2 = −ê_1 | — |
| `page02_seg07.png` | `1700x340+0+1860` | dê_3/dt = ω×ê_3 (bottom of written content) | — |

## Page 03 — Rotating reference frames / rigid body rotations (6 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page03_seg01.png` | `1700x460+0+0` | "Rotating reference frames"; inertial ê°_i vs rotating ê_i frame diagrams and b(t); db/dt in the inertial expansion and db/dt)_body definition | — |
| `page03_seg02.png` | `1700x400+0+400` | ê'_i = dê_i/dt = ω×ê_i; "For rotations" db/dt|inertial = db/dt)_body + Σ b_i(ω×ê_i); **boxed** db/dt|inertial = db/dt)_body + ω×b | — |
| `page03_seg03.png` | `1700x400+0+740` | "Rigid body rotations" header; body-frame axes diagram; r_P = position of point P in the body frame (constant in body frame); rigid body with one fixed point; T = Σ ½m_P v_P² = Σ ½m_P (ω×r_P)² | — |
| `page03_seg04.png` | `1700x400+0+1080` | Levi-Civita symbol definition and its values (ε_123 = ε_231 = ε_312 = +1, etc.); ê_1×ê_2 = ê_3 = Σ_ℓ ε_12ℓ ê_ℓ; ê_i×ê_j = Σ_ℓ ε_ijℓ ê_ℓ | — |
| `page03_seg05.png` | `1700x380+0+1420` | a×b in component/ε form, (a×b)_k = Σ ε_ijk a_i b_j; "Also" the contracted identity Σ_i ε_jki ε_ℓmi = δ_jℓ δ_km − δ_jm δ_ℓk | — |
| `page03_seg06.png` | `1700x460+0+1740` | Cyclic property ε_ijk = ε_jki = ε_kij; full derivation of (A×B)·(C×D) = (A·C)(B·D) − (A·D)(B·C) (bottom of content) | — |

## Page 04 — In summary: inertia tensor, T and L (6 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page04_seg01.png` | `1700x360+0+0` | "IN SUMMARY"; T = Σ ½m_P v_P² = Σ (m_P/2)[ω²r_P² − (ω·r_P)²]; the (A×B)·(C×D) identity applied to (ω×r_P)·(ω×r_P) | — |
| `page04_seg02.png` | `1700x420+0+300` | T = ½Σm_P Σ_ij [r_P²δ_ij − r_Pi r_Pj] ω_i ω_j; **boxed** T = ½Σ I_ij ω_i ω_j and **boxed** I_ij ≡ Σ_P m_P[r_P²δ_ij − r_Pi r_Pj], labelled "moment of inertia tensor (SYMMETRIC)" | — |
| `page04_seg03.png` | `1700x360+0+660` | L = Σ m_P r_P × v_P = Σ m_P r_P×(ω×r_P); start of the "Aside: using summation notation" block with [A×(B×C)]_i | — |
| `page04_seg04.png` | `1700x340+0+960` | Completion of [A×(B×C)]_i = (A·C)B_i − (A·B)C_i via ε-contraction; applied to [r_P×(ω×r_P)]_i = (r_P·r_P)ω_i − (r_P·ω)r_Pi | — |
| `page04_seg05.png` | `1700x380+0+1240` | L_i = Σ m_P[r_P²ω_i − Σ_j r_Pi r_Pj ω_j] = Σ_j I_ij ω_j, with the brace identifying I_ij | — |
| `page04_seg06.png` | `1700x340+0+1560` | Three boxed results: L_i = Σ_j I_ij ω_j, T = ½ ω·L, T = ½ Σ_ij I_ij ω_i ω_j (bottom of written content) | — |

## Page 05 — Principal axes, examples, diagonal inertia tensor (6 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page05_seg01.png` | `1700x380+0+0` | **Boxed** I_ij = I_ji = I*_ji ⇒ Hermitian ⇒ diagonalizable, with diag(I_1,I_2,I_3); "Directions that diagonalize I_ij are called PRINCIPAL AXES" | — |
| `page05_seg02.png` | `1700x380+0+320` | EXAMPLES; homogeneous cube or sphere ⇒ I·1_{3×3}; start of the rod (a≪b) and disk (a≫b) diagrams | — |
| `page05_seg03.png` | `1700x420+0+640` | Rod diagram with 2b height and a-radius, a≪b ⇒ I_1 = I_2 > I_3; lens/disk diagram, a≫b ⇒ I_1 = I_2 < I_3; boxed I_ij and I_33 definitions begin | — |
| `page05_seg04.png` | `1700x420+0+1000` | I = Σ m_P (distance to axis)² = Σ m_P r_P⊥²; I_33 reduction showing r_P1² + r_P2² = x² + y² = ρ²; scalings I_3 ~ Ma², I_1 ~ Mb²; limits a≪b ⇒ I_3 ≪ I_1, a≫b ⇒ I_3 ≫ I_1 | — |
| `page05_seg05.png` | `1700x380+0+1360` | "None irregular: I_1 I_2 I_3 all different"; section rule; diag(I_1,I_2,I_3) ↔ I_ij = I_i δ_ij; L_i = Σ_j I_ij ω_j = I_i ω_i; start of the (L_1,L_2,L_3) matrix equation | — |
| `page05_seg06.png` | `1700x520+0+1680` | Matrix form (L_1,L_2,L_3)ᵀ = diag(I)(ω_1,ω_2,ω_3)ᵀ; T = ½ω·L = ½Σ I_i ω_i²; **boxed** L_i = I_i ω_i and **boxed** T = ½Σ I_i ω_i² (extends to page bottom) | — |

## Page 06 — Parallel axis theorem (tensor form); rotation about a moving point (6 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page06_seg01.png` | `1700x420+0+0` | "Parallel Axis THEOREM" (Ī_ij = M of I wrt CM); hanging-pendulum sketch; origin-O vs origin-CM axes with displacement a; **boxed** I_ij = Ī_ij + M[δ_ij a² − a_i a_j] | — |
| `page06_seg02.png` | `1700x340+0+360` | Bottom of the diagrams; "Elementary version: I = Ī + Md²"; header "Rotation wrt an arbitrarily moving point" | — |
| `page06_seg03.png` | `1700x420+0+640` | "No longer look at a point in the body fixed in space"; bullet definitions of inertial frame, CM frame (may not be inertial if R̈≠0, axes ∥ inertial), body frame (origin at CM, axes 123 rotating); large three-frame vector diagram | — |
| `page06_seg04.png` | `1700x400+0+1000` | r = R + r'; dr/dt|inertial = dR/dt + dr'/dt|CM; **boxed** dr/dt|inertial = dR/dt + dr'/dt|body + ω×r'; start of the "IF RIGID BODY" box | — |
| `page06_seg05.png` | `1700x360+0+1340` | **Boxed** rigid-body case dr/dt|inertial = dR/dt + ω×r'; "For any system of particles": M = Σm_P, R ≡ CM position; T = ½MṘ² + T′ | — |
| `page06_seg06.png` | `1700x560+0+1640` | T′ = Σ (m_P/2)ṙ_P′², L = R×MṘ + L′, L′ = Σ r_P′×m_P ṙ_P′ (measured in the CM frame); "For rigid body" ṙ_P′ = ω×r_P′, giving L and T with the "calculated before" braces L′_i = Σ_j Ī_ij ω_j and T′ = ½Σ_ij Ī_ij ω_i ω_j (extends to page bottom) | — |

## Page 07 — Euler's equations; Kater's pendulum (6 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page07_seg01.png` | `1700x360+0+0` | "EULER'S EQUATIONS"; dL/dt = N valid IF inertial frame or CM frame ("translated but not rotated") | — |
| `page07_seg02.png` | `1700x380+0+300` | N = dL/dt = dL/dt|body + ω×L; component form N_1 = dL_1/dt|body + ω_2 L_3 − ω_3 L_2 | — |
| `page07_seg03.png` | `1700x320+0+620` | L_i = I_i ω_i; İ_i|body = 0 for a rigid body (ṙ_P = 0 in the body frame); N_1 = I_1 dω_1/dt|body + ω_2ω_3(I_3 − I_2) | — |
| `page07_seg04.png` | `1700x480+0+880` | **Boxed** Euler's equations: I_1 ω̇_1 = ω_2ω_3(I_2−I_3) + N_1; I_2 ω̇_2 = ω_3ω_1(I_3−I_1) + N_2; I_3 ω̇_3 = ω_1ω_2(I_1−I_2) + N_3 | — |
| `page07_seg05.png` | `1700x460+0+1300` | "APPLICATIONS — Kater's Pendulum"; upper half of the pendulum diagram with body axes ê_1,ê_2,ê_3 = ê_1×ê_2; n = 1 degree of freedom, angle Φ as generalized coordinate, no friction; lab frame I ω̇_3 = dL_3/dt = N_3 = −Mgl sinΦ | — |
| `page07_seg06.png` | `1700x760+0+1440` | Complete Kater's-pendulum diagram (Q, CM, P, l, l′, l_1, Mg, g direction) plus N = lê_1×Mg = −Mgl sinΦ ê_3; small-angle limit IΦ̈ ≈ −MglΦ, Φ̈ = −Ω²Φ, Ω = (Mgl/I)^½ frequency of oscillation (extends to page bottom) | — |

## Page 08 — Radius of gyration, percussion center; torque-free symmetric top (6 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page08_seg01.png` | `1700x340+0+0` | "Parallel axis theorem" I = Ī + Ml² = M(k̄² + l²) = Mk²; definition of the radius of gyration k by I ≡ Mk²; definition l_1 ≡ k²/l = l + k̄²/l | — |
| `page08_seg02.png` | `1700x420+0+280` | Ω_Q² = Mgl/M(k̄²+l²) = g/l_1; dimensional check [Ω²] = 1/T²; comparison with the simple pendulum Ω = √(g/l), point mass ⇒ Ī = 0 ⇒ k̄ = 0 ⇒ l_1 = l | — |
| `page08_seg03.png` | `1700x480+0+640` | Ī = ∫d³r ρ(r)(r_1²+r_2²) with distances measured wrt CM; r_1/r_2 diagram and point-mass case r_1 = r_2 = 0; full expression k̄² = Ī/M = ∫d³r ρ(r)(r_1²+r_2²)/∫d³r ρ(r) = mass-weighted mean square distance to the axis | — |
| `page08_seg04.png` | `1700x340+0+1000` | Interpretation of k̄² as the average squared distance to the rotation axis; "Suspend the pendulum from point P ('percussion center') at distance l_1 from Q, along the direction through the CM" | — |
| `page08_seg05.png` | `1700x320+0+1280` | Ω_Q² = g/l_1 alongside Ω_P² = gl′/(k̄²+l′²) reduced step by step to gl/(l²+k̄²) = Ω_Q²; supporting relations l_1 = l + k̄²/l, l_1 − l = k̄²/l, (l_1−l)² = k̄⁴/l² | — |
| `page08_seg06.png` | `1700x660+0+1540` | "Torque-Free Motion in 3D: SYMMETRIC TOP", I_1 = I_2 ≠ I_3, Ω ≡ ω_3(I_3−I_1)/I_1; the three Euler equations reduced to the **boxed** set ω̇_1 = −Ωω_2, ω̇_2 = Ωω_1, ω̇_3 = 0 (extends to page bottom) | — |

## Page 09 — Precession; Euler angles (7 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page09_seg01.png` | `1700x340+0+0` | ω̇ = Ω ê_3 × ω ⇔ ω rotates with angular velocity Ωê_3 ⇒ PRECESSION; component form ω̇_1 = −Ωω_2, ω̇_2 = Ωω_1, ω̇_3 = 0 | — |
| `page09_seg02.png` | `1700x400+0+280` | "ω rotates around ê_3 with angular speed Ω"; initial condition ω = ω(sinλ ê_1 + cosλ ê_3); **boxed** solution ω_1 = ω sinλ cos(Ωt), ω_2 = ω sinλ sin(Ωt), ω_3 = ω cosλ | — |
| `page09_seg03.png` | `1700x380+0+620` | Precession-cone diagram (Ω precession vs ω rotation, half-angle λ); section rule; start of the inertial/body unit-vector definitions | — |
| `page09_seg04.png` | `1700x400+0+940` | ê°_1 ê°_2 ê°_3 = inertial (non-rotating) set vs ê_1 ê_2 ê_3 = body (rotating) set; CM/inertial axes diagram; "we need 6 coordinates to describe all points in a rigid body" | — |
| `page09_seg05.png` | `1700x340+0+1280` | 6 coordinates split: CM position R ↔ XYZ, plus 3 coordinates fixing the orientation of ê_i wrt ê°_i; "We choose Euler angles α, β, γ"; "Following Ch 5 F&W (skipping a lot)" | (1)–(5) intro |
| `page09_seg06.png` | `1700x620+0+1460` | Complete Euler-angle diagram (ê°_i, ê_i, ê_β line of nodes, angles α, β, γ); bullet definitions — ê_β ⊥ ê°_3, ê_3; β polar / α azimuthal orientation of the new north pole; γ additional rotation about ê_3; α,β,γ as generalized coordinates; T = ½(I_1ω_1²+I_2ω_2²+I_3ω_3²); ω = α̇ê°_3 + β̇ê_β + γ̇ê_3; ê_β = cosγ ê_2 + sinγ ê_1; ê°_3 = cosβ ê_3 + sinβ[cosγ(−ê_1) + sinγ ê_2] | (1)(2)(3)(4) |
| `page09_seg07.png` | `1700x400+0+1800` | Lower part of the Euler-angle diagram with the line of nodes labelled; eqs (1)–(4) again plus the **green-boxed** master result ω = (−α̇ sinβ cosγ + β̇ sinγ)ê_1 + (α̇ sinβ sinγ + β̇ cosγ)ê_2 + (γ̇ + α̇ cosβ)ê_3 | (1)(2)(3)(4)(5) |

## Page 10 — Infinitesimal rotations; kinetic energy; symmetric-top Lagrangian (7 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page10_seg01.png` | `1700x320+0+0` | NOTE on infinitesimal rotations: R_α = 1 + M_α α̇ dt, R_β = 1 + M_β β̇ dt; R_αR_β and R_βR_α agree to order dt ⇒ infinitesimal rotations add, ω = ω_α + ω_β + ω_γ | (6)(7)(8)(9)(10) |
| `page10_seg02.png` | `1700x340+0+260` | "KINETIC ENERGY — general case"; **boxed** T = ½I_1ω_1² + ½I_2ω_2² + ½I_3ω_3² written out fully in α̇, β̇, γ̇ | (11) |
| `page10_seg03.png` | `1700x340+0+540` | Symmetric top I_1 = I_2; **boxed** T = (I_1/2)(β̇² + α̇²sin²β) + (I_3/2)(γ̇ + α̇cosβ)²; torque-free motion of a symmetric top, **boxed** L = T | (12)(13)(14) |
| `page10_seg04.png` | `1700x380+0+820` | α,β,γ generalized coordinates ⇒ 3 Lagrange equations; 2 cyclic coordinates α, γ ⇒ 2 constants of motion p_α = I_1 sin²β α̇ + I_3(γ̇+α̇cosβ)cosβ and p_γ = I_3(γ̇+α̇cosβ); boxed preview p_α = L·ê°_3, p_γ = L·ê_3 | (15)(16)(17)(18)(19) |
| `page10_seg05.png` | `1700x360+0+1140` | "Recall" the ω expansion (5); p_γ = I_3ω_3 = L·ê_3 "as anticipated"; also p_α; L = I_1(ω_1ê_1 + ω_2ê_2) + I_3ω_3ê_3 | (5)(16)(17)(19)(20) |
| `page10_seg06.png` | `1700x380+0+1440` | "Compare with" L·ê°_3 expanded using (20) and (4); the long substitution of the ω components | (20)(21)(22) |
| `page10_seg07.png` | `1700x440+0+1760` | Simplification using cos²γ + sin²γ = 1; **boxed** L·ê°_3 = I_1 α̇ sin²β + I_3(γ̇+α̇cosβ)cosβ = p_α ✓ (bottom of written content) | (22)(23)(18) |

## Page 11 — p_β; description in the inertial (CM) frame (7 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page11_seg01.png` | `1700x460+0+0` | p_β = ∂L/∂β̇ = I_1β̇, not a constant in principle because β appears explicitly in the Lagrangian; ∂L/∂β evaluated; **boxed** ṗ_β = α̇ sinβ (I_1 α̇ cosβ − I_3 ω_3), with "(However, see later)" | (24)(25)(26) |
| `page11_seg02.png` | `1700x380+0+400` | "Compare p_β with" L·ê_β using (20) and (3); "Recall" the ω expansion (5); L·ê_β expanded in components | (20)(3)(5)(27) |
| `page11_seg03.png` | `1700x340+0+720` | L·ê_β = I_1β̇(sin²γ + cos²γ) = I_1β̇ ⇒ **boxed** L·ê_β = p_β ✓; header "Description in Inertial (or CM) Frame"; choose ê°_3 ∥ L ⇒ L·ê°_3 = |L| and L = |L| ê°_3 | (27)(28)(29)(32)(34)(35) |
| `page11_seg04.png` | `1700x400+0+1000` | No torque ⇒ L̇ = 0 ⇒ |L| does not change; L·ê_3 = p_γ is a constant of the motion ⇒ ê°_3·ê_3 constant | (30)(31)(32)(33)(35)(36)(37) |
| `page11_seg05.png` | `1700x380+0+1340` | const = ê°_3·ê_3 = cos(angle between ê_3 and ê°_3) = cosβ ⇒ β is a constant of the motion ⇒ β̇ = 0 ⇒ **boxed** p_β = I_1β̇ = L·ê_β = 0; margin note that for this choice of axes p_β and L·ê_β are both zero | (38)(39)(40)(41) |
| `page11_seg06.png` | `1700x340+0+1660` | From L·ê_β = 0 with L ≠ 0 and |ê_β| = 1 ⇒ L ⊥ ê_β ⇒ **boxed** L lies in the plane of ê_3 and ê°_3; "CONSTANTS: I_1, I_3, β, I_3ω_3 = L_3, p_α"; p_α = I_1 sin²β α̇ + I_3 ω_3 cosβ ⇒ **boxed** α̇ constant | (41)(42)(43)(16)(5)(44)(45) |
| `page11_seg07.png` | `1700x260+0+1940` | p_γ = I_3(γ̇ + α̇cosβ) with I_3, p_γ, α̇, β constant ⇒ **boxed** γ̇ constant; α = α̇_0 t and γ = γ̇_0 t with constant rates (bottom of page) | (17)(46)(47)(48) |

## Page 12 — Precession rate; closing comparison (4 segments)

| File | Geometry | Content | Eqs |
|---|---|---|---|
| `page12_seg01.png` | `1700x340+0+0` | 0 = ṗ_β = α̇ sinβ(I_1 α̇ cosβ − I_3ω_3) ⇒ **boxed** α̇ cosβ = I_3ω_3/I_1; from (5), ω_3 = γ̇ + α̇cosβ ⇒ **boxed** γ̇ = ω_3(I_1−I_3)/I_1 = −Ω | (41)(26)(49)(5)(51) |
| `page12_seg02.png` | `1700x340+0+280` | ê_3 / ω / Ω orientation sketch; Ω = ω_3(I_3−I_1)/I_1 with the note that it was defined earlier when looking at the body-frame evolution of ω; start of the boxed ω = α̇ê°_3 + γ̇ê_3 | (50)(51)(52) |
| `page12_seg03.png` | `1700x340+0+560` | **Boxed** ω = α̇ê°_3 + γ̇ê_3 ⇒ **boxed** ê_3, ê°_3, ω, L are coplanar; "Consider cases where I_1 = I_2 < I_3 or I_1 = I_2 > I_3"; L = I_1(ω_1ê_1 + ω_2ê_2) + I_3ω_3ê_3 | (2)(40)(52)(53)(20) |
| `page12_seg04.png` | `1700x340+0+840` | Closing comparison box: simple pendulum θ̈ = −(g/l) sinθ vs thumbtack (angle)″ = −[awful mess]·sin(angle); closing rule. Remainder of page 12 is blank. | — |

---

## Notes / marginal legibility

* Page 12 is only ~half full: all written content ends by y ≈ 1110 px. Segments below that would be blank and were not produced.
* Handwriting shorthand that may need care downstream: "None irregular" on page 05 (likely "Now irregular"/"More irregular"); "Kater's Pendulum" heading on page 07 is loosely written; "Levi-Civita" is consistently spelled "Levi-Cuita" in the notes.
* Page 05 has a stray tick mark in the right margin around y ≈ 1500 (not content).
* Equation numbering restarts between page 01 (1)–(27) and page 09 (1)–(53). Pages 02–08 carry no marginal numbers; references to (16), (17), (20), (5) etc. on pages 10–12 point to the page-09-onward series.
* Colour coding in the source: blue = section headers/emphasis (pages 01, 07); green = Euler-angle kinematics (pages 09–11); red = "use α β γ as generalized coordinates" annotation (page 09).
