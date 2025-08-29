#!/usr/bin/env python3
"""
Extract Markdown content from existing HTML protocol files.

This script helps migrate from manual HTML editing to the new source-based workflow
by extracting content from docs/site/protocols/*.html and creating corresponding
Markdown files with front-matter in src/protocols/
"""

import re
import json
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from typing import Dict, List


def extract_protocol_metadata(soup: BeautifulSoup) -> Dict[str, str]:
    """Extract metadata from HTML protocol page."""
    # Get title
    title_elem = soup.find('h1')
    title = title_elem.get_text(strip=True) if title_elem else "Unknown Protocol"
    
    # Get duration from badge
    badge_elem = soup.find('div', class_='protocol-badge')
    duration = badge_elem.get_text(strip=True) if badge_elem else "Unknown Duration"
    
    # Get description from meta tag
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc.get('content', '') if meta_desc else "No description available"
    
    # Generate slug from title
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    
    return {
        'title': title,
        'duration': duration,
        'description': description,
        'slug': slug
    }


def extract_tags_from_content(content_text: str) -> List[str]:
    """Extract likely tags from content text."""
    # Common protocol-related keywords to look for
    tag_keywords = {
        'mindfulness': ['mindfulness', 'meditation', 'awareness'],
        'digital-detox': ['digital', 'phone', 'smartphone', 'screen'],
        'sleep': ['sleep', 'circadian', 'rest'],
        'stress': ['stress', 'anxiety', 'cortisol'],
        'nutrition': ['nutrition', 'diet', 'food', 'supplement'],
        'craving': ['craving', 'urge', 'wanting'],
        'dopamine': ['dopamine', 'reward'],
        'recovery': ['recovery', 'baseline'],
        'attention': ['attention', 'focus', 'concentration']
    }
    
    content_lower = content_text.lower()
    found_tags = []
    
    for tag, keywords in tag_keywords.items():
        if any(keyword in content_lower for keyword in keywords):
            found_tags.append(tag)
    
    return found_tags[:5]  # Limit to 5 tags


def html_to_markdown(element) -> str:
    """Convert HTML elements to Markdown."""
    if isinstance(element, NavigableString):
        return str(element)
    
    tag = element.name
    text = element.get_text()
    
    # Handle different HTML tags
    if tag == 'h1':
        return f"# {text}\n\n"
    elif tag == 'h2':
        return f"## {text}\n\n"
    elif tag == 'h3':
        return f"### {text}\n\n"
    elif tag == 'h4':
        return f"#### {text}\n\n"
    elif tag == 'p':
        # Handle paragraphs with emphasis
        md_text = ""
        for child in element.children:
            if isinstance(child, NavigableString):
                md_text += str(child)
            elif child.name == 'strong':
                md_text += f"**{child.get_text()}**"
            elif child.name == 'em':
                md_text += f"*{child.get_text()}*"
            elif child.name == 'sup':
                # Handle footnote references
                md_text += f"[^{child.get_text().strip('[]')}]"
            else:
                md_text += child.get_text()
        return f"{md_text}\n\n"
    elif tag == 'ul':
        items = []
        for li in element.find_all('li'):
            items.append(f"- {li.get_text()}")
        return "\n".join(items) + "\n\n"
    elif tag == 'ol':
        items = []
        for i, li in enumerate(element.find_all('li'), 1):
            items.append(f"{i}. {li.get_text()}")
        return "\n".join(items) + "\n\n"
    elif tag == 'div' and 'protocol-steps' in element.get('class', []):
        # Handle special protocol steps section
        content = ""
        for child in element.children:
            content += html_to_markdown(child)
        return content
    else:
        return f"{text}\n\n"


def extract_protocol_content(soup: BeautifulSoup) -> str:
    """Extract the main content from protocol article."""
    article = soup.find('article', class_='protocol-article')
    if not article:
        return "No content found"
    
    markdown_content = ""
    
    # Skip the badge div and process other elements
    for element in article.children:
        if hasattr(element, 'name'):
            if element.name == 'div' and 'protocol-badge' in element.get('class', []):
                continue  # Skip badge, it's handled in metadata
            markdown_content += html_to_markdown(element)
    
    return markdown_content.strip()


def extract_protocol_from_html(html_path: Path) -> Dict:
    """Extract protocol data from HTML file."""
    content = html_path.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    
    metadata = extract_protocol_metadata(soup)
    content_text = extract_protocol_content(soup)
    
    # Extract tags from content
    tags = extract_tags_from_content(content_text)
    
    return {
        'metadata': metadata,
        'content': content_text,
        'tags': tags
    }


def create_markdown_file(protocol_data: Dict, output_path: Path) -> None:
    """Create a Markdown file with front-matter from protocol data."""
    metadata = protocol_data['metadata']
    
    # Create front-matter
    front_matter = f"""---
title: "{metadata['title']}"
duration: "{metadata['duration']}"
tags:
{chr(10).join(f'  - {tag}' for tag in protocol_data['tags'])}
description: "{metadata['description']}"
slug: "{metadata['slug']}"
---

"""
    
    # Combine front-matter and content
    full_content = front_matter + protocol_data['content']
    
    output_path.write_text(full_content, encoding='utf-8')
    print(f"Created: {output_path}")


def main():
    """Main extraction process."""
    # Paths
    html_dir = Path('docs/site/protocols')
    output_dir = Path('src/protocols')
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all HTML protocol files
    html_files = list(html_dir.glob('*.html'))
    
    if not html_files:
        print(f"No HTML files found in {html_dir}")
        return
    
    print(f"Found {len(html_files)} HTML protocol files")
    
    for html_file in html_files:
        print(f"Processing: {html_file.name}")
        
        try:
            # Extract protocol data
            protocol_data = extract_protocol_from_html(html_file)
            
            # Create output filename
            slug = protocol_data['metadata']['slug']
            output_file = output_dir / f"{slug}.md"
            
            # Skip if already exists (don't overwrite manual work)
            if output_file.exists():
                print(f"  Skipping: {output_file} already exists")
                continue
            
            # Create markdown file
            create_markdown_file(protocol_data, output_file)
            
        except Exception as e:
            print(f"  Error processing {html_file.name}: {e}")
            continue
    
    print("\nExtraction complete!")
    print("Next steps:")
    print("1. Review and edit the generated Markdown files in src/protocols/")
    print("2. Run: python scripts/build_site.py")
    print("3. Run tests: python -m pytest tests/test_site_functionality.py -v")


if __name__ == '__main__':
    main()
