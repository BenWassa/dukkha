# Tree of Practice — **Sprint A (MVP) Commission**

**Owner:** Project Dukkha
**Type:** Implementation Sprint (SVG + Index Integration)
**Audience:** Coding LLM (e.g., Codex), front-end collaborator
**Repo:** `docs/` static site; pages in `docs/site/`

---

## 0) Executive Brief

**Situation →** We need a working “Tree of Practice” on the landing page that maps Roots → Protocols → Branches and deep-links into existing pages.
**Key Insight →** Ship a deterministic, accessible MVP first; defer all artistry/animation to a follow-up sprint.
**Decision Required →** Implement the minimal interactive SVG + anchors now.
**Impact →** Clickable, comprehensible user journey with clean links and a11y; zero visual bikeshedding.

---

## 1) Scope (Sprint A = MVP)

### Goals (in scope)

* Render a **responsive** SVG tree on `docs/index.html`.
* Show **7** root→protocol→branch pathways (pills + connecting curves).
* **Hover/focus** highlights entire pathway; **click/tap** navigates to target anchor.
* **A11y**: keyboard nav, visible focus, `<title>/<desc>`, text fallback.
* **Dark-mode** via CSS variables (no hardcoded colors).
* Add **anchors** on `docs/site/*.html` so deep-links resolve.

### Non-Goals (explicitly out of scope → Sprint B)

* Organic bark/roots/leaf art, textures, filters, gradients beyond basics.
* Animations (glow/flow), `prefers-reduced-motion` logic.
* Advanced performance polish beyond “works smoothly”.

---

## 2) Deliverables

* `docs/index.html`: one `<section id="tree-of-practice">` containing inline SVG, JSON data, minimal JS, and `<noscript>` fallback.
* `docs/site/attention.html`, `docs/site/recovery.html`, `docs/site/model.html`: anchor stubs (see §6).
* (Optional) `docs/assets/tree_of_practice.js`: if you externalize the inline script.

---

## 3) Design Tokens (use site vars; no hardcoded colors)

```css
:root{
  --tree-bg: var(--color-surface);
  --tree-ink: var(--color-text-primary);
  --tree-mute: var(--color-text-secondary);
  --tree-root:#8a8f98;       /* roots */
  --tree-branch:#1d976c;     /* branches */
  --tree-accent:#c6a656;     /* link paths */
  --tree-stroke:#d0d5dc;
  --tree-shadow:rgba(0,0,0,.12);
  --tree-font:var(--font-sans,"Inter",system-ui,sans-serif);
}
```

---

## 4) Data Model (authoritative IDs/labels/links)

```json
{
  "pairs": [
    { "root": "distracted",   "protocol": "focus-sprint",          "branch": "focused",    "href": "site/attention.html#focus-sprint" },
    { "root": "burned-out",   "protocol": "recovery-reset",        "branch": "energized",  "href": "site/recovery.html#recovery-reset" },
    { "root": "fatigued",     "protocol": "sleep-optimization",    "branch": "rested",     "href": "site/recovery.html#sleep-optimization" },
    { "root": "stressed",     "protocol": "stress-management",     "branch": "calm",       "href": "site/recovery.html#stress-management" },
    { "root": "addicted",     "protocol": "digital-detox",         "branch": "untethered", "href": "site/attention.html#digital-detox" },
    { "root": "malnourished", "protocol": "nutrition",             "branch": "nourished",  "href": "site/recovery.html#nutrition" },
    { "root": "reactive",     "protocol": "mindfulness-awareness", "branch": "lucid",      "href": "site/model.html#mindfulness-awareness" }
  ],
  "labels": {
    "roots": ["Distracted","Burned Out","Fatigued","Stressed","Addicted","Malnourished","Reactive"],
    "protocols": ["Focus Sprint","Recovery Reset","Sleep Optimization","Stress Management","Digital Detox","Nutrition & Supplementation","Mindfulness & Awareness"],
    "branches": ["Focused","Energized","Rested","Calm","Untethered","Nourished","Lucid"]
  }
}
```

---

## 5) Acceptance Criteria (Definition of Done)

* [ ] **Visual:** Roots at bottom, trunk center (7 protocol plaques), branches at top; legible desktop & mobile.
* [ ] **Data:** Exactly 7 pathways wired; IDs/labels match §4.
* [ ] **Nav:** Click/tap on any node **or** its connecting path opens the target anchor.
* [ ] **Anchors:** Required IDs present on destination pages (§6).
* [ ] **A11y:** SVG has `<title>` + `<desc>`; nodes tabbable; `Enter/Space` activates; visible focus; `<noscript>` text outline.
* [ ] **Dark Mode:** Text passes AA contrast against node fills; only tokens used.
* [ ] **Perf:** Hover/interaction smooth on mobile (no heavy filters per element).

---

## 6) Anchor Stubs (add to destination pages)

```html
<!-- docs/site/attention.html -->
<h3 id="focus-sprint">Focus Sprint</h3>
<h3 id="digital-detox">Digital Detox</h3>

<!-- docs/site/recovery.html -->
<h3 id="recovery-reset">Recovery Reset</h3>
<h3 id="sleep-optimization">Sleep Optimization</h3>
<h3 id="stress-management">Stress Management</h3>
<h3 id="nutrition">Nutrition &amp; Supplementation</h3>

<!-- docs/site/model.html -->
<h3 id="mindfulness-awareness">Mindfulness &amp; Awareness</h3>
```

---

## 7) QA Plan

**Automated (optional):** run any HTML linter + a simple anchor check script.
**Manual:**

* Hover any node → entire pathway highlights; click goes to correct anchor.
* `Tab` through nodes; focus visible; `Enter/Space` activates link.
* Test light/dark modes; verify contrast.
* Mobile Safari/Chrome: tap targets ≥ 40px, no accidental zoom/scroll jumps.

---

## 8) Appendix A — Minimal Drop-in Section (`docs/index.html`)

> Deterministic layout; no fancy filters/gradients; small, readable script.
> You may externalize the JS to `docs/assets/tree_of_practice.js`.

```html
<section id="tree-of-practice" class="mb-20 md:mb-32">
  <div class="text-center mb-6">
    <h2 class="text-3xl font-bold">Tree of Practice</h2>
    <p class="max-w-2xl mx-auto" style="color:var(--tree-mute)">
      Start in the <strong>Roots</strong> (deficits), climb the <strong>Trunk</strong> (protocols), and grow into the <strong>Branches</strong> (outcomes).
    </p>
  </div>

  <div class="rounded-xl border" style="background:var(--tree-bg); border-color:var(--tree-stroke); box-shadow:0 10px 30px var(--tree-shadow);">
    <svg id="treeSVG" viewBox="0 0 1440 1024" role="img" aria-labelledby="treeTitle treeDesc" style="width:100%;height:auto;">
      <title id="treeTitle">Tree of Practice — roots → protocols → branches</title>
      <desc id="treeDesc">Seven pathways: Distracted→Focus Sprint→Focused; Burned Out→Recovery Reset→Energized; Fatigued→Sleep Optimization→Rested; Stressed→Stress Management→Calm; Addicted→Digital Detox→Untethered; Malnourished→Nutrition→Nourished; Reactive→Mindfulness & Awareness→Lucid.</desc>

      <g id="layer-roots"    data-layer="roots"    font-family="var(--tree-font)"></g>
      <g id="layer-trunk"    data-layer="trunk"    font-family="var(--tree-font)"></g>
      <g id="layer-branches" data-layer="branches" font-family="var(--tree-font)"></g>
      <g id="layer-links"    data-layer="links"    fill="none" stroke="var(--tree-accent)" stroke-width="3" opacity="0.7"></g>
    </svg>
  </div>

  <!-- Data -->
  <script type="application/json" id="tree-data">
  {
    "canvas": { "w": 1440, "h": 1024, "padding": 64 },
    "layoutHints": {
      "rootsY": 900, "branchesY": 140,
      "trunkX": 720, "trunkTopY": 240, "trunkBottomY": 800,
      "rootSpread":   [120, 310, 500, 690, 880, 1070, 1260],
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

  <!-- Minimal script -->
  <script>
    (function(){
      const NS='http://www.w3.org/2000/svg';
      const svg=document.getElementById('treeSVG');
      const data=JSON.parse(document.getElementById('tree-data').textContent);
      const gR=svg.getElementById('layer-roots'), gT=svg.getElementById('layer-trunk'), gB=svg.getElementById('layer-branches'), gL=svg.getElementById('layer-links');

      function pill(parent,id,x,y,text,role,href){
        const g=document.createElementNS(NS,'g');
        g.setAttribute('id',id); g.setAttribute('tabindex','0'); g.setAttribute('role','link');
        if(href) g.dataset.href=href;
        const w=Math.max(120,text.length*8+44), h=40, rx=18;

        const rect=document.createElementNS(NS,'rect');
        rect.setAttribute('x',x-w/2); rect.setAttribute('y',y-h/2); rect.setAttribute('width',w); rect.setAttribute('height',h);
        rect.setAttribute('rx',rx); rect.setAttribute('ry',rx);
        rect.style.fill = role==='root' ? 'var(--tree-root)' : role==='branch' ? 'var(--tree-branch)' : '#fff';
        rect.style.stroke='var(--tree-stroke)'; rect.style.strokeWidth='1.5';

        const label=document.createElementNS(NS,'text');
        label.setAttribute('x',x); label.setAttribute('y',y+2);
        label.setAttribute('text-anchor','middle'); label.setAttribute('dominant-baseline','middle');
        label.style.fontFamily='var(--tree-font)'; label.style.fontSize='16px'; label.style.fill='var(--tree-ink)';
        label.textContent=text;

        g.append(rect,label);
        g.addEventListener('click',()=>{ if(g.dataset.href) location.href=g.dataset.href; });
        g.addEventListener('keypress',(e)=>{ if(e.key==='Enter'||e.key===' ') { e.preventDefault(); if(g.dataset.href) location.href=g.dataset.href; } });
        parent.appendChild(g);
        return g;
      }

      // Layout: roots bottom, branches top, trunk center plaques
      data.nodes.roots.forEach((n,i)=> pill(gR,n.id, data.layoutHints.rootSpread[i],   data.layoutHints.rootsY,    n.label,'root'));
      const top=data.layoutHints.trunkTopY, bot=data.layoutHints.trunkBottomY, cx=data.layoutHints.trunkX;
      const step=(bot-top)/(data.nodes.protocols.length+1);
      data.nodes.protocols.forEach((p,i)=> pill(gT,p.id, cx, top+step*(i+1), p.label,'protocol'));
      data.nodes.branches.forEach((n,i)=> pill(gB,n.id, data.layoutHints.branchSpread[i], data.layoutHints.branchesY, n.label,'branch'));

      function q(x1,y1,x2,y2){ return `M ${x1},${y1} Q ${(x1+x2)/2},${(y1+y2)/2} ${x2},${y2}`; }
      data.paths.forEach((p)=>{
        const r=svg.getElementById(p.root), pr=svg.getElementById(p.protocol), b=svg.getElementById(p.branch);
        if(!r||!pr||!b) return;
        const rb=r.getBBox(), pb=pr.getBBox(), bb=b.getBBox();
        const l1=document.createElementNS(NS,'path'); l1.setAttribute('d', q(rb.x+rb.width/2, rb.y, pb.x+pb.width/2, pb.y+pb.height));
        const l2=document.createElementNS(NS,'path'); l2.setAttribute('d', q(pb.x+pb.width/2, pb.y, bb.x+bb.width/2, bb.y+bb.height));
        [l1,l2].forEach(el=>{ el.style.pointerEvents='stroke'; el.addEventListener('click',()=>location.href=p.href); gL.appendChild(el); });
        const on=(on)=>{ [l1,l2].forEach(el=>{ el.style.strokeWidth=on?'5':'3'; el.style.opacity=on?'1':'0.7'; }); };
        [r,pr,b].forEach(el=>{ el.addEventListener('mouseenter',()=>on(true)); el.addEventListener('mouseleave',()=>on(false)); el.addEventListener('focus',()=>on(true)); el.addEventListener('blur',()=>on(false)); });
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

---

## 9) Sprint B (Deferred Enhancements)

Organic tree art (roots/branches), textures/gradients, animated path glow, `prefers-reduced-motion`, contrast/focus polish, mobile hit-target tuning, grouped filter perf.
