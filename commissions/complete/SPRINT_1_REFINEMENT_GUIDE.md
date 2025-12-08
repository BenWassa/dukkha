# Sprint 1 Refinement Guide: Implementation Details

**Purpose:** Specific, actionable refinements to complete Sprint 1 and prepare for Sprint 2  
**Last Updated:** December 7, 2025

---

## 1. CSS Refinements Required

### 1.1 Add Mobile Responsiveness to `.page-hero__inner`

**Current Code (lines 1193-1200):**
```css
.page-hero__inner {
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 0 var(--container-padding);
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: var(--space-12);
  align-items: center;
}
```

**Issue:** No mobile breakpoint defined. Visual slot remains on right at all viewport sizes, causing excessive whitespace on mobile.

**Refined Code:**
```css
.page-hero__inner {
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 0 var(--container-padding);
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr);
  gap: var(--space-12);
  align-items: center;
}

/* Mobile: stack content and visual vertically */
@media (max-width: 768px) {
  .page-hero__inner {
    grid-template-columns: 1fr;
    gap: var(--space-8);
  }
  
  .page-hero__visual {
    order: 2; /* Ensure visual appears below content */
  }
}

/* Tablet: adjust gap */
@media (min-width: 768px) and (max-width: 1024px) {
  .page-hero__inner {
    gap: var(--space-8);
  }
}
```

**Rationale:**
- Breakpoint at 768px aligns with standard tablet boundary
- Gap reduced to `--space-8` (32px) on tablet to improve density
- Visual moves below content on mobile for better readability
- Maintains desktop priority hierarchy (side-by-side layout)

---

### 1.2 Fix Navigation Offset

**Current Code (line 1175):**
```css
.page-hero {
  position: relative;
  margin: var(--space-12) 0 var(--space-16);
  padding: var(--space-14) 0;
  background: linear-gradient(135deg, var(--color-surface) 0%, var(--color-background) 100%);
  overflow: hidden;
}
```

**Issue:** `margin-top: var(--space-12)` (48px) doesn't account for fixed nav (48px). Content can be hidden under nav on page load.

**Refined Code:**
```css
.page-hero {
  position: relative;
  margin: calc(var(--nav-height) + var(--space-8)) 0 var(--space-16);
  padding: var(--space-14) 0;
  background: linear-gradient(135deg, var(--color-surface) 0%, var(--color-background) 100%);
  overflow: hidden;
}
```

**Rationale:**
- Uses `--nav-height` (48px) variable defined elsewhere in styles.css
- Adds extra `--space-8` (32px) for breathing room
- Total offset: 80px, sufficient to prevent nav overlap
- Dynamic: if nav height changes, all heroes update automatically

---

### 1.3 Adjust Deck Font Size for Mobile

**Current Code (line 1231):**
```css
.page-hero__deck {
  font-size: var(--text-lg);
  line-height: 1.7;
  color: var(--color-text-secondary);
  max-width: 60ch;
}
```

**Issue:** `var(--text-lg)` (18px) with 60ch max-width causes awkward wrapping on mobile (<40ch available width).

**Refined Code:**
```css
.page-hero__deck {
  font-size: var(--text-lg);
  line-height: 1.7;
  color: var(--color-text-secondary);
  max-width: 60ch;
}

@media (max-width: 768px) {
  .page-hero__deck {
    font-size: var(--text-base);
    max-width: 100%;
  }
}
```

**Rationale:**
- Reduce to `--text-base` (16px) on mobile for better readability
- Allow full width wrapping instead of constraining to 60ch
- Improves scanning and reduces awkward line breaks
- Desktop maintains original 60ch for optimal reading length

---

### 1.4 Improve Label Styling on Mobile

**Current Code (line 1209):**
```css
.page-hero__label {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-accent);
  padding: var(--space-2) var(--space-3);
  background: rgba(201, 169, 97, 0.08);
  border-radius: var(--border-radius);
  width: fit-content;
}
```

**Issue:** At `--text-xs` (12px) with tight padding, label may be hard to read on small screens.

**Refined Code:**
```css
.page-hero__label {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-accent);
  padding: var(--space-2) var(--space-3);
  background: rgba(201, 169, 97, 0.08);
  border-radius: var(--border-radius);
  width: fit-content;
  transition: background-color var(--transition-fast);
}

@media (max-width: 768px) {
  .page-hero__label {
    padding: var(--space-2) var(--space-2);
    gap: var(--space-1);
  }
}
```

**Rationale:**
- Slight padding reduction on mobile to maintain proportions
- Transition for potential hover effects
- Maintains visibility without excessive screen real estate

---

### 1.5 Enhance Meta Chips for Mobile Wrapping

**Current Code (line 1238):**
```css
.page-hero__meta {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
  margin-top: var(--space-2);
}
```

**Issue:** Works but could benefit from explicit mobile adjustment.

**Refined Code:**
```css
.page-hero__meta {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
  margin-top: var(--space-2);
}

@media (max-width: 480px) {
  .page-hero__meta {
    gap: var(--space-2);
  }
  
  .meta-chip {
    font-size: var(--text-2xs);
    padding: var(--space-1) var(--space-2);
  }
}
```

**Rationale:**
- At 480px and below, reduce gap and font to prevent excessive wrapping
- Maintains readability while optimizing space
- Preserves all chip content (doesn't hide any)

---

### 1.6 Refine Print Styles

**Current Code (lines 7-30 in print.css):**
```css
@media print {
  .page-hero, .page-hero::before {
    background: transparent !important;
  }
  
  .page-hero__visual, .page-hero__meta, .page-hero__cta-row {
    display: none !important;
  }

  .page-hero__inner {
    grid-template-columns: 1fr !important;
  }
  
  /* ... existing styles ... */
}
```

**Refined Code (replace above):**
```css
@media print {
  .page-hero, .page-hero::before {
    background: transparent !important;
  }
  
  .page-hero__visual, .page-hero__meta, .page-hero__cta-row {
    display: none !important;
  }

  .page-hero__inner {
    grid-template-columns: 1fr !important;
  }
  
  .page-hero {
    padding: var(--space-8) 0 !important;
    margin: var(--space-8) 0 !important;
    border: none !important;
    page-break-after: avoid;
  }
  
  .page-hero__label {
    display: block !important;
    margin-bottom: var(--space-3);
    background: transparent !important;
    padding: 0 !important;
    color: var(--color-text-primary) !important;
  }
  
  .page-hero__title {
    page-break-after: avoid;
    margin-bottom: var(--space-4);
  }
  
  .page-hero__deck {
    page-break-after: avoid;
    margin-bottom: 0;
  }
  
  /* ... existing styles ... */
}
```

**Rationale:**
- Increase padding from `--space-6` (24px) to `--space-8` (32px) for breathing room
- Explicitly set label display: block and remove background for clean print
- Add page-break rules to prevent orphaned headlines
- Preserve label in print output (was missing before)

---

## 2. HTML Migration Template

For migrating remaining 5 pages (library, model, myths, recovery, protocols).

**Use attention.html as template (lines 47-72):**

```html
<section class="page-hero page-hero--[PAGE_NAME]">
    <div class="page-hero__inner">
        <div class="page-hero__content">
            <div class="page-hero__label">[LABEL_TEXT]</div>
            <h1 class="page-hero__title">[TITLE_TEXT]</h1>
            <p class="page-hero__deck">[DECK_TEXT]</p>
            <div class="page-hero__meta" aria-label="Page metadata" role="list">
                <span class="meta-chip" role="listitem">[CHIP_1]</span>
                <span class="meta-chip" role="listitem">[CHIP_2]</span>
                <span class="meta-chip meta-chip--accent" role="listitem">[CHIP_3]</span>
            </div>
            <div class="page-hero__cta-row" aria-label="Page actions">
                <a class="page-hero__cta page-hero__cta--primary" href="[PRIMARY_ANCHOR]">[PRIMARY_TEXT]</a>
                <a class="page-hero__cta page-hero__cta--secondary" href="[SECONDARY_LINK]">[SECONDARY_TEXT]</a>
            </div>
        </div>
        <div class="page-hero__visual">
            <div class="page-hero__badge">[BADGE_TEXT]</div>
            <p class="page-hero__note">[NOTE_TEXT]</p>
        </div>
    </div>
</section>
```

**Per-Page Values:**

**library.html:**
- `page-hero--library`
- Label: "Reference"
- Title: "Research Library" (current h1 text)
- Deck: "Curated citations underlying every insight."
- Chips: "Evidence", "Updated 2024", "High-Impact" (accent)
- CTA Primary: "Jump to Recent Studies" → "#recent-high-impact-studies-post-2015"
- CTA Secondary: "Explore by topic" → "[anchor TBD]"
- Badge: "Library"
- Note: "Curated sources underlying every insight in Project Dukkha."

**model.html:**
- `page-hero--model`
- Label: "Model"
- Title: "The Reward Compass" (current h1 text, simplified)
- Deck: "A balanced neurochemical model for understanding dopamine, motivation, and optimal states."
- Chips: "Model", "Interactive", "7-min read" (accent)
- CTA Primary: "Jump to Core Schemas" → "#core-schemas-baseline-spikes-sensitivity-tolerance"
- CTA Secondary: "View diagram" → "[anchor TBD]"
- Badge: "Compass"
- Note: "Understand your dopamine system through a 2×2 matrix of baseline and sensitivity."

**myths.html:**
- `page-hero--myths`
- Label: "Myths & Canon"
- Title: "Five Myths" (current h1 text, simplified)
- Deck: "Debunking misconceptions about dopamine and the Buddhist canon to reveal evidence-based truths."
- Chips: "Mythbusting", "Grounded in Canon", "5 Truths" (accent)
- CTA Primary: "Jump to Myth #1" → "#myth-1-buddhism-says-life-is-suffering-so-its-a-pessimistic-philosophy"
- CTA Secondary: "All myths" → "[TBD]"
- Badge: "Myths"
- Note: "Five common misconceptions dispelled with science and wisdom."

**recovery.html:**
- `page-hero--recovery`
- Label: "Recovery Guide"
- Title: "Recovery & Baseline" (current h1 text, simplified)
- Deck: "Restoring tonic dopamine for stability and resilience through evidence-backed protocols."
- Chips: "Recovery", "Baseline", "4-min read" (accent)
- CTA Primary: "Jump to Vicious Cycle" → "#the-vicious-cycle-stress-sleep-and-dopamine-depletion"
- CTA Secondary: "Protocols" → "[anchor TBD]"
- Badge: "Recovery"
- Note: "Break the stress-sleep-dopamine cycle with targeted behavioral strategies."

**protocols.html:**
- `page-hero--protocols`
- Label: "Protocols"
- Title: "Protocols" (current h1 text, keep simple)
- Deck: "Time-bound, evidence-based practices for recalibrating your dopamine system and building sustainable habits."
- Chips: "Actionable", "Week-by-week", "Evidence-Based" (accent)
- CTA Primary: "Browse all protocols" → "#protocol-cards-or-anchor"
- CTA Secondary: "Protocol guide" → "[TBD]"
- Badge: "Protocols"
- Note: "Five practical protocols to manage attention, sleep, stress, nutrition, and awareness."

---

## 3. Accessibility Improvements

### 3.1 Fix Secondary CTA Button Pattern

**Current Code (attention.html, line 63):**
```html
<button class="page-hero__cta page-hero__cta--secondary" type="button" onclick="window.print()">Print this guide</button>
```

**Issue:** `onclick` handler is not keyboard-accessible if focus management is poor.

**Refined Code (Option A - Using Link):**
```html
<a class="page-hero__cta page-hero__cta--secondary" href="javascript:window.print()" aria-label="Print this guide">
    <span>Print</span>
</a>
```

**Refined Code (Option B - Using Button with JavaScript):**
```html
<button class="page-hero__cta page-hero__cta--secondary" type="button" data-action="print" aria-label="Print this guide">
    Print
</button>

<script>
document.querySelector('[data-action="print"]').addEventListener('click', () => window.print());
</script>
```

**Recommendation:** Use Option A for simplicity (print is a standard browser action). Avoid Option B unless you have a general event handler system.

---

### 3.2 Enhance Meta Chip Semantics

**Current Code (attention.html, line 57):**
```html
<div class="page-hero__meta" aria-label="Page metadata">
    <span class="meta-chip">Depth Work</span>
    <span class="meta-chip">Evidence-Based</span>
    <span class="meta-chip meta-chip--accent">5-min read</span>
</div>
```

**Refined Code:**
```html
<div class="page-hero__meta" aria-label="Page metadata" role="list">
    <span class="meta-chip" role="listitem">Depth Work</span>
    <span class="meta-chip" role="listitem">Evidence-Based</span>
    <span class="meta-chip meta-chip--accent" role="listitem">5-min read</span>
</div>
```

**Rationale:**
- `role="list"` + `role="listitem"` improves screen reader navigation
- Semantically clearer structure for assistive technology
- No CSS changes needed

---

### 3.3 Add CTA Row Label

**Current Code (attention.html, line 61):**
```html
<div class="page-hero__cta-row">
    <a class="page-hero__cta page-hero__cta--primary" href="...">Jump to Dopamine Compass</a>
    <button ...>Print this guide</button>
</div>
```

**Refined Code:**
```html
<div class="page-hero__cta-row" aria-label="Page actions">
    <a class="page-hero__cta page-hero__cta--primary" href="...">Jump to Dopamine Compass</a>
    <a class="page-hero__cta page-hero__cta--secondary" href="javascript:window.print()" aria-label="Print this guide">Print</a>
</div>
```

**Rationale:**
- `aria-label` on wrapper provides context for grouped CTAs
- Improved screen reader experience
- Clarifies the section's purpose

---

## 4. Visual Enhancement Recommendations

### 4.1 Add Page-Specific Icons/Visuals

Currently, the `.page-hero__visual` slot is generic (badge + note). Recommend adding page-specific visual hints:

**attention.html:** Brain/focus icon, or subtle animation of concentric circles (focus)
**library.html:** Book stack icon, or subtle open book graphic
**model.html:** Compass or 2×2 matrix hint, or gauge icon
**myths.html:** Magnifying glass or lightbulb icon, or myth symbol
**recovery.html:** Upward arrow or cycle refresh icon, or heart/wellness symbol
**protocols.html:** Checklist or timeline icon, or protocol steps graphic

**CSS Pattern for Icons:**
```css
.page-hero--[page]__visual::before {
  content: '🧠'; /* emoji or SVG inline */
  font-size: 3rem;
  opacity: 0.2;
  position: absolute;
  top: 50%;
  right: 5%;
  transform: translateY(-50%);
  pointer-events: none;
}
```

**Recommendation:** Use Unicode emojis for quick implementation, or SVG inlines for polished look.

---

## 5. Legacy CSS Removal Checklist

Once all pages are migrated to `.page-hero`, remove these legacy rules from `styles.css`:

**Lines to Delete:**
- 241-264: `.hero-container` through `.hero-subtitle--protocol`
- 286-300: `.hero-description`, `.hero-ctas`
- 365-370: `.hero-visual`
- 1106-1163: All `.hero-attention`, `.hero-recovery`, etc. and their pseudo-elements

**Total Savings:** ~150 lines of CSS, reducing file size and eliminating confusion.

**Timing:** Only after all 6 pages are confirmed working with `.page-hero`.

---

## 6. Testing Checklist for Completion

### Desktop (1440px+)
- [ ] Hero displays two-column layout (content left, visual right)
- [ ] Navigation not overlapped
- [ ] Text rendering at full size
- [ ] Print preview shows no backgrounds, metadata, or CTAs
- [ ] All 6 pages visually consistent

### Tablet (768px-1024px)
- [ ] Grid gap reduced to `--space-8`
- [ ] Two-column layout maintained
- [ ] Touch targets adequate for CTAs
- [ ] No horizontal scroll

### Mobile (375px-768px)
- [ ] Single-column layout (content, then visual below)
- [ ] Deck font reduced, wrapping readable
- [ ] Chips stack gracefully with reduced gap
- [ ] Label and title legible at small sizes
- [ ] CTAs remain touch-friendly (min 44px height)

### Print
- [ ] No backgrounds or gradients
- [ ] Label visible at top of page
- [ ] Title and deck readable
- [ ] No metadata chips or CTAs
- [ ] Page breaks avoid orphaned headlines
- [ ] PDF exports cleanly

### Accessibility
- [ ] All pages pass WAVE accessibility audit
- [ ] Screen reader announces metadata as list
- [ ] CTA links/buttons keyboard accessible
- [ ] Print stylesheet maintains hierarchy

---

## 7. Implementation Priority

**Phase 1 (Critical - 1 hour):**
1. CSS mobile breakpoint (1.1)
2. Navigation offset fix (1.2)
3. Print styling refinement (1.6)
4. Migrate remaining 5 pages using template (Section 2)

**Phase 2 (Polish - 1 hour):**
5. Deck font size mobile adjustment (1.3)
6. Label styling mobile (1.4)
7. Meta chips mobile wrapping (1.5)
8. Accessibility improvements (Section 3)

**Phase 3 (Enhancement - 45 min):**
9. Add page-specific visual hints (4.1)
10. Remove legacy CSS (Section 5)
11. Full QA testing (Section 6)

---

## Estimated Timeline

- **Phase 1:** 60 minutes
- **Phase 2:** 60 minutes
- **Phase 3:** 45 minutes
- **Buffer:** 15 minutes (QA findings, minor fixes)
- **Total:** ~3 hours

---

## Success Criteria

✅ All 6 core pages (attention, library, model, myths, recovery, protocols) use `.page-hero` component  
✅ Mobile responsive (tested at 375px, 768px, 1024px, 1440px)  
✅ Print stylesheet removes backgrounds, chips, CTAs while preserving header hierarchy  
✅ Navigation offset resolved (no content hidden under nav)  
✅ ARIA roles and labels properly applied  
✅ Page-specific visual hints added to all pages  
✅ Legacy `.hero-*` CSS removed  
✅ Cross-browser testing passed (Chrome, Safari, Firefox)  
✅ All pages visually consistent and professional
