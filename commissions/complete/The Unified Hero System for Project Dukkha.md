# The Unified Hero System for Project Dukkha

Your six core pages — Attention, Library, Model, Myths, Protocols, Recovery — deserve a consistent, elevated hero experience that sets tone, communicates purpose, and provides clear orientation for the reader. Right now the heroes are solid but functionally sparse and visually minimal compared with the sophistication of the rest of your site.

Upgrading them into a shared, flexible system will improve:
- Brand coherence
- Readability + UX
- Searchability and scannability
- Onboarding to each page’s intent
- Navigation clarity (via metadata + CTAs)
- Maintainability (one CSS pattern, six uses)

Below is the consolidated, highest-impact plan.

---

## 1. Create a Shared Hero System

### Key structural principles

Your new hero should use:

**A. Two-column grid on desktop (1 column on mobile)**  
Left: Title, deck, metadata, CTA  
Right: Optional meta visual (icon, diagram hint, protocol badge, etc.)  
This mirrors the aesthetic quality of your index page hero and rewards users with an immediate orientation.

**B. Full-width canvas, constrained inner grid**  
- Outer section: spans the full viewport width  
- Inner container: max-width based on `var(--container-width)`

**C. Layered visual treatment**  
Reuse your existing design tokens:  
- Subtle diagonal gradient  
- Soft radial highlight in a corner  
- Decorative override removed in print view  
This maintains the aesthetic of your current `.hero-*` classes without rewriting your visual identity.

**D. Semantic clarity**  
Every page gets a top label, a small-caps element above the headline:  
- Attention: “Field Guide”  
- Library: “Reference”  
- Model: “Model”  
- Myths: “Myths & Canon”  
- Protocols: “Protocols”  
- Recovery: “Recovery Guide”  
This immediately differentiates conceptual vs actionable vs reference content.

**E. Metadata Row (Chips)**  
A horizontal list of 2–4 chips:  
- Topic categories  
- Estimated reading time  
- Last updated (optional)  
- Evidence / Actionability indicators  
These chips anchor expectations and encourage scrolling.

**F. CTA Pair**  
- Primary: jump to first major section  
- Secondary: print / share / or alternative navigation  
Keep the CTAs minimal, neutral, non-promotional.

**G. Typography Strategy**  
- Serif headlines (Crimson): gravitas, timelessness  
- Sans deck/meta (Inter): precision, clarity  
- Line-length capped at ~60ch for readability

**H. Print considerations**  
Your print stylesheet should strip:  
- Radial gradients  
- Background artwork  
- CTAs  
- Meta chips  
But retain: Label → H1 → Deck → Section content

---

## 2. System Architecture

Add a unified component in `styles.css`:  
- `.page-hero` → wrapper  
- `.page-hero__label`  
- `.page-hero__title`  
- `.page-hero__deck`  
- `.page-hero__meta` (chip list)  
- `.meta-chip` / `.meta-chip--accent`  
- `.page-hero__cta-row`  
- `.page-hero__cta--primary` / `.secondary`  
- `.page-hero__visual`

Then remap your existing page-specific classes:  
- `.hero-attention` → `.page-hero attention-hero`  
- `.hero-library` → `.page-hero library-hero`  
…etc.  
This avoids breaking existing styling while pushing all future work into one component pattern.

---

## 3. Per-Page Messaging Strategy

### Attention (`attention.html`)
- Headline: Focus & Attention  
- Deck: Reclaiming deep work in a distraction economy.  
- Meta chips: Depth Work, Evidence-Based, 5-min read  
- Primary CTA: Scroll to “The Dopamine Compass”

### Library (`library.html`)
- Headline: Research Library  
- Deck: Curated citations underlying every insight.  
- Meta chips: Evidence, Updated 2024  
- Primary CTA: Jump to “Recent & High-Impact Studies”

### Model (`model.html`)
- Headline: The Reward Compass  
- Deck: A balanced neurochemical model for modern behaviour.  
- Meta chips: Model, Diagram, 7-min read  
- Primary CTA: Jump to interactive matrix

### Myths (`myths.html`)
- Headline: Five Myths  
- Deck: Debunking misconceptions about dopamine and the Buddhist canon.  
- Meta chips: Mythbusting, Grounded in Canon  
- Primary CTA: Jump to Myth #1

### Protocols (`protocols.html`)
- Headline: Protocols  
- Deck: Time-bound practices for recalibrating behaviour.  
- Meta chips: Actionable, Week-by-week  
- Primary CTA: Protocol List

### Recovery (`recovery.html`)
- Headline: Recovery & Baseline  
- Deck: Restoring tonic dopamine for stability and resilience.  
- Meta chips: Recovery, Baseline, 4-min read  
- Primary CTA: First practice section

---

## 4. Implementation Order (Correct and Efficient)

**Step 1 — Build Component Styles**  
Add a new `.page-hero` system in `styles.css`. Ensure tokens match your existing spacing and color system.

**Step 2 — Replace HTML Structures**  
In each of the six pages:  
- Remove old `.hero-*` markup  
- Insert new component markup  
- Keep old classes as fallbacks until migration complete

**Step 3 — Add Visual Meta Elements**  
For example:  
- A small icon next to labels  
- A thematic accent for each page  
- A subdued, non-distracting right-column illustration (optional)

**Step 4 — Validate Responsive Views**  
Mobile must collapse into: Label → Title → Deck → Meta chips → CTA → Visual

**Step 5 — Validate Print Views**  
Ensure backgrounds are removed and hierarchy is maintained.

**Step 6 — Add ARIA Enhancements**  
- `aria-label="Page metadata"` for meta chip list  
- `aria-label="Jump to section"` for primary CTA

---

## 5. Strategic Rationale

This upgrade is not cosmetic. It increases:

**A. Cognitive clarity**  
Users immediately understand: “What is this page, what is it about, and what should I read first?”

**B. Narrative coherence**  
Your project spans neuroscience, philosophy, UX ethics. A shared hero system visually unifies it.

**C. Professional polish**  
This elevates the site to the level of an editorial field guide — almost book-like — which fits your goals and tone.

**D. Maintainability**  
Future updates require changing one pattern, not six disconnected files.

**E. Scalability**  
If you add new pages later (e.g., “Craving”, “Addiction”, “Design Ethics”), the hero system simply extends.

---

## 6. My Recommendation

You have the right concept and the correct plan. The next move is implementation.

If you want, I can:  
- Generate the full shared CSS block, ready to paste  
- Generate the new HTML hero markup for each page  
- Apply the edits directly

---

## Sprint Breakdown

**Sprint 1 — System foundation**  
- Add `.page-hero` component styles to `docs/styles.css` (desktop grid, mobile stack, chips, CTA styles, label typography, visual slot).  
- Update `print.css` to strip backgrounds/CTAs/meta chips while preserving hierarchy.  
- Wire a single page (e.g., `docs/site/attention.html`) to the new markup structure as the pilot.  
- Quick QA: desktop/mobile/print for the pilot page.

**Sprint 2 — Page migrations**  
- Migrate remaining pages to the new hero markup: `library.html`, `model.html`, `myths.html`, `protocols.html`, `recovery.html`.  
- Apply per-page labels, decks, meta chips, and CTA anchors (jump links) per the plan.  
- Light visual accents per page (optional icons/illustrations in the right column).  
- QA each page for responsiveness and accessibility (aria-labels on meta list/CTAs).

**Sprint 3 — Polish & governance**  
- Refine spacing/typography tokens if needed (line-length clamp, top padding with fixed nav).  
- Validate print view across all pages; ensure backgrounds/CTAs/chips are hidden.  
- Add small utility helpers if helpful (e.g., `.meta-chip--accent` variants).  
- Write a short “hero system” note in the docs/commissions or README to guide future pages.  
- Final cross-browser smoke test and tidy any unused legacy hero styles.
