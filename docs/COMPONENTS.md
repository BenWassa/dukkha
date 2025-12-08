# Component Migration Plan

This document provides a step-by-step prompt strategy and examples for migrating key UI pieces into React components.

Use this prompt strategy when asking the LLM to convert HTML -> React components:

> I am converting a site to React + Tailwind.
> 1. Here is my `tailwind.config.js` settings: (link or paste the file)
> 2. Here is the HTML structure for the component: (paste relevant HTML snippet)
> 3. Here is the CSS for these classes: (paste the `.class { ... }` from `styles.css`)
> Create a reusable React component named `[ComponentName]`.

---

## 1. NavBar (`NavBar.tsx`)

- Source: `index.html` nav block and `site/js/site-ui.js` dropdown logic.
- Key requirements:
  - Make component accessible (keyboard navigation, ARIA attributes).
  - Replace dropdown logic with `useState` and `useEffect` for keyboard handling.
  - Ensure active-state detection (for local dev, use simple pathname checks then enhance for React Router later).

Props & API:
- None for static nav. Consider `items` prop (array of { label, href }) for reuse.

Example stub:
```tsx
import React, { useState, useEffect, useRef } from 'react';

export default function NavBar({ items }) {
  const [open, setOpen] = useState(false);
  // keyboard/focus handling here
  return (
    <nav className="nav">
      {/* ... */}
    </nav>
  );
}
```

---

## 2. Hero (`Hero.tsx`)

- Source: `index.html` hero section.
- Key considerations:
  - `hero-title` uses serif font.
  - Keep or replace the `compass` CSS art with an SVG component.

Props (optional): `title`, `subtitle`, `description`, `cta`.

Example stub:
```tsx
export default function Hero({ title, subtitle, description }) {
  return (
    <section className="hero">
      {/* ... */}
    </section>
  );
}
```

---

## 3. AccessCard (`AccessCard.tsx`)

- Convert the repeating `.access-card` markup into a single, reusable component.
- Props: `title`, `icon`, `painPoint`, `description`, `link`.
- Render the grid by mapping over an array of cards data.

Example stub:
```tsx
export default function AccessCard({ title, icon, painPoint, description, link }) {
  return (
    <article className="access-card group">
      <div className="card-header">/* icon & pain point */</div>
      <div className="card-content">/* content */</div>
    </article>
  );
}
```

---

## 4. Technical Notes for Migration

- Keep `variables.css` in the project and import it as the source of truth for design tokens until everything is transitioned to Tailwind utils.
- For interactive elements (eg dropdowns, progress bars), implement custom hooks used by relevant components:
  - `useScrollProgress` (scroll progress, visibility)
  - `useDropdown` (open/close state & keyboard traps)
  - `useFootnotesToggle` (collapsible footnotes section)

---

If you'd like, I can scaffold the components and hooks inside `docs/src/components/` and create a minimal `Home.tsx` that uses them. Proceed with scaffolding?