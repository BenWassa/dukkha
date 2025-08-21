# Docs Directory – Site Build & Live Assets

This folder hosts the published version of Project Dukkha. Source material lives in `src/` and is compiled here by running `python scripts/build_site.py`. Only commit generated files or assets that are meant to be served on the live site.

## Recent Updates (August 2025)
- **Complete Footnotes System**: All 5 protocols now have comprehensive citations (49 total) with clean separation
- **Enhanced Build System**: Resolved duplicate footnotes issue - citations appear only in dedicated sections
- **Interactive Features**: Collapsible footnotes sections with smooth scrolling navigation
- **Quality Validation**: Zero duplicate footnotes verified across all generated HTML pages

## Directory map
- `index.html` – landing page linking to all major sections.
- `site/` – generated pages (**do not** edit manually).
- `images/` – diagrams, icons and placeholders used by the live site.
- `assets/` – data files and reference material consumed by pages.
- `styles.css`, `variables.css`, `utilities.css`, `print.css`, `index-ui.js` – styling and interactivity.

## Live site pages
| File | Purpose | Connected assets |
| --- | --- | --- |
| `index.html` | Entry point with quick access cards for protocols and resources. | icons `focus-target.svg`, `moon2.svg`, `myth-busting.svg`, `Dopamine.svg`, `research-library.svg`; diagram `simple dopamine case process.svg` |
| `site/attention.html` | Home for the **Focus Sprint** protocol addressing the ping‑scroll loop. | diagram `ping_scroll_loop_original.svg`; sources `assets/content_sources/A_attention` |
| `site/recovery.html` | **Recovery Reset** protocol restoring baseline via sleep and stress management. | diagrams `dopamine_baseline_spike.svg`, `stress_sensitization_loop.svg`; sources `assets/content_sources/B_recovery` |
| `site/myths.html` | Seven dopamine myths with citations. | sources `assets/content_sources/C_myths` |
| `site/model.html` | Explains dopamine baseline/spike and reward compass model. | diagrams `dopamine_baseline_spike.svg`, `reward_compass.svg` |
| `site/library.html` | Searchable research library compiled from references. | data `assets/content_sources/references_extracted.csv` |
| `site/protocols.html` | Index of extended protocols. | icons as on landing page |
| `site/protocols/*.html` | Detailed protocol pages: digital detox, mindfulness, sleep, nutrition and stress. | Complete footnotes sections with 49 total research citations; served with `protocols/manifest.json` for PWA |

## Live images
### Diagrams (`images/diagrams/`)
- `simple dopamine case process.svg` – landing page overview of dopamine cycle.
- `ping_scroll_loop_original.svg` – illustrates the attention ping/scroll loop.
- `dopamine_baseline_spike.svg` – compares baseline vs spike; shared across model & recovery pages.
- `reward_compass.svg` – visualizes the reward compass on the model page.
- `stress_sensitization_loop.svg` – stress‑reward loop featured on the recovery page.
- Other files in this folder are drafts or unused; keep them outside `docs/` when not deployed.

### Icons (`images/icons/`)
- `focus-target.svg` – Focus Sprint quick‑access card.
- `moon2.svg` – Recovery Reset card.
- `myth-busting.svg` – Myth Busting card.
- `Dopamine.svg` – Dopamine Model card.
- `research-library.svg` – Research Library card.
- `ouroboros-svgrepo-com.svg` – background motif referenced in `styles.css`.
- Additional icons (`3.svg`, `lightbulb.svg`, `ouroboros-simple.svg`, `recovery-moon.svg`, `sleeper.svg`) are available but not currently referenced.

### Placeholders (`images/placeholders/`)
- `diagram_placeholder.svg` – reserved for future diagram slots; not used in production.

## Non-image assets
- `assets/content_sources/A_attention` – raw references for attention protocol.
- `assets/content_sources/B_recovery` – references for recovery protocol.
- `assets/content_sources/C_myths` – references for myths page.
- `assets/content_sources/references_extracted.csv` – master citation list powering the research library.

## Update & test workflow
1. Make edits in `src/`.
2. Rebuild: `python scripts/build_site.py`.
3. Run tests: `pytest tests/`.
4. Optional link check: `pwsh scripts/qa_check.ps1 -CheckUrls` (Windows PowerShell).
5. Commit updated `src/` and generated `docs/` files.

Maintaining accurate asset mapping keeps the site aligned with Project Dukkha’s mission: integrating Buddhist wisdom with contemporary dopamine science.

