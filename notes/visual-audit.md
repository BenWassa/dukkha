Sprint 0 — Visual Audit (Sprint run on 2025-08-19)
===============================================

Scope
-----
Quick visual audit of the live site in `docs/site/`, plus a cursory review of the global stylesheet `docs/styles.css`. The goal was to capture the top visual/markup debt to prioritize work for the visual upgrades roadmap.

What I inspected
-----------------
- Pages: `myths.html`, `attention.html`, `recovery.html`, `library.html`, `model.html`
- Global stylesheet: `docs/styles.css`
- Shared JS snippets embedded in pages (footnote behavior)

High-level summary
------------------
The site has a solid foundation: centralized `styles.css` with many useful CSS custom properties (colors, spacing, font stacks), semantic HTML structure, accessible alt text on SVG diagrams, and a clearly-stated typographic intent (Crimson Text for headings, Inter for UI). Several content components already exist (`action-box`, `protocol-steps`, `print-checklist`) and there is a lightweight footnote UX implemented via client-side JS.

Top priorities (quick wins)
--------------------------
1. Duplicate / mismatched footnote IDs and anchors (Critical)
   - Observed in `myths.html`: multiple `<li id="fn1">` and duplicates of `id="fn2"`, etc. This breaks anchor linking and will be flagged by the QA script.
   - Fix: canonicalize footnote IDs (unique, sequential), update anchor hrefs, and run the `scripts/qa_check.ps1` to validate.

2. Hero section class inconsistency (High)
   - Styles in `styles.css` target `.hero` and `.hero-container`, but pages use `class="hero-myths"`, `hero-attention`, etc. Result: hero visuals and spacing may not render consistently.
   - Fix: either update pages to use `.hero` (recommended) or add `.hero-myths`, `.hero-attention` as simple aliases in CSS.

3. Responsive rules / breakpoints missing or incomplete (High)
   - I didn't find media queries for the main grid or navigation. The `hero-container` uses a two-column grid which can break on narrow screens.
   - Fix: add breakpoints (mobile-first) and responsive grid rules; ensure nav collapses or stacks on small viewports.

4. Fixed nav overlap and top spacing (Medium)
   - Nav is fixed with a top offset; some hero sections rely on `margin-top: 80px` to avoid overlap. This pattern is fragile.
   - Fix: add a consistent `body` padding-top or use an anchor offset utility, and ensure each page uses `.container` so content doesn't hide under the nav.

5. Footnote markup duplication & ordering glitches (Medium)
   - Some pages include repeated footnote lists and duplicate text blocks (likely from markdown conversion). This confuses readers and accessibility tools.
   - Fix: reconcile footnote blocks, keep a single canonical footnotes section at the bottom of `<main>` per page.

6. Missing / weak content styles for tables, pre/code, and lists (Medium)
   - CSS currently lacks a dedicated, polished pattern for tables, responsive tables, code blocks, and definition lists.
   - Fix: add `content.css` styles for tables (overflow wrappers), `pre` with monospace, and readable `code` styling.

7. Icons are currently glyphs / emoji (Low)
   - The brand symbol is a unicode lightning glyph. It's fine, but inline SVG icons would enable theming and better accessibility.
   - Fix: create `assets/icons/` (optimized SVGs) and a simple inline-SVG pattern or sprite.

8. No Mermaid or diagram authoring support (Low)
   - Diagrams are static SVGs which is okay; if you want editable flow/process diagrams, add Mermaid client-side render support.
   - Fix: add `mermaid.min.js` and an init script, plus guidance for authors.

9. Missing styleguide / component examples (Low)
   - There's no centralized styleguide page yet for content authors to preview tokens and components.
   - Fix: add `docs/site/_styleguide.html` showing examples of headings, lists, tables, callouts, components, and diagrams.

10. Minor accessibility checks to run (Low)
    - Colors, focus states, keyboard nav, and landmark roles look reasonable but need an axe/Lighthouse pass.
    - Fix: run Lighthouse/axe, fix contrast or missing ARIA where flagged.

Page-specific notes
-------------------
- `myths.html`
  - Duplicate footnote IDs and repeated footnote blocks. Also the content contains a repeated copy of a large HTML fragment — likely a conversion artifact.
  - Use consistent hero class, remove duplicate blocks, and canonicalize footnotes.

- `attention.html` & `recovery.html`
  - Good semantic layout and diagrams with alt text. Ensure responsive behavior for `figure img.diagram-visual` (max-width: 100%, height: auto) and consider lazy-loading large SVGs.

- `library.html`
  - Long citation lists may benefit from typographic rhythm (smaller text, tight leading, or a two-column layout on wide viewports).

- `model.html`
  - Uses several large SVG diagrams; ensure they are optimized (svgo) and have accessible titles/desc elements.

Quick technical checklist (Sprint 0 deliverable)
-----------------------------------------------
- [x] Inspect `docs/site/*.html` for visible markup issues
- [x] Inspect `docs/styles.css` for variables and existing tokens
- [x] Produce top-10 prioritized issues (this file)
- [ ] Capture screenshots of each page at desktop and mobile widths (optional manual step)
- [ ] Run `scripts/qa_check.ps1` locally to catch anchor/id parity and verify results

Suggested immediate fixes (next micro-tasks)
--------------------------------------------
1. Fix footnote IDs in `myths.html` (critical) and re-run QA script.
2. Add `.hero-myths`, `.hero-attention`, `.hero-recovery` aliases to existing `.hero` CSS rules OR update pages to use `.hero` consistently.
3. Add a simple responsive breakpoint block at the end of `styles.css` to stack grids and collapse nav for mobile:
   - e.g., @media (max-width: 768px) { .hero-container { grid-template-columns: 1fr; } .nav-menu { display: none; } }
4. Add `.container` wrappers where missing, or ensure `.page-content` uses the same container padding.
5. Draft `docs/site/_styleguide.html` to anchor visual changes and acceptance criteria.

Notes on verification
---------------------
- After applying fixes, run `.\	ools\scripts\qa_check.ps1` (from repo root) to verify footnote anchors. Use PowerShell on Windows.
- Run Lighthouse (Chrome) locally for accessibility and performance quick checks.

Files created/modified by Sprint 0
---------------------------------
- Created: `notes/visual-audit.md` (this file)

Next steps (pick one)
---------------------
- I can: (A) fix the duplicate footnotes in `docs/site/myths.html` now and re-run the QA script, or (B) implement the hero aliasing + a small responsive breakpoint patch in `docs/styles.css`.

Choose (A) or (B) or both and I'll proceed with the edits and verification.
