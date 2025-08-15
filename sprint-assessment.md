---
title: "Sprint Assessment — Project Dukkha"
updated: "2025-08-15"
---

# Sprint assessment — evidence, gaps, and next steps

Purpose: evaluate whether recent sprints produced correct and sufficient work, identify remaining tasks, and provide a prioritized action plan you can pick up from.

High-level plan I followed
- Scan the repo for evidence (site nav, docs pages, README, mkdocs config).
- Map completed pages to sprint claims and note 'status' front-matter.
- Surface gaps, risks, and concrete next steps (priority + owner tasks).

Summary of findings (short)
- Broad scaffolding and core content are present: `mkdocs.yml`, `README.md`, `docs/index.md` and topical pages under `docs/manifesto`, `docs/truth`, `docs/model`, `docs/practice`, `docs/briefs`, and `docs/library` exist.
- Several pages are in `review` or `draft` state (front-matter `status` field). No build or runtime artifacts found in repo (site is Markdown + MkDocs config).
- Missing or not found: `partials/main.py` (expected by your earlier plan but file absent). If this was meant to hold macros or helpers, confirm its location or recreate.

Evidence mapping (what's present, with file refs)
- Home: `docs/index.md` — status: `draft`, updated: 2025-08-15.
- Manifesto: `docs/manifesto/index.md` — status: `review`, contains thesis_card and references.
- Truth: `docs/truth/index.md` — status: `review`, contains core claims and glossary hooks.
- Model: `docs/model/index.md` — status: `draft`, includes an `atlas-wll.svg` figure and protocol steps.
- Project config: `mkdocs.yml` — MkDocs Material theme, plugins (bibtex, macros, awesome-pages, gen-files), and site nav configured.
- README: `README.md` documents how to run locally (pip install list + `mkdocs serve`).

Assessment against original sprint claims
- Sprint 1 (Content pass): Done — `manifesto` and `truth` pages drafted and in `review`.
- Sprint 2 (Model Atlas v1): Partially done — `model/index.md` and figure exist, but `status: draft` and explanatory text is sparse.
- Sprint 3 (Practice protocol v1): Not fully evidenced — `practice/index.md` exists in nav, but the file needs verification; explicit `craving reset` protocol text not located in top-level model pages scanned.
- Sprint 4 (Brief + Library): Partially done — `briefs/index.md` and `library/index.md` exist in nav; library references appear referenced but completeness unverified.
- Sprint 5 (QA & Governance): Partially done — `CONTRIBUTING.md` and `docs/ethics.md` exist, but editorial workflow (pull request templates, CI checks) not present.

Key gaps & risks (what still needs attention)
1) Draft states: multiple pages remain `draft`/`review` — content needs editing, citations, and sign-off.
2) Missing helper code: `partials/main.py` referenced in workspace view but not present.
3) Practice content thinness: The practical protocol(s) (craving reset) are referenced but not found in full; low user value until fleshed out.
4) No automated checks: No CI, no link-check or mkdocs build tasks detected — risk of broken navigation/links.
5) References hygiene: `bibtex` plugin configured but confirm `docs/data/references.bib` exists and entries are used.

Prioritized next steps (do these in order)
1. Confirm and add missing files
	- Verify whether `partials/main.py` should exist. If so, restore or remove references. (Quick: check your editor history or git branch.)
2. Convert draft -> review -> final: pick a single page (Manifesto) and bring it to `final` by resolving references and copy edits; use it as the style guide.
3. Flesh out Practice protocols: locate or author the `Craving Reset` protocol and add concrete steps, instruments, and an example case.
4. Add lightweight QA: a `mkdocs build` check in CI (GitHub Actions or similar) and an HTML link-checker step.
5. Verify bibliography: ensure `docs/data/references.bib` exists and key refs (e.g., `schultz1997`, `berridge2009`) resolve.

Concrete owner checklist (short) — copy this into tasks or issues
- [ ] Restore/confirm `partials/main.py` or remove references (owner: you).
- [ ] Promote `docs/manifesto/index.md` from `review` -> `final` (resolve refs, polish) (owner: you or editor).
- [ ] Draft full `Craving Reset` protocol page under `docs/practice/` and link from `docs/truth/index.md` (owner: you).
- [ ] Add `docs/data/references.bib` verification and a few missing bib entries if needed (owner: you).
- [ ] Add CI: GitHub Actions workflow with steps: install deps, `mkdocs build`, `mkdocs serve` smoke step optional, link-check (owner: you / devops).
- [ ] Manual pass: run `mkdocs serve` locally and walk site to spot content/layout issues (owner: you).

Quick verification commands (Windows PowerShell)
```powershell
pip install mkdocs mkdocs-material mkdocs-bibtex mkdocs-macros-plugin mkdocs-awesome-pages-plugin mkdocs-glightbox pymdown-extensions mkdocs-gen-files; mkdocs build
mkdocs serve
```

Contract (what "done" looks like)
- Inputs: markdown pages with front-matter `status`, `updated`, and valid citations.
- Outputs: a buildable MkDocs site where each top-level section is `final` or has a clear `review` owner.
- Error modes: broken links, missing figures, incomplete protocols, missing bib entries.

Edge cases & checks
- Empty or missing `bib` file: build will still succeed but references won't render — add guard in docs or CI to fail if key keys absent.
- Image path issues: ensure `assets/figures/*` are referenced with relative paths used by MkDocs Material.
- Long-running changes: if many pages are `draft`, split into smaller PRs per section.

Quality gates (minimal)
- Local: `mkdocs build` (PASS/FAIL)
- Lint: run a Markdown linter if available (recommended)
- Review: at least one editorial pass moving `status` to `review`, then a final to `final`.

Notes and next offers
- I replaced this file with an evidence-first assessment and a prioritized plan. If you want, I can:
	- open small PRs for the top 3 fixes (restore partials, promote Manifesto, add practice protocol scaffold), or
	- create a GitHub Actions workflow file for `mkdocs build` and link-check.

Requirements coverage
- Scour codebase and produce replacement assessment: Done (this file).
- Optimize report format and provide actionable checklist: Done.
- Flag missing files and concrete next steps: Done.

Small follow-ups you might ask next
- "Create the Actions workflow for mkdocs build"
- "Scaffold a practice protocol page with steps and example"

---
Generated on 2025-08-15 by automated assessment.

