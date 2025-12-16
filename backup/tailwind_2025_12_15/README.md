# Project Dukkha — Docs React Migration

This folder will house the new React + Tailwind site that replaces the static docs currently in `/backup`.

## Migration Summary

Goals:
- Use Vite + React (TypeScript) + Tailwind to modernize the site
- Keep design tokens consistent via CSS variables and a Tailwind config derived from `variables.css`
- Convert individual UI pieces into reusable React components
- Replace imperative `site-ui.js` with React logic (hooks and small components)

Why this approach:
- Component-driven migration (NavBar, Hero, AccessCard, Footnotes, etc.) minimizes breakage and allows progressive conversion
- Reusing design tokens ensures visual continuity while moving to utility-first styling

## Suggested File Structure

- docs/
  - package.json (vite project root)
  - tailwind.config.js
  - postcss.config.js
  - index.html
  - public/
    - images/
  - src/
    - main.tsx
    - App.tsx
    - pages/
      - Home.tsx
      - Protocols.tsx
    - components/
      - NavBar.tsx
      - Hero.tsx
      - AccessCard.tsx
      - Footer.tsx
    - hooks/
      - useScrollProgress.ts
      - useDropdown.ts
    - styles/
      - variables.css (imported)  // merge or reference from backup
      - globals.css

## Migration Steps (High-level)

1. Create the Vite React + TypeScript project inside `docs/`.
2. Add the `tailwind.config.js` and `postcss.config.js` to the project and map design tokens.
3. Create minimal page(s) and import `variables.css` and `styles.css` as a fallback initially.
4. Build the small components one-by-one by converting page fragments from `index.html`:
   - NavBar (convert dropdown to React `useState` & accessible keyboard handling)
   - Hero (keep the CSS visual or replace with an inline SVG)
   - AccessCard (props-driven component: `title`, `icon`, `painPoint`, `description`, `link`)
   - Footnotes -> component with collapsible logic
5. Convert imperative code in `site-ui.js` to React hooks and components:
   - `useScrollProgress` to set a progress bar width and visibility
   - `ScrollToTop` component to support React Router
   - `useDropdown` to manage nav dropdown menu & keyboard traps
6. Replace `styles.css` gradually with Tailwind utilities while preserving the look.
7. Add tests & smoke tests (e.g., Playwright or Jest + React Testing Library) for critical components.

## Notes & Recommendations
- Keep `variables.css` as a source of truth; the Tailwind tokens mirror it to enable utility-first conversion over time.
- Preserve the `compass` CSS div art if desired, or replace with a more maintainable SVG component.
- Build incrementally: start with a single homepage (Home.tsx) and core components, verify them visually, then move other pages.
- Use `manifest.json` inside `protocols/` to dynamically populate the protocols dropdown as currently implemented in `site-ui.js`.

---

If you want, I can scaffold a minimal Vite project in `docs/` with a minimal `NavBar`, `Hero`, and `AccessCard` components (TSX) and the `tailwind.config.js` created. I have scaffolded a starter Vite project and components in `docs/src/` already.

Try it locally:
```bash
cd docs
npm install
npm run dev
```

Notes:
- The starter uses Tailwind + CSS variables. It includes component stubs and `useScrollProgress` hook.
- Replace the content and continue converting pages to React components using the component migration guides.