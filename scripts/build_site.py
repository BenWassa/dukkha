#!/usr/bin/env python3
"""
New build system for Project Dukkha protocols.

Reads Markdown files with front-matter from src/protocols/
Generates HTML pages to docs/site/protocols/
Uses templates from src/templates/

Usage: python scripts/build_site.py
"""

import re
import json
import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Any

try:
    import markdown
    from markdown.extensions import codehilite, toc, extra
except ImportError:
    raise SystemExit("Missing dependency: pip install markdown")

try:
    import yaml
except ImportError:
    raise SystemExit("Missing dependency: pip install pyyaml")


@dataclass
class Protocol:
    """Data class for a protocol with front-matter metadata."""
    title: str
    duration: str
    tags: List[str]
    description: str
    slug: str
    content: str
    filename: str
    
    @classmethod
    def from_markdown_file(cls, path: Path) -> 'Protocol':
        """Parse a markdown file with YAML front-matter."""
        content = path.read_text(encoding='utf-8')
        
        # Split front-matter and content
        if content.startswith('---\n'):
            try:
                _, front_matter, body = content.split('---\n', 2)
                metadata = yaml.safe_load(front_matter)
            except ValueError:
                raise ValueError(f"Invalid front-matter format in {path}")
        else:
            raise ValueError(f"No front-matter found in {path}")
        
        # Convert markdown to HTML
        md = markdown.Markdown(extensions=['extra', 'toc', 'codehilite'])
        html_content = md.convert(body.strip())
        
        return cls(
            title=metadata['title'],
            duration=metadata['duration'],
            tags=metadata.get('tags', []),
            description=metadata['description'],
            slug=metadata['slug'],
            content=html_content,
            filename=f"{metadata['slug']}.html"
        )


class SiteBuilder:
    """Builds the static site from source files."""
    
    def __init__(self):
        self.root = Path(__file__).resolve().parents[1]
        self.src_dir = self.root / 'src'
        self.protocols_dir = self.src_dir / 'protocols'
        self.templates_dir = self.src_dir / 'templates'
        self.output_dir = self.root / 'docs' / 'site'
        self.protocols_output_dir = self.output_dir / 'protocols'
        
        # Ensure output directories exist
        self.protocols_output_dir.mkdir(parents=True, exist_ok=True)
    
    def load_template(self, name: str) -> str:
        """Load a template file."""
        template_path = self.templates_dir / f"{name}.html"
        if not template_path.exists():
            # Return a basic template if none exists
            return self.get_default_protocol_template()
        return template_path.read_text(encoding='utf-8')
    
    def get_default_protocol_template(self) -> str:
        """Default protocol page template."""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Project Dukkha</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="../../styles.css">
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
                <li><a href="../attention.html" class="nav-link">Focus & Attention</a></li>
                <li><a href="../recovery.html" class="nav-link">Recovery & Baseline</a></li>
                <li><a href="../myths.html" class="nav-link">Five Myths</a></li>
                <li><a href="../model.html" class="nav-link">Model</a></li>
                <li><a href="../protocols.html" class="nav-link">Protocols</a></li>
                <li><a href="../library.html" class="nav-link">Library</a></li>
            </ul>
        </div>
    </nav>

    <main class="page-content">
        <section class="hero-protocols">
            <h1>{title}</h1>
            <p class="hero-subtitle hero-subtitle--protocol">Practical, time-bound protocols designed to help you recalibrate your dopamine system, improve focus, and build sustainable habits. Each protocol is grounded in peer-reviewed research and designed for immediate implementation.</p>
        </section>

        <section class="container">
            <article class="protocol-article">
                <div class="protocol-badge">{duration}</div>
                {content}
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
                    <a href="../library.html">Research</a>
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
</html>'''
    
    def get_protocols_index_template(self) -> str:
        """Template for the protocols index page."""
        return '''<!DOCTYPE html>
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
                <li><a href="../attention.html" class="nav-link">Focus & Attention</a></li>
                <li><a href="../recovery.html" class="nav-link">Recovery & Baseline</a></li>
                <li><a href="../myths.html" class="nav-link">Five Myths</a></li>
                <li><a href="../model.html" class="nav-link">Model</a></li>
                <li><a href="../protocols.html" class="nav-link active" aria-current="page">Protocols</a></li>
                <li><a href="../library.html" class="nav-link">Library</a></li>
            </ul>
        </div>
    </nav>

    <main class="page-content">
        <section class="hero-protocols">
            <h1>Protocols: Evidence-Based Experiments</h1>
            <p class="hero-subtitle hero-subtitle--protocol">Practical, time-bound protocols designed to help you recalibrate your dopamine system, improve focus, and build sustainable habits. Each protocol is grounded in peer-reviewed research and designed for immediate implementation.</p>
        </section>

        <section class="container">
            <div class="protocol-list">
                {protocol_cards}
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
                    <a href="../library.html">Research</a>
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
</html>'''
    
    def build_protocol_page(self, protocol: Protocol) -> None:
        """Build a single protocol page."""
        template = self.get_default_protocol_template()
        
        html = template.format(
            title=protocol.title,
            description=protocol.description,
            duration=protocol.duration,
            content=protocol.content
        )
        
        output_path = self.protocols_output_dir / protocol.filename
        output_path.write_text(html, encoding='utf-8')
        print(f"Generated: {output_path}")
    
    def build_protocols_index(self, protocols: List[Protocol]) -> None:
        """Build the protocols index page."""
        # Generate protocol cards
        cards = []
        for protocol in protocols:
            tags_str = " • ".join(protocol.tags[:3])  # Show first 3 tags
            card = f'''
            <div class="protocol-card">
                <div class="protocol-badge">{protocol.duration}</div>
                <h3><a href="protocols/{protocol.filename}">{protocol.title}</a></h3>
                <p>{protocol.description}</p>
                <div class="protocol-meta">{tags_str}</div>
            </div>'''
            cards.append(card)
        
        template = self.get_protocols_index_template()
        html = template.format(protocol_cards='\n'.join(cards))
        
        output_path = self.output_dir / 'protocols.html'
        output_path.write_text(html, encoding='utf-8')
        print(f"Generated: {output_path}")
    
    def build_manifest(self, protocols: List[Protocol]) -> None:
        """Build the protocols manifest JSON."""
        manifest = {
            "generated_at": str(Path(__file__).stat().st_mtime),
            "protocols": [
                {
                    "title": p.title,
                    "slug": p.slug,
                    "filename": p.filename,
                    "description": p.description,
                    "duration": p.duration,
                    "tags": p.tags
                }
                for p in protocols
            ]
        }
        
        manifest_path = self.protocols_output_dir / 'manifest.json'
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
        print(f"Generated: {manifest_path}")
    
    def build(self) -> None:
        """Build the entire site."""
        if not self.protocols_dir.exists():
            raise FileNotFoundError(f"Source directory not found: {self.protocols_dir}")
        
        # Load all protocols
        protocols = []
        md_files = list(self.protocols_dir.glob("*.md"))
        
        if not md_files:
            print(f"No markdown files found in {self.protocols_dir}")
            return
        
        print(f"Found {len(md_files)} protocol files")
        
        for md_file in md_files:
            try:
                protocol = Protocol.from_markdown_file(md_file)
                protocols.append(protocol)
                print(f"Loaded: {protocol.title}")
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
                continue
        
        if not protocols:
            print("No valid protocols to build")
            return
        
        # Build individual protocol pages
        for protocol in protocols:
            self.build_protocol_page(protocol)
        
        # Build index page
        self.build_protocols_index(protocols)
        
        # Build manifest
        self.build_manifest(protocols)
        
        print(f"\nBuild complete! Generated {len(protocols)} protocol pages.")


def main():
    """Main entry point."""
    builder = SiteBuilder()
    builder.build()


if __name__ == '__main__':
    main()
