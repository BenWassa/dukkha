"""Site-level integration tests that validate generated HTML files under docs/site.

These tests avoid importing or invoking `scripts/build_protocols.py` and instead
assert the presence and structure of the generated pages and manifest.
"""

import json
from pathlib import Path
from bs4 import BeautifulSoup


BASE = Path('docs') / 'site'


def _load_html(path: Path):
    text = path.read_text(encoding='utf-8')
    return BeautifulSoup(text, 'lxml')


def test_protocols_index_exists():
    index = BASE / 'protocols.html'
    assert index.exists(), f"Missing {index} - run the site build first"
    doc = _load_html(index)
    assert doc.select_one('.protocol-list') is not None


def test_each_protocol_has_hero_subtitle_and_no_lead_paragraph():
    proto_dir = BASE / 'protocols'
    assert proto_dir.exists(), f"Missing {proto_dir}"
    for f in proto_dir.glob('*.html'):
        doc = _load_html(f)
        # hero subtitle exists and is non-empty
        subtitle = doc.select_one('.hero-subtitle--protocol')
        assert subtitle is not None and subtitle.get_text(strip=True), f"Missing hero subtitle in {f.name}"

        # first direct <p> child inside .protocol-article should be absent or empty
        article = doc.select_one('.protocol-article')
        if article:
            first_p = article.find('p')
            if first_p:
                assert not first_p.get_text(strip=True), f"Non-empty lead paragraph left in {f.name}"


def test_manifest_matches_files():
    manifest = BASE / 'protocols' / 'manifest.json'
    assert manifest.exists(), "Manifest missing; run build to generate docs/site/protocols/manifest.json"
    m = json.loads(manifest.read_text(encoding='utf-8'))
    for entry in m.get('protocols', []):
        path = BASE / 'protocols' / entry.get('filename', '')
        assert path.exists(), f"Manifest references missing file: {path}"
