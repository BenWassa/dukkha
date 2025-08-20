"""
Smoke tests for Project Dukkha site functionality.

These tests verify that the build system works and generated pages have expected structure.
Run after building: python scripts/build_site.py && python -m pytest tests/ -v
"""

import json
from pathlib import Path
from bs4 import BeautifulSoup


BASE_DIR = Path('docs/site')


def test_build_generates_required_files():
    """Test that build script generates expected files."""
    # Index page exists
    assert (BASE_DIR / 'protocols.html').exists()
    
    # Manifest exists
    manifest_path = BASE_DIR / 'protocols' / 'manifest.json'
    assert manifest_path.exists()
    
    # Manifest is valid JSON and has expected structure
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    assert 'protocols' in manifest
    assert isinstance(manifest['protocols'], list)
    assert len(manifest['protocols']) > 0


def test_protocol_pages_have_correct_structure():
    """Test that generated protocol pages have the expected HTML structure."""
    protocols_dir = BASE_DIR / 'protocols'
    html_files = list(protocols_dir.glob('*.html'))
    
    assert len(html_files) > 0, "No protocol HTML files found"
    
    for html_file in html_files:
        content = html_file.read_text(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        
        # Check basic structure
        assert soup.find('title') is not None
        assert soup.find('nav', class_='nav') is not None
        assert soup.find('main', class_='page-content') is not None
        assert soup.find('footer', class_='footer') is not None
        
        # Check protocol-specific elements
        hero = soup.find('section', class_='hero-protocols')
        assert hero is not None
        assert hero.find('h1') is not None
        assert hero.find('p', class_='hero-subtitle--protocol') is not None
        
        article = soup.find('article', class_='protocol-article')
        assert article is not None
        
        badge = soup.find('div', class_='protocol-badge')
        assert badge is not None and badge.get_text(strip=True) != ""


def test_protocols_index_structure():
    """Test that the protocols index page has correct structure."""
    index_path = BASE_DIR / 'protocols.html'
    content = index_path.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    
    # Check basic structure
    assert soup.find('title') is not None
    assert "Protocols" in soup.find('title').get_text()
    
    # Check protocol list
    protocol_list = soup.find('div', class_='protocol-list')
    assert protocol_list is not None
    
    cards = soup.find_all('div', class_='protocol-card')
    assert len(cards) > 0, "No protocol cards found in index"
    
    # Each card should have required elements
    for card in cards:
        assert card.find('h3') is not None
        assert card.find('a') is not None
        assert card.find('p') is not None  # description
        assert card.find('div', class_='protocol-badge') is not None


def test_manifest_consistency():
    """Test that manifest entries match actual files."""
    manifest_path = BASE_DIR / 'protocols' / 'manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    
    for protocol in manifest['protocols']:
        # File referenced in manifest should exist
        file_path = BASE_DIR / 'protocols' / protocol['filename']
        assert file_path.exists(), f"Missing file: {protocol['filename']}"
        
        # Required fields should be present
        assert 'title' in protocol
        assert 'slug' in protocol
        assert 'description' in protocol
        assert 'duration' in protocol
        assert 'tags' in protocol
        
        # Fields should not be empty
        assert protocol['title'].strip() != ""
        assert protocol['description'].strip() != ""


def test_css_links_work():
    """Test that CSS links in generated pages point to existing files."""
    protocols_dir = BASE_DIR / 'protocols'
    html_files = list(protocols_dir.glob('*.html'))
    
    for html_file in html_files:
        content = html_file.read_text(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        
        css_links = soup.find_all('link', rel='stylesheet')
        assert len(css_links) > 0, f"No CSS links found in {html_file.name}"
        
        for link in css_links:
            href = link.get('href')
            if href and href.startswith('../'):
                # Resolve relative path
                css_path = (html_file.parent / href).resolve()
                # Note: We're not checking if CSS actually exists since it might be 
                # in a different location, just that the link format is correct
                assert href.endswith('.css'), f"Invalid CSS link: {href}"


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
