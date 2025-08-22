# Diagram Notes

This document contains visual specifications for the site diagrams used across the Project Dukkha pages.

## The Ping/Scroll Loop (attention.html)

**Visual vision**

To represent the relentless, self-reinforcing cycle of digital distraction. A sleek, minimalist cyclical flowchart that feels clean, modern, slightly abstract, and immediately intuitive. The loop should feel almost inescapable, with clear "intervention" off-ramps.

**Key visual elements**

- Nodes: Five to six rounded-rectangle nodes arranged in a circular/oval loop.
- Loop flow: Smooth, graceful curved arrows connecting nodes. Use `var(--color-text-secondary)` for general flow. The arrow leading into the "Anticipation & Craving" node may use `var(--color-accent)` to emphasize reward.
- Highlight node: "Anticipation & Craving (Dopamine Spike)" should be prominent — filled with `var(--color-accent)` and text in `var(--color-background)` for strong contrast.
- Intervention points: Smaller rounded rectangles (or pills) outside the main loop, connected by dashed lines using `var(--color-text-muted)` to indicate off-ramps.
- Typography: Use `var(--font-sans)`; node text 14–16px, labels ~12px.
- Overall coloring: Place on `var(--color-background)`; nodes in `var(--color-surface-elevated)` with thin `var(--color-border)` strokes.

## Dopamine Baseline vs. Spike (recovery.html, model.html)

**Visual vision**

A precise, minimalist line graph that shows baseline dopamine, a sharp spike in response to reward, the compensatory dip below baseline, and gradual return. The graph should feel authoritative and uncluttered.

**Key visual elements**

- Axes: Clean X-axis (Time) and Y-axis (Dopamine Level (Relative)). Thin, subtle lines using `var(--color-text-muted)` with arrowheads at the ends.
- Baseline: Horizontal dashed line labeled "Baseline" using `var(--color-text-muted)`.
- Dopamine curve: A single smooth Bezier curve that:
  - starts at baseline
  - quickly rises to a sharp spike
  - falls below baseline into a trough
  - slowly returns toward baseline
  Use `var(--color-accent)` for the curve and its label "Dopamine Level".
- Typography: Labels use `var(--font-sans)`; axes 10–12px, curve label slightly larger.
- Overall coloring: Render inside a framed box with `var(--color-surface-elevated)` background and a `var(--color-border)` frame.

## Stress-Sensitization Loop (with Exit Points) (recovery.html)

**Visual vision**

Illustrate how stress drives maladaptive coping that depletes resources and amplifies stress, forming a downward/spiral loop. Clearly show intervention "exit points" that break the pattern—professional, insightful, and hopeful.

**Key visual elements**

- Main loop nodes: Rounded rectangles for stages (e.g., "Stress / Anxiety", "Attention on Quick Rewards", "Impulse / Reward-Seeking", "Brief Relief", "Baseline Drops", "More Stress"). Arrange in an elongated vertical loop if helpful.
- Loop flow: Solid, smooth curved arrows using `var(--color-text-secondary)`. Highlight the "Brief Relief (Dopamine Spike)" node with `var(--color-accent)` fill and `var(--color-background)` text.
- Exit points: Oval/pill-shaped nodes outside the main loop connected with dashed lines (`var(--color-text-muted)`) to show interruption (e.g., "Exit: Breathwork", "Exit: Exercise").
- Labels: Clear node and intervention labels; use `var(--font-sans)`.
- Overall coloring: Nodes in `var(--color-surface-elevated)` with `var(--color-border)` strokes. Exit nodes can use `var(--color-surface)` + `var(--color-border)` with `var(--color-text-primary)` text.

## The Reward Compass (model.html)

**Visual vision**

A 2×2 quadrant model (compass) that maps reward system states and guides users toward an "optimal" zone.

**Key visual elements**

- Axes: Two intersecting lines forming four quadrants. X-axis: "Spike vs. Sensitivity" (Desensitized/High Spikes ↔ Highly Sensitive/Low Spikes). Y-axis: "Dopamine Baseline Level" (Low ↔ High). Use `var(--color-text-muted)` for axis lines.
- Quadrant zones: Distinct subtle background fills (alternating `var(--color-surface)` and `var(--color-surface-elevated)` with opacity) for visual layering.
- Quadrant labels: Examples — "Low Drive / Anhedonia", "Compulsive Seeking / Burnout", "Optimal Flow / Contentment", "High Spikes / Low Sensitivity". Use `var(--color-text-muted)`.
- Optimal zone highlight: Emphasize "Optimal Flow / Contentment" with a subtle border or icon using `var(--color-accent)`.
- Central motif: Small compass-like circle with crosshairs at the axes intersection, using `var(--color-accent)` and `var(--color-background)`.
- Typography: All labels use `var(--font-sans)`.
- Overall coloring: Neutral palette with `var(--color-accent)` used sparingly to highlight the optimal state.