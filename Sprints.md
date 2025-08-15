# Sprints.md (LLM‑Optimized)

> **Project:** Project Dukkha — Dopamine Cartography
> **Stack:** Python‑only (MkDocs + Material)
> **Operator:** LLM (Codex) running tasks sequentially as written.
> **Contract:** Each task = one atomic change + one verification + one commit.

---

## 0. LLM Operator Guidelines (Read First)

* **Atomicity:** One task = one commit.
* **Idempotency:** If a file exists, overwrite exactly with the content below.
* **Paths:** Treat all paths as relative to repo root.
* **Verification:** Run the exact commands; confirm expected strings.
* **Stop Conditions:** If verification fails, stop and report the failing step and stderr.
* **Style:** Use provided commit message format; open PRs as specified.

---

## 1) Global Setup (One‑time)

### 1.1 Create repo scaffolding

**Action**

* Create folders:

```
docs/
docs/manifesto/
docs/truth/
docs/model/
docs/practice/
docs/briefs/
docs/library/
docs/assets/figures/
docs/partials/
docs/data/
ci/
```

* Create files:

```
.gitignore
LICENSE
README.md
mkdocs.yml
docs/index.md
docs/manifesto/index.md
docs/truth/index.md
docs/model/index.md
docs/practice/index.md
docs/briefs/index.md
docs/library/index.md
docs/data/references.bib
docs/data/glossary.yaml
docs/partials/main.py
```

**File: `.gitignore` (overwrite)**

```
site/
*.pyc
__pycache__/
```

**File: `LICENSE` (overwrite)**

```
MIT License

Copyright (c) 2025 …

Permission is hereby granted, free of charge, to any person obtaining a copy…
```

**File: `README.md` (overwrite)**

````markdown
# Project Dukkha — Dopamine Cartography

Python-only site using MkDocs + Material. Author in Markdown + YAML front-matter.
Run locally:
```bash
pip install mkdocs mkdocs-material mkdocs-bibtex mkdocs-macros-plugin mkdocs-awesome-pages-plugin mkdocs-glightbox pymdown-extensions mkdocs-gen-files
mkdocs serve
````

Sections: Manifesto, Truth, Model, Practice, Briefs, Library.
Editorial states: `draft` → `review` → `final`.

````

**File: `mkdocs.yml` (overwrite)**
```yaml
site_name: Project Dukkha
theme:
  name: material
  palette:
    - scheme: slate
  features:
    - navigation.sections
    - content.code.copy
    - content.tabs.link
markdown_extensions:
  - admonition
  - attr_list
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed
  - pymdownx.critic
plugins:
  - search
  - bibtex:
      bib_file: docs/data/references.bib
  - macros
  - awesome-pages
  - glightbox
  - gen-files
nav:
  - Home: index.md
  - Manifesto:
      - manifesto/index.md
  - Truth:
      - truth/index.md
  - Model:
      - model/index.md
  - Practice:
      - practice/index.md
  - Briefs:
      - briefs/index.md
  - Library:
      - library/index.md
extra_css:
  - assets/dukkha.css
````

**File: `docs/index.md` (overwrite)**

```markdown
---
title: "Project Dukkha"
status: "draft"
updated: "2025-08-15"
---

# Project Dukkha — Dopamine Cartography

- [Manifesto](manifesto/index.md)
- [Truth](truth/index.md)
- [Model](model/index.md)
- [Practice](practice/index.md)
- [Briefs](briefs/index.md)
- [Library](library/index.md)

{{ thesis_card(title="Dopamine as Mythic Engine", takeaway="We map wanting, liking, and learning to regain autonomy.", refs=[]) }}
```

**Files: section placeholders (overwrite each)**

```markdown
---
title: "PLACEHOLDER"
status: "draft"
updated: "2025-08-15"
---
Section placeholder. Content forthcoming.
```

**File: `docs/data/references.bib` (overwrite)**

```
@article{schultz1997,
  author = {Schultz, Wolfram and Dayan, Peter and Montague, P. Read},
  title = {A Neural Substrate of Prediction and Reward},
  journal = {Science},
  year = {1997}
}
@article{berridge2009,
  author = {Berridge, Kent C. and Kringelbach, Morten L.},
  title = {Affective neuroscience of pleasure: reward in humans and animals},
  journal = {Psychopharmacology},
  year = {2009}
}
```

**File: `docs/data/glossary.yaml` (overwrite)**

```yaml
incentive salience: "The 'wanting' property of a stimulus that grabs attention and drives approach."
reward prediction error: "The difference between expected and received reward; key driver in learning."
```

**File: `docs/partials/main.py` (overwrite)**

```python
def define_env(env):
    """MkDocs Macros plugin entrypoint."""
    def thesis_card(title="", takeaway="", refs=None):
        refs = refs or []
        ref_html = "" if not refs else "<div class='refs'>Refs: " + ", ".join(refs) + "</div>"
        return f"<div data-component='thesis-card'><h3>{title}</h3><p>{takeaway}</p>{ref_html}</div>"
    def caution_callout(heading="", body=""):
        return f"<div data-component='caution-callout'><strong>{heading}</strong><p>{body}</p></div>"
    def protocol_steps(steps=None):
        steps = steps or []
        lis = "".join([f"<li>{s}</li>" for s in steps])
        return f"<ol data-component='protocol-steps'>{lis}</ol>"
    def myth_science_pair(myth="", insight=""):
        return f"<div data-component='myth-science'><div class='myth'>{myth}</div><div class='insight'>{insight}</div></div>"
    def figure_with_caption(src="", caption="", id=""):
        return f"<figure id='{id}'><img src='{src}' alt='{caption}' /><figcaption>{caption}</figcaption></figure>"
    def glossary_term(term=""):
        return f"<span data-glossary='{term}'>{term}</span>"

    env.macro(thesis_card)
    env.macro(caution_callout)
    env.macro(protocol_steps)
    env.macro(myth_science_pair)
    env.macro(figure_with_caption)
    env.macro(glossary_term)
```

**File: `docs/assets/dukkha.css` (create)**

```css
[data-component='thesis-card']{border:1px solid #444;padding:1rem;border-radius:.5rem;margin:1rem 0}
[data-component='caution-callout']{border-left:4px solid #a66;padding:.75rem 1rem;background:#1b1b1b;margin:1rem 0}
[data-component='protocol-steps']{margin:1rem 0 1rem 1.25rem}
[data-component='myth-science']{display:grid;gap:.5rem}
figure{margin:1rem 0}
figcaption{font-size:.9rem;opacity:.8}
```

**Verify**

```bash
pip install mkdocs mkdocs-material mkdocs-bibtex mkdocs-macros-plugin mkdocs-awesome-pages-plugin mkdocs-glightbox pymdown-extensions mkdocs-gen-files
mkdocs serve
```

**Expect**

* Console includes: `INFO - Building documentation...` and `Serving on http://127.0.0.1:8000/`
* Home page shows a “Thesis Card” block.

**Commit**

```
feat(bootstrap): add MkDocs Material config, macros, and project scaffold
```

---

## 2) Sprint 1 — Content Pass 1

### 2.1 Manifesto page (review)

**File: `docs/manifesto/index.md` (overwrite)**

```markdown
---
title: "Dopamine as Mythic Engine"
tags: ["primer","myth:dukkha"]
takeaway: "Reframe dopamine from chemical to cultural force."
status: "review"
updated: "2025-08-15"
---

{{ thesis_card(title="Thesis", takeaway="Wanting ≠ liking; autonomy requires reading the reward map.", refs=["schultz1997","berridge2009"]) }}

{{ caution_callout(heading="Scope", body="This is a field guide, not medical advice.") }}

Intro: Why “Dukkha” matters; map over microscope; cultural drift and design.

**Key Premise**
- Dopamine steers attention via prediction error and salience.
- Systems exploit variable reward → doomscrolling, compulsion loops.

_Scholia Mode →_ [References](../library/index.md#references)
```

**Verify**

```bash
mkdocs build
```

**Expect**

* Build succeeds; page renders; references show on Library page (for now, via bib listing later).

**Commit**

```
feat(content): add Manifesto page (review) with thesis and callout
```

### 2.2 Truth page (review)

**File: `docs/truth/index.md` (overwrite)**

```markdown
---
title: "Desire ≠ Pleasure"
tags: ["misconception","incentive-salience"]
takeaway: "Incentive salience drives seeking even without pleasure."
status: "review"
updated: "2025-08-15"
---

Desire is not identical to pleasure; it is often stronger when pleasure is absent.

{{ thesis_card(title="Core Claim", takeaway="Wanting is separable from liking and learning.", refs=["berridge2009"]) }}

{{ glossary_term(term="incentive salience") }}

- Evidence sketch and implications for daily behavior.
- Practice link → craving reset protocol (forthcoming).
```

**Verify**

```bash
mkdocs build
```

**Expect**

* Build succeeds; no missing cite keys.

**Commit**

```
feat(content): add Truth page 'Desire ≠ Pleasure' (review)
```

---

## 3) Sprint 2 — Model Atlas v1

### 3.1 Add figure and model page

**File: `docs/model/index.md` (overwrite)**

```markdown
---
title: "Atlas: Wanting–Liking–Learning"
tags: ["model","triad"]
takeaway: "Three systems, distinct yet coupled."
status: "draft"
updated: "2025-08-15"
---

{{ figure_with_caption(src="/assets/figures/atlas-wll.svg", caption="The W–L–L Triad.", id="fig-wll-atlas") }}

{{ protocol_steps(steps=[
  "Start with Wanting (salience/approach).",
  "Differentiate Liking (hedonic tone).",
  "Track Learning (RPE-driven updates)."
]) }}
```

**Placeholder diagram**

* Add any valid SVG to `docs/assets/figures/atlas-wll.svg` (can be a minimal stub).

**Verify**

```bash
mkdocs build
```

**Expect**

* Diagram renders with caption; no broken links.

**Commit**

```
feat(model): add Atlas W–L–L page with placeholder diagram and reading steps
```

---

## 4) Sprint 3 — Practice Protocol v1

### 4.1 Craving Reset page

**File: `docs/practice/index.md` (overwrite)**

```markdown
---
title: "The 48‑Hour Craving Reset"
tags: ["protocol","reset"]
takeaway: "Reduce variable rewards; restore signal clarity."
status: "draft"
updated: "2025-08-15"
---

{{ caution_callout(heading="Safety", body="Behavioral routine only; stop if distress escalates.") }}

{{ myth_science_pair(myth="Icarus", insight="Over-prediction of reward under novelty inflates risk-taking.") }}

{{ protocol_steps(steps=[
  "Prepare: Identify variable reward cues (apps/sites) and remove for 48h.",
  "Replace: Pre-plan alternative activities (walk, call friend, read).",
  "Observe: Note craving peaks; use 2×5 min breathwork windows.",
  "Reflect: After 48h, reintroduce selectively with time boxes."
]) }}
```

**Verify**

```bash
mkdocs build
```

**Commit**

```
feat(practice): add 48‑Hour Craving Reset protocol (draft)
```

---

## 5) Sprint 4 — Brief + Library

### 5.1 Doomscrolling brief

**File: `docs/briefs/index.md` (overwrite)**

```markdown
---
title: "Doomscrolling & Variable Reward"
tags: ["brief","intermittent-reinforcement"]
takeaway: "Intermittent schedules maximize attention capture."
status: "draft"
updated: "2025-08-15"
---

Mechanism overview; checklist of anti-patterns; links to Truth and Practice.

- See: [Desire ≠ Pleasure](../truth/index.md)
- Use: [Craving Reset](../practice/index.md)
```

**Commit**

```
feat(briefs): add Doomscrolling & Variable Reward brief (draft)
```

### 5.2 Library index (temporary)

**File: `docs/library/index.md` (overwrite)**

```markdown
---
title: "Library"
status: "draft"
updated: "2025-08-15"
---

# References
Citations are managed via BibTeX in `docs/data/references.bib`.  
(Full render can be enhanced with templates later.)

# Glossary
- {{ glossary_term(term="incentive salience") }}
- {{ glossary_term(term="reward prediction error") }}
```

**Verify**

```bash
mkdocs build
```

**Commit**

```
feat(library): add Library index with glossary hooks
```

---

## 6) Sprint 5 — QA & Governance

### 6.1 CONTRIBUTING and ethics

**File: `CONTRIBUTING.md` (overwrite)**

```markdown
# Contributing

Statuses: `draft` → `review` → `final`.  
Each analytical page: ≥2 primary sources; glossary links where relevant.  
Run: `mkdocs build` before committing.
```

**File: `docs/ethics.md` (create)**

```markdown
---
title: "Editorial Policy & Ethics"
status: "draft"
updated: "2025-08-15"
---
We prioritize autonomy-preserving design and transparent claims with citations.
```

**Verify**

```bash
mkdocs build
```

**Commit**

```
docs(governance): add CONTRIBUTING and Editorial Policy & Ethics
```

---

## 7) CI Placeholder (optional when allowed)

**File: `ci/linkcheck.yml` (create)**

```yaml
# Placeholder for future link checks
```

**Commit**

```
chore(ci): add linkcheck placeholder
```

---

## Machine‑Readable Checklist (for Codex)

```yaml
version: 1
tasks:
  - id: 0.1
    name: bootstrap_scaffold
    modifies: ["mkdocs.yml",".gitignore","LICENSE","README.md","docs/**","ci/**"]
    verify: ["mkdocs serve (expect 'Serving on http://127.0.0.1:8000/')"]
  - id: 1.1
    name: manifesto_page
    modifies: ["docs/manifesto/index.md"]
    verify: ["mkdocs build (expect no errors)"]
  - id: 1.2
    name: truth_page
    modifies: ["docs/truth/index.md"]
    verify: ["mkdocs build (expect no errors)"]
  - id: 2.1
    name: model_page
    modifies: ["docs/model/index.md","docs/assets/figures/atlas-wll.svg"]
    verify: ["mkdocs build (expect no errors)"]
  - id: 3.1
    name: practice_page
    modifies: ["docs/practice/index.md"]
    verify: ["mkdocs build (expect no errors)"]
  - id: 4.1
    name: brief_page
    modifies: ["docs/briefs/index.md"]
    verify: ["mkdocs build (expect no errors)"]
  - id: 4.2
    name: library_index
    modifies: ["docs/library/index.md"]
    verify: ["mkdocs build (expect no errors)"]
  - id: 5.1
    name: governance
    modifies: ["CONTRIBUTING.md","docs/ethics.md"]
    verify: ["mkdocs build (expect no errors)"]
```

---

## PR Protocol

* Branch per sprint: `feat/sprint-<n>-<slug>`
* PR title: `feat(sprint-<n>): <summary>`
* Description: paste the task IDs completed and verification logs.
* Merge only after `mkdocs build` success and manual glance at localhost rendering.