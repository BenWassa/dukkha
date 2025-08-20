# Project Dukkha - Site Build System

This document describes the standard workflow for maintaining the Project Dukkha site using a source-first approach.

## Folder Structure

```
dukkha/
├── src/                          # Source files (single source of truth)
│   ├── protocols/               # Protocol markdown files with front-matter
│   │   ├── mindfulness-awareness-protocol.md
│   │   ├── digital-detox-protocol.md
│   │   └── ...
│   └── templates/               # HTML templates (optional)
│       ├── protocol.html
│       └── index.html
├── scripts/
│   └── build_site.py           # Main build script
├── docs/site/                  # Generated HTML (DO NOT EDIT DIRECTLY)
│   ├── protocols/
│   │   ├── *.html
│   │   └── manifest.json
│   └── protocols.html
└── tests/                      # Smoke tests
    └── test_site_functionality.py
```

## Workflow

### 1. Edit Content (Standard Practice)

**Always edit source files in `src/protocols/`**, never the generated HTML in `docs/site/`.

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

### 2. Build the Site

After editing source files, regenerate the site:

```bash
python scripts/build_site.py
```

This reads all `.md` files from `src/protocols/`, processes the front-matter, converts Markdown to HTML, and generates:
- Individual protocol pages in `docs/site/protocols/`
- Index page at `docs/site/protocols.html`
- Manifest at `docs/site/protocols/manifest.json`

### 3. Test Functionality

Run smoke tests to ensure the site works:

```bash
python -m pytest tests/ -v
```

### 4. Deploy

Commit all changes to Git (including both source and generated files) and deploy `docs/site/` to your web server.

## Benefits of This Approach

1. **Single Source of Truth**: All content lives in `src/protocols/` as structured Markdown
2. **Consistency**: Templates ensure all pages have the same structure and styling
3. **Maintainability**: Adding new protocols or changing layouts is easy
4. **Testability**: Automated tests can verify the build process and site functionality
5. **Version Control**: Clear history of content changes in readable Markdown format

## Migration from Manual HTML Editing

When moving from manual HTML editing to this system:

1. Extract content from existing HTML files into Markdown format
2. Add front-matter metadata for each protocol
3. Run the build script to regenerate HTML
4. Test that the output matches the previous manual version
5. Update any remaining protocols following the same pattern

## Troubleshooting

- **Missing dependencies**: Run `pip install pyyaml markdown`
- **Front-matter errors**: Ensure YAML is properly formatted with `---` delimiters
- **Build failures**: Check that all required front-matter fields are present
- **CSS/JS issues**: Verify template paths point to correct stylesheet and script locations
