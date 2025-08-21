# Scripts Directory

This directory contains the build system and development tools for Project Dukkha. All scripts are designed to work from the repository root directory.

## 🔧 Core Scripts

### `build_site.py` - Main Build System
**Purpose**: Converts markdown source files to HTML website  
**Usage**: `python scripts/build_site.py`

**What it does**:
- Reads markdown files with YAML front-matter from `src/protocols/` and `src/pages/`
- Converts markdown to HTML with proper footnote handling
- Generates individual protocol pages, main content pages, and protocol index
- Preserves manual CSS improvements and navigation structure
- Creates manifest file for protocol metadata

**Output**:
- Protocol pages: `docs/site/protocols/*.html`
- Main pages: `docs/site/*.html` (attention, recovery, myths, etc.)
- Protocol index: `docs/site/protocols.html`
- Manifest: `docs/site/protocols/manifest.json`

**Dependencies**: `pyyaml`, `markdown`

**Safety**: Automatically preserves your manual HTML corrections through improved templates

### `qa_check.ps1` - Quality Assurance
**Purpose**: Validates footnote references and optionally checks URLs  
**Usage**: 
```powershell
# Basic footnote validation
powershell -ExecutionPolicy Bypass -File scripts/qa_check.ps1

# Include URL validation (slower)
powershell -ExecutionPolicy Bypass -File scripts/qa_check.ps1 -CheckUrls
```

**What it checks**:
- Footnote anchor/ID parity (every `href="#fnN"` has matching `id="fnN"`)
- Optional: HTTP status of all external URLs in references CSV
- Generates summary report with detailed error information

**Output**: Console report with pass/fail status for each HTML file

### `extract_protocols.py` - Migration Utility
**Purpose**: Converts existing HTML protocol files to markdown source format  
**Usage**: `python scripts/extract_protocols.py`

**What it does**:
- Extracts content from `docs/site/protocols/*.html`
- Converts to markdown with YAML front-matter
- Outputs to `src/protocols/*.md`
- Preserves metadata like title, description, duration, tags

**Note**: This was used for the initial migration and may not be needed for ongoing development.

### `run_qa_check.bat` - Windows Convenience Wrapper
**Purpose**: Runs PowerShell QA script from Windows Explorer or CMD  
**Usage**: Double-click in Explorer or `scripts/run_qa_check.bat [-CheckUrls]`

**What it does**:
- Provides easy access to QA script without opening PowerShell
- Forwards all arguments to the PowerShell script
- Handles execution policy issues automatically

## 🗂️ Archived Scripts

The `archived/` folder contains scripts that are no longer needed but preserved for reference:

- **`build_protocols.py`** - Empty file, replaced by `build_site.py`
- **`check-markdown-formatting.ps1`** - Checked for markdown remnants in HTML (no longer needed with source-first approach)
- **`update-css-refs.ps1`** - Updated CSS references during architecture overhaul (one-time use)

## 🚀 Typical Workflows

### Daily Development
```bash
# Edit content in src/protocols/ or src/pages/
# Then rebuild and test:
python scripts/build_site.py
python -m pytest tests/ -v
powershell -ExecutionPolicy Bypass -File scripts/qa_check.ps1
```

### Adding New Protocol
1. Create `src/protocols/new-protocol.md` with YAML front-matter
2. Run `python scripts/build_site.py`
3. Check output in `docs/site/protocols/new-protocol.html`
4. Validate with `powershell -ExecutionPolicy Bypass -File scripts/qa_check.ps1`

### Adding New Main Page
1. Create `src/pages/new-page.md` with YAML front-matter
2. Run `python scripts/build_site.py` 
3. Check output in `docs/site/new-page.html`
4. Validate with QA script

### Full Validation
```powershell
# Complete build and validation pipeline
python scripts/build_site.py; python -m pytest tests/ -v; powershell -ExecutionPolicy Bypass -File scripts/qa_check.ps1 -CheckUrls
```

## 🔍 Script Dependencies

### Python Scripts
- **Python 3.7+** (tested with 3.13)
- **pyyaml**: YAML front-matter parsing
- **markdown**: Markdown to HTML conversion with extensions
- **beautifulsoup4**: HTML parsing (for extract_protocols.py)
- **requests**: URL validation (used by some utilities)

Install with: `pip install pyyaml markdown beautifulsoup4 requests`

### PowerShell Scripts
- **PowerShell 5.1+** (Windows PowerShell or PowerShell Core)
- **No external dependencies** (uses built-in cmdlets)

## 🛡️ Safety Features

### Backup Protection
- Current HTML files are automatically backed up to `backup/current-html/` before builds
- Templates preserve all manual improvements (CSS structure, navigation, JavaScript)

### Validation
- QA script checks for broken footnote references
- Automated tests verify page structure and functionality
- URL validation ensures external links are working

### Source Control
- All content changes tracked in readable markdown format
- Generated HTML changes are also committed for deployment
- Clear separation between source (`src/`) and generated (`docs/site/`) content

## 🔧 Troubleshooting

### Missing Dependencies
```bash
# Error: ModuleNotFoundError: No module named 'yaml'
pip install pyyaml markdown beautifulsoup4 requests
```

### PowerShell Execution Policy
```powershell
# Error: execution of scripts is disabled on this system
powershell -ExecutionPolicy Bypass -File scripts/qa_check.ps1
```

### Build Failures
- Check YAML front-matter formatting (must have `---` delimiters)
- Ensure all required fields are present (title, slug, description)
- Verify markdown syntax

### Path Issues
- Always run scripts from repository root directory
- Use forward slashes or escaped backslashes in paths
- Check that source directories exist (`src/protocols/`, `src/pages/`)

## 📊 Script Metrics

| Script | Purpose | Runtime | Dependencies |
|--------|---------|---------|-------------|
| `build_site.py` | Site generation | ~1-2s | pyyaml, markdown |
| `qa_check.ps1` | Validation | ~1s (basic), ~10s (URLs) | PowerShell |
| `extract_protocols.py` | Migration | ~2-3s | beautifulsoup4 |
| `run_qa_check.bat` | Wrapper | <1s | Windows CMD |

**Total build + test + validate time**: ~5-10 seconds

## 🔄 Recent Updates

- **August 2025**: Overhauled build system to support both protocols and main pages
- **Template Improvements**: Preserved manual HTML corrections in build templates
- **Safety Features**: Added backup system and validation pipeline
- **Script Cleanup**: Archived outdated utilities, focused on core functionality
- **Documentation**: Created comprehensive README with usage examples
