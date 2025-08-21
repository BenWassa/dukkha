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


4. key notes/tldr at the start of each page besides index.html in the hero section

5. each myth - different style for "truth:."    <br>
   - Use a distinct font style (e.g., italic or bold) for "Truth:" to make it stand out
   - Consider using a different background color or border to visually separate the truth statements
- Add a subtle animation (e.g., fade-in) when the truth statements appear to draw attention

---

## Implementation Notes
- Progress indicators should be visually minimal and not distract from reading
- Playful prompts should be optional and only on attention.html
- Protocols dropdown should be consistent across all pages

## Next Steps
- Prototype progress indicator (donut/line)
- Add playful prompts to attention.html
- Update nav for protocols dropdown
