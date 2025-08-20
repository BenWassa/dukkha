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
      content = TEMPLATE.replace('{TITLE}', data['title']).replace('{SUMMARY}', data['summary']).replace('{CONTENT}', data['html'])
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

