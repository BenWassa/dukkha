R5 — Ethics & Persuasive Design Guardrails (locked specs)


```yaml

\# claims.yaml

\- id: R5-C01

&nbsp; text: "Infinite scrolling feeds and autoplay mechanisms exploit users’ propensity for endless consumption, significantly increasing time-on-platform through continuous, variable rewards:contentReference\[oaicite:0]{index=0}. \*\*Guardrail:\*\* Introduce natural stopping points (e.g. “Are you still there?” prompts or pagination) to restore user control without entirely sacrificing convenience."

&nbsp; importance: High

&nbsp; strength: High

&nbsp; scope: human

&nbsp; caveats: "May reduce user engagement metrics; individual differences in self-control."

&nbsp; evidence\_cites: \["culp2023"]

&nbsp; contradictions: \[]



\- id: R5-C02

&nbsp; text: "Short-form video reels (e.g. TikTok) induce flow states – marked by heightened concentration and time distortion – that fuel compulsive usage, especially in younger users:contentReference\[oaicite:1]{index=1}. \*\*Guardrail:\*\* Implement “breaks” or gentle interruptions (e.g. reminder screens after prolonged viewing) and encourage mindful use by allowing users to set time limits."

&nbsp; importance: High

&nbsp; strength: High

&nbsp; scope: human

&nbsp; caveats: "User bypass of breaks; potential decreased engagement."

&nbsp; evidence\_cites: \["qin2022"]

&nbsp; contradictions: \[]



\- id: R5-C03

&nbsp; text: "Frequent or gamified notifications and unpredictable reward cues (likes, badges) exploit the brain’s reward pathways, prompting habitual app-checking akin to a slot machine effect:contentReference\[oaicite:2]{index=2}. \*\*Guardrail:\*\* Ensure notification hygiene – default to minimal, batched notifications, and empower users with granular control over alerts."

&nbsp; importance: High

&nbsp; strength: Medium

&nbsp; scope: human

&nbsp; caveats: "Overzealous filtering could cause users to miss important alerts; user habituation to reduced notifications varies."

&nbsp; evidence\_cites: \["culp2023"]

&nbsp; contradictions: \[]



\- id: R5-C04

&nbsp; text: "Personalized recommendation feeds can leverage user data to maximize engagement, sometimes by exploiting cognitive biases or reinforcing filter bubbles:contentReference\[oaicite:3]{index=3}. \*\*Guardrail:\*\* Provide transparency (“Why am I seeing this?” explanations) and user agency (content filters or the ability to reset/tune the algorithm) to preserve informed choice and diversity of content."

&nbsp; importance: High

&nbsp; strength: Medium

&nbsp; scope: human

&nbsp; caveats: "Trade-off with recommendation efficiency; some users may find explanations confusing."

&nbsp; evidence\_cites: \["ftc2022"]

&nbsp; contradictions: \[]



\- id: R5-C05

&nbsp; text: "E-commerce interfaces commonly use \*\*urgency and sneaking\*\* dark patterns – e.g. countdown timers, low-stock warnings, hidden extra fees – which can pressure users into purchases:contentReference\[oaicite:4]{index=4}:contentReference\[oaicite:5]{index=5}. \*\*Guardrail:\*\* Mandate honest disclosures (no fake scarcity), clear pricing upfront, and require explicit user consent for add-ons (no pre-ticked upsells). Such practices align with emerging regulations against deceptive design."

&nbsp; importance: High

&nbsp; strength: High

&nbsp; scope: human

&nbsp; caveats: "May reduce short-term conversion rates; enforcement requires continuous monitoring."

&nbsp; evidence\_cites: \["brignull2013", "mathur2019"]

&nbsp; contradictions: \[]



\- id: R5-C06

&nbsp; text: "\*\*Obstruction patterns\*\* like “roach motels” (easy sign-up, hard cancellation) and forced continuity trap users in subscriptions:contentReference\[oaicite:6]{index=6}. These sludges impede autonomy and have triggered regulatory action (e.g. laws mandating simple online cancellations):contentReference\[oaicite:7]{index=7}:contentReference\[oaicite:8]{index=8}. \*\*Guardrail:\*\* Ensure symmetry in user flows – cancellation or opt-out should be as straightforward as sign-up – and add friction only to confirm truly high-risk actions (not to discourage legitimate exits)."

&nbsp; importance: High

&nbsp; strength: High

&nbsp; scope: human

&nbsp; caveats: "Businesses fear increased churn; what constitutes 'high-risk' must be defined (e.g. permanently deleting data vs. canceling a trial)."

&nbsp; evidence\_cites: \["ftc2022", "gray2023"]

&nbsp; contradictions: \[]



\- id: R5-C07

&nbsp; text: "Default settings exert outsized influence on user behavior:contentReference\[oaicite:9]{index=9}. Pre-selected choices that benefit the provider (e.g. opt-out data sharing or add-on services) exploit inertia and have been deemed unlawful in contexts like consent (EU’s Planet49 ruling):contentReference\[oaicite:10]{index=10}. \*\*Guardrail:\*\* Use \*\*benign defaults\*\* that favor user privacy and well-being (opt-in for optional features), and obtain active consent for any deviation."

&nbsp; importance: High

&nbsp; strength: High

&nbsp; scope: human

&nbsp; caveats: "May reduce uptake of certain features if not pre-enabled; requires education so users understand benefits of opt-in features."

&nbsp; evidence\_cites: \["cma2022", "lupianez2022"]

&nbsp; contradictions: \[]



\- id: R5-C08

&nbsp; text: "Dark patterns are pervasive and demonstrably effective at manipulating users. A large-scale audit found ~11% of shopping sites deploy them:contentReference\[oaicite:11]{index=11}, and an EU study reported 97% of popular apps/websites contain at least one deceptive interface element:contentReference\[oaicite:12]{index=12}. Even mild dark patterns can double user compliance with unwanted offers:contentReference\[oaicite:13]{index=13}. \*\*Guardrail:\*\* Given this scope of harm, design teams should treat \*\*compliance as a floor\*\* and proactively implement “fair pattern” alternatives, emphasizing user empowerment over exploitative gains."

&nbsp; importance: High

&nbsp; strength: High

&nbsp; scope: human

&nbsp; caveats: "Causality can be context-dependent; some dark pattern effects might diminish as users become aware of them."

&nbsp; evidence\_cites: \["mathur2019", "luguri2021", "lupianez2022", "ftc2022"]

&nbsp; contradictions: \[]



\- id: R5-C09

&nbsp; text: "Ethical design frameworks and regulations call for \*\*transparency, consent, and clarity\*\* in persuasive design. Interfaces should use plain language (avoid trick wording), clearly distinguish advertising or sponsored content, and provide accessible privacy controls:contentReference\[oaicite:14]{index=14}:contentReference\[oaicite:15]{index=15}. \*\*Guardrail:\*\* Incorporate an “informed consent” mindset – e.g. a \*\*Scholia Mode\*\* where users can toggle on explanations or citations behind claims and recommendations – to support autonomous decision-making rather than covert influence."

&nbsp; importance: Medium

&nbsp; strength: Medium

&nbsp; scope: human

&nbsp; caveats: "Some users may ignore available transparency features; balancing transparency with UI simplicity is needed."

&nbsp; evidence\_cites: \["gray2023", "ftc2022"]

&nbsp; contradictions: \[]



\- id: R5-C10

&nbsp; text: "In sensitive domains (health, finance, and apps for minors), \*\*persuasive elements require heightened ethical oversight\*\*. Any behavioral nudges must be evidence-based and come with explicit, informed consent. Dark patterns that could exploit vulnerabilities in these contexts are broadly condemned by standards (e.g. bans on manipulative health app prompts) and may violate laws like GDPR if consent is not “freely given”:contentReference\[oaicite:16]{index=16}. \*\*Guardrail:\*\* Adopt a precautionary approach: default to user wellbeing (e.g. encourage breaks, informed medical advice) over engagement, and involve ethics reviews or user testing to catch unintended coercion."

&nbsp; importance: High

&nbsp; strength: Medium

&nbsp; scope: human

&nbsp; caveats: "Defining manipulation vs. acceptable persuasion can be subjective; requires constant updating with clinical and legal guidance."

&nbsp; evidence\_cites: \["lupianez2022", "thaler2018"]

&nbsp; contradictions: \[]



```


```markdown

\# quotes.md

“Instances where design choices subvert, impair, or distort the ability of a user to make autonomous and informed choices…” — Gray et al. 2023, p. 1【2†L43-L49】 (key: gray2023)



“Dark Patterns are tricks u

wired.com

s and apps that make you do things you didn’t mean to, like buying or signing up for something.” — Brignull 2013, para. 1 (key: brignull2013)



“Relatively mild dark patterns more than doubled the percentage of consumers who signed up for a dubious identity theft protection service… and aggressive dark patterns increased it even further.” — Luguri \& Strahilevitz 2021, p. 82 (key: luguri2021)



“97% of the most popular websites and apps used by EU consumers deployed at least one dark pattern…” — Lupiáñez-Villanueva et al. 2022, p. 1 (key: lupianez

pmc.ncbi.nlm.nih.gov

ok has one of the most advanced algorithm systems and is the most addictive as compared to other social media platforms.” — Qin et al. 2022, p. 2 (key: qin2022)



“I noticed… a gesture that had become as commonplace as breathing… my thumb compulsively brushing upward… yanking the lever on the largest and most addictive slot machine in the world.” — Culp 2023, para. 3【21†L107-L115】 (key: culp2023)



“There is strong evidence that… changing or setting defaults is more effective at influencing consumer choices and behaviours than changing t

wired.com

.” — CMA 2022, p. 13 (key: cma2022)



“Dark patterns often take advantage of consumers’ cognitive biases… Research shows that dark patterns are highly effective at influencing consumer behavior.” — FTC 2022, p. 1【59†L85-L94】 (key: ftc2022)

```


```bibtex

% refs.bib

@inproceedings{gray2023,

&nbsp; author = {Gray, Colin M. and Santos, Cristiana and Bielova, Nataliia},

&nbsp; year = {2023},

&nbsp; title = {Towards a Preliminary Ontology of Dark Patterns Knowledge},

&nbsp; booktitle :contentReference\[oaicite:0]{index=0} Extended Abstracts of the 2023 CHI Conference on Human Factors in Computing Systems},

&nbsp; pages = {1--9},

&nbsp; publisher = {ACM},

&nbsp; doi = {10.1145/3544549.3585676}

}



@misc{brignull2013,

&nbsp; author = {Brignull, Harry},

&nbsp; year = {2013},

&nbsp; title = {Dark Patterns: Inside the Interfaces Designed to Trick You},

&nbsp; howpublished = {The Verge (Aug 29, 2013)},

&nbsp; url = {https://www.theverge.com/2013/8/29/4640308/dark-patterns-inside-the-interfaces-designed-to-trick-you}

}



@article{luguri2021,

&nbsp; author = {Luguri, Jamie and Strahilevitz, Lior J.},

&nbsp; year = {2021},

&nbsp; :contentReference\[oaicite:1]{index=1}ng a Light on Dark Patterns},

&nbsp; journal = {Journal of Legal Analysis},

&nbsp; volume = {13},

&nbsp; number = {1},

&nbsp; pages = {43--109},

&nbsp; doi = {10.1093/jla/laaa006}

}



@article{mathur2019,

&nbsp; author = {Mathur, Arunesh and Acar, Gunes and Friedman, Michael J. and Lucherini, Elena and Mayer, Jonathan and Chetty, Marshini and Narayanan, Arvind},

&nbsp; year = {2019},

&nbsp; title = {Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites},

&nbsp; journal = {Proceedings of the ACM on Human-Computer Interaction},

&nbsp; volume = {3},

&nbsp; number = {CSCW},

&nbsp; pages:contentReference\[oaicite:2]{index=2}2},

&nbsp; doi = {10.1145/3359183}

}



@article{qin2022,

&nbsp; author = {Qin, Yao and Omar, Bahiyah and Musetti, Alessandro},

&nbsp; year = {2022},

&nbsp; title = {The addiction behavior of short-form video app TikTok: The information quality and system quality perspective},

&nbsp; journal = {Frontiers in Psychology},

&nbsp; volume = {13},

&nbsp; pages = {932805},

&nbsp; doi = {10.3389/fpsyg.2022.932805},

&nbsp; pmid = {36148123}

}



@techreport{lupianez2022,

&nbsp; author = {Lupia\\'{n}ez-Villanueva, Francisco and Boluda, Alba and Bogliacino, Francesco and Liva, Giovanni and Lechardoy, Lucie and :contentReference\[oaicite:3]{index=3} de las Heras Ballell, Teresa},

&nbsp; year = {2022},

&nbsp; title = {Behavioural Study on Unfair Commercial Practices in the Digital Environment: Dark Patterns and Manipulative Personalisation (Final Report)},

&nbsp; institution = {European Commission, Directorate-General for Justice and Consumers},

&nbsp; doi = {10.2838/859030}

}



@techreport{cma2022,

&nbsp; author = {{Competition and Markets Authority (UK)}},

&nbsp; year = {2022},

&nbsp; title = {Evidence Review of Online Choice Architecture and Consumer and Competition Harm},

&nbsp; institution = {Competition and Markets Authority},

&nbsp; number = {Research Paper},

&nbsp; note = {Published April 2022:contentReference\[oaicite:4]{index=4}:contentReference\[oaicite:5]{index=5}}



@report{ftc2022,

&nbsp; author = {{Federal Trade Commission}},

&nbsp; year = {2022},

&nbsp; title = {Bringing Dark Patterns to Light: Staff Report},

&nbsp; institution = {FTC Bureau of Consumer Protection},

&nbsp; month = {September},

&nbsp; url = {https://www.ftc.gov/system/files/ftc\_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf}

}



@article{culp2023,

&nbsp; author = {Culp, Samantha},

&nbsp; year = {2023},

&nbsp; title = {There's an Alternative to the Infinite Scroll},

&nbsp; journal = {Wired},

&nbsp; volume = {31},

&nbsp; number = {9},

&nbsp; pages = {NA},

&nbsp; month = {September},

&nbsp; url = {https://www.wired.com/story/lexicon-scrol :contentReference\[oaicite:6]{index=6}g-mindfulness-linguistics/}

}



@article{thaler2018,

&nbsp; author = {Thaler, Richard H.},

&nbsp; year = {2018},

&nbsp; title = {Nudge:contentReference\[oaicite:7]{index=7}:contentReference\[oaicite:8]{index=8} {Science},

&nbsp; volume = {361},

&nbsp; number = {6401},

&nbsp; pages = {431},

&nbsp; doi = {10.1126/science.aau9241},

&nbsp; pmid = {30072515}

}



@inproceedings{nouwens2020,

&nbsp; author = {Nouwens, Midas and Liccardi, Ilaria and Veale, Michael and Karger, David and Kagal, Lalana},

&nbsp; year = {2020},

&nbsp; title = {Dark Patterns after the GDPR: Scraping Consent Pop-ups and Demonstrating their Influence},

&nbsp; booktitle = {CHI '20: Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems},

&nbsp; pages = {1--13},

&nbsp; publisher = {ACM},

&nbsp; doi = {10.1145/3313831.3376321}

:contentReference\[oaicite:9]{index=9}:contentReference\[oaicite:10]{index=10}:contentReference\[oaicite:11]{index=11}:contentReference\[oaicite:12]{index=12}:contentReference\[oaicite:13]{index=13}:contentReference\[oaicite:14]{index=14}:contentReference\[oaicite:15]{index=15}:contentReference\[oaicite:16]{index=16}:contentReference\[oaicite:17]{index=17}:contentReference\[oaicite:18]{index=18}:contentReference\[oaicite:19]{index=19}:contentReference\[oaicite:20]{index=20}:contentReference\[oaicite:21]{index=21}:contentReference\[oaicite:22]{index=22}:contentReference\[oaicite:23]{index=23}:contentReference\[oaicite:24]{index=24}:contentReference\[oaicite:25]{index=25}:contentReference\[oaicite:26]{index=26}:contentReference\[oaicite:27]{index=27}:contentReference\[oaicite:28]{index=28}:contentReference\[oaicite:29]{index=29}:contentReference\[oaicite:30]{index=30}:contentReference\[oaicite:31]{index=31}:contentReference\[oaicite:32]{index=32}:contentReference\[oaicite:33]{index=33}:contentReference\[oaicite:34]{index=34}:contentReference\[oaicite:35]{index=35}:contentReference\[oaicite:36]{index=36}:contentReference\[oaicite:37]{index=37}:contentReference\[oaicite:38]{index=38}:contentReference\[oaicite:39]{index=39}:contentReference\[oaicite:40]{index=40}:contentReference\[oaicite:41]{index=41}:contentReference\[oaicite:42]{index=42}:contentReference\[oaicite:43]{index=43}:contentReference\[oaicite:44]{index=44}:contentReference\[oaicite:45]{index=45}:contentReference\[oaicite:46]{index=46}:contentReference\[oaicite:47]{index=47}:contentReference\[oaicite:48]{index=48}:contentReference\[oaicite:49]{index=49}:contentReference\[oaicite:50]{index=50}:contentReference\[oaicite:51]{index=51}:contentReference\[oaicite:52]{index=52}:contentReference\[oaicite:53]{index=53}:contentReference\[oaicite:54]{index=54}:contentReference\[oaicite:55]{index=55}:contentReference\[oaicite:56]{index=56}:contentReference\[oaicite:57]{index=57}:contentReference\[oaicite:58]{index=58}:contentReference\[oaicite:59]{index=59}:contentReference\[oaicite:60]{index=60}

```



```markdown

# evidence.md

Ethics in Persuasive Design – Guardrails Checklist



Recent research and policy analyses indicate that many digital interfaces leverage “dark patterns” – deceptive or coercive design tactics – that under

wired.com

nomy【2†L43-L49】【59†L85-L93】. These patterns are pervasive, with audits finding them on the vast majority of popular sites and apps【19†L177-L185】. Given their proven effectiveness at exploiting cognitive biases (e.g. doubling sign-up rates for unwanted services【59†L93-L101】), regulators worldwide (EU, US, UK, etc.) now view mere legal compliance as a baseline, not a gold standard【2†L75-L83】. The goal is to move beyond avoiding illegality, towards proactively preserving user autonomy and welfare. Below is a checklist of design guardrails – drawn

pmc.ncbi.nlm.nih.gov

frameworks and empirical findings – to counter dopamine-fueled persuasive tricks:



Transparent Disclosure: No more bait-and-switch. Clearly label ads, endorsements, or paid content. Disclose all terms (price, data use) upfront in plain language – before the user makes a decision【59†L85-L93】. For example, if an app might share health data, say so conspicuously (GDPR-style informed consent). Surprise charges or fine-print conditions erode trust and violate most consumer protection laws.



Friction for High-Risk Actions: U

wired.com

hically. Design friction can be a force for good when it protects users from unintended harm (as opposed to “sludge” that traps them【32†L200-L205】). Require an extra confirmation click for irreversible or high-stakes actions (deleting an account, sending money, making a health decision). Conversely, remove unnecessary hurdles for beneficial actions like opting out or canceling subscriptions – several jurisdictions now mandate easy online cancellations to combat “roach motel” tactics【59†L113-L121】.



Benign Defaults: Defaults should be

ftc.gov

&nbsp;not self-serving. Since users often stick with pre-selected options, ensure default settings favor privacy, safety, and well-being【38†L1298-L1306】. For instance, a social app might default to minimal data sharing and ask users to opt-in to more invasive tracking (if truly necessary) rather than opting everyone in by default. The EU’s ban on pre-ticked consent boxes reflects this principle【38†L1308-L1316】. Defaults should never be used to smuggle undesired products or permissions (no “sneaking” extras into the cart by default【26†L69-L77】【26†L109-L117】).



Rate Limits \& Breaks: Re-introduce st

deceptive.design

deceptive.design

&nbsp;experiences. Features like infinite scroll, autoplay, and endless feeds deliberately eliminate natural stopping points, fostering “doomscrolling” and bingeing through dopamine-driven reward loops【21†L155-L163】. To counter this, implement gentle breaks: e.g. “You've been scrolling for a while – take a moment?” prompts or mandatory pauses after X episodes/videos. Even Netflix added an “Are you still watching?” prompt – a small friction that encourages mindful use. Such circuit-breakers help users regain agency in experiences engineered to be bottomless.



Notification Hygiene: Respec

deceptive.design

tion. Unrestrained push notifications manipulate our reward systems, training us to check apps reflexively (much like

ftc.gov

ftc.gov

ayoffs)【21†L109-L117】. Guardrails here include batching notifications (deliver at set intervals rather than continuous interrupts), smart filtering of non-urgent pings, and opt-in consent for promotional alerts. Design notification settings that are on by default for truly critical alerts (e.g. account security) but off by default for promotional or engagement-oriented nudges. Users should be able to easily customize or mute notifications, and the default state should minimize distraction, not maximize “click-through.”



Honest UI Ar

gov.uk

ark Patterns): Structure choices for clarity, not coercion. Follow a “fair pattern” approach: For any user decision, present choices evenly and avoid manipulative layout. For exampl

gov.uk

erarchies\*\* (don’t highlight a “Yes” button in bright colors and bury the “No” in grey text)【19†L179-L187】. No confirmshaming – don’t guilt-trip users who decline offers (“No, I hate saving money”). No hidden options – if there’s a “Reject All” for cookies or a free tier, it must be as visible as the “Accept” or paid upgrade【26†L85-L93】. Design dialogs and forms so that the easiest path is the honest path, not a trap.



Easy Exit and Undo: Make reversibility a core feature. Users should be able to undo or revise decisions without undue effort. This mea

ar5iv.labs.arxiv.org

&nbsp;simple cancellation processes (one-click unsubscribe, online cancellation flows that mirror sign-up

op.europa.eu

)【59†L113-L121】. It also means allowing cooling-off: e.g. after a big in-

ftc.gov

or a super-long usage session, consider a follow-up “Did you mean to do that? Here’s how to reverse if needed.” Some jurisdictions require easy refunds or cancellations within a time window for online purchases – design should facilitate, not hinder, those rights.



Explainability (“Why Am I Seeing This?”): Provide algorithmic transparency. Whenever content is personalized or a recommendation is made, give users an accessible explanation. For example, social platforms and news apps can implement a “Why am I seeing this post/ad?” button that reveals key factors (e.g. “Because you watched X, we thought you’d like Y”). This transparency, akin to a nutrition label for content, helps users understand and adjust the system’s influence on them. Re

colingray.me

ftc.gov

rency can increase user trust and satisfaction, even if it modestly reduces click-through on hyper-targeted content【10†L123-L131】.



Scholia Mode for Context: Empower users with knowledge at the point of persuasion. Inspired by scholia (marginal notes that explain or cite sources), a “Scholia Mode” could let users toggle on contextual information in content feeds or interfaces. For instance, a health app giving behavior prompts might include a “Evidence” link to peer-reviewed research, or a finance app’s nudges (like “Save more now!”) might come with a brief note on how it calculated that recommendation. By designing interfaces to cite their claims or rationale, users prone to impulsive decisions get a gentle nudge toward informed deliberation, counteracting pure emotional or dopamine-driven triggers.



Informed Consent as Ongoing Process: Especially in health, finance, or apps for children, pri

gov.uk

&nbsp;consent and user understanding at every step. This goes beyond one-time agreement screens. It means using understandable language, offering just-in-time explanations (e.g. if a wellness app suggests an anxiety exercise, briefly note why, and allow refusal without penalty), and never exploiting vulnerabilities (e.g. a mental health app should not use dark patterns to lock in a user seeking help). For minors, comply with stricter codes (like privacy-by-default and game designs that don’t exploit children’s cognitive biases). When in doubt, err on the side of user well-being over growth: persuasive design in these conte

colingray.me

be grounded in transparency and beneficence, not engagement-at-any-cost.



In summary, autonomy-preserving design is now the target bar: interfaces should empower users to make choices “as judged by themselves” (to borrow a key principle from nudge theory)【30†L129-L133】. Dark patterns might boost short-term clicks or conversions, but they invite regulatory scrutiny and erode user trust long-term【2†L75-L83】【59†L127-L136】. By contrast, integrating the guardrails above – from honest defaults and disclosures to built-in breaks and explainability – aligns digital products with emerging ethics standards and legal frameworks (GDPR, DSA, FTC guidance, etc.) that explicitly call out manipulative design【2†L75-L83】. Designing with these guardrails is not just about avoiding penalties; it’s about respecting user dignity and fostering sustainable engagement built on trust rather than compulsion【59†L123-L131】.



Ultimately, an ethical, autonomy-first approach to persuasive tech can stil

wired.com

chology and data for user good – e.g. nudging toward healthy habits or saving money – but it does so with the user’s informed participation, not through deception. By following the above checklist, product teams can deliver “dopamine-sensitive” features (feeds, notifications, recommendations) in a manner that supports user autonomy, transparency, and well-being, rather than under

ftc.gov

r engagement’s sake【2†L43-L49】【59†L85-L93】. This alignment of design with user autonomy is rapidly becoming the expected norm – the new floor set by compliance and the ceiling strived for by conscientious innovators.



Sources:



Gray, C.M. et al. (2023). Towards a Preliminary Ontology of Dark Patterns Knowledge. CHI EA ’23.【2†L43-L49】【2†L75-L83】



Brignull, H. (2013). Dark Patterns: Inside the Interfaces Designed to Trick You. The Verge.【45†L21-L29】



Luguri, J., \& Strahilevitz, L. (2021). Shining a Light on Dark Patterns. J. of Legal Analysis, 13(1), 43–109.【59†L93-L101】



Mathur, A. et al. (2019). Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites. PACM HCI, 3(CSCW), Article 81.【14†L25-L33】【26†L69-L77】



Qin, Y. et al. (2022). The addiction behavior of short-form video app TikTok.... Front. Psychol. 13: 932805.【23†L153-L162】【24†L1-L4】



Lupiáñez-Villanueva, F. et al. (2022). Behavioural Study on Dark Patterns… (EU Commission Report).【19†L177-L185】



Competition \& Markets Authority (2022). Online Choice Architecture: Evidence Review (Report).【38†L1298-L1306】【38†L1301-L1308】



Federal Trade Commission (2022). Bringing Dark Patterns to Light (Staff Report).【59†L85-L94】【59†L113-L121】



Culp, S. (2023). There’s an Alternative to the Infinite Scroll. Wired, Sep. 19, 2023.【21†L107-L115】【21†L155-L163】



Thaler, R.H. (2018). Nudge, not sludge. Science, 361(6401): 431.【30†L129-L134】

```