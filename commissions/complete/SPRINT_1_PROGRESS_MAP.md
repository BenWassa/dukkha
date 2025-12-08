# Sprint 1 Investigation: Visual Progress Map

## Current State Overview

```
THE UNIFIED HERO SYSTEM FOR PROJECT DUKKHA
Sprint 1 Assessment & Refinement Plan

┌─────────────────────────────────────────────────────────────┐
│ COMPONENT SYSTEM ARCHITECTURE                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ✅ CSS Foundation (docs/styles.css, lines 1174-1355)       │
│     ├─ .page-hero (wrapper with gradient + backdrop)       │
│     ├─ .page-hero__inner (grid: 1.1fr | 0.9fr)             │
│     ├─ .page-hero__content (left column)                   │
│     │   ├─ .page-hero__label (uppercase accent)            │
│     │   ├─ .page-hero__title (serif, clamp())              │
│     │   ├─ .page-hero__deck (sans, 60ch)                   │
│     │   ├─ .page-hero__meta + .meta-chip (chips)           │
│     │   └─ .page-hero__cta-row (primary + secondary)       │
│     └─ .page-hero__visual (right column, optional)         │
│        ├─ .page-hero__badge                                │
│        └─ .page-hero__note                                 │
│                                                              │
│  ✅ Print Stylesheet (docs/print.css)                       │
│     ├─ Backgrounds → transparent                           │
│     ├─ Metadata, CTAs → hidden                             │
│     └─ Grid → collapse to 1 column                         │
│                                                              │
│  ⚠️  Responsive Design (needs mobile breakpoint)            │
│  ⚠️  Navigation Offset (needs calc() fix)                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ PAGE MIGRATION STATUS                                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ✅ attention.html        [FULLY MIGRATED]                  │
│     Label: "Field Guide"                                    │
│     Status: Complete with all elements                      │
│                                                              │
│  ❌ library.html          [NEEDS MIGRATION]                 │
│     Label: "Reference"                                      │
│     Status: Still using .hero-library                       │
│                                                              │
│  ❌ model.html            [NEEDS MIGRATION]                 │
│     Label: "Model"                                          │
│     Status: Still using .hero-model                         │
│                                                              │
│  ❌ myths.html            [NEEDS MIGRATION]                 │
│     Label: "Myths & Canon"                                  │
│     Status: Still using .hero-myths                         │
│                                                              │
│  ❌ recovery.html         [NEEDS MIGRATION]                 │
│     Label: "Recovery Guide"                                 │
│     Status: Still using .hero-recovery                      │
│                                                              │
│  ❌ protocols.html        [NEEDS MIGRATION]                 │
│     Label: "Protocols"                                      │
│     Status: Still using .hero-protocols                     │
│                                                              │
│  Progress: 1/6 pages (16.7%)                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ SPRINT 1 COMPLETION CHECKLIST                               │
├──────────────────────────┬────────────────────────────────┤
│ Task                     │ Status                         │
├──────────────────────────┼────────────────────────────────┤
│ ✅ Step 1: CSS Component │ COMPLETE                       │
│    Styles Added          │ All tokens, spacing, colors OK │
│                          │                                │
│ ✅ Step 2: HTML Template │ COMPLETE (attention.html)      │
│    & Pilot Migration     │ 5 pages remaining              │
│                          │                                │
│ ⚠️  Step 3: Visual Meta  │ PARTIAL                        │
│    Elements              │ Generic badge/note, needs      │
│                          │ page-specific icons            │
│                          │                                │
│ ❌ Step 4: Responsive    │ INCOMPLETE                     │
│    Views Validation      │ No mobile breakpoint           │
│                          │                                │
│ ⚠️  Step 5: Print Views  │ NEEDS REFINEMENT               │
│    Validation            │ Rules present, padding tight   │
│                          │                                │
│ ⚠️  Step 6: ARIA         │ PARTIAL                        │
│    Enhancements          │ Basic labels OK, missing       │
│                          │ role="list", button pattern    │
│                          │                                │
└──────────────────────────┴────────────────────────────────┘
```

---

## Issue Severity Map

```
🔴 BLOCKING (Must fix before validation)
├─ [NAV OFFSET] Content hidden under fixed nav
│  └─ Fix: Add margin calc(var(--nav-height) + var(--space-8))
│
├─ [MOBILE RESPONSIVE] No grid collapse at 768px
│  └─ Fix: Add @media query to stack columns on mobile
│
└─ [PAGE COVERAGE] Only 1 of 6 pages migrated
   └─ Fix: Complete migrations using provided template

🟡 IMPORTANT (Should fix for quality)
├─ [VISUAL CONTENT] Generic badge + note, needs page-specific hints
│  └─ Fix: Add icons or diagram hints per page
│
├─ [PRINT POLISH] Padding tight (24px), label visibility unclear
│  └─ Fix: Increase to var(--space-8), ensure label prints
│
├─ [ACCESSIBILITY] Missing role="list", button pattern issue
│  └─ Fix: Add semantic roles, fix button onclick handler
│
└─ [LEGACY CSS] Old .hero-* classes still defined (150+ lines)
   └─ Fix: Remove once all pages migrated

🟢 NICE-TO-HAVE (Can defer to later sprints)
└─ [ADVANCED VISUALS] Animations, interactive elements
   └─ Consider for Sprint 2 enhancements
```

---

## Refinement Phases

```
PHASE 1: CRITICAL (Complete Sprint 1 foundation)
Duration: ~1 hour
┌──────────────────────────────────────────────────┐
│ 1. Add mobile breakpoint @media (max-width: 768px)│
│    • Grid from [1.1fr, 0.9fr] → [1fr]            │
│    • Gap from --space-12 → --space-8             │
│                                                   │
│ 2. Fix nav offset with calc()                    │
│    • margin: var(--space-12) → calc(var(...)    │
│                                                   │
│ 3. Migrate 5 remaining pages                     │
│    • Use template from refinement guide          │
│    • Apply per-page labels, chips, CTAs          │
│                                                   │
│ 4. Refine print styles                           │
│    • Padding var(--space-6) → var(--space-8)    │
│    • Ensure label visibility                     │
└──────────────────────────────────────────────────┘
  ACCEPTANCE: All 6 pages consistent, mobile tested, nav fixed

PHASE 2: POLISH (Improve quality & accessibility)
Duration: ~1 hour
┌──────────────────────────────────────────────────┐
│ 5. Adjust deck font for mobile                   │
│    • var(--text-lg) → var(--text-base) @768px   │
│                                                   │
│ 6. Enhance label styling on small screens        │
│    • Adjust padding/gap responsively             │
│                                                   │
│ 7. Meta chips wrapping on very small screens     │
│    • @media (max-width: 480px) adjustments       │
│                                                   │
│ 8. Add accessibility roles                       │
│    • role="list" on meta chips                   │
│    • aria-label on CTA row                       │
│    • Fix button onclick → proper event handler   │
└──────────────────────────────────────────────────┘
  ACCEPTANCE: Mobile/tablet optimal, WCAG compliant

PHASE 3: ENHANCEMENT (Visual polish & cleanup)
Duration: ~45 minutes
┌──────────────────────────────────────────────────┐
│ 9. Add page-specific visual hints                │
│    • Icons or diagram hints per page             │
│    • CSS ::before or SVG inline                  │
│                                                   │
│ 10. Remove legacy CSS                            │
│     • Delete lines 1106-1163 (old .hero-* rules) │
│     • Clean up unnecessary selectors             │
│                                                   │
│ 11. Full QA testing                              │
│     • Breakpoints: 375px, 768px, 1024px, 1440px │
│     • Browsers: Chrome, Safari, Firefox          │
│     • Print: PDF export validation               │
│     • Accessibility: WAVE audit                  │
└──────────────────────────────────────────────────┘
  ACCEPTANCE: Polished, maintainable, tested system

TOTAL TIME: ~3 hours
```

---

## Resource Map

### Documentation Generated

```
/commissions/complete/
├─ SPRINT_1_INVESTIGATION_SUMMARY.md
│  └─ High-level overview, status, next steps
│
├─ SPRINT_1_ASSESSMENT.md
│  └─ Detailed audit, issue breakdown, metrics
│
└─ SPRINT_1_REFINEMENT_GUIDE.md
   └─ Step-by-step implementation with code
```

### Key Files to Edit

```
docs/styles.css
├─ Lines 1174-1360: .page-hero system (MAINTAIN, ADD RESPONSIVE)
├─ Lines 1106-1163: Legacy .hero-* classes (DELETE after migration)
└─ Add @media queries for mobile breakpoints

docs/print.css
├─ Lines 7-30: .page-hero rules (REFINE padding, label visibility)
└─ Add page-break rules for print hierarchy

docs/site/[5 remaining pages].html
└─ Replace .hero-* sections with .page-hero markup (use template)
```

---

## Quality Metrics

```
Current State → Target State (Post-Sprint 1)

Component Coverage:
  1/6 pages ████░░░░░░░░░░░░░░  16.7% → 6/6 pages ██████████████████  100%

Responsive Coverage:
  Desktop only ████░░░░░░░░░░░░░  25% → All (mobile, tablet, desktop) ██████████  100%

Accessibility:
  Basic ARIA ███░░░░░░░░░░░░░░  30% → WCAG Compliant █████████░ 90%+

Technical Debt:
  High (150+ lines legacy CSS) → Low (clean component-only system)

Code Quality:
  B+ (strong foundation, incomplete) → A (polished, maintainable)
```

---

## Quick Reference: Per-Page Migration Values

```
library.html
  Label: "Reference"
  Chips: "Evidence", "Updated 2024", "High-Impact" (accent)
  Primary CTA: "Jump to Recent Studies" → #recent-high-impact-studies-post-2015

model.html
  Label: "Model"
  Chips: "Model", "Interactive", "7-min read" (accent)
  Primary CTA: "Jump to Core Schemas" → #core-schemas-baseline-spikes-sensitivity-tolerance

myths.html
  Label: "Myths & Canon"
  Chips: "Mythbusting", "Grounded in Canon", "5 Truths" (accent)
  Primary CTA: "Jump to Myth #1" → #myth-1-buddhism-says-life-is-suffering-so-its-a-pessimistic-philosophy

recovery.html
  Label: "Recovery Guide"
  Chips: "Recovery", "Baseline", "4-min read" (accent)
  Primary CTA: "Jump to Vicious Cycle" → #the-vicious-cycle-stress-sleep-and-dopamine-depletion

protocols.html
  Label: "Protocols"
  Chips: "Actionable", "Week-by-week", "Evidence-Based" (accent)
  Primary CTA: "Browse all protocols" → [anchor TBD]

See SPRINT_1_REFINEMENT_GUIDE.md Section 2 for full details
```

---

## Success Definition

Sprint 1 is **COMPLETE** when:

- ✅ All 6 pages use `.page-hero` component (not legacy `.hero-*`)
- ✅ Mobile responsive (tested at 375px, 768px, 1024px, 1440px)
- ✅ Navigation offset fixed (no content under nav)
- ✅ Print stylesheet refined (proper padding, label visibility)
- ✅ ARIA roles added (role="list" on meta, proper button pattern)
- ✅ Legacy CSS removed (clean codebase, no technical debt)
- ✅ Visual hints added (page-specific icons or diagram hints)
- ✅ Cross-browser tested (Chrome, Safari, Firefox)
- ✅ All pages visually consistent and professional

**Timeline:** ~3 hours focused implementation work

**Readiness for Sprint 2:** Once complete, ready for visual enhancements (icons, animations, layout polish)

---

## Next Action

👉 **Review the three generated documents:**
1. `SPRINT_1_INVESTIGATION_SUMMARY.md` — Overview & strategy
2. `SPRINT_1_ASSESSMENT.md` — Detailed findings & metrics
3. `SPRINT_1_REFINEMENT_GUIDE.md` — Step-by-step implementation guide

👉 **Begin Phase 1 refinements** using the code provided in the refinement guide

👉 **Refer to per-page migration values** (above) when updating remaining 5 pages
