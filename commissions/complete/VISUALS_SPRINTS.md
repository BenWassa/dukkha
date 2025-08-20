## Visual & Content Upgrade Sprints

Purpose
-------
This document breaks the visual and content-style upgrade you requested into a sequence of small, testable sprints. Each sprint has clear goals, deliverables, tasks, acceptance criteria, estimated effort, and risks. The work assumes the existing site in `docs/site/` will be progressively enhanced using CSS, small JS as needed, and lightweight tooling (no heavy CMS required).

Requirements captured
---------------------
- Upgrade formatting and style: bold, italic, headings, spacing
- Improve typographic scale and font sizing
- Establish consistent spacing and rhythm
- Design responsive grids and content layouts
- Style tables and code blocks
- Render simple diagrams (Mermaid) and process flows
- Add and standardize icons and inline visuals
- Create reusable components (cards, callouts, footnotes)
- Ensure accessibility and responsive behavior

Sprint conventions
------------------
- Sprint length: 1 week (can be split into 2x 2-3 day micro-sprints)
- Definition of Done (DoD): PR with changes, visual diff screenshots, QA checklist passed locally, README notes for any new dev steps
- Estimate notation: (S) small = 1-2 days, (M) medium = 3-5 days, (L) large = 1+ week

Sprint 0 — Audit & baseline (S: 1-2 days)
------------------------------------------------
Goal
- Create a lightweight audit of current pages and capture visual debt.

Deliverables
- `docs/site/` visual audit (spreadsheet or Markdown list)
- Baseline screenshots of key pages: index, attention, recovery, myths, library
- A short `notes/visual-audit.md` (or section in this file) listing top 10 issues

Tasks
- Review `docs/site/*.html` for inconsistent typography, spacing, and headings
- Capture screenshots (desktop & mobile sizes) of 5 representative pages
- Note missing assets (icons, diagram sources) and problematic tables

Acceptance criteria
- Audit file added to repo or attached to PR
- Top 10 issues prioritized

Sprint 1 — Design tokens & typography (M: 3-5 days)
------------------------------------------------
Goal
- Establish a robust typographic system and CSS tokens for fonts, sizes, weights, and spacing.

Deliverables
- `docs/styles.css` updated (or new `docs/styles/tokens.css`) containing CSS custom properties: --font-base, --scale-1..6, --leading, --measure, --space-1..6, --radius
- A short spec section describing scale and recommended usage (h1..h6, p, small, captions)

Tasks
- Pick primary & fallback fonts and define font stacks (Crimson Text for headings, Inter for UI/body as in index.html)
- Define a modular scale (e.g., 1.125) and set root font-size and line-heights
- Add utility spacing variables and small helper classes (.lead, .muted, .caps)

Acceptance criteria
- All HTML pages render with consistent headings, paragraph sizes, and readable measure on desktop and mobile
- CSS tokens documented in the repo

Sprint 2 — Layout, grids & responsive rules (M: 3 days)
------------------------------------------------
Goal
- Create a simple grid system and responsive layout rules for content pages and landing pages.

Deliverables
- Grid utilities (CSS grid / flex) in `docs/styles/grid.css` or merged into main stylesheet
- Templates for three content layouts: article (single column), two-column with sidebar, card/grid gallery

Tasks
- Implement a 12-column grid or a responsive 1 / 2 / 3 column pattern using CSS variables
- Set breakpoints and ensure typographic scale responds sensibly
- Update a representative page (e.g., `site/attention.html`) to use the new layout

Acceptance criteria
- Layout patterns re-used on at least two pages and responsive behavior verified

Sprint 3 — Content styles: headings, lists, tables, code, and callouts (M: 3-5 days)
------------------------------------------------
Goal
- Standardize semantics and visual flavor for content elements: headings, lists, blockquotes, callouts, tables, and code blocks.

Deliverables
- `docs/styles/content.css` with styles for headings, ol/ul, dl, blockquote, .callout, .note, table, pre, code
- Examples page `docs/site/_styleguide.html` or `docs/styleguide.md` illustrating components

Tasks
- Normalize heading margins and weights; create consistent spacing rules for headings and paragraphs
- Style tables: zebra or gentle borders, responsive wrapping, caption styles
- Add callout styles for tip/warning/info and a footnote style
- Add small readable styling for inline code and fenced pre blocks

Acceptance criteria
- Styleguide page added and used as acceptance reference

Sprint 4 — Components & reusable blocks (M: 4 days)
------------------------------------------------
Goal
- Build a small library of HTML/CSS components used across pages: cards, chips, footnote references, evidence chips, and protocol steps.

Deliverables
- `docs/styles/components.css` and an example include or fragment snippets for each component
- Update one page to use components (e.g., research claim cards on `site/library.html`)

Tasks
- Implement card, chip, badge, CTA button, and footnote pill
- Document markup so writers can use components in Markdown/HTML

Acceptance criteria
- Components used on at least two pages; documented snippets present

Sprint 5 — Diagrams: Mermaid & simple SVG workflow patterns (M: 3 days)
------------------------------------------------
Goal
- Enable inline diagrams using Mermaid where appropriate and standardize simple SVG embeds for the Compass/atlas visuals.

Deliverables
- Lightweight Mermaid enablement (client-side) and an example diagram in `site/myths.html` or a new `site/diagrams.html`
- Guidelines for embedding SVG (optimize, set viewBox, use `role="img"` and accessible titles)

Tasks
- Add mermaid.min.js and a small init script that converts `<div class="mermaid">` blocks to SVG on load
- Add example flowchart and sequence diagram
- Add documentation: when to use Mermaid vs hand-authored SVG

Acceptance criteria
- Mermaid diagrams render in modern browsers and degrade gracefully when JS disabled

Sprint 6 — Icons, imagery & visual language (M: 3-5 days)
------------------------------------------------
Goal
- Adopt an icon strategy and clarify imagery rules (SVG sprites, inline SVG, or icon font) and light illustration style.

Deliverables
- `assets/icons/` with an initial set of optimized SVG icons
- A small icon usage guide in the styleguide

Tasks
- Choose icon approach (inline SVG recommended for accessibility and theming)
- Convert a handful of existing glyphs into accessible SVGs (compass, lightning, book, checklist)
- Ensure color and sizing variables apply to icons

Acceptance criteria
- Icons used consistently in navigation and CTAs; colorable via CSS variables

Sprint 7 — Accessibility, performance & QA (M: 3-5 days)
------------------------------------------------
Goal
- Ensure accessible contrast, keyboard nav, semantic HTML, and reasonable performance for images and SVGs.

Deliverables
- Accessibility checklist added to `scripts/qa_check.ps1` or a new `scripts/qa_accessibility.ps1` (optional)
- Image optimization notes and a basic audit report

Tasks
- Run axe or Lighthouse locally and capture top 10 issues
- Fix heading order, ARIA labels for diagrams, alt text for images
- Ensure responsive images and optimized SVGs

Acceptance criteria
- Lighthouse score improved (accessibility > 90 recommended) and major a11y blockers fixed

Sprint 8 — Integration, docs, and rollout (S-M: 2-5 days)
------------------------------------------------
Goal
- Wire everything together: update docs, add styleguide links from main pages, and prepare a PR checklist and rollout plan.

Deliverables
- `docs/styleguide.md` (or `docs/site/_styleguide.html`) that documents tokens, components, and markup examples
- PR checklist template for visual changes (include screenshot diffs)

Tasks
- Add styleguide link to footer or dev nav
- Create PR template in `.github/PULL_REQUEST_TEMPLATE.md` suggesting screenshot diffs and accessibility checks

Acceptance criteria
- PRs for visual changes follow the checklist and include screenshots

Optional future sprints (nice-to-have)
- Design system extraction (small npm package or `styles/` module)
- Automated visual regression testing (Percy, Playwright snapshot testing)
- Tiny component library in Web Components or a lightweight framework

Risks & mitigation
- Risk: scope creep. Keep each sprint focused on one surface area and avoid redesigning entire pages in one go.
- Risk: browser differences. Test on Chrome, Firefox, and at least one mobile breakpoint.
- Risk: performance regressions from large SVGs or third-party libs. Mitigate by optimizing SVGs and lazy-loading heavy assets.

Next steps (recommended immediate actions)
1. Run Sprint 0 (audit) to produce a short prioritized list. (S)
2. Implement Sprint 1 (typography & tokens) and land as a single PR that updates `docs/styles.css`.
3. Create `docs/site/_styleguide.html` during Sprint 3 or 4 and use it as acceptance criteria for subsequent sprints.

Contacts & ownership
- If you want, I can implement Sprints 0–2 in sequence and open PRs with screenshots. Tell me whether you prefer small incremental PRs (recommended) or a single big PR.

---
Generated on: 2025-08-19
