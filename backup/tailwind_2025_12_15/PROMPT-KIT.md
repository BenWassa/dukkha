# Prompt Kit for React + Tailwind Migration

Paste this into LLM prompts to keep output consistent.

## Tokens (Tailwind)
- Colors: `primary` #1e293b (light #334155), `accent` #c9a961 (light #d4b574), `surface` #f8fafc, `surface.elevated` #ffffff, `text.primary` #0f172a, `text.secondary` #475569, `text.muted` #64748b, `border` #e2e8f0 (light #f1f5f9).
- Fonts: `font-serif` = "Crimson Text", `font-sans` = Inter, `font-mono` = SF Mono.
- Radius/Shadow: radius 12px (`var(--tw-radius)`), soft shadow `0 15px 45px rgba(15, 23, 42, 0.08)`.
- Backgrounds: `bg-hero-gradient`, `bg-radial-glow`.

## Utility patterns
- Buttons: `.btn-primary` = accent bg, white text, rounded; `.btn-ghost` = border + text-primary.
- Shells: `.section-shell` = `max-w-6xl mx-auto px-6`; `.card-shell` = `bg-white border border-border rounded-xl shadow-sm`.
- Anim: `.animate-spin-slow` for compass ring.

## Component prompts
- Ask: “TSX + Tailwind classes, no inline styles, use tokens above, keep ARIA/semantics, no custom colors.”
- NavBar: data-driven links, dropdown via `useState`; use `Link` for internal routes, `<a>` for legacy `/site/*.html`.
- Hero: serif headline, accent subhead, CTA buttons using `.btn-primary` / `.btn-ghost`, optional compass visual using the provided CSS classes.
- AccessCard: props `{ title, icon, painPoint, description, link }`, wrap in `.card-shell`, hover translate/shadow.

## Layout
- Use `<Layout>` with `max-w-6xl` content and `pt-24` top padding under fixed nav.
- Prefer `grid grid-cols-1 md:grid-cols-3 gap-6` for cards; `flex flex-col gap-4` for stacks.

## Accessibility
- Use semantic landmarks (`header/nav/main/section/footer`), meaningful `aria-label` on buttons/menus, keyboard-friendly dropdowns, alt text on images.

## Avoid
- Avoid hard-coded Tailwind defaults like `bg-blue-500`; stick to tokens.
- Avoid inline styles; prefer classnames and the utilities above.
