R2 — Variable Reward Schedules & Doomscrolling → Targets: Briefs, Practice, Manifesto

```yaml
# claims.yaml
- id: R2-C01
  text: "Intermittent/variable reward schedules drive persistent, high-rate checking; modern feeds and notifications emulate these contingencies."
  importance: High
  strength: High
  scope: mixed
  caveats: "Classic evidence is lab-based; translation to complex apps inferred via HCI experiments."
  evidence_cites: ["ferster1957", "oulasvirta2012", "fitz2019"]
  contradictions: []

- id: R2-C02
  text: "Smartphone checking is a brief, frequent habit reinforced by fast, informational rewards."
  importance: High
  strength: High
  scope: human
  caveats: "Student-heavy samples; early smartphones."
  evidence_cites: ["oulasvirta2012"]
  contradictions: []

- id: R2-C03
  text: "Auditory/tactile notifications capture attention and impair performance even without phone interaction."
  importance: High
  strength: High
  scope: human
  caveats: "Lab task generalizability to real work varies."
  evidence_cites: ["stothart2015"]
  contradictions: []

- id: R2-C04
  text: "Batching notifications at predictable times improves attention, mood, perceived control, and reduces stress versus default variable delivery; turning all notifications off can elevate anxiety/FoMO."
  importance: High
  strength: High
  scope: human
  caveats: "Two-week field trial; MTurk/India sample."
  evidence_cites: ["fitz2019"]
  contradictions: []

- id: R2-C05
  text: "Novelty signals recruit midbrain (SN/VTA) and hippocampal systems and promote exploration, supporting attentional capture by endlessly novel feeds."
  importance: High
  strength: High
  scope: human
  caveats: "fMRI inference; task differences."
  evidence_cites: ["bunzeck2006", "krebs2009", "lisman2005"]
  contradictions: []

- id: R2-C06
  text: "Grayscale display (cue desaturation) reduces daily screen time and problematic use; effects are modest and compliance varies."
  importance: Medium
  strength: Medium
  scope: human
  caveats: "Short interventions; self-selected compliance; mixed outcomes across studies."
  evidence_cites: ["holte2020", "dekker2024", "wickord2023", "olson2022"]
  contradictions: []

- id: R2-C07
  text: "Removing/quieting cues (disabling non‑essential notifications, moving/removing icon shortcuts) reduces use in multi‑strategy interventions."
  importance: High
  strength: Medium
  scope: human
  caveats: "Bundled interventions limit isolation of effects."
  evidence_cites: ["olson2022", "fitz2019", "stothart2015"]
  contradictions: []

- id: R2-C08
  text: "‘Wanting’ (incentive salience) can be amplified by cues/rewards without increased ‘liking,’ explaining compulsive checking under variable schedules."
  importance: High
  strength: High
  scope: mixed
  caveats: "Addiction framework extrapolated to digital habits."
  evidence_cites: ["berridge2016"]
  contradictions: []

- id: R2-C09
  text: "During infinite scrolling, context‑aware frictions (timely prompts/pauses) reduce scrolling when aligned with states like sleepiness or at‑home use."
  importance: Medium
  strength: Medium
  scope: human
  caveats: "Short (7‑day) study; acceptance depends on context."
  evidence_cites: ["meinhardt2025"]
  contradictions: []

- id: R2-C10
  text: "Adolescents show heightened ventral striatum reward sensitivity and greater peer‑amplified reward seeking, suggesting stronger susceptibility to novelty/variable cues."
  importance: Medium
  strength: High
  scope: human
  caveats: "Developmental heterogeneity; lab tasks."
  evidence_cites: ["galvan2006", "chein2011"]
  contradictions: []

- id: R2-C11
  text: "For high‑frequency social media users, short, pervasive checking patterns indicate stronger habit loops; batching and added friction are likely necessary."
  importance: Medium
  strength: Medium
  scope: human
  caveats: "Direct moderation tests limited."
  evidence_cites: ["oulasvirta2012", "fitz2019"]
  contradictions: []

- id: R2-C12
  text: "Design frictions that slow continuous consumption can improve recall/goal adherence but may reduce satisfaction."
  importance: Medium
  strength: Low
  scope: human
  caveats: "Some evidence from preprints and small samples."
  evidence_cites: ["ruiz2024", "meinhardt2025"]
  contradictions: []
```

```markdown
# quotes.md
> "A checking habit: brief, repetitive inspection of dynamic content quickly accessible on the device." — Oulasvirta 2012, p. 105 (key: oulasvirta2012)

> "Participants whose notifications were batched three-times-a-day felt more attentive, productive, in a better mood, and in greater control of their phones." — Fitz et al. 2019, p. 84 (key: fitz2019)

> "Never receiving notifications backfires… producing instead an increase in anxiety mediated by fear of missing out." — Fitz et al. 2019, p. 90 (key: fitz2019)

> "Cellular phone notifications alone significantly disrupted performance on an attention-demanding task." — Stothart et al. 2015, p. 893 (key: stothart2015)

> "Absolute coding of stimulus novelty in the human substantia nigra/VTA." — Bunzeck & Düzel 2006, p. 369 (key: bunzeck2006)

> "Novelty… represents a salient learning signal that can motivate ‘exploration’ in search for potential rewards." — Krebs et al. 2009, p. 2272 (key: krebs2009)

> "Activation of the [hippocampal–VTA] loop begins when the hippocampus detects newly arrived information that is not already stored." — Lisman & Grace 2005, p. 703 (key: lisman2005)

> "‘Wanting’ is mediated by large and robust neural systems that include mesolimbic dopamine… ‘liking’ is not dependent on dopamine." — Berridge & Robinson 2016, p. 670 (key: berridge2016)

> "The presence of peers increases adolescent risk taking by heightening sensitivity to the potential reward value of risky decisions." — Chein et al. 2011, p. F1 (key: chein2011)

> "It appears changing to grayscale makes smartphones less gratifying and can assist individuals in controlling their smartphone use." — Holte & Ferraro 2020, p. 274 (key: holte2020)
```

```bibtex
% refs.bib
@book{ferster1957,
  author = {Ferster, Charles B. and Skinner, B. F.},
  year = {1957},
  title = {Schedules of Reinforcement},
  journal = {Appleton-Century-Crofts},
  volume = {},
  pages = {1--741},
  doi = {10.1037/10627-000},
  pmid = {}
}

@article{oulasvirta2012,
  author = {Oulasvirta, Antti and Rattenbury, Tye and Ma, Lingyi and Raita, Eeva},
  year = {2012},
  title = {Habits make smartphone use more pervasive},
  journal = {Personal and Ubiquitous Computing},
  volume = {16},
  number = {1},
  pages = {105--114},
  doi = {10.1007/s00779-011-0412-2},
  pmid = {}
}

@article{stothart2015,
  author = {Stothart, Cary and Mitchum, Ainsley and Yehnert, Courtney},
  year = {2015},
  title = {The Attentional Cost of Receiving a Cell Phone Notification},
  journal = {Journal of Experimental Psychology: Human Perception and Performance},
  volume = {41},
  number = {4},
  pages = {893--897},
  doi = {10.1037/xhp0000100},
  pmid = {26121498}
}

@article{fitz2019,
  author = {Fitz, Nicholas and Kushlev, Kostadin and Jagannathan, Ranjan and Lewis, Terrel and Paliwal, Devang and Ariely, Dan},
  year = {2019},
  title = {Batching smartphone notifications can improve well-being},
  journal = {Computers in Human Behavior},
  volume = {101},
  number = {},
  pages = {84--94},
  doi = {10.1016/j.chb.2019.07.016},
  pmid = {}
}

@article{bunzeck2006,
  author = {Bunzeck, Nico and Düzel, Emrah},
  year = {2006},
  title = {Absolute coding of stimulus novelty in the human substantia nigra/VTA},
  journal = {Neuron},
  volume = {51},
  number = {3},
  pages = {369--379},
  doi = {10.1016/j.neuron.2006.06.021},
  pmid = {16880131}
}

@article{krebs2009,
  author = {Krebs, Ruth M. and Schott, Björn H. and Schütze, Hartmut and Düzel, Emrah},
  year = {2009},
  title = {The novelty exploration bonus and its attentional modulation},
  journal = {Neuropsychologia},
  volume = {47},
  number = {11},
  pages = {2272--2281},
  doi = {10.1016/j.neuropsychologia.2009.01.015},
  pmid = {19524091}
}

@article{lisman2005,
  author = {Lisman, John E. and Grace, Anthony A.},
  year = {2005},
  title = {The hippocampal-VTA loop: controlling the entry of information into long-term memory},
  journal = {Neuron},
  volume = {46},
  number = {5},
  pages = {703--713},
  doi = {10.1016/j.neuron.2005.05.002},
  pmid = {15924857}
}

@article{berridge2016,
  author = {Berridge, Kent C. and Robinson, Terry E.},
  year = {2016},
  title = {Liking, wanting, and the incentive-sensitization theory of addiction},
  journal = {American Psychologist},
  volume = {71},
  number = {8},
  pages = {670--679},
  doi = {10.1037/amp0000059},
  pmid = {27977239}
}

@inproceedings{meinhardt2025,
  author = {Meinhardt, Luca-Maxim and Elhaidary, Maryam and Colley, Mark and Rietzler, Michael and Rixen, Jan Ole and Purohit, Aditya Kumar and Rukzio, Enrico},
  year = {2025},
  title = {Scrolling in the Deep: Analysing Contextual Influences on Intervention Effectiveness during Infinite Scrolling on Social Media},
  journal = {Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '25)},
  volume = {},
  number = {},
  pages = {},
  doi = {10.1145/3706598.3713187},
  pmid = {}
}

@article{holte2020,
  author = {Holte, Alex J. and Ferraro, F. Richard},
  year = {2020},
  title = {True colors: Grayscale setting reduces screen time in college students},
  journal = {The Social Science Journal},
  volume = {60},
  number = {2},
  pages = {274--290},
  doi = {10.1080/03623319.2020.1737461},
  pmid = {}
}

@article{dekker2024,
  author = {Dekker, Clara A. and Zhang, Runkun and Twyman, Maya},
  year = {2024},
  title = {Is life brighter when your phone is not? The efficacy of a grayscale smartphone intervention},
  journal = {Mobile Media \& Communication},
  volume = {},
  number = {},
  pages = {},
  doi = {10.1177/20501579231212062},
  pmid = {}
}

@article{wickord2023,
  author = {Wickord, Lea-Christin and Quaiser-Pohl, Claudia},
  year = {2023},
  title = {Suffering from problematic smartphone use? Why not use grayscale setting as an intervention! – An experimental study},
  journal = {Computers in Human Behavior Reports},
  volume = {10},
  number = {},
  pages = {100294},
  doi = {10.1016/j.chbr.2023.100294},
  pmid = {}
}

@article{olson2022,
  author = {Olson, Jay A. and Sandra, Dasha A. and Chmoulevitch, Denis and Raz, Amir and Veissi{\`e}re, Samuel P. L.},
  year = {2022},
  title = {A Nudge-Based Intervention to Reduce Problematic Smartphone Use: Randomised Controlled Trial},
  journal = {International Journal of Mental Health and Addiction},
  volume = {},
  number = {},
  pages = {1--23},
  doi = {10.1007/s11469-022-00826-w},
  pmid = {35600564}
}

@article{chein2011,
  author = {Chein, Jason and Albert, Dustin and O’Brien, Lia and Uckert, Karen and Steinberg, Laurence},
  year = {2011},
  title = {Peers increase adolescent risk taking by enhancing activity in the brain’s reward circuitry},
  journal = {Developmental Science},
  volume = {14},
  number = {2},
  pages = {F1--F10},
  doi = {10.1111/j.1467-7687.2010.01035.x},
  pmid = {21499511}
}

@article{galvan2006,
  author = {Galv{\'a}n, Adriana and Hare, Todd A. and Parra, Cynthia E. and Penn, Julie and Voss, Henning and Glover, Gary and Casey, B. J.},
  year = {2006},
  title = {Earlier Development of the Accumbens Relative to Orbitofrontal Cortex Might Underlie Risk-Taking Behavior in Adolescents},
  journal = {Journal of Neuroscience},
  volume = {26},
  number = {25},
  pages = {6885--6892},
  doi = {10.1523/JNEUROSCI.1062-06.2006},
  pmid = {16793895}
}

@article{ruiz2024,
  author = {Ruiz, Nicolas and Molina Le{\'o}n, Gabriela and Heuer, Hendrik},
  year = {2024},
  title = {Design Frictions on Social Media: Balancing Reduced Mindless Scrolling and User Satisfaction},
  journal = {arXiv preprint},
  volume = {arXiv:2407.18803},
  number = {},
  pages = {},
  doi = {},
  pmid = {}
}
```

```markdown
# evidence.md
**Core mechanism.** Variable reward and novelty are potent drivers of attention and approach. Classic operant work shows intermittent schedules sustain high, persistent responding (ferster1957). In smartphones, *checking* is a brief, frequent habit reinforced by fast informational rewards (oulasvirta2012). Notifications capture attention and impair task performance even when ignored (stothart2015).

**Novelty & exploration.** Human fMRI links novelty to SN/VTA and hippocampal systems, promoting exploration and learning (bunzeck2006; krebs2009; lisman2005). Infinite feeds exploit continuous novelty; HCI fieldwork shows context-aware frictions can curb scrolling when well timed (meinhardt2025).

**Mitigations—individual level (priority).**
- **Batch notifications** to 3×/day: better attention/mood/control; stress ↓; full shutoff can raise anxiety/FoMO (fitz2019).
- **Cue removal/desaturation:** disable non‑essential notifications, move/remove app icons; supported within multi‑strategy RCT reducing screen time/problematic use (olson2022).
- **Grayscale:** reduces use and problematic symptoms with modest effects; compliance varies (holte2020; dekker2024; wickord2023).

**Guardrails—system level (secondary).** Context-sensitive **frictions** (pause/confirm, timely prompts) during infinite scroll reduce overuse but can reduce satisfaction; design for optionality and timing (meinhardt2025; ruiz2024).

**Populations.** Adolescents show heightened reward sensitivity and peer‑amplified seeking—apply stronger defaults (e.g., notification batching by default, bedtime quiet hours) (galvan2006; chein2011). High‑frequency users exhibit stronger habit loops—expect greater gains from batching + frictions (oulasvirta2012; fitz2019).

**Practice takeaway.** Start with: (1) batch notifications 3×/day; (2) disable non‑essential alerts; (3) grayscale + move icons off home screen; (4) insert voluntary scroll-pauses at context‑relevant moments.
```
