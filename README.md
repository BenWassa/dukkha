# Project Dukkha — Research Workspace

This repository collects the research artifacts, notes, and reference material that feed the Dukkha / "Dopamine Cartography" project. It's an artifact-first repo: there isn't a published site in this tree right now — instead you'll find per-paper research folders and a few PDFs.

## Quick summary
- Primary content: curated research notes and bibliographies under `research/`.
- No build step required to read the material — open the Markdown, YAML, or PDF files directly.

## What to expect here
- Research claims and notes (R1..R5) — YAML and Markdown summaries, evidence and quotes, and BibTeX references.
- Additional source PDFs (R6, R7).

## Quick start
Open files in your editor or a PDF viewer. Example (from repository root):

```powershell
# open R1 claims in the default editor (Windows)
# start will open the file with the associated application
start .\research\R1\claims.yaml
# open a PDF
start .\research\R6\"R6 - Attention & Drive in a Distracting Economy.pdf"
```

Or simply browse the `research/` folder in VS Code.

## Repository structure (actual)
```
dukkha.code-workspace
README.md
research/
  R1/
    claims.yaml
    evidence.md
    quotes.md
    refs.bib
  R2/
    claims.yaml
    evidence.md
    quotes.md
    refs.bib
  R3/
    claims.yaml
    evidence.md
    quotes.md
    refs.bib
  R4/
    claims.yaml
    evidence.md
    quotes.md
    refs.bib
  R5/
    claims.yaml
    evidence.md
    quotes.md
    refs.bib
  R6/
    R6 - Attention & Drive in a Distracting Economy.pdf
  R7/
    R7 - Recovery, Stress, Sleep & the Dopamine Baseline.pdf
```

## Notes / next steps
- If you'd like a lightweight site generated from these notes (the earlier README assumed a `site/` folder), I can scaffold a simple static site generator (Eleventy, or a tiny Node/HTML pipeline) that reads `research/*` and produces `site/`.
- I can also add a CONTRIBUTING or index that surfaces claims across R1..R5 if you want a quick navigation UI.

## License
No license file found in the repo. If you want this project public, consider adding a `LICENSE` (for example, MIT) or a short note here about sharing terms.

---
Updated to reflect the repository contents on disk (research-first).


