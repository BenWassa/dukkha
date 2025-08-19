# Dukkha — Dopamine Cartography (research-first field guide)

A mythic, strategic field guide that reframes dopamine beyond pop-neuro: culture, habits, meaning, and design.

This repository is an artifact-first workspace of curated research, claims, and source material that feed a larger project: a short, practical field guide (print + small web view) and companion design guardrails.

## Vision

Reframe dopamine as a cultural and behavioral engine — not just a neurotransmitter headline. Produce a compact, actionable field guide that helps readers:
- See recurring patterns (traps, rituals, resets) across media and products.
- Map scientific claims to practical mitigations and design ethics.
- Use short, printable artifacts and interactive diagrams to teach and reflect.

Tone: mythic and humane — rigorous on evidence, generous on analogy, practical in mitigations.

## Audience
- Designers and product teams building attention-sensitive experiences.
- Practitioners interested in habit, attention, and wellbeing.
- Curious readers who want evidence-grounded, usable explanations rather than pop summaries.

## Project contract (tiny)
- Inputs: curated papers, notes, BibTeX entries, and a handful of PDFs in `research/`.
- Outputs: concise guide pages, print checklists, diagrams (SVG), and a minimal site/index (optional).
- Success: a single-passable field guide that communicates core claims and mitigations in ≤ 10 minutes to a new reader.
- Error modes: unstated claims, missing citations, outdated references.

Edge cases considered: missing PDFs, partially-complete claim YAMLs, large bibliographies, private/copyrighted PDFs.

## What this repo contains (current)
This is research-first: raw notes and sources live in `research/` and are the canonical artifacts for the project.

Structure (on disk):

```
dukkha.code-workspace
README.md
research/
  R1/  (triad: wanting / liking / learning)
    claims.yaml
    evidence.md
    quotes.md
    refs.bib
  R2/  (traps: variable reward, doomscrolling)
    ...
  R3/  (myth: taṇhā / dukkha)
    ...
  R4/  (stress: salience, relapse)
    ...
  R5/  (ethics: design guardrails)
    ...
  R6/  (PDF: Attention & Drive in a Distracting Economy)
  R7/  (PDF: Recovery, Stress, Sleep & the Dopamine Baseline)
```

Files named `claims.yaml` contain distilled claims; `evidence.md` is the curated supporting notes; `refs.bib` contains BibTeX citations.

## How to read this repo (quick)
- Open a claim file (e.g. `research/R1/claims.yaml`) to see the distilled claim + confidence and reference pointers.
- Read `evidence.md` for the curated evidence and short excerpts.
- Open PDFs with your system viewer for full sources.

Example PowerShell commands (from repo root):

```powershell
# open the R1 claims YAML in the default app
start .\research\R1\claims.yaml

# open a PDF
start .\research\R6\"R6 - Attention & Drive in a Distracting Economy.pdf"

# list research folders
Get-ChildItem .\research\ | Select-Object Name
```

## What the field guide will (eventually) include
- Home: a short quick-take and CTAs.
- Triad: wanting / liking / learning — atlas SVG + claim/evidence chips.
- Traps: variable reward, doomscrolling, and mitigations.
- Myth: cultural framing (taṇhā / dukkha) with analogies and limits.
- Stress: a human-first playbook linking stress → salience → relapse.
- Ethics: design guardrails mapped to recognized taxonomies.
- Reset: a 48-hour craving-reset checklist (print-ready).
- Library: curated DOIs and landmark reviews.

## Non-goals
- This repo will not host a large CMS or full book draft.
- It won't attempt exhaustive citation harvesting; it curates a focused set of high-value sources.

## Contribution guide (short)
- Add or update a research folder under `research/` following the existing pattern: `claims.yaml`, `evidence.md`, `quotes.md`, `refs.bib`.
- If you add a PDF, put it under a new folder `R{n}/` and reference it in `refs.bib`.
- Keep claims atomic and tag them with a confidence score (high/medium/low) and one-line provenance.

Suggested small PR checklist:
- [ ] Update `claims.yaml` (atomic claim, confidence, source refs)
- [ ] Add supporting excerpt to `evidence.md` with page numbers
- [ ] Add BibTeX entry to `refs.bib`
- [ ] Run a quick proofread for clarity and tone

## Roadmap & next steps (pick one)
- Scaffold a tiny static site generator that renders `research/*` into `site/` (Eleventy / simple Node script). Priority: index + triad page + printable reset.
- Add a short `CONTRIBUTING.md` and examples for claim YAML structure.
- Add `LICENSE` (recommended: MIT) if you plan to publish.

If you want, I can scaffold the site and make a first pass that renders each `claims.yaml` to a small HTML card index.

## Quality gates
- No build tools are required to read the repo. If we scaffold a site, we'll add a small build and CI checks.
- When adding code or a site, include a minimal smoke test that the generated `site/index.html` exists and contains expected headings.

## License
No `LICENSE` file is present in this repository. Add one if you want public reuse; I can add an MIT license file on request.

---

If you'd like, I will now:
- scaffold a minimal static site generator that renders `research/*` to `site/` (small Node script), or
- add `CONTRIBUTING.md` and a claim YAML example, or
- create a `LICENSE` file (MIT).

Tell me which next step to run and I'll implement it.


