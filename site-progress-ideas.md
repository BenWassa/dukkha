# Site Progress & UX Ideas

## Issues Found & Fixed

### Missing Myths Content (FIXED ✅)
- **Issue:** myths.html had inconsistent titles ("Five Myths" vs "Seven Lies") and only showed 3 of 5 myths
- **Fixed:** 
  - Changed section title to "Five Common Myths About Dopamine & Desire" for consistency
  - Added Myth 4: "I can get addicted to dopamine itself – I need to do a 'dopamine detox'"
  - Added Myth 5: "Buddhism teaches that we should eliminate all pleasure and become emotionless monks"
  - Added proper footnotes and citations for new myths
  - Now shows complete set of 5 myths with consistent structure

### CSS File Organization (FIXED ✅)
- **Issue:** Single massive styles.css file (was ~40KB) was becoming unwieldy for maintenance
- **Fixed:** Split into modular CSS architecture:
  - `variables.css` (2.5KB) - Design tokens, CSS custom properties, color schemes
  - `styles.css` (32.3KB) - Main layout, components, page-specific styles  
  - `utilities.css` (3.6KB) - Utility classes, loading states, diagram helpers
  - `print.css` (1.2KB) - Print-optimized styles (loaded only for print media)
- **Benefits:** Better maintainability, selective loading, clearer separation of concerns
- **Implementation:** Updated all 12 HTML files with new CSS imports, maintained load order

### Truth Statement Styling Enhancement (FIXED ✅)  
- **Issue:** "Truth:" statements in myths.html needed better visual distinction
- **Fixed:** Added comprehensive styling with:
  - Green gradient background and left border for visual hierarchy
  - Checkmark icon (✓) and bold italic typography
  - Hover animations and fade-in effects
  - Dark mode support and responsive design
  - Professional appearance that reinforces correctness vs myths

---

## 1. Progress Indicator for Each Page
- **Concept:** Display a clean, minimal progress bar or donut on the right side of each page to show reading progress.
- **Design:**
  - Donut (circular) progress indicator that fills as the user scrolls
  - Alternatively, a thin vertical line/bar that fills up
  - Minimal, unobtrusive, matches site aesthetic
  - Could use CSS/JS for scroll tracking
- **Placement:**
  - Fixed to the right edge of the viewport
  - Only visible on desktop/tablet (hide on mobile for simplicity)

## 2. Playful Reading Prompts (Attention Page Only)
- **Concept:** Add a lighthearted, motivational message as the user reads through attention.html
- **Examples:**
  - "Keep reading... you're almost done!"
  - "Just one section left!"
  - "You made it!"
- **Trigger:**
  - Use scroll position to show/hide messages
  - Only enabled for attention.html

## 3. Protocols Nav Tab: Dropdown for Each Protocol
- **Concept:** In the main navigation, make the "Protocols" tab a dropdown listing each protocol
- **Design:**
  - On hover/click, show a dropdown menu with links to each protocol page
  - Clean, minimal styling (matches nav aesthetic)
  - Accessible (keyboard and screen reader friendly)
- **Implementation:**
  - Update nav HTML/CSS/JS
  - Dynamically generate protocol list if possible

## 4. Key Notes / TL;DR in Hero Section (All Pages Except Index)
- **Concept:** Display a concise summary or key notes at the top of each page (except index.html) within the hero section.
- **Design:**
    - Prominent placement in the hero area for quick reference
    - Clear, minimal styling to match site aesthetic
    - Bullet points or short sentences for easy scanning

## 5. Distinct Styling for "Truth:" in Myths Section
- **Concept:** Make "Truth:" statements visually stand out in each myth.
- **Design:**
    - Use a distinct font style (e.g., bold or italic) for "Truth:"
    - Apply a different background color or border to separate truth statements from the rest of the myth
    - Add a subtle animation (e.g., fade-in) when truth statements appear to draw attention
- **Implementation:**
    - Update myths HTML/CSS for new styles and animation
    - Ensure accessibility and consistency across all myths

---

## Implementation Notes
- Progress indicators should be visually minimal and not distract from reading
- Playful prompts should be optional and only on attention.html
- Protocols dropdown should be consistent across all pages

## Next Steps
- Prototype progress indicator (donut/line)
- Add playful prompts to attention.html
- Update nav for protocols dropdown
