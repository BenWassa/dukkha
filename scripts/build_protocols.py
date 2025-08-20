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
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s)
    return s.strip('-')

def extract_metadata(content: str) -> dict:
    lines = content.strip().split('\n')
    if not lines[0].startswith('# '):
        return {'title': 'Unknown Protocol', 'summary': 'No summary available'}
    
    title = lines[0][2:].strip()
    summary = 'No summary available'
    
    for i, line in enumerate(lines[1:10], 1):
        if line.strip() and not line.startswith('#'):
            summary = line.strip()
            break
    
    return {'title': title, 'summary': summary}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE} - Project Dukkha</title>
    <meta name="description" content="{SUMMARY}">
    <link rel="stylesheet" href="../styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="nav" role="navigation" aria-label="Main navigation">
        <div class="nav-container">
            <div class="nav-brand">
                <div class="brand-symbol"></div>
            </div>
            <ul class="nav-menu">
                <li><a href="../index.html" class="nav-link">Home</a></li>
                <li><a href="attention.html" class="nav-link">Focus & Attention</a></li>
                <li><a href="recovery.html" class="nav-link">Recovery & Baseline</a></li>
                <li><a href="myths.html" class="nav-link">Five Myths</a></li>
                <li><a href="model.html" class="nav-link">Model</a></li>
                <li><a href="protocols.html" class="nav-link">Protocols</a></li>
                <li><a href="library.html" class="nav-link">Library</a></li>
            </ul>
        </div>
    </nav>

    <main class="page-content">
        <section class="hero-protocols">
            <h1>{TITLE}</h1>
            <p class="tagline">A Field Guide to the Rewarded Animal</p>
        </section>

        <section class="container">
            <article class="protocol-article">
                {CONTENT}
            </article>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <div class="brand-symbol"></div>
                    <span>Project Dukkha</span>
                </div>
                <div class="footer-links">
                    <a href="library.html">Research</a>
                    <a href="#" class="print-link" onclick="window.print()">Print Guide</a>
                    <a href="mailto:contact@projectdukkha.com">Contact</a>
                </div>
            </div>
            <div class="footer-note">
                <p>This field guide is for educational purposes. Consult healthcare professionals for medical decisions.</p>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            // Smooth navigation highlighting
            const navLinks = document.querySelectorAll('.nav-link');
            navLinks.forEach(link => {{
                link.addEventListener('mouseenter', function() {{
                    this.style.transform = 'translateY(-1px)';
                }});
                link.addEventListener('mouseleave', function() {{
                    this.style.transform = 'translateY(0)';
                }});
            }});
        }});
    </script>
</body>
</html>"""

def generate_index_html(index_items: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Protocols - Project Dukkha</title>
    <meta name="description" content="Evidence-based protocols for digital detox, stress management, sleep optimization, and mindfulness practices.">
    <link rel="stylesheet" href="../styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="nav" role="navigation" aria-label="Main navigation">
        <div class="nav-container">
            <div class="nav-brand">
                <div class="brand-symbol"></div>
            </div>
            <ul class="nav-menu">
                <li><a href="../index.html" class="nav-link">Home</a></li>
                <li><a href="attention.html" class="nav-link">Focus & Attention</a></li>
                <li><a href="recovery.html" class="nav-link">Recovery & Baseline</a></li>
                <li><a href="myths.html" class="nav-link">Five Myths</a></li>
                <li><a href="model.html" class="nav-link">Model</a></li>
                <li><a href="protocols.html" class="nav-link active" aria-current="page">Protocols</a></li>
                <li><a href="library.html" class="nav-link">Library</a></li>
            </ul>
        </div>
    </nav>

    <main class="page-content">
        <section class="hero-protocols">
            <h1>Protocols: Evidence-Based Experiments</h1>
            <p class="tagline">A Field Guide to the Rewarded Animal</p>
            <p>Practical, time-bound protocols designed to help you recalibrate your dopamine system, improve focus, and build sustainable habits. Each protocol is grounded in peer-reviewed research and designed for immediate implementation.</p>
        </section>

        <section class="container">
            <div class="protocol-list">
                {index_items}
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <div class="brand-symbol"></div>
                    <span>Project Dukkha</span>
                </div>
                <div class="footer-links">
                    <a href="library.html">Research</a>
                    <a href="#" class="print-link" onclick="window.print()">Print Guide</a>
                    <a href="mailto:contact@projectdukkha.com">Contact</a>
                </div>
            </div>
            <div class="footer-note">
                <p>This field guide is for educational purposes. Consult healthcare professionals for medical decisions.</p>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            // Smooth navigation highlighting
            const navLinks = document.querySelectorAll('.nav-link');
            navLinks.forEach(link => {{
                link.addEventListener('mouseenter', function() {{
                    this.style.transform = 'translateY(-1px)';
                }});
                link.addEventListener('mouseleave', function() {{
                    this.style.transform = 'translateY(0)';
                }});
            }});
        }});
    </script>
</body>
</html>"""

def convert_md_to_html(md_path: Path) -> tuple[str, dict]:
    content = md_path.read_text(encoding='utf-8')
    metadata = extract_metadata(content)
    html_content = markdown.markdown(content, extensions=['extra', 'toc'])
    return html_content, metadata

def process_protocols():
    md_files = list(SRC_DIR.glob('*.md'))
    if not md_files:
        print(f"No Markdown files found in {SRC_DIR}")
        return
    
    print(f"Found {len(md_files)} protocol files")
    
    protocols = []
    index_items = []
    
    for md_file in md_files:
        print(f"Processing: {md_file.name}")
        html_content, metadata = convert_md_to_html(md_file)
        
        slug = slugify(metadata['title'])
        html_filename = f"{slug}.html"
        
        final_html = TEMPLATE.format(
            TITLE=metadata['title'],
            SUMMARY=metadata['summary'],
            CONTENT=html_content
        )
        
        output_path = OUT_DIR / html_filename
        output_path.write_text(final_html, encoding='utf-8')
        print(f"  → {output_path}")
        
        protocols.append({
            'title': metadata['title'],
            'slug': slug,
            'filename': html_filename,
            'summary': metadata['summary']
        })
        
        index_items.append(f"""
            <div class="protocol-card">
                <h3><a href="protocols/{html_filename}">{metadata['title']}</a></h3>
                <p>{metadata['summary']}</p>
            </div>""")
    
    # Generate index page
    index_html = generate_index_html('\n'.join(index_items))
    index_path = ROOT / 'docs' / 'site' / 'protocols.html'
    index_path.write_text(index_html, encoding='utf-8')
    print(f"Index page: {index_path}")
    
    # Generate manifest
    manifest = {
        'generated_at': str(Path(__file__).stat().st_mtime),
        'protocols': protocols
    }
    manifest_path = OUT_DIR / 'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f"Manifest: {manifest_path}")
    
    print(f"\nGenerated {len(protocols)} protocol pages")

if __name__ == '__main__':
    process_protocols()

