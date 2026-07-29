# Multi-Agent Pipeline — Run 4 Log

**Date:** 2026-07-29
**Spec:** `Multi_Agent_Outline.md`
**Batch:** 4 source PDFs, 24 pages total, processed in parallel by per-document subagent chains.

Runs 1–2 (2026-07-06) and Run 3 (2026-07-23) covered the scattering lecture only; all are archived.
Run 4 is the first **multi-input batch** run under the revised spec (parallel subagent chains,
archive-then-run-fresh, no Mathpix path, no meta-introduction in the output).

---

## Stage 0 — Ingest & Pre-flight Archive

Previous-job directories (`segments/`, `assembled/`, `mathpix_ready/`, `Final_Product_Ready/`, `Run2_Archive/`)
and the Run-3 `PIPELINE_LOG.md` were archived to `Run_Archive/2026-07-29_150406/` before anything else ran.
Fresh `segments/`, `assembled/`, `Final_Product_Ready/` were then created.

`mathpix_ready/` is **not** recreated — the Mathpix path was removed from the spec.

### Inputs registered

| Slug | Source PDF | Pages | Medium | Subject |
|------|-----------|-------|--------|---------|
| `scattering` | `Lecture-scattering-Hamiltonian_241022-forward.pdf` | 4 | handwritten | Scattering / Hamiltonian formulation |
| `oscillations` | `Lecture-Oscillations-241119_241114.pdf` | 7 | handwritten (graph paper) | Small oscillations, normal modes |
| `rotations` | `Lecture-Rotations-Rigid-241031.pdf` | 12 | handwritten (graph paper) | Elementary rotations, rigid-body dynamics |
| `comp1015` | `Lecture-241015_comp.pdf` | 1 | whiteboard photograph | Motion in a central potential, Kepler problem |

All pages verified readable and rendered to PNG at 200 DPI under `segments/<slug>/pages/`.

---

## Stage 4a — Reference Textbook Convention (decided at ingest, challenged at review)

**Chosen: Goldstein, Poole & Safko, *Classical Mechanics*, 3rd ed. (Addison-Wesley).**
Secondary/tie-break for undergraduate-level passages: Taylor, *Classical Mechanics* (University Science Books).

**Justification.** The choice is not inferred — it is stated in the source notes themselves:

- The `oscillations` notes are titled *"SMALL OSCILLATIONS (Chapter 6 Goldstein)"* in the lecturer's own hand.
- The `comp1015` whiteboard opens with *"Chapter 3 — Motion in Central Potential V(r)"*, matching Goldstein Ch. 3
  (central-force problem, Kepler, orbit equation, eccentricity).
- `scattering` covers the scattering cross-section and Hamiltonian material of Goldstein Ch. 3 / Ch. 8.
- `rotations` covers Goldstein Ch. 4–5 (rigid-body kinematics, inertia tensor, parallel-axis theorem).

The four lectures are therefore a single coherent graduate classical-mechanics course tracking Goldstein
chapter by chapter, and one convention applies across the whole batch.

**Scope of use — context and notation only.** Goldstein fixes: `L` for the Lagrangian and `\vec{L}` for angular
momentum, `T`/`V` for kinetic/potential energy, `q_j`/`\dot q_j` for generalized coordinates, `\eta` for small
displacements from equilibrium, `T_{ij}`/`V_{ij}` for the kinetic- and potential-energy matrices, `\mu` for
reduced mass, `\ell` for the conserved angular momentum in the central-force problem, and the standard
boxed-result equation style. It is **not** used to restructure, expand, or re-voice the notes.

---

## Stage 1 — Segmentation

Four segmentation subagents launched in parallel, one per document. *(in progress)*

## Stage 2 — Expert Review Loop

*(pending)*

## Stage 3 — Assembly

*(pending)*

## Stage 4b/4c — LaTeX Compilation & Publication Review

*(pending)*
