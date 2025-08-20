# Dukkha — Dopamine Cartography

Mythic yet practical research on dopamine as a cultural and behavioural engine.
This repository is a workspace for assembling an evidence‑grounded field guide
and a handful of supporting design guardrails.

## Table of contents

1. [Vision](#vision)
2. [Audience](#audience)
3. [Repository layout](#repository-layout)
4. [Getting started](#getting-started)
5. [Contributing](#contributing)
6. [QA & quality gates](#qa--quality-gates)
7. [Roadmap](#roadmap)
8. [License](#license)

## Vision

Reframe dopamine beyond pop‑neuro headlines. The project aims to produce a
compact field guide that helps readers:

- Recognise recurring traps, rituals and resets in everyday products.
- Map scientific claims to practical mitigations and design ethics.
- Use concise printables and interactive diagrams for teaching and reflection.

Tone: mythic and humane — rigorous about evidence yet generous with analogy and
practicality.

## Audience

- Designers and product teams building attention‑sensitive experiences.
- Practitioners interested in habit, attention and wellbeing.
- Curious readers seeking evidence‑grounded explanations rather than pop
  summaries.

## Repository layout

The workspace is artifact‑first. Raw research is canonical; everything else is
derived from it.

```
dukkha.code-workspace
README.md
docs/        # prototype static site and assets
pages/       # skeleton prose for eventual guide pages
research/    # curated claims, evidence, quotes and refs
scripts/     # QA helpers (PowerShell / batch)
notes/       # scratch notes and planning material
```

Key research files inside each `research/Rn` folder:

- `claims.yaml` – distilled claim, confidence and reference pointers.
- `evidence.md` – curated supporting notes and excerpts.
- `quotes.md` – pulled quotations for future prose.
- `refs.bib` – BibTeX citations; PDFs live alongside when available.

## Getting started

1. Browse a claim file, e.g. `research/R1/claims.yaml`, for the distilled claim
   and references.
2. Read `evidence.md` in the same folder for supporting excerpts.
3. Open related PDFs with your system viewer for full context.
4. Explore draft guide pages under `pages/` or the prototype site in `docs/`.

Example PowerShell usage from the repository root:

```powershell
# open a claims YAML in the default app
start .\research\R1\claims.yaml

# open a PDF
start .\research\R6\"R6 - Attention & Drive in a Distracting Economy.pdf"

# list research folders
Get-ChildItem .\research\ | Select-Object Name
```

## Contributing

This project is lightweight and informal. To add or update research:

1. Create or modify a folder under `research/` following the existing pattern:
   `claims.yaml`, `evidence.md`, `quotes.md`, `refs.bib` and optional PDFs.
2. Keep claims atomic and tag each with a confidence score and a one‑line
   provenance statement.
3. Add supporting excerpts to `evidence.md` with page numbers and a brief
   explanation.
4. Add a BibTeX entry to `refs.bib` and ensure any new PDF lives in the same
   folder.
5. Proofread for clarity and tone before submitting a pull request.

Suggested pull‑request checklist:

- [ ] Update `claims.yaml` (claim, confidence, source refs).
- [ ] Add excerpt to `evidence.md` with page numbers.
- [ ] Add BibTeX entry to `refs.bib`.
- [ ] Run the QA script (see below) if you touched the site.

## QA & quality gates

No build tools are required to read the repository. For the experimental site
in `docs/`, a small PowerShell script checks footnote anchors and (optionally)
reference URLs:

```powershell
pwsh scripts/qa_check.ps1        # anchor/id parity only
pwsh scripts/qa_check.ps1 -CheckUrls  # also validate reference URLs
```

When adding code or site content, include a minimal smoke test that the
generated HTML renders the expected headings.

## Roadmap

- Scaffold a tiny static site generator that renders `research/*` to `docs/`.
- Add a short `CONTRIBUTING.md` with a claim YAML example.
- Add an explicit `LICENSE` (MIT recommended) if the project is published.

## License

No dedicated `LICENSE` file is present. Add one if you plan to permit public
reuse.

