---
title: Research
status: draft
---

<!-- A custom research landing page: hero, mission, and quick links. -->

---
title: Research
status: draft
---

<style>
	.research-hero { display:flex; gap:2rem; align-items:center; margin:2rem 0; }
	.research-hero .left { flex:1 }
	.research-hero .right { flex:1; text-align:center }
	.claim-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:1rem; margin-top:1.5rem }
	.claim-card { border:1px solid #ddd; padding:1rem; border-radius:8px; background:#fff; color:inherit; text-decoration:none }
	.claim-card h4 { margin:0 0 .5rem 0 }
	.claim-card p { margin:0 }
	@media (max-width:700px){ .research-hero{flex-direction:column} }
</style>

<div class="research-hero">
	<div class="left">
		<h1>Research — Project Dukkha</h1>
		<p style="font-size:1.05rem;margin-top:.25rem">Field guide research runs and claim fragments that anchor the manifesto and model to empirical sources.</p>
		<p>Goal: make evidence and claims discoverable and attributable so readers can inspect the link between theory (wanting, liking, learning) and primary sources.</p>
		<p style="margin-top:1rem"><a class="md-button md-button--primary" href="R1.md">Open R1 — Wanting (initial)</a></p>
	</div>
	<div class="right">
		<img src="/assets/figures/atlas-wll.svg" alt="Atlas" style="max-width:320px;width:100%"/>
	</div>
</div>

<h3>Quick claims (R1)</h3>
<p>R1 collects the first run of nine claims; click any card to open the R1 summary and per-claim anchors.</p>

<div class="claim-grid">
	<a class="claim-card" href="R1.md#R1-C01"><div><h4>R1-C01 — Incentive salience</h4><p>Wanting can drive approach without hedonic pleasure.</p></div></a>
	<a class="claim-card" href="R1.md#R1-C02"><div><h4>R1-C02 — Reward prediction error</h4><p>Dopamine signals a prediction error that teaches approach behaviour.</p></div></a>
	<a class="claim-card" href="R1.md#R1-C03"><div><h4>R1-C03 — Hedonic hotspots</h4><p>Specific sites amplify pleasure separate from wanting.</p></div></a>
	<a class="claim-card" href="R1.md#R1-C04"><div><h4>R1-C04 — Incentive sensitization</h4><p>Repeated cue exposure increases cue 'wanting'.</p></div></a>
	<a class="claim-card" href="R1.md#R1-C05"><div><h4>R1-C05 — Dissociation evidence</h4><p>Lesion and pharmacology studies dissociate liking vs wanting.</p></div></a>
	<a class="claim-card" href="R1.md#R1-C06"><div><h4>R1-C06 — Phasic vs tonic dopamine</h4><p>Different timescales map to learning vs motivation.</p></div></a>
	<a class="claim-card" href="R1.md#R1-C07"><div><h4>R1-C07 — Context sensitivity</h4><p>Environment and cues modulate incentive salience.</p></div></a>
	<a class="claim-card" href="R1.md#R1-C08"><div><h4>R1-C08 — Computational models</h4><p>RPE in reinforcement learning captures many empirical patterns.</p></div></a>
	<a class="claim-card" href="R1.md#R1-C09"><div><h4>R1-C09 — Practical implications</h4><p>Design patterns exploit RPE and salience; mitigation is possible.</p></div></a>
</div>

<hr/>
<p>If you want a completely custom HTML page outside the MkDocs template (full control of CSS/JS), I can add a standalone `research.html` in the repo root or `site/` and wire navigation directly to it — say the word and I’ll scaffold that.</p>

<!-- end custom research landing -->
