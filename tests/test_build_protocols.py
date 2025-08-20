import json
import importlib.util
from pathlib import Path


def load_builder():
    REPO_ROOT = Path(__file__).resolve().parents[1]
    MODULE_PATH = REPO_ROOT / 'scripts' / 'build_protocols.py'
    spec = importlib.util.spec_from_file_location('build_protocols', MODULE_PATH)
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    return builder


def test_extract_metadata_and_slugify(tmp_path):
    md = tmp_path / "sample.md"
    md.write_text("# My Protocol\n\nA short summary line.\n\nContent here.")

    content = md.read_text()
    builder = load_builder()
    meta = builder.extract_metadata(content)
    assert meta["title"] == "My Protocol"
    assert "short summary" in meta["summary"].lower()

    slug = builder.slugify(meta["title"])
    assert slug == "my-protocol"


def test_convert_md_to_html_roundtrip(tmp_path):
    md = tmp_path / "roundtrip.md"
    md.write_text("# Roundtrip Test\n\nThis is a *markdown* paragraph.")

    builder = load_builder()
    html_content, metadata = builder.convert_md_to_html(md)
    assert "<p>" in html_content
    assert "markdown" in html_content
    assert metadata["title"] == "Roundtrip Test"


def test_process_protocols_writes_manifest_and_pages(tmp_path, monkeypatch):
    # Create a temporary source dir with a single md file
    temp_src = tmp_path / "src"
    temp_src.mkdir()
    (temp_src / "one-protocol.md").write_text("# One Protocol\n\nSummary text here.\n\nContent.")

    temp_out = tmp_path / "out"
    temp_out.mkdir()

    # Load builder and monkeypatch module globals to point to temp dirs
    builder = load_builder()
    monkeypatch.setattr(builder, 'SRC_DIR', temp_src)
    monkeypatch.setattr(builder, 'OUT_DIR', temp_out)

    # Run process_protocols and assert outputs
    builder.process_protocols()

    manifest = temp_out / 'manifest.json'
    assert manifest.exists()
    m = json.loads(manifest.read_text(encoding='utf-8'))
    assert isinstance(m.get('protocols'), list)

    generated_files = list(temp_out.glob('*.html'))
    assert len(generated_files) >= 1
