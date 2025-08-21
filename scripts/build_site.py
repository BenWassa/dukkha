#!/usr/bin/env python3
"""
Build system for Project Dukkha         # Convert markdown to HTML with footnotes support
        md = markdown.Markdown(extensions=['extra', 'toc', 'codehilite', 'footnotes'])
        html_content = md.convert(body.strip())
        
        # Remove the footnotes div from main content since we'll handle it separately
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove all auto-generated footnotes divs
        for footnotes_div in soup.find_all('div', class_='footnote'):
            footnotes_div.decompose()
        for footnotes_div in soup.find_all('div', class_='footnotes'):
            footnotes_div.decompose()
        
        html_content = str(soup)
        
        return cls(
            title=metadata['title'],
            duration=metadata['duration'],
            tags=metadata.get('tags', []),
            description=metadata['description'],
            slug=metadata['slug'],
            content=html_content,
            filename=f"{metadata['slug']}.html"
        )s Markdown files with front-matter from:
- src/protocols/ for protocol pages
- src/pages/ for main content pages

Generates HTML pages preserving manual corrections:
- Individual protocol pages to docs/site/protocols/
- Main content pages to docs/site/
- Uses improved CSS structure and navigation

Usage: python scripts/build_site.py
"""

import re
import json
import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Any, Optional

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


@dataclass
class Page:
    """Data class for a main page with front-matter metadata."""
    title: str
    slug: str
    description: str
    page_type: str
    active_nav: str
    hero_class: str
    content: str
    filename: str
    
    @classmethod
    def from_markdown_file(cls, path: Path) -> 'Page':
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
        
        # Convert markdown to HTML with footnotes support
        md = markdown.Markdown(extensions=['extra', 'toc', 'codehilite', 'footnotes'])
        html_content = md.convert(body.strip())
        
        # Remove the footnotes div from main content since we'll handle it separately
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove all auto-generated footnotes divs
        for footnotes_div in soup.find_all('div', class_='footnote'):
            footnotes_div.decompose()
        for footnotes_div in soup.find_all('div', class_='footnotes'):
            footnotes_div.decompose()
        
        html_content = str(soup)
        
        return cls(
            title=metadata['title'],
            slug=metadata['slug'],
            description=metadata['description'],
            page_type=metadata.get('page_type', 'main'),
            active_nav=metadata.get('active_nav', metadata['slug']),
            hero_class=metadata.get('hero_class', 'hero'),
            content=html_content,
            filename=f"{metadata['slug']}.html"
        )


class SiteBuilder:
    """Builds the static site from source files."""
    
    def __init__(self):
        self.root = Path(__file__).resolve().parents[1]
        self.src_dir = self.root / 'src'
        self.protocols_dir = self.src_dir / 'protocols'
        self.pages_dir = self.src_dir / 'pages'
        self.protocols_source_dir = self.protocols_dir  # For footnotes extraction
        self.pages_source_dir = self.pages_dir  # For footnotes extraction
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
            if name == "protocol":
                return self.get_default_protocol_template()
            elif name == "page":
                return self.get_default_page_template()
        return template_path.read_text(encoding='utf-8')
    
    def get_default_protocol_template(self) -> str:
        """Default protocol page template with improved CSS structure."""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Project Dukkha</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="../../variables.css">
    <link rel="stylesheet" href="../../styles.css">
    <link rel="stylesheet" href="../../utilities.css">
    <link rel="stylesheet" href="../../print.css" media="print">
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
                <li><a href="../../index.html" class="nav-link">Home</a></li>
                <li><a href="../attention.html" class="nav-link">Focus & Attention</a></li>
                <li><a href="../recovery.html" class="nav-link">Recovery & Baseline</a></li>
                <li><a href="../myths.html" class="nav-link">Five Myths</a></li>
                <li><a href="../model.html" class="nav-link">Model</a></li>
                <li class="nav-dropdown">
                    <a href="#" class="nav-link nav-dropdown__toggle" aria-haspopup="true" aria-expanded="false">Protocols</a>
                    <ul class="nav-dropdown__menu" role="menu"></ul>
                </li>
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

    <!-- Footnotes Section -->
    <section class="footnotes" id="footnotes">
        <div class="container">
            <h3>Notes & Citations</h3>
            <ol class="footnote-list">
                {footnotes_content}
            </ol>
        </div>
    </section>

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

    <script src="../js/site-ui.js" defer></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            // Collapsible footnotes section
            const footnotesSection = document.querySelector('.footnotes');
            const footnotesHeader = document.querySelector('.footnotes h3');
            
            if (footnotesHeader && footnotesSection) {{
                footnotesHeader.addEventListener('click', function() {{
                    footnotesSection.classList.toggle('collapsed');
                }});
            }}

            // Footnote click handling
            document.querySelectorAll('a[href^="#fn"]').forEach(link => {{
                link.addEventListener('click', function(e) {{
                    e.preventDefault();
                    const targetId = this.getAttribute('href').substring(1);
                    // Handle both fn:1 and fn1 formats
                    let targetElement = document.getElementById(targetId);
                    if (!targetElement && targetId.startsWith('fn') && !targetId.includes(':')) {{
                        targetElement = document.getElementById('fn:' + targetId.substring(2));
                    }} else if (!targetElement && targetId.includes(':')) {{
                        targetElement = document.getElementById(targetId.replace(':', ''));
                    }}
                    if (targetElement) {{
                        // If footnotes section is collapsed, expand it first
                        if (footnotesSection && footnotesSection.classList.contains('collapsed')) {{
                            footnotesSection.classList.remove('collapsed');
                        }}
                        // Smooth scroll to the footnote
                        targetElement.scrollIntoView({{ 
                            behavior: 'smooth',
                            block: 'center'
                        }});
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>'''
    
    def get_default_page_template(self) -> str:
        """Default main page template with improved CSS structure."""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Project Dukkha</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="../variables.css">
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="../utilities.css">
    <link rel="stylesheet" href="../print.css" media="print">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <div class="read-prompt" role="status" aria-live="polite">
        <button class="read-prompt__close" aria-label="Dismiss">&times;</button>
        <p class="read-prompt__text"></p>
    </div>
    <!-- Navigation -->
    <nav class="nav" role="navigation" aria-label="Main navigation">
        <div class="nav-container">
            <div class="nav-brand">
                <div class="brand-symbol"></div>
            </div>
            <ul class="nav-menu">
                <li><a href="../index.html" class="nav-link{home_active}">Home</a></li>
                <li><a href="attention.html" class="nav-link{attention_active}">Focus & Attention</a></li>
                <li><a href="recovery.html" class="nav-link{recovery_active}">Recovery & Baseline</a></li>
                <li><a href="myths.html" class="nav-link{myths_active}">Five Myths</a></li>
                <li><a href="model.html" class="nav-link{model_active}">Model</a></li>
                <li class="nav-dropdown">
                    <a href="#" class="nav-link nav-dropdown__toggle{protocols_active}" aria-haspopup="true" aria-expanded="false">Protocols</a>
                    <ul class="nav-dropdown__menu" role="menu"></ul>
                </li>
                <li><a href="library.html" class="nav-link{library_active}">Library</a></li>
            </ul>
        </div>
    </nav>

    <main class="page-content">
        <section class="{hero_class}">
            <h1>{page_title}</h1>
            <p>{hero_description}</p>
        </section>

        <section class="content-claims">
            {content}
        </section>
    </main>

    <!-- Footnotes Section -->
    <section class="footnotes" id="footnotes">
        <div class="container">
            <h3>Notes & Citations</h3>
            <ol class="footnote-list">
                {footnotes_content}
            </ol>
        </div>
    </section>

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

    <script src="js/site-ui.js" defer></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            // Collapsible footnotes section
            const footnotesSection = document.querySelector('.footnotes');
            const footnotesHeader = document.querySelector('.footnotes h3');
            
            if (footnotesHeader && footnotesSection) {{
                footnotesHeader.addEventListener('click', function() {{
                    footnotesSection.classList.toggle('collapsed');
                }});
            }}

            // Footnote click handling
            document.querySelectorAll('a[href^="#fn"]').forEach(link => {{
                link.addEventListener('click', function(e) {{
                    e.preventDefault();
                    const targetId = this.getAttribute('href').substring(1);
                    // Handle both fn:1 and fn1 formats
                    let targetElement = document.getElementById(targetId);
                    if (!targetElement && targetId.startsWith('fn') && !targetId.includes(':')) {{
                        targetElement = document.getElementById('fn:' + targetId.substring(2));
                    }} else if (!targetElement && targetId.includes(':')) {{
                        targetElement = document.getElementById(targetId.replace(':', ''));
                    }}
                    if (targetElement) {{
                        // If footnotes section is collapsed, expand it first
                        if (footnotesSection && footnotesSection.classList.contains('collapsed')) {{
                            footnotesSection.classList.remove('collapsed');
                        }}
                        // Smooth scroll to the footnote
                        targetElement.scrollIntoView({{ 
                            behavior: 'smooth',
                            block: 'center'
                        }});
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>'''
    
    def get_protocols_index_template(self) -> str:
        """Template for the protocols index page with improved structure."""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Protocols - Project Dukkha</title>
    <meta name="description" content="Evidence-based protocols for digital detox, stress management, sleep optimization, and mindfulness practices.">
    <link rel="stylesheet" href="../variables.css">
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="../utilities.css">
    <link rel="stylesheet" href="../print.css" media="print">
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
                <li class="nav-dropdown">
                <a href="#" class="nav-link nav-dropdown__toggle" aria-haspopup="true" aria-expanded="false">Protocols</a>
                <ul class="nav-dropdown__menu" role="menu"></ul>
            </li>
                <li><a href="library.html" class="nav-link">Library</a></li>
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

    <script src="js/site-ui.js" defer></script>
</body>
</html>'''
    
    def build_protocol_page(self, protocol: Protocol) -> None:
        """Build a single protocol page."""
        template = self.get_default_protocol_template()
        
        # Read the original markdown file to extract footnotes
        protocol_file = self.protocols_source_dir / f"{protocol.slug}.md"
        original_content = protocol_file.read_text(encoding='utf-8')
        # Extract just the body content after front matter
        if '---\n' in original_content:
            _, _, body = original_content.split('---\n', 2)
            footnotes_content = self._extract_footnotes(body.strip())
        else:
            footnotes_content = ""
        
        html = template.format(
            title=protocol.title,
            description=protocol.description,
            duration=protocol.duration,
            content=protocol.content,
            footnotes_content=footnotes_content
        )
        
        output_path = self.protocols_output_dir / protocol.filename
        output_path.write_text(html, encoding='utf-8')
        print(f"Generated: {output_path}")
    
    def build_page(self, page: Page) -> None:
        """Build a single main page."""
        template = self.get_default_page_template()
        
        # Extract title and hero description from content
        page_title = page.title
        hero_description = page.description
        
        # Read the original markdown file to extract footnotes
        page_file = self.pages_source_dir / f"{page.slug}.md"
        original_content = page_file.read_text(encoding='utf-8')
        # Extract just the body content after front matter
        if '---\n' in original_content:
            _, _, body = original_content.split('---\n', 2)
            footnotes_content = self._extract_footnotes(body.strip())
        else:
            footnotes_content = ""
        
        # Set active navigation classes
        nav_classes = {
            'home_active': '',
            'attention_active': '',
            'recovery_active': '',
            'myths_active': '',
            'model_active': '',
            'protocols_active': '',
            'library_active': ''
        }
        
        if page.active_nav in nav_classes:
            nav_classes[f'{page.active_nav}_active'] = ' active" aria-current="page'
        
        html = template.format(
            title=page.title,
            description=page.description,
            page_title=page_title,
            hero_description=hero_description,
            hero_class=page.hero_class,
            content=page.content,
            footnotes_content=footnotes_content,
            **nav_classes
        )
        
        output_path = self.output_dir / page.filename
        output_path.write_text(html, encoding='utf-8')
        print(f"Generated: {output_path}")
    
    def _extract_footnotes(self, original_content: str) -> str:
        """Extract footnotes from the original markdown content and process with markdown."""
        # Process the original markdown content to get footnotes
        md = markdown.Markdown(extensions=['extra', 'toc', 'codehilite', 'footnotes'])
        html_content = md.convert(original_content)
        
        from bs4 import BeautifulSoup
        
        # If there's no footnotes div, return empty
        if '<div class="footnote">' not in html_content:
            return ""
        
        soup = BeautifulSoup(html_content, 'html.parser')
        footnotes_div = soup.find('div', class_='footnote')
        
        if not footnotes_div:
            return ""
        
        # Find the footnote list
        footnote_list = footnotes_div.find('ol')
        if not footnote_list:
            return ""
        
        # Extract footnote items and reformat them
        footnote_items = []
        for li in footnote_list.find_all('li', recursive=False):
            # Get the footnote ID
            footnote_id = li.get('id', '')
            
            # Remove the backlink anchor but keep other content
            backlink = li.find('a', class_='footnote-backref')
            if backlink:
                backlink.decompose()
            
            # Get the cleaned content
            li_content = str(li)
            # Clean up the opening/closing li tags to just get inner content
            li_content = li_content.replace(f'<li id="{footnote_id}">', '').replace('</li>', '').strip()
            
            if footnote_id and li_content:
                footnote_items.append(f'<li id="{footnote_id}">{li_content}</li>')
        
        return '\n                '.join(footnote_items)
    
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
        protocols = []
        pages = []
        
        # Load protocols
        if self.protocols_dir.exists():
            protocol_files = list(self.protocols_dir.glob("*.md"))
            print(f"Found {len(protocol_files)} protocol files")
            
            for md_file in protocol_files:
                try:
                    protocol = Protocol.from_markdown_file(md_file)
                    protocols.append(protocol)
                    print(f"Loaded protocol: {protocol.title}")
                except Exception as e:
                    print(f"Error processing protocol {md_file}: {e}")
                    continue
        
        # Load main pages
        if self.pages_dir.exists():
            page_files = list(self.pages_dir.glob("*.md"))
            print(f"Found {len(page_files)} page files")
            
            for md_file in page_files:
                try:
                    page = Page.from_markdown_file(md_file)
                    pages.append(page)
                    print(f"Loaded page: {page.title}")
                except Exception as e:
                    print(f"Error processing page {md_file}: {e}")
                    continue
        
        # Build individual protocol pages
        for protocol in protocols:
            self.build_protocol_page(protocol)
        
        # Build main pages
        for page in pages:
            self.build_page(page)
        
        # Build protocols index page
        if protocols:
            self.build_protocols_index(protocols)
        
        # Build manifest
        if protocols:
            self.build_manifest(protocols)
        
        print(f"\nBuild complete! Generated {len(protocols)} protocol pages and {len(pages)} main pages.")


def main():
    """Main entry point."""
    builder = SiteBuilder()
    builder.build()


if __name__ == '__main__':
    main()
