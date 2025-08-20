# Commission: Protocols Index + Inline Collapsible Summaries (Option 1)

Date: 2025-08-20
Author: Automated commissioning file (for site maintainers / LLM implementer)

## Purpose

Provide a deterministic, LLM-executable commissioning document to implement Option 1: a single `protocols.html` index page plus lightweight, collapsible `<details>` protocol summaries embedded in topic pages (e.g., `attention.html`, `recovery.html`). Keep site pages lean while making canonical protocol content discoverable from `research/protocol expansions/*.md`.

## Assumptions

- Canonical protocol content lives in `research/protocol expansions/*.md`.
- Site pages live in `docs/site/*.html` and global styles in `docs/styles.css`.
- The implementer has write access to the repository and can commit changes.
- No server-side rendering; changes are static HTML/CSS edits.

## Requirements Checklist (explicit)

- [x] Create a new index page at `docs/site/protocols.html` that lists protocols with a 1–2 sentence summary and link to the canonical MD.
- [x] Insert compact `<details>` summary blocks into topic pages (`docs/site/attention.html`, `docs/site/recovery.html`, etc.) at the relevant protocol anchor spots.
- [x] Add a navigation link to `protocols.html` across site pages (header/navbar include area).
- [x] Add minimal CSS to `docs/styles.css` to style protocol cards/details and ensure print-friendly and accessible rendering.
- [x] Provide QA steps: internal anchor validation, visual smoke test, and commit instructions.

## Acceptance Criteria

- `docs/site/protocols.html` exists and lists all protocol titles with a 1–2 sentence summary and a link to the source MD in `research/`.
- Topic pages show a collapsed summary for each protocol with a short blurb and a prominent `Read full protocol` link (pointing to either `protocols.html#id` or the `research/` MD converted to an HTML page if available).
- The site navigation contains a visible link to `protocols.html`.
- Visual layout matches the site style and remains single-column where appropriate.
- All inserted internal links point to existing files/anchors (internal validation passes).

## High-level Implementation Steps (deterministic)

1. Create `docs/site/protocols.html` with the following structure:
   - Title and short intro.
   - A list/grid of protocol cards. Each card includes:
     - Protocol title (H2)
     - 1–2 sentence summary (pulled from the first paragraph of the corresponding MD)
     - Link to canonical MD (relative path: `../../research/protocol expansions/Name of Protocol.md`) — or, if you prefer converted HTML pages, link to `protocols.html#protocol-slug`.
   - Minimal meta/SEO tags matching other pages.

   Template snippet (HTML):

   <!-- Use this template inside protocols.html -->
   <section class="protocol-list">
     <!-- Repeat per protocol -->
     <article class="protocol-card" id="protocol-focus-sprint">
       <h2>The Focus Sprint — 7-day experiment</h2>
       <p>One-sentence summary pulled from the canonical MD: short goal + duration.</p>
       <a href="../../research/protocol expansions/Digital Detox Protocol.md">Read canonical protocol (MD)</a>
       <!-- Optional: link into site: <a href="protocols.html#protocol-focus-sprint">Open on site</a> -->
     </article>
   </section>

2. Insert `<details>` blocks in target topic pages (`docs/site/attention.html`, `docs/site/recovery.html`, etc.) where the protocol anchor belongs.
   - Each `<details>` should include a `<summary>` with the protocol title and an inline 1–2 sentence blurb. Inside the expanded panel include a short bulletized steps preview and a `Read full protocol` link.

   Template snippet (to insert at the protocol anchor location):

   <details class="protocol-summary" id="protocol-focus-sprint-summary">
     <summary>The Focus Sprint — 7-day experiment</summary>
     <p>Goal: Short statement of the experiment. Duration: 7 days.</p>
     <ul>
       <li>Day 1–3: Step concise</li>
       <li>Day 4–7: Continue with X</li>
     </ul>
     <p><a href="../protocols.html#protocol-focus-sprint">Read full protocol and resources</a></p>
   </details>

   Notes:
   - Use `id` values that match the `protocols.html` card `id` for cross-linking (e.g., `protocol-focus-sprint`).
   - Keep content short — 3–5 lines — so pages remain lean.

3. Update navigation/header include on each `docs/site/*.html` page to add a link:

   <nav>
     ...existing links...
     <a href="protocols.html">Protocols</a>
   </nav>

   - Place the link in the same structural area as other top-level links.

4. CSS changes — append to `docs/styles.css` (minimal and accessible):

   /* Protocol list & details styles (append) */
   .protocol-list { display:grid; gap:1rem; grid-template-columns:1fr; max-width:900px; margin:0 auto; }
   .protocol-card { border:1px solid var(--muted); padding:1rem; border-radius:8px; background:var(--card-bg); }
   details.protocol-summary { border:1px solid var(--muted); padding:0.6rem; border-radius:6px; background:transparent; }
   details.protocol-summary summary { font-weight:600; cursor:pointer; }
   details.protocol-summary[open] { background: rgba(0,0,0,0.02); }

   /* Print rules */
   @media print { details.protocol-summary { display:block; } details.protocol-summary summary { font-weight:700; } }

5. QA validation (deterministic checks):
   - For each protocol link inserted, validate the target file exists.
     - If linking to a file path like `../../research/protocol expansions/X.md`, ensure the file name and spacing match exactly.
   - For each `protocols.html#protocol-slug` internal link, open `docs/site/protocols.html` and verify an element with `id="protocol-slug"` exists.
   - Run a visual smoke test: open `docs/index.html` (or `docs/site/attention.html`) in a browser using file:// and confirm collapsed blocks render and expand.
   - Accessibility quick check: ensure keyboard can focus and toggle the `<summary>` elements.

6. Commit instructions (example):
   - Branch: `feature/protocols-index`
   - Commit message: `Add protocols index and inline collapsible summaries (Option 1)`

## Data mapping guidance

- Source canonical text from `research/protocol expansions/*.md`.
- Extract the first paragraph and the H1 as the title when generating the 1–2 sentence summary.
- Suggested slug generation: lowercase, replace spaces with `-`, remove punctuation. Example: `The Focus Sprint — 7-day experiment` -> `protocol-focus-sprint`.

## Edge cases & notes

- Names with ampersands, slashes, or non-ASCII characters: normalize the slug and keep the original title in the UI.
- If the MD filenames contain spaces, match the exact filename in links or optionally convert MD to site HTML and link to the converted page.
- If you prefer not to link directly to raw MD files for users, create small HTML wrappers under `docs/site/protocols/` that render the MD content or copy the canonical summary.

## Small optional enhancements (post-acceptance)

- Add an anchor-link icon next to each protocol title in `protocols.html` for easy deep-linking.
- Add `aria-controls` and `aria-expanded` attributes to `<summary>` elements for stronger accessibility.
- Convert the canonical MDs into HTML pages under `docs/site/protocols/` for consistent site UX.

## QA checklist to mark when done

- [ ] `docs/site/protocols.html` exists and is linked from site nav
- [ ] `<details>` inserted into `docs/site/attention.html` and `recovery.html` at correct positions
- [ ] CSS appended to `docs/styles.css` and no visual regressions on index/home
- [ ] All internal links/anchors validate
- [ ] Visual smoke test completed in local browser
- [ ] Changes committed on `feature/protocols-index` branch


---

End of commissioning document.
