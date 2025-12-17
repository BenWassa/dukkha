# CSS Cleanup Plan — Project Dukkha 🔧

**Status:** Draft — add your notes below. 

## TL;DR
- Normalize spacing using design tokens (`--space-*`, `--container-*`).
- Remove fixed-width/height traps (diagrams, hero backdrops, cards, footer columns).
- Ensure consistent wrapper structure (add missing `.protocol-list` wrappers).
- Make small, low-risk fixes first (quick wins), then tackle larger responsive refactors.

---

## Prioritized Steps (High → Low) 🚩
1. Replace raw spacing values (px/rem) with tokens in `docs/styles.css` and `docs/utilities.css`.
2. Tokenize component sizes: introduce `--diagram-max-width`, `--diagram-max-height` in `docs/variables.css` and apply to `.diagram-visual`.
3. Remove fixed `min-height` and fixed `width/height` on card and visual components (`.access-card`, `.protocol-card`, `.compass-container`) — use `max-width`/`max-height` tokens and `min-block-size` where needed.
4. Convert footer grid to flexible `minmax()` columns or token-based columns in `docs/styles.css` (`.site-footer__grid`).
5. Rework hero decoration pseudo-elements to use relative sizes and controlled media queries (`.page-hero::before`).
6. Audit `position: fixed` elements (nav, dropdown) to ensure content isn't overlapped and that height tokens are used (`--nav-height`).
7. Add a small visual QA checklist and snapshots for hero, protocol-list, and diagrams.

---

## Quick Wins (low-risk, high ROI) ✅
- Replace `gap: 1rem` → `gap: var(--space-4)` across components.
- Wrap protocol cards in a `.protocol-list` container where missing (apply grid styles immediately).
- Change `.diagram-visual { height: 400px; }` → `max-height: var(--diagram-max-height)` (introduce `--diagram-max-height: 480px`).

---

## File-by-file PR Checklist (suggested diffs)

- `docs/variables.css`
  - Add tokens: `--diagram-max-width`, `--diagram-max-height`, `--visual-max-width`.
  - Confirm spacing scale includes `--space-1..--space-32` and `--container-padding`.

- `docs/utilities.css`
  - Replace raw `gap: 1rem` usages with `gap: var(--space-4)`.
  - Update `.diagram-visual` to use `max-width: var(--diagram-max-width)` + `max-height: var(--diagram-max-height)` and remove fixed `height`.

- `docs/styles.css`
  - Replace fixed `min-height: 380px` on `.access-card` and `.protocol-card` with token-based sizing or remove entirely.
  - Update `.site-footer__grid` to `grid-template-columns: 1fr minmax(220px, 360px) minmax(220px, 320px)` and add breakpoint adjustments.
  - Change `.bulging-phone-figure { max-width: 460px }` → `max-width: var(--visual-max-width)`.

- `docs/index-vision.css`
  - Mirror any brand or visual-size token changes used in `styles.css`.

- `docs/site/*.html` (markup)
  - Ensure long lists (protocol cards) are wrapped with `<div class="protocol-list">...</div>` so `.protocol-list` grid styles apply.
  - Remove inline fixed height or inline style overrides that conflict with CSS tokens.

- Example: `.diagram-visual` changes
  - **Before:** `max-width: 700px; height: 400px; object-fit: none;`
  - **After:** `max-width: var(--diagram-max-width); max-height: var(--diagram-max-height); object-fit: cover;` (or `contain` per diagram)

---

## Alignment & Breakpoint Notes
- Use `align-items: start` for grids containing visuals + text to avoid vertical center mismatch unless intentionally centered.
- Prefer `grid-template-columns: 1fr` on mobile and `1fr 420px` (or var token) on desktop for two-column content.
- Test hero and footer at 320, 480, 768, 1024, 1280 widths.

---

## Further considerations & testing 💡
- Add a short visual test script (or manual checklist) to confirm hero, protocol-list, and diagram render correctly after each change.
- Keep PRs small and focused: apply one tokenization per PR, then the corresponding markup or layout fixes.

---

## Notes (your input)
_Add your notes below — I'll incorporate them into the plan or patch changes._

- 

---

File created by: GitHub Copilot (Raptor mini (Preview))
Date: 2025-12-16
