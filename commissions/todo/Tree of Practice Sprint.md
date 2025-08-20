# Tree of Practice — Sprint Commission (LLM Implementation)

**Owner:** Project Dukkha
**Type:** Implementation Sprint (SVG + Index Integration)
**Audience:** Coding LLM (e.g., Codex), front-end collaborator
**Repo Context:** Static site under `docs/` with pages in `docs/site/` and assets in `docs/assets/`

---

## 0) Executive Brief

**Situation →** We need a large, stylized, *responsive* SVG “Tree of Practice” for the landing page that maps **Roots (deficits)** → **Trunk (protocols)** → **Branches (growth outcomes)** and deep-links into existing site pages.
**Key Insight →** Treat the tree as a single semantic SVG with three layers and data-driven node/link placement. Keep styling token-based for light/dark mode and brand cohesion.
**Decision Required →** Implement the SVG, wire interactions, and add anchor targets on destination pages.
**Impact →** Users instantly grasp the narrative path from pain → practice → growth, and can navigate to the appropriate protocol with one click.

---

## 1) Goals & Non-Goals

### Goals (In Scope)

* Render a **responsive** SVG Tree (roots, trunk, branches) on `docs/index.html`.
* Embed a data model (JSON) to map **7** root→protocol→branch pathways.
* Implement **hover highlights** and **click navigation** along entire pathways.
* Ensure **accessibility** (role/ARIA, keyboard focus, fallback outline) and **dark-mode** compatibility via CSS variables.
* Add **anchors** on destination pages (`docs/site/*.html`) so deep-links resolve cleanly.
* Provide a **single export** of the final art as `docs/images/diagrams/tree_of_practice.svg`.

### Non-Goals (Out of Scope)

* Rewriting protocol prose or research content.
* Creating a general icon system beyond this diagram.
* Building a site generator or altering research pipeline.

---

## 2) File Plan (Create/Modify)

```
docs/
  index.html                          # MODIFY: embed Tree section + data + script (or import)
  images/diagrams/tree_of_practice.svg# ADD: exported final SVG (also keep inline version in index for now)
  assets/
    tree_of_practice.js               # ADD: (optional) externalized JS, if splitting from index
site/
  attention.html                      # MODIFY: add anchors (see §7)
  recovery.html                       # MODIFY: add anchors
  model.html                          # MODIFY: add anchors
scripts/
  qa_check.ps1                        # (no change; use for anchor/URL checks)
```

> Keep all new code **idempotent** and **non-destructive**.

---

## 3) Design Tokens (inherit from site variables)

Extend the site CSS variables with the following (if not present). Reference these within the SVG; do **not** hardcode colors in shapes if tokens exist.

```css
:root {
  --tree-bg: var(--color-surface);               /* panel background */
  --tree-ink: var(--color-text-primary);         /* labels */
  --tree-mute: var(--color-text-secondary);
  --tree-root: #8a8f98;                          /* roots (deficits) neutral */
  --tree-trunk: #0f5132;                         /* deep green trunk */
  --tree-branch: #1d976c;                        /* branch fill (emerald) */
  --tree-accent: #c6a656;                        /* muted gold accent */
  --tree-stroke: #d0d5dc;
  --tree-hover: #e1b955;                         /* hover highlight (gold) */
  --tree-shadow: rgba(0,0,0,.12);
  --tree-font: var(--font-sans, "Inter", system-ui, sans-serif);
}
```

---

## 4) Information Model

Seven fixed pathways. Keys are **ids** used inside SVG node groups.

```jsonc
{
  "pairs": [
    { "root": "distracted",  "protocol": "focus-sprint",          "branch": "focused",     "href": "site/attention.html#focus-sprint" },
    { "root": "burned-out",  "protocol": "recovery-reset",        "branch": "energized",   "href": "site/recovery.html#recovery-reset" },
    { "root": "fatigued",    "protocol": "sleep-optimization",    "branch": "rested",      "href": "site/recovery.html#sleep-optimization" },
    { "root": "stressed",    "protocol": "stress-management",     "branch": "calm",        "href": "site/recovery.html#stress-management" },
    { "root": "addicted",    "protocol": "digital-detox",         "branch": "untethered",  "href": "site/attention.html#digital-detox" },
    { "root": "malnourished","protocol": "nutrition",             "branch": "nourished",   "href": "site/recovery.html#nutrition" },
    { "root": "reactive",    "protocol": "mindfulness-awareness", "branch": "lucid",       "href": "site/model.html#mindfulness-awareness" }
  ]
}
```

**Canonical labels (UI text):**

* Roots: *Distracted, Burned Out, Fatigued, Stressed, Addicted, Malnourished, Reactive*
* Protocols: *Focus Sprint, Recovery Reset, Sleep Optimization, Stress Management, Digital Detox, Nutrition & Supplementation, Mindfulness & Awareness*
* Branches: *Focused, Energized, Rested, Calm, Untethered, Nourished, Lucid*

---

## 5) Implementation Contract

### 5.1. Embed section on `docs/index.html`

Insert **one** `<section id="tree-of-practice">…</section>` block containing:

* Heading, subtitle
* **Inline SVG** with **four layers**: `#layer-roots`, `#layer-trunk`, `#layer-branches`, `#layer-links`
* `<script type="application/json" id="tree-data">` containing **canvas**, **layoutHints**, **nodes**, **paths**
* A minimal script to render pills, draw curves, and wire interactions
* `<noscript>` text outline fallback

> A ready-to-use scaffold is provided in **Appendix A**.

### 5.2. SVG structure (semantic layers)

* `#layer-roots` (bottom): root nodes + optional organic root shapes
* `#layer-trunk` (center): trunk path and **seven** protocol plaques
* `#layer-branches` (top): branch nodes + leaf/fruit clusters
* `#layer-links`: two curves per pathway (root→protocol, protocol→branch)

**Defs:** at minimum a trunk gradient and softDropShadow filter; extend as needed.

### 5.3. Layout

Use deterministic layout first (see `layoutHints`). LLM may **beautify** organically but must preserve **hit areas** and **legibility** on widths ≥ 360px.

* Canvas default: `viewBox="0 0 1440 1024"`
* Roots baseline: \~`y=900`; Branches band: \~`y=140`; Trunk: `x=720`, top ≈ 220 to bottom ≈ 820
* Spreads supplied in the JSON; **do not** hardcode positions elsewhere.

### 5.4. Node rendering

Use a reusable **pill** factory for each node type. Minimum spec:

* Rounded rect (rx≈18), label centered
* Respect `--tree-font`, `--tree-ink`
* Roles: `"root" | "protocol" | "branch"` influence fill
* Cursor=pointer when `data-href` is present
* Keyboard focus ring (via CSS/outline or an SVG focus path) on `tab`

### 5.5. Path drawing

* Two quadratic Bézier paths per mapping:

  * Root→Protocol (upward)
  * Protocol→Branch (upward)
* Stroke: `--tree-accent`, width: 3, opacity: 0.65 (tweakable)
* On **hover/focus** of any node in a path: **highlight entire pathway** (increase stroke width/opacity; optional glow)

### 5.6. Interactions

* **Click:** Navigate to `href` (on any node or path in that trio).
* **Hover:** Subtle brighten on node; highlight connected paths.
* **Keyboard:** `Tab` to node, `Enter`/`Space` activates link.
* **ARIA:** SVG `role="img"` with `<title>` + `<desc>`; nodes have `aria-label`.

### 5.7. Accessibility & Fallback

* High contrast: labels must pass WCAG AA against node fill in light/dark modes.
* Provide `<noscript>` with a text outline list of all seven pathways.
* Ensure focus order is logical (roots → trunk → branches, left→right).

### 5.8. Performance

* Avoid heavy filters on every element; use group-level shadows where possible.
* Defer non-critical stylization (e.g., bark textures) or bake into exported SVG.
* Keep DOM node count reasonable (< 400 elements target).

### 5.9. Export

* After inline version works, export a **flattened** `tree_of_practice.svg` into `docs/images/diagrams/` (keep interactivity inlined if feasible).
* Do **not** break links; inline CSS where necessary.

---

## 6) Acceptance Criteria (Definition of Done)

* [ ] **Visual:** Roots bottom, trunk centered with seven protocol plaques, branches top; balanced on desktop and mobile.
* [ ] **Data:** Exactly **7** pathways; ids/labels match §4.
* [ ] **Navigation:** Clicking any node or its connecting path opens target anchor.
* [ ] **Anchors:** Destination pages contain `<h3 id="…">` or equivalent at targets.
* [ ] **Accessibility:** SVG has `<title>` + `<desc>`; keyboard operable; focus visible; text fallback present.
* [ ] **Dark Mode:** Legible in both themes; tokens used; no hardcoded light-only colors.
* [ ] **Performance:** No layout thrash; interaction <16ms frame budget on hover.
* [ ] **Artifacts:** `docs/images/diagrams/tree_of_practice.svg` exported and loads.
* [ ] **QA:** `scripts/qa_check.ps1` passes (anchors/URLs), manual click-through verified.

---

## 7) Anchor Stubs to Add (Destination Pages)

Update these files under `docs/site/` with at least the following headings (placements can be near the relevant content).

```html
<!-- attention.html -->
<h3 id="focus-sprint">Focus Sprint</h3>
<h3 id="digital-detox">Digital Detox</h3>

<!-- recovery.html -->
<h3 id="recovery-reset">Recovery Reset</h3>
<h3 id="sleep-optimization">Sleep Optimization</h3>
<h3 id="stress-management">Stress Management</h3>
<h3 id="nutrition">Nutrition &amp; Supplementation</h3>

<!-- model.html -->
<h3 id="mindfulness-awareness">Mindfulness &amp; Awareness</h3>
```

---

## 8) QA & Test Plan

### Automated

* Run `pwsh scripts/qa_check.ps1` to verify anchor/id parity and (optionally) URL reachability.
* Add a quick HTML lint pass if available.

### Manual

* **Hover tests:** Entire path highlights when hovering any of its nodes.
* **Keyboard tests:** Tab through nodes left→right; focus ring visible; `Enter` activates.
* **Dark mode:** Switch OS/theme; verify label contrast and link visibility.
* **Mobile:** iOS/Android Chrome/Safari; tap targets usable; scroll/zoom stable.

---

## 9) Delivery & Handover

* Commit with message: `feat(tree): add Tree of Practice SVG, anchors, and interactivity`
* Attach both: `index.html` snippet (inline SVG) and exported `tree_of_practice.svg`
* Note any deviations from layout hints or tokens.

---

## 10) Stretch Enhancements (Optional, post-MVP)

* Organic root tendrils and branch leaf clusters (background shapes).
* Animated “sap flow” along the gold paths on hover/focus.
* Small “fruit” badges that pulse subtly on first load.
* `prefers-reduced-motion` media query to disable animation.

---

## Appendix A — Drop-in Section for `docs/index.html`

> Paste this inside `<body>` where the Tree should appear. It includes data + a minimal script.
> You may externalize the script to `docs/assets/tree_of_practice.js` after testing.

```html
<section id="tree-of-practice" class="mb-20 md:mb-32">
  <div class="text-center mb-6">
    <h2 class="text-3xl font-bold">Tree of Practice</h2>
    <p class="max-w-2xl mx-auto" style="color:var(--tree-mute)">
      Start in the <strong>Roots</strong> (deficits), climb the <strong>Trunk</strong> (protocols), and grow into the <strong>Branches</strong> (outcomes).
    </p>
  </div>

  <div class="rounded-xl border" style="background:var(--tree-bg); border-color:var(--tree-stroke); box-shadow:0 10px 30px var(--tree-shadow);">
    <svg id="treeSVG" viewBox="0 0 1440 1024" role="img" aria-labelledby="treeTitle treeDesc" style="width:100%; height:auto;">
      <title id="treeTitle">Tree of Practice — from deficits (roots) through protocols (trunk) to growth (branches)</title>
      <desc id="treeDesc">
        Seven pathways: Distracted→Focus Sprint→Focused; Burned Out→Recovery Reset→Energized; Fatigued→Sleep Optimization→Rested;
        Stressed→Stress Management→Calm; Addicted→Digital Detox→Untethered; Malnourished→Nutrition→Nourished; Reactive→Mindfulness & Awareness→Lucid.
      </desc>

      <defs>
        <linearGradient id="trunkGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#134e4a"/>
          <stop offset="100%" stop-color="#0f5132"/>
        </linearGradient>
        <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="rgba(0,0,0,.2)"/>
        </filter>
      </defs>

      <g id="layer-roots" data-layer="roots" font-family="var(--tree-font)" fill="var(--tree-root)"></g>
      <g id="layer-trunk" data-layer="trunk" fill="url(#trunkGrad)"></g>
      <g id="layer-branches" data-layer="branches" font-family="var(--tree-font)" fill="var(--tree-branch)"></g>
      <g id="layer-links" data-layer="links" fill="none" stroke="var(--tree-accent)" stroke-width="3" opacity="0.65"></g>
      <g id="focus-ring" visibility="hidden" stroke="var(--tree-hover)" stroke-width="4" fill="none"></g>
    </svg>
  </div>

  <script type="application/json" id="tree-data">
  {
    "canvas": { "w": 1440, "h": 1024, "padding": 64 },
    "layoutHints": {
      "rootsY": 900, "branchesY": 140,
      "trunkX": 720, "trunkTopY": 220, "trunkBottomY": 820,
      "rootSpread": [120, 310, 500, 690, 880, 1070, 1260],
      "branchSpread": [160, 360, 560, 720, 880, 1080, 1280]
    },
    "nodes": {
      "roots": [
        {"id":"root-distracted","label":"Distracted"},
        {"id":"root-burned-out","label":"Burned Out"},
        {"id":"root-fatigued","label":"Fatigued"},
        {"id":"root-stressed","label":"Stressed"},
        {"id":"root-addicted","label":"Addicted"},
        {"id":"root-malnourished","label":"Malnourished"},
        {"id":"root-reactive","label":"Reactive"}
      ],
      "protocols": [
        {"id":"proto-focus-sprint","label":"Focus Sprint"},
        {"id":"proto-recovery-reset","label":"Recovery Reset"},
        {"id":"proto-sleep-optimization","label":"Sleep Optimization"},
        {"id":"proto-stress-management","label":"Stress Management"},
        {"id":"proto-digital-detox","label":"Digital Detox"},
        {"id":"proto-nutrition","label":"Nutrition & Supplementation"},
        {"id":"proto-mindfulness-awareness","label":"Mindfulness & Awareness"}
      ],
      "branches": [
        {"id":"branch-focused","label":"Focused"},
        {"id":"branch-energized","label":"Energized"},
        {"id":"branch-rested","label":"Rested"},
        {"id":"branch-calm","label":"Calm"},
        {"id":"branch-untethered","label":"Untethered"},
        {"id":"branch-nourished","label":"Nourished"},
        {"id":"branch-lucid","label":"Lucid"}
      ]
    },
    "paths": [
      {"root":"root-distracted","protocol":"proto-focus-sprint","branch":"branch-focused","href":"site/attention.html#focus-sprint"},
      {"root":"root-burned-out","protocol":"proto-recovery-reset","branch":"branch-energized","href":"site/recovery.html#recovery-reset"},
      {"root":"root-fatigued","protocol":"proto-sleep-optimization","branch":"branch-rested","href":"site/recovery.html#sleep-optimization"},
      {"root":"root-stressed","protocol":"proto-stress-management","branch":"branch-calm","href":"site/recovery.html#stress-management"},
      {"root":"root-addicted","protocol":"proto-digital-detox","branch":"branch-untethered","href":"site/attention.html#digital-detox"},
      {"root":"root-malnourished","protocol":"proto-nutrition","branch":"branch-nourished","href":"site/recovery.html#nutrition"},
      {"root":"root-reactive","protocol":"proto-mindfulness-awareness","branch":"branch-lucid","href":"site/model.html#mindfulness-awareness"}
    ]
  }
  </script>

  <script>
    (function(){
      const svgNS = 'http://www.w3.org/2000/svg';
      const svg = document.getElementById('treeSVG');
      const data = JSON.parse(document.getElementById('tree-data').textContent);
      const gRoots = svg.getElementById('layer-roots');
      const gBranches = svg.getElementById('layer-branches');
      const gTrunk = svg.getElementById('layer-trunk');
      const gLinks = svg.getElementById('layer-links');

      function pill(group, id, x, y, text, role, href){
        const g = document.createElementNS(svgNS,'g');
        g.setAttribute('id', id);
        g.setAttribute('data-role', role);
        if (href) g.setAttribute('data-href', href);
        g.setAttribute('tabindex', '0');
        g.setAttribute('role', 'link');
        g.setAttribute('aria-label', text + (href ? ' (opens section)' : ''));
        const padX = 22, h = 40, rx = 18;
        const approxW = Math.max(120, text.length * 8 + padX*2);

        const rect = document.createElementNS(svgNS,'rect');
        rect.setAttribute('x', x - approxW/2);
        rect.setAttribute('y', y - h/2);
        rect.setAttribute('width', approxW);
        rect.setAttribute('height', h);
        rect.setAttribute('rx', rx);
        rect.setAttribute('ry', rx);
        rect.setAttribute('filter','url(#softShadow)');
        rect.style.fill = role==='root' ? 'var(--tree-root)' : role==='branch' ? 'var(--tree-branch)' : '#ffffff';
        rect.style.stroke = 'var(--tree-stroke)';
        rect.style.strokeWidth = '1.5';

        const label = document.createElementNS(svgNS,'text');
        label.setAttribute('x', x);
        label.setAttribute('y', y + 2);
        label.setAttribute('text-anchor','middle');
        label.setAttribute('dominant-baseline','middle');
        label.style.fontSize = '16px';
        label.style.fill = 'var(--tree-ink)';
        label.textContent = text;

        g.appendChild(rect);
        g.appendChild(label);

        const activate = () => {
          const url = g.getAttribute('data-href');
          if (url) window.location.href = url;
        };
        g.addEventListener('click', activate);
        g.addEventListener('keypress', (e) => { if (e.key==='Enter' || e.key===' ') activate(); });
        g.addEventListener('mouseenter', () => g.style.filter = 'brightness(1.05)');
        g.addEventListener('mouseleave', () => g.style.filter = 'none');

        group.appendChild(g);
        return g;
      }

      // Roots
      data.nodes.roots.forEach((n, i) => {
        pill(gRoots, n.id, data.layoutHints.rootSpread[i], data.layoutHints.rootsY, n.label, 'root');
      });

      // Branches
      data.nodes.branches.forEach((n, i) => {
        pill(gBranches, n.id, data.layoutHints.branchSpread[i], data.layoutHints.branchesY, n.label, 'branch');
      });

      // Trunk plaques (protocols)
      const trunkTop = data.layoutHints.trunkTopY, trunkBottom = data.layoutHints.trunkBottomY, trunkX = data.layoutHints.trunkX;
      const step = (trunkBottom - trunkTop) / (data.nodes.protocols.length + 1);
      data.nodes.protocols.forEach((p, i) => {
        pill(gTrunk, p.id, trunkX, trunkTop + step*(i+1), p.label, 'protocol');
      });

      function pathBetween(x1,y1,x2,y2, viaX){
        const qx = viaX ?? ((x1 + x2)/2);
        const qy = (y1 + y2)/2;
        return `M ${x1},${y1} Q ${qx},${qy} ${x2},${y2}`;
      }

      // Links + pathway hover
      data.paths.forEach((p) => {
        const r = svg.getElementById(p.root);
        const pr = svg.getElementById(p.protocol);
        const b = svg.getElementById(p.branch);
        if (!r || !pr || !b) return;

        const rb = r.getBBox(), pb = pr.getBBox(), bb = b.getBBox();

        const l1 = document.createElementNS(svgNS,'path');
        l1.setAttribute('d', pathBetween(rb.x + rb.width/2, rb.y, pb.x + pb.width/2, pb.y + pb.height, pb.x + pb.width/2));
        l1.setAttribute('data-path', `${p.root}->${p.protocol}`);

        const l2 = document.createElementNS(svgNS,'path');
        l2.setAttribute('d', pathBetween(pb.x + pb.width/2, pb.y, bb.x + bb.width/2, bb.y + bb.height, pb.x + pb.width/2));
        l2.setAttribute('data-path', `${p.protocol}->${p.branch}`);

        [l1,l2].forEach(el => {
          el.style.pointerEvents = 'stroke';
          el.addEventListener('click', () => window.location.href = p.href);
        });

        const highlight = (on) => {
          [l1,l2].forEach(el => { el.style.strokeWidth = on? '5' : '3'; el.style.opacity = on? '0.95' : '0.65'; });
        };

        [r, pr, b].forEach(el => {
          el.addEventListener('mouseenter', () => highlight(true));
          el.addEventListener('mouseleave', () => highlight(false));
          el.addEventListener('focus', () => highlight(true));
          el.addEventListener('blur', () => highlight(false));
          el.addEventListener('click', () => window.location.href = p.href);
        });

        gLinks.appendChild(l1);
        gLinks.appendChild(l2);
      });
    })();
  </script>

  <noscript>
    <ul>
      <li>Distracted → Focus Sprint → Focused</li>
      <li>Burned Out → Recovery Reset → Energized</li>
      <li>Fatigued → Sleep Optimization → Rested</li>
      <li>Stressed → Stress Management → Calm</li>
      <li>Addicted → Digital Detox → Untethered</li>
      <li>Malnourished → Nutrition → Nourished</li>
      <li>Reactive → Mindfulness & Awareness → Lucid</li>
    </ul>
  </noscript>
</section>
```
