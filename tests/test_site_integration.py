import requests
from bs4 import BeautifulSoup
from pathlib import Path

BASE_DIR = Path('docs/site')


def test_protocols_index_exists():
    index = BASE_DIR / 'protocols.html'
    assert index.exists()
    text = index.read_text(encoding='utf-8')
    assert '<div class="protocol-list"' in text or 'Protocols: Evidence-Based Experiments' in text


def test_manifest_matches_files():
    manifest = BASE_DIR / 'protocols' / 'manifest.json'
    assert manifest.exists()
    m = json.loads(manifest.read_text(encoding='utf-8'))
    for p in m.get('protocols', []):
        path = BASE_DIR / 'protocols' / p['filename']
        assert path.exists()
