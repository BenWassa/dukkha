# Sprint Ticket: Convert Protocol MDs into Styled HTML + Index

Date: 2025-08-20
Owner: TBD
Branch: `feature/protocols-html`
Estimate: 1 sprint (4-6 hours)

## Goal
Convert canonical Markdown protocols from `research/protocol expansions/` into styled HTML pages under `docs/site/protocols/`, add a `docs/site/protocols.html` index, and insert accessible inline `<details>` summaries into relevant topic pages. Ensure styling matches `docs/styles.css` and that internal links validate.

## Deliverables
- `scripts/build_protocols.py` — converter script (Python) that reads MD files and emits HTML pages + index.
- `docs/site/protocols/` — generated HTML files, one per protocol (slugified filenames).
- `docs/site/protocols.html` — index page listing summaries with links to generated pages.
- CSS snippet appended to `docs/styles.css` to style protocol pages and inline summaries.
- `<details>` snippets added to `docs/site/attention.html` and `docs/site/recovery.html`.
- QA report and checklist (internal link validation, visual smoke test).

## Tasks
1. Create branch `feature/protocols-html`.
2. Implement `scripts/build_protocols.py`:
   - Read `research/protocol expansions/*.md`.
   - Extract H1 as title and first paragraph as summary.
   - Generate slugified filename and write `docs/site/protocols/<slug>.html` using a template that links `../styles.css`.
   - Generate `docs/site/protocols.html` index with cards and anchors.
3. Add namespaced CSS rules to `docs/styles.css` for `.protocol-article`, `.protocol-list`, and `details.protocol-summary`.
4. Run the script and review generated pages locally (file:// preview).
5. Insert `<details>` summaries into `docs/site/attention.html` and `docs/site/recovery.html` at protocol anchor spots.
6. Run QA: internal link validation and visual smoke test across desktop and mobile widths.
7. Commit and open a PR with screenshots and QA notes.

## Acceptance Criteria
- Generated protocol pages render with site CSS and consistent typography.
- Index lists all protocols with summaries and deep links.
- Topic pages show working `<details>` summaries that link to generated pages.
- All internal links validate.

## Notes
- Use `markdown` Python package (or `markdown2`) to convert MD to HTML blocks.
- Keep original MD files as canonical source in `research/`.
- If owner prefers Node, rewrite the script as `scripts/build_protocols.js` using `marked`.

## QA checklist
- [ ] Branch created
- [ ] Script implemented
- [ ] Pages generated
- [ ] CSS appended
- [ ] `<details>` inserted
- [ ] Internal links validated
- [ ] Visual smoke test passed

