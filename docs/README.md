# Docs Directory – Website Assets & Images

The `docs/` folder contains the built static site for Project Dukkha along with all assets required for deployment. Source files live in `src/` and are transformed via the build script.

## Structure Overview
- `index.html` – Site entry point
- `site/` – Generated HTML (do **not** edit manually)
- `images/` – Diagrams, icons and placeholders used across the site
- `assets/` – Supporting data such as CSVs and reference material

See the root [README](../README.md) and [`BUILD_WORKFLOW.md`](BUILD_WORKFLOW.md) for the full build system and project vision.

## Image Best Practices
- Use **SVG** for diagrams and icons when possible; compress PNG/JPG assets.
- Name files with descriptive `kebab-case` and store them in the appropriate subfolder (`diagrams/`, `icons/`, `placeholders/`).
- Provide meaningful `alt` text whenever an image is referenced.
- Optimize file size before committing (target <500 KB when feasible).
- Keep working or layered source files outside `docs/` unless they are required on the site.

## Asset Best Practices
- Place non-image resources under `assets/` and group related files (e.g., `assets/content_sources/`).
- Use relative paths when linking to assets from HTML pages.
- Avoid committing unused or temporary assets.

## Updating the Site
1. Edit content in `src/` (never in `docs/site/`).
2. Rebuild: `python scripts/build_site.py`
3. Test: `pytest tests/`
4. Optional link check: `pwsh scripts/qa_check.ps1 -CheckUrls` (when PowerShell is available)
5. Commit both source and generated files, including any new assets.

Maintaining a clean `docs/` directory ensures the site deploys smoothly and reflects Project Dukkha's goal of uniting Buddhist wisdom with modern dopamine science.
