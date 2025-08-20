# LLM-Executable Sprint: Convert Protocol MDs → Styled HTML pages + Index

Date: 2025-08-20
Owner: automated agent / repo maintainer
Branch: `feature/protocols-html` (recommended; working on `main` is allowed per instruction)
Estimate: 4–6 hours (single sprint)

Purpose
-------
This file contains deterministic, machine-executable instructions for converting canonical Markdown protocols from `research/protocol expansions/` into styled HTML pages under `docs/site/protocols/`, generating an index (`docs/site/protocols.html`), appending safe CSS rules, and inserting compact `<details>` summaries into topic pages. The content below includes an exact Python script, CSS snippet, insertion rules, run commands (PowerShell), and QA steps so an LLM or automation can execute with no ambiguity.

Top-level checklist (mark each step done)
- [ ] Create branch `feature/protocols-html` (or operate on `main` per permission)
- [ ] Add `scripts/build_protocols.py` (exact script included)
- [ ] Run converter to generate `docs/site/protocols/` and `docs/site/protocols.html`
- [ ] Append CSS rules to `docs/styles.css` (exact snippet included)
- [ ] Insert `<details>` snippets into `docs/site/attention.html` and `docs/site/recovery.html` at the section `<section class="protocol-section">`
- [ ] Validate internal links and anchors
- [ ] Produce a JSON report at `commissions/todo/protocols-next-sprint-report.json`
- [ ] Commit changes and push branch (or commit to `main`)

Inputs and outputs (contract)
- Inputs:
   - Markdown sources: `research/protocol expansions/*.md`
   - Site stylesheet: `docs/styles.css`
   - Topic pages to update: `docs/site/attention.html`, `docs/site/recovery.html`
- Outputs:
   - HTML pages: `docs/site/protocols/<slug>.html` (one per MD)
   - Index: `docs/site/protocols.html`
   - Manifest: `docs/site/protocols/manifest.json`
   - Appended CSS block in `docs/styles.css`
   - Modified topic pages with `<details>` snippets

Slug rules (deterministic)
- Lowercase
- Replace any sequence of non-alphanumeric characters with `-`
- Trim leading/trailing `-`
- Collapse multiple `-` into single `-`
- Example: `Mindfulness & Awareness Protocol.md` -> `mindfulness-awareness-protocol`

Exact Python converter (copy this file verbatim)
------------------------------------------------
Create file: `scripts/build_protocols.py`

```python
#!/usr/bin/env python3
"""Build protocol HTML pages from Markdown source files.
Run: python scripts/build_protocols.py
"""
import re
import json
from pathlib import Path

try:
      import markdown
except Exception:
      raise SystemExit("Missing dependency: run 'pip install markdown' before running this script.")

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / 'research' / 'protocol expansions'
OUT_DIR = ROOT / 'docs' / 'site' / 'protocols'
OUT_DIR.mkdir(parents=True, exist_ok=True)
STYLE_LINK = '../styles.css'

def slugify(name: str) -> str:
      s = name.lower()
      s = re.sub(r"[^a-z0-9]+", '-', s)
      s = re.sub(r'-{2,}', '-', s)
      s = s.strip('-')
      return s

def read_md(p: Path) -> dict:
      text = p.read_text(encoding='utf-8')
      title_m = re.search(r'^#\s+(.+)$', text, flags=re.M)
      title = title_m.group(1).strip() if title_m else p.stem
      parts = re.split(r'\n\s*\n', text.strip())
      summary = parts[1].strip() if len(parts) > 1 else (parts[0].strip() if parts else '')
      html = markdown.markdown(text, extensions=['fenced_code', 'tables'])
      return {'title': title, 'summary': summary, 'html': html}

TEMPLATE = f'''<!doctype html>
<html lang="en">
<head>
   <meta charset="utf-8" />
   <meta name="viewport" content="width=device-width, initial-scale=1" />
   <title>{{TITLE}} — Project Dukkha</title>
   <link rel="stylesheet" href="{STYLE_LINK}">
</head>
<body>
   <nav class="nav"><div class="nav-container"><a href="../index.html">Home</a> · <a href="../protocols.html">Protocols</a></div></nav>
   <main class="protocol-article container">
      <article>
         <h1>{{TITLE}}</h1>
         <p class="lead">{{SUMMARY}}</p>
         <section class="protocol-body">{{CONTENT}}</section>
      </article>
   </main>
   <footer class="footer container"><p>Project Dukkha</p></footer>
</body>
</html>'''

manifest = []
for md in sorted(SRC_DIR.glob('*.md')):
      data = read_md(md)
      slug = slugify(data['title'] or md.stem)
      out = OUT_DIR / f"{slug}.html"
      # handle duplicates deterministically
      i = 1
      base = slug
      while out.exists():
            slug = f"{base}-{i}"
            out = OUT_DIR / f"{slug}.html"
            i += 1
      content = TEMPLATE.replace('{{TITLE}}', data['title']).replace('{{SUMMARY}}', data['summary']).replace('{{CONTENT}}', data['html'])
      out.write_text(content, encoding='utf-8')
      manifest.append({'title': data['title'], 'slug': slug, 'file': f'protocols/{slug}.html', 'summary': data['summary']})

manifest_path = OUT_DIR / 'manifest.json'
manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
print(f'Generated {len(manifest)} pages in {OUT_DIR}')

# Generate top-level index
INDEX_PATH = ROOT / 'docs' / 'site' / 'protocols.html'
index_items = '\n'.join([f"<article class=\"protocol-card\" id=\"protocol-{m['slug']}\">\n  <h2>{m['title']}</h2>\n  <p>{m['summary']}</p>\n  <a href=\"protocols/{m['slug']}.html\">Read full protocol</a>\n</article>" for m in manifest])
INDEX_HTML = f"""<!doctype html>
<html lang=\"en\"> 
<head>
   <meta charset=\"utf-8\"> 
   <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> 
   <title>Protocols — Project Dukkha</title>
   <link rel=\"stylesheet\" href=\"../styles.css\"> 
</head>
<body>
   <nav class=\"nav\"><div class=\"nav-container\"><a href=\"../index.html\">Home</a></div></nav>
   <main class=\"container protocol-list\">{index_items}</main>
</body>
</html>"""
INDEX_PATH.write_text(INDEX_HTML, encoding='utf-8')
print(f'Wrote index: {INDEX_PATH}')

```

Dependencies & run
------------------
- Python 3.8+
- Install dependency:

```powershell
pip install markdown
```

Run (PowerShell) — deterministic commands
------------------------------------------------
From repo root:

```powershell
# create branch (optional)
git checkout -b feature/protocols-html
# run converter
python .\scripts\build_protocols.py
```

CSS snippet to append (exact)
-----------------------------
Append the following block at the end of `docs/styles.css`.

```css
/* Protocol page styles - appended by sprint */
.protocol-list { display:grid; gap:1rem; grid-template-columns:1fr; max-width:900px; margin:2rem auto; }
.protocol-card { border:1px solid var(--color-border); padding:1rem; border-radius:8px; background:var(--color-surface-elevated); }
.protocol-article { max-width:900px; margin:6rem auto; padding:var(--space-6); background:var(--color-surface-elevated); border-radius:var(--border-radius); box-shadow:var(--shadow-sm); }
.protocol-article .lead { font-size:var(--text-lg); color:var(--color-text-secondary); }
details.protocol-summary { border:1px solid var(--color-border); padding:0.6rem; border-radius:6px; background:transparent; }
details.protocol-summary summary { font-weight:600; cursor:pointer; }
@media print { details.protocol-summary { display:block; } }
```

Exact `<details>` snippet to insert
---------------------------------
Insert this inside the `<section class="protocol-section">` element of `docs/site/attention.html` and `docs/site/recovery.html`. Replace `{{slug}}`, `{{Title}}`, and `{{One-sentence summary}}` deterministically from `manifest.json`.

```html
<details class="protocol-summary" id="protocol-{{slug}}-summary">
   <summary>{{Title}}</summary>
   <p>{{One-sentence summary}}</p>
   <ul>
      <li>Quick step 1</li>
      <li>Quick step 2</li>
   </ul>
   <p><a href="protocols/{{slug}}.html">Read full protocol and resources</a></p>
</details>
```

Deterministic insertion rule
----------------------------
1. Open `docs/site/attention.html`.
2. Locate the substring `<section class="protocol-section">` and insert the details snippet immediately after the opening tag and before any existing content in that section.
3. Repeat for `docs/site/recovery.html`.
4. If the section is missing, create it below the last `</section>` before the footer using the exact opening tag and then insert snippets.

Validation steps (LLM must run and record results)
-------------------------------------------------
1. Confirm `docs/site/protocols/manifest.json` exists and parse it.
2. For each manifest entry, assert the corresponding `docs/site/protocols/<slug>.html` file exists.
3. Assert `docs/site/protocols.html` contains `<article id="protocol-<slug>">` for each slug.
4. Assert `docs/site/attention.html` and `docs/site/recovery.html` contain `id="protocol-<slug>-summary"` for inserted snippets.
5. Optionally confirm `docs/site/protocols/<slug>.html` contains the stylesheet link `<link rel="stylesheet" href="../styles.css">`.

Reporting (JSON)
-----------------
Write `commissions/todo/protocols-next-sprint-report.json` with the shape:

```
{
   "generated": <number>,
   "files": [ "docs/site/protocols/<slug>.html", ... ],
   "index": "docs/site/protocols.html",
   "manifest": "docs/site/protocols/manifest.json",
   "inserted_details": [ "docs/site/attention.html#protocol-<slug>-summary", ... ],
   "errors": []
}
```

Commit instructions (exact commands)
-----------------------------------
```powershell
git add docs/site/protocols/ docs/site/protocols.html docs/styles.css scripts/build_protocols.py
git commit -m "Add generated protocol pages, index, and styles (feature/protocols-html)"
git push --set-upstream origin feature/protocols-html
```

Acceptance criteria (must be auto-checked)
- All generated HTML files exist and link the stylesheet.
- `docs/site/protocols.html` includes an entry for every MD file in `research/protocol expansions/`.
- `<details>` snippets exist in target topic pages and point to generated pages.
- `docs/styles.css` contains the appended CSS block.
- `docs/site/protocols/manifest.json` exists and is non-empty.

If you'd like, reply with "go" and I will implement this sprint now (create the script, run it, append CSS, insert snippets, and produce the report). 

