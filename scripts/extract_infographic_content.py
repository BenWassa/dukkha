#!/usr/bin/env python3
"""Simple HTML -> Markdown extractor for Project Dukkha pages.

This script scans the `backup/current-html` directory and converts each
HTML page (and protocol pages) into a Markdown file under `infographic_content/`.
It also copies original HTML files into `infographic_content/context/original_html/`.

The converter uses simple regex-based extraction and tag replacements which
is sufficient for the site's clean structure. It is not a full HTML to MD
converter but produces readable content for NotebookLM ingestion.
"""
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / 'backup' / 'current-html'
OUT_DIR = ROOT / 'infographic_content'
CONTEXT_DIR = OUT_DIR / 'context' / 'original_html'


def ensure_dirs():
    OUT_DIR.mkdir(exist_ok=True)
    CONTEXT_DIR.mkdir(parents=True, exist_ok=True)


def read_file(p: Path) -> str:
    return p.read_text(encoding='utf-8')


def write_md(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def copy_original(src: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(src.read_text(encoding='utf-8'), encoding='utf-8')


def strip_tags(html: str) -> str:
    # Convert headings
    html = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', html, flags=re.S|re.I)
    html = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', html, flags=re.S|re.I)
    html = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', html, flags=re.S|re.I)
    html = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', html, flags=re.S|re.I)

    # Figures / images
    def img_repl(m):
        attrs = m.group(1)
        alt = re.search(r'alt="([^"]*)"', attrs)
        src = re.search(r'src="([^"]*)"', attrs)
        alt_text = alt.group(1) if alt else ''
        src_text = src.group(1) if src else ''
        return f'![{alt_text}]({src_text})\n'

    html = re.sub(r'<img([^>]*)>', img_repl, html, flags=re.S|re.I)

    # Links
    html = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html, flags=re.S|re.I)

    # Lists
    html = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html, flags=re.S|re.I)
    html = re.sub(r'<ul[^>]*>', '', html, flags=re.S|re.I)
    html = re.sub(r'</ul>', '', html, flags=re.S|re.I)
    html = re.sub(r'<ol[^>]*>', '', html, flags=re.S|re.I)
    html = re.sub(r'</ol>', '', html, flags=re.S|re.I)

    # Paragraphs
    html = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', html, flags=re.S|re.I)

    # Remove scripts, styles, nav, footer and other non-content blocks
    html = re.sub(r'(?s)<script.*?</script>', '', html)
    html = re.sub(r'(?s)<style.*?</style>', '', html)
    html = re.sub(r'(?s)<nav.*?</nav>', '', html)
    html = re.sub(r'(?s)<footer.*?</footer>', '', html)
    html = re.sub(r'(?s)<header.*?</header>', '', html)

    # Remove remaining tags
    html = re.sub(r'<[^>]+>', '', html)

    # Collapse multiple blank lines
    html = re.sub(r'\n\s*\n\s*\n+', '\n\n', html)
    return html.strip()


def extract_metadata(html: str) -> dict:
    meta = {}
    title = re.search(r'<title>(.*?)</title>', html, flags=re.I|re.S)
    if title:
        meta['title'] = title.group(1).strip()
    desc = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html, flags=re.I)
    if desc:
        meta['description'] = desc.group(1).strip()
    return meta


def extract_main(html: str) -> str:
    m = re.search(r'<main[^>]*>(.*?)</main>', html, flags=re.S|re.I)
    if m:
        return m.group(1)
    # Fallback: use body
    b = re.search(r'<body[^>]*>(.*?)</body>', html, flags=re.S|re.I)
    return b.group(1) if b else html


def process_file(src_path: Path, out_md_path: Path, original_dest: Path):
    html = read_file(src_path)
    meta = extract_metadata(html)
    main_html = extract_main(html)
    md_body = strip_tags(main_html)

    header_lines = [f'<!-- Source: {src_path.relative_to(ROOT)} -->']
    if 'title' in meta:
        header_lines.append(f'# {meta.get("title")}')
    if 'description' in meta:
        header_lines.append(f'**Description:** {meta.get("description")}')

    header_lines.append('\n---\n')
    md = '\n'.join(header_lines) + '\n' + md_body + '\n'

    write_md(out_md_path, md)
    copy_original(src_path, original_dest)


def walk_and_convert():
    for root, dirs, files in os.walk(SRC_DIR):
        rel = Path(root).relative_to(SRC_DIR)
        for f in files:
            if not f.lower().endswith('.html'):
                continue
            src = Path(root) / f
            # Determine output path
            if rel == Path('.'):
                out_md = OUT_DIR / f.replace('.html', '.md')
            else:
                out_md = OUT_DIR / rel / f.replace('.html', '.md')

            orig_dest = CONTEXT_DIR / rel / f
            print(f'Processing {src} -> {out_md}')
            process_file(src, out_md, orig_dest)


def main():
    ensure_dirs()
    if not SRC_DIR.exists():
        print(f'Source directory not found: {SRC_DIR}')
        return
    walk_and_convert()
    # Write a helpful README in the context folder
    (OUT_DIR / 'context' / 'README.md').write_text(
        '# Context for infographic generation\n\n' \
        'This folder contains original HTML copies of pages used to generate the Markdown files. ' \
        'Use these files as reference for images, exact markup and diagrams when creating infographics.\n',
        encoding='utf-8')


if __name__ == '__main__':
    main()
