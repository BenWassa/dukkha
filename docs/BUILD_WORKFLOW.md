# Project Dukkha - Site Build System

This document describes the standard workflow for maintaining the Project Dukkha site using a source-first approach that preserves manual HTML improvements.

## Folder Structure

```
dukkha/
├── src/                          # Source files (single source of truth)
│   ├── protocols/               # Protocol markdown files with front-matter
│   │   ├── mindfulness-awareness-protocol.md
│   │   ├── digital-detox-protocol.md
│   │   └── ...
│   └── pages/                   # Main page markdown files with front-matter
│       ├── attention.md
│       ├── recovery.md
│       ├── myths.md
│       └── ...
├── scripts/
│   ├── build_site.py           # Main build script (supports both protocols and pages)
│   └── qa_check.ps1            # Quality assurance checks
├── docs/site/                  # Generated HTML (DO NOT EDIT DIRECTLY)
│   ├── *.html                  # Main pages (attention.html, recovery.html, etc.)
│   ├── protocols/
│   │   ├── *.html
│   │   └── manifest.json
│   └── protocols.html
├── backup/                     # Backup of manually corrected HTML
│   └── current-html/
└── tests/                      # Smoke tests
    └── test_site_functionality.py
```

## Key Improvements Preserved

The build system now preserves your manual corrections including:
- **Multiple CSS files**: `variables.css`, `styles.css`, `utilities.css`, `print.css`
- **Dropdown navigation**: Proper dropdown structure and active states
- **External JavaScript**: Uses `site-ui.js` instead of inline scripts
- **Enhanced accessibility**: Proper ARIA attributes and navigation structure
- **Print support**: Print-specific CSS and functionality

## Workflow

### 1. Prerequisites

Install required dependencies:

```bash
pip install pyyaml markdown beautifulsoup4 requests
```

### 2. Edit Content (Standard Practice)

**Always edit source files in `src/protocols/` and `src/pages/`**, never the generated HTML in `docs/site/`.

#### Protocol files (`src/protocols/`)
Each protocol file has YAML front-matter followed by Markdown content:

```yaml
---
title: "Protocol Name"
duration: "14 Days"
tags:
  - tag1
  - tag2
description: "Brief description for meta tags and cards"
slug: "protocol-name"
---

# Protocol Name

Your markdown content here...
```

#### Page files (`src/pages/`)
Each main page file has YAML front-matter followed by Markdown content:

```yaml
---
title: "Page Title"
slug: "page-name"
description: "Meta description"
page_type: "main"
active_nav: "page-name"
hero_class: "hero-page-name"
---

# Page Title

Your markdown content here...
```

### 3. Build the Site

After editing source files, regenerate the site:

```bash
python scripts/build_site.py
```

This reads all `.md` files from `src/protocols/` and `src/pages/`, processes the front-matter, converts Markdown to HTML, and generates:
- Individual protocol pages in `docs/site/protocols/`
- Main content pages in `docs/site/`
- Index page at `docs/site/protocols.html`
- Manifest at `docs/site/protocols/manifest.json`

### 4. Test Functionality

Run smoke tests to ensure the site works:

```bash
python -m pytest tests/ -v
```

Run PowerShell QA checks:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/qa_check.ps1
```

For URL validation (optional):

```powershell
powershell -ExecutionPolicy Bypass -File scripts/qa_check.ps1 -CheckUrls
```

### 5. Deploy

Commit all changes to Git (including both source and generated files) and deploy `docs/site/` to your web server.

## Benefits of This Approach

1. **Single Source of Truth**: All content lives in `src/protocols/` and `src/pages/` as structured Markdown
2. **Preserves Manual Improvements**: Build system maintains your CSS structure, navigation improvements, and JavaScript enhancements
3. **Consistency**: Templates ensure all pages have the same structure and styling
4. **Maintainability**: Adding new protocols or pages is easy with front-matter metadata
5. **Testability**: Automated tests can verify the build process and site functionality
6. **Version Control**: Clear history of content changes in readable Markdown format

## Safety Features

- **Backup Creation**: Current HTML is backed up to `backup/current-html/` before any builds
- **Validation**: QA scripts check for broken links and missing footnote references
- **Testing**: Automated tests verify page structure and functionality
- **Source Control**: All manual improvements are captured in the build templates

## Migration Status

✅ **Completed**: 
- Protocol pages (`src/protocols/*.md` → `docs/site/protocols/*.html`)
- Attention page (`src/pages/attention.md` → `docs/site/attention.html`)
- Improved CSS structure preservation
- Dropdown navigation structure
- External JavaScript integration

🔄 **In Progress**:
- Recovery page markdown source
- Myths page markdown source  
- Model page markdown source
- Library page markdown source

## Troubleshooting

- **Missing dependencies**: Run `pip install pyyaml markdown beautifulsoup4 requests`
- **Front-matter errors**: Ensure YAML is properly formatted with `---` delimiters
- **Build failures**: Check that all required front-matter fields are present
- **CSS/JS issues**: Verify template paths point to correct stylesheet and script locations
- **PowerShell execution policy**: Use `powershell -ExecutionPolicy Bypass -File scripts/qa_check.ps1`
