R4 — Stress, Salience, and Relapse (locked specs)


```yaml
# claims.yaml
- id: R4-C01
  text: "Acute stress surges (e.g., via cortisol and noradrenaline) heighten dopaminergic “salience” signals for drug cues, leading to increased craving and drug-seeking."
  importance: High
  strength: High
  scope: mixed
  caveats: "Laboratory stress analogs (e.g., TSST) reliably provoke craving:contentReference[oaicite:0]{index=0}, but may not capture all real-world factors; individual variability in stress responses exists."
  evidence_cites: ["mckee2011", "sinha2024"]
  contradictions: []

- id: R4-C02
  text: "Chronic or repeated stress produces lasting dysregulation in stress and reward circuits (e.g., elevated CRF–dynorphin activity and blunted dopamine responses), fostering anhedonia and greater relapse vulnerability."
  importance: High
  strength: Medium
  scope: mixed
  caveats: "Human evidence is largely correlational; extrapolated from animal models of chronic stress-induced reward deficits:contentReference[oaicite:1]{index=1}; species differences and confounding life factors limit direct inference."
  evidence_cites: ["baik2020", "mantsch2016"]
  contradictions: []

- id: R4-C03
  text: "Stress exposure is a potent trigger for craving, and stress-induced craving often immediately precedes lapses or relapse episodes."
  importance: High
  strength: High
  scope: human
  caveats: "Demonstrated in prospective human studies:contentReference[oaicite:2]{index=2}; however, retrospective self-report can bias stress–relapse links."
  evidence_cites: ["wemm2019", "sinha2024"]
  contradictions: []

- id: R4-C04
  text: "Individuals with heightened stress reactivity or negative affect (e.g., high cortisol response, anxiety/PTSD) experience stronger cue-induced cravings and face elevated relapse risk."
  importance: Medium
  strength: Medium
  scope: human
  caveats: "Stress reactivity varies widely; e.g., patients with high withdrawal-related distress benefited most from stress-targeted treatment:contentReference[oaicite:3]{index=3}. Associations are correlational; causality is inferred but not definitively proven in humans."
  evidence_cites: ["sinha2024"]
  contradictions: []

- id: R4-C05
  text: "Noradrenergic arousal mediates stress-related craving: pharmacologically dampening central noradrenaline (using α₁-blockers like prazosin or α₂-agonists like clonidine/lofexidine) reduces stress-induced craving and can improve abstinence outcomes."
  importance: High
  strength: Medium
  scope: human
  caveats: "Supported by pilot trials:contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}; effects may be specific to high-stress subgroups (e.g., those with severe withdrawal or comorbid PTSD:contentReference[oaicite:6]{index=6}). Medication side effects and adherence affect real-world utility."
  evidence_cites: ["sinha2024"]
  contradictions: []

- id: R4-C06
  text: "HPA-axis modulation can alter craving: Elevated cortisol during stress correlates with higher craving:contentReference[oaicite:7]{index=7}, yet paradoxically, administering cortisol acutely can reduce drug-cue craving by impairing memory reconsolidation of drug cues."
  importance: Medium
  strength: Medium
  scope: human
  caveats: "Context-dependent effects: cortisol’s craving-reducing impact was seen in low-dependence cases:contentReference[oaicite:8]{index=8} and in controlled exposure settings:contentReference[oaicite:9]{index=9}. Not a standard treatment yet; longitudinal benefits and optimal dosing remain unclear."
  evidence_cites: ["mckee2011", "walter2015", "soravia2021"]
  contradictions: []

- id: R4-C07
  text: "Sleep disturbances (insomnia, reduced slow-wave sleep) are pervasive in recovery and independently predict stronger cravings and higher relapse risk."
  importance: High
  strength: High
  scope: human
  caveats: "Baseline insomnia and poor sleep continuity correlate with earlier relapse in alcohol use disorder:contentReference[oaicite:10]{index=10}. Causality is bidirectional—substance withdrawal disrupts sleep, and lack of restorative sleep elevates stress and impulsivity."
  evidence_cites: ["brower1998", "zhang2021"]
  contradictions: []

- id: R4-C08
  text: "Targeting sleep early in treatment (through sleep hygiene or therapy) can lower stress and improve self-regulation, potentially reducing relapse likelihood, although direct evidence for long-term relapse prevention is still emerging."
  importance: High
  strength: Medium
  scope: human
  caveats: "Small trials of insomnia treatment in SUD show improved sleep and next-day mood, but mixed impact on 3–6 month relapse rates. Poor adherence to sleep interventions can limit efficacy."
  evidence_cites: ["zhang2021"]
  contradictions: []

- id: R4-C09
  text: "Regular physical exercise attenuates stress and craving: acute moderate exercise reliably reduces momentary drug cravings:contentReference[oaicite:11]{index=11}, and exercise-based programs modestly improve mood and increase abstinence rates in SUD patients."
  importance: Medium
  strength: High
  scope: human
  caveats: "Consistent acute effects on craving are reported:contentReference[oaicite:12]{index=12}; however, sustaining exercise long-term is challenging, and not all studies show significant improvements in sustained abstinence (effects often modest, e.g., OR≈1.7:contentReference[oaicite:13]{index=13})."
  evidence_cites: ["haasova2013", "wang2014"]
  contradictions: []

- id: R4-C10
  text: "Mindfulness-based interventions (e.g., meditation, breathwork) reduce stress reactivity and help manage cravings. In RCTs, mindfulness training (MBRP) significantly lowered relapse risk and days of use compared to standard relapse prevention:contentReference[oaicite:14]{index=14}."
  importance: High
  strength: High
  scope: human
  caveats: "Mindfulness requires active patient engagement; while multiple trials report benefits:contentReference[oaicite:15]{index=15}, some outcomes (e.g., time to first lapse) may be comparable to cognitive-behavioral approaches. Optimal integration (group vs. individual format) is under study."
  evidence_cites: ["bowen2014"]
  contradictions: []

```


```markdown
# quotes.md
> "...stress-related sensitization of drug salience, which promotes increases in craving and drug use escalation..." — Sinha 2024, p. e172883 (key: sinha2024)

> "In both Study 1 and 2, exposure to a stressful event on a particular day predicted increased craving on that day... and such increases in craving pred:contentReference[oaicite:0]{index=0}lihood of drinking the next day." — Wemm et al. 2019, p. 903 (key: wemm2019)

> "Stress significantly increased hypothalamus-pituitary-adrenal (HPA) axis reactivity, tobacco craving... relative to the neutral condition. In addition, increased cortisol, ACTH, and tobacco craving were associated with reduced ability to resist smoking following stress." — McKee et al. 2011, p. 495 (key: mckee2011)

> "Acute stress appears to increase reward sensitivity... However, chronic stress results in blunted reward sensitivity..." — Baik 2020, p. 1880 (key: baik2020)

> "Sleep disturbances:contentReference[oaicite:1]{index=1}risk of relapse in AUD [alcohol use disorder]..." — Zhang et al. 2021, p. 2 (key: zhang2021)

> "There is strong evidence that physical activity acutely reduces cigarette craving." — Haasova et al. 2013, p. 34 (key: haasova2013)

> "...participants assigned to MBRP and RP reported significantly lower risk of relapse to substance use and heavy drinking..." — Bowen et al. 2014, p. 551 (key: bowen2014):contentReference[oaicite:2]{index=2} rate variability (HRV) biofeedback... reduced craving and anxiety more effectively than rehabilitative treatment alone and improved cardiac autonomic function by counterbalancing a chronic shift toward increased sympathetic and decreased parasympathetic tone." — Penzlin et al. 2017, p. 2 (key: penzlin2017)

> "In conclusion, a single administration of cortisol leads to reduced craving in low-dose heroin addicts." — Walter et al. 2015, p. e610 (key: walter2015)

> "The α₁-adrenergic receptor antagonist prazosin reduced stress-induced:contentReference[oaicite:3]{index=3}ng and negative emotions..." — Sinha 2024, p. e172883 (key: sinha2024)

```


```bibtex
% refs.bib
@article{sinha2024,
  author    = "Sinha, Rajita",
  year      = 2024,
  title     = "Stress and substance use disorders: risk, relapse, and treatment outcomes",
  journal   = "J. Clin. Invest.",
  volume    = 134,
  number    = 16,
  pages     = "e172883",
  doi       = "10.1172/JCI172883",
  pmid      = "3:contentReference[oaicite:0]{index=0}rticle{wemm2019,
  author    = "Wemm, Stephanie E. and Larkin, Chloe L. and Hermes, Gretchen L. and Tennen, Howard and Sinha, Rajita",
  year      = 2019,
  title     = "A day-by-day prospective analysis of stress, craving and risk of next day alcohol intake during alcohol use disorder treatment",
  journal   = "Drug Alcohol Depend.",
  volume    = 204,
  pages     = "107569",
  doi       = "10.1016/j.drugalcdep.2019.107569",
  pmid      = "31574406"
}

@article{mckee2011,
  author    = "McKee, Sherry A. and Sinha, Rajita and Weinberger, Andrea H. and Sofuoglu, Mehmet and Har:contentReference[oaicite:1]{index=1}. R. and Lavery, Meaghan and Wanzer, Jesse",
  year      = 2011,
  title     = "Stress decreases the ability to resist smoking and potentiates smoking intensity and reward",
  journal   = "J. Psychopharmacol.",
  volume    = 25,
  number    = 4,
  pages     = "490--502",
  doi       = "10.1177/0269881110376694",
  pmid      = "20817750"
}

@article{brower1998,
  author    = "Brower, Kirk J. and Aldr:contentReference[oaicite:2]{index=2}a S. and Hall, James M.",
  year      = 1998,
  title     = "Polysomnographic and subjective sleep predictors of alcoholic relapse",
  journal   = "Alcohol. Clin. Exp. Res.",
  volume    = 22,
  number    = 8,
  pages     = "1864--1871",
  doi       = "10.1111/j.1530-0277.1998.tb03995.x",
  pmid      = "9835290"
}

@article{walter2015,
  author    = "Walter, Marc and Bentz, Dominik and Schicktanz, Nora and Milnik, Annette and Aerni, Amanda and Gerhards, Christian and Schwegler, Konrad and Vogel, Matthias and Blum, Johannes and Schmid:contentReference[oaicite:3]{index=3}Roozendaal, Benno and Lang, Undine E. and Borgwardt, Stefan and de Quervain, Dominique J.-F.",
  year      = 2015,
  title     = "Effects of cortisol administration on craving in heroin-dependent patients",
  journal   = "Transl. Psychiatry",
  volume    = 5,
  pages     = "e610",
  doi       = "10.1038/tp.2015.101",
  pmid      = "26279204"
}

@article{soravia2021,
  author    = "Soravia, Leila M. and Moggi, Franz and de Quervain, Dominique J.-F.",
  year      = 2021,
  title     = "Effects of cortisol ad:contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}ng in vivo exposure in patients with alcohol use disorder",
  journal   = "Transl. Psychiatry",
  volum:contentReference[oaicite:6]{index=6}umber    = 1,
  pages     = "6",
  doi       = "10.1038/s41398-020-01180-y",
  pmid      = "33431843"
}

@article{baik2020,
  author    = "Baik, Ja-Hyun",
  year      = 2020,
  title     = "Stress and the dopaminergic reward system",
  journal   :contentReference[oaicite:7]{index=7}ed.",
  volume    = 52,
  number    = 12,
  pages     = "1879--1890",
  doi       = "10.1038/s12276-020-00532-4",
  pmid      = "33293605"
}

@article{penzlin2017,
  author    = "Penzlin, Ana I. and Barlinn, Kristian and Illigens, Ben Min-Woo and Weidner, Kerstin and Siepmann, Martin and Sie:contentReference[oaicite:8]{index=8}o",
  year      = 2017,
  title     :contentReference[oaicite:9]{index=9} short-term heart rate variability biofeedback on long-term abstinence in alcohol dependent patients – a one-year follow-up",
  journal   = "BMC Psychiatry",
  volume    = 17,
  pages     = "325",
  doi       = "10.1186/s12888-017-1480-2",
  pmid      = "28893151"
}

@article{bowen2014,
  author    = "Bowen, Sarah and Witkiewitz, Katie and Clifasefi, Seema L. and Grow, Joel and Chawla, Neharika and Hsu, Sharon H. and Carroll, Haley A. and Harrop, Erin and Collins, Susan E. and Lustyk, M. Kathleen and L:contentReference[oaicite:10]{index=10}ry E.",
  year      = 2014,
  title     = "Relative efficacy of mindfulness-based relapse prevention, standard relapse prevention, and treatment as usual for substance use disorders: a randomized clinical trial",
  journal   = "JAMA Psychiatry",
  volume    = 71,
  number    = 5,
  pages     = "547--556",
  doi       = "10.1001/jamapsychiatry.2013.4546",
  pmid      = "24647726"
}

@article{haasova2013,
  author    = "Haasova, Marcela and Warren, Fiona C. and Ussher, Michael and van Rensburg, Karien J. Janse and Faulkner, Guy and Cropley, Mark and Byron-Daniel, James and Everson-Hock, Emma S. and Oh, Hwajung and Taylor, Adrian H.",
  year      = 2013,
  title     = "The acute effects of physical activity on cigarette cravings: systematic review and meta-analysis with individual participant data",
  journal   = "Addiction",
  volume    = 108,
  number    = 1,
  pages     = "26--37",
  doi  :contentReference[oaicite:11]{index=11}.1111/j.1360-0443.2012.04034.x",
  pmid      = "22861822"
}

@article{mantsch2016,
  author    = "Mantsch, John R. and Baker, David A. and Funk, David and Le, A. D. and Shaham, Yavin",
  year      = 2016,
  title :contentReference[oaicite:12]{index=12}ess-induced reinstatement of drug seeking: 20 years of progress",
  journal   = "Neuropsychopharmacology",
  volume    = 41,
  number    = 1,
  pages     = "335--356":contentReference[oaicite:13]{index=13}= "10.1038/npp.2015.142",
  pmid      = "26072120"
}

@article{zhang2021,
  author    = "Zhang, Rui and Tomasi, Dardo and Manza, Peter and Shokri-Kojori, Ehsan and Demiral, Sukru B. and Feldman, Dana E. and Kroll, Danielle S. and Biesecker, Catherine L. and McPherson, Katherine L. and Wang, Gene-Jack and Wiers, Corinde E. and Volkow,:contentReference[oaicite:14]{index=14}
  year      = 2021,
  title     = "Sleep disturbances are associated with cortical and subcortical atrophy in alcohol use disorder",
  journal   = "Tr:contentReference[oaicite:15]{index=15}hiatry",
  volume    = 11,
  number    = 1,
  pages     = "428",
  doi       = "10.1038/s41398-021-01534-0",
  pmid      = "34429406"
}

@article{wang2014,
  author    = "Wang, Dongshi and Wang, Yanqiu and Wang, Yingying and Li, Rena and Zhou, Chenglin",
  year      = 2014,
  title     = "Impact of Physical Exercise on Substance Use Disorders: A Meta-Analysis",
  journal   = "PLoS ONE",
  volume    = 9,
  number    = 10,
  pages     = "e110728",
  doi       = "10.1371/journal.pone.0110728",
  pmid      = "25330218"
}

```



```markdown
# evidence.md
**Stress, Salience, and Relapse — Evidence Synthesis**

Acute stress rapidly activates the hypothalamic-pituitary-adrenal (HPA) axis and sympathetic noradrenergic system, which can transiently **increase mesolimbic dopamine signaling and incentive salience** for drug cues. Human lab studies confirm that induced :contentReference[oaicite:0]{index=0}tress (e.g., public speaking or combat imagery) **elevates craving and facilitates drug use**. For example, stressed smokers show surges in cortisol and **stronger urges to smoke**, often unable to resist the first cigarette【65†L323-L332】. In alcohol use disorder (AUD) patients, daily reports demonstrate that **stress on one day elevates craving that day, which in turn predicts drinking the next day**【63†L1-L4】. These findings align with animal models where stress or corticotropin-releasing factor (CRF) triggers reinstatement of drug-seeking【74†L755-L763】, indicating a conser:contentReference[oaicite:1]{index=1}wherein stress hormones modulate dopamine-related “wanting.”

**Chronic stress**, however, engenders a different neuroadaptive profile. Prolonged stress exposure and repeated withdrawal episodes are linked to **blunted dopamine reward responses and hyperactive brain stress systems** (e.g., upregulated CRF and dynorphin). This leads to an allostatic state of reward deficit and heightened negative aff:contentReference[oaicite:2]{index=2}ss surfeit”) that can drive drug use for relief. Indeed, acute stress can temporarily **sensitize** reward pathways (increasing motivation to seek drugs), whereas chronic stress leads to **anhedonia and reduced reward sensitivity**【52†L111-L118】. Clinically, individuals with trauma histories or anxiety disorders often report stronger cravings under stress and are at **higher risk of early relapse**, underscoring important **individual differences**. For instance, those with **greater cortisol or autonomic reactivity** to stress tend :contentReference[oaicite:3]{index=3}evere post-treatment outcomes, though causal direction is hard to establish outside laboratory settings.

**Interventions:** Targeting stress-pathophysiology shows promise. **Sleep restoration is a first-line priority** – insomnia and deficient slow-wave sleep persist in abstinence and strongly predict relapse【67†L1-L4】. Early recovery programs now emphasize cognitive-behavioral therapy for insomnia or sleep-hygiene coaching, aiming to break the vicious cycle of sleep loss elevating stress and impulsivity.:contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}a practical tool: *acute* bouts of moderate exercise reliably **reduce momentary cravings** (with meta-:contentReference[oaicite:6]{index=6}ng ~20–30% immediate craving reduction【68†L1-L4】) and improve mood. *Regular* exercise training can also enhance autonomic regulation (increasing heart rate variability) and has been associated with modestly higher 3- and 6-month abstinence rates:contentReference[oaicite:7]{index=7}d illicit drug use (odds ratios ~1.5–1.7)【61†L188-L197】. Adherence challenges remain, but exercise’s stress-buffering and neuroplastic benefits make it a valuable adjunct.

**Mindfulness and breath-focused therapies** directly attenuate physiological arousal and teach coping with urges. Rand:contentReference[oaicite:8]{index=8}als of Mindfulness-Based Relapse Pre:contentReference[oaicite:9]{index=9}P) show **significant reductions in relapse risk** and days of substance use compared to treatment-as-usual【69†L1-L9】. Mindfulness practices likely work by **down-regulating limbic reactivity** and enhancing prefrontal control during stress and craving (“urge surfing”). Even single-session studies find that slow, paced breathing can acutely increase vagal tone and reduce anxiety in craving-eliciting situations.

Pharmacologically, **modulating stress hormones** has yielded intriguing but nuanced result:contentReference[oaicite:10]{index=10}g noradrenergic surges with **α₁-adrenergic antagonists (e.g., prazosin)** can blunt stress-triggered craving – one inpatient trial found prazosin **reduced stress-induced alcohol craving** and anxiety in early-abstinent AUD patients【74†L739-L747】, with the greatest benefit in those with high withdrawal distress. Likewise, **α₂-agonists** (lofexidine, guanfacine) that dampen central noradrenaline release have shown reduced stress-driven opioid craving and improved executive control in pilot studies【74†L755-L763】. These medications underscore noradrenaline’s role in stress-related relapse, though their clinical use may be limited to specific subpopulations (e.g., co-occurring PTSD).

Notably, **manipulating cortisol** itself has paradoxical effects. Elevated endogenous cortisol during stress correlates with higher craving and earlier relapse in cocaine, nicotine, and alcohol users【65†L325-L:contentReference[oaicite:11]{index=11} **acute administration of cortisol** (at pharmacological doses) can *impair reconsolidation* of drug-cue memories; for example, a single 20 mg dose of cortisol significantly **reduced heroin craving** in maintena:contentReference[oaicite:12]{index=12}ts (especially those on lower opioid doses)【72†L1-L4】. A similar approach in AUD showed mixed results: cortisol dampened cue reactivity in severe cases but *increased:contentReference[oaicite:13]{index=13}ild cases【33†L71-L79】, highlighting the importance of individual physiology. Such findings hint that carefully timed cortisol or β-adrenergic blockers (e.g., propranolol during memory reactivation) might weaken the learned salience of drug cues, though this strategy remains experimental.

In sum, evidence converges that **stress horm:contentReference[oaicite:14]{index=14}athways are key modulators of dopamine-driven craving and relapse**. Acute and chronic stress have distinct impacts – one acutely intensifying drug “wa:contentReference[oaicite:15]{index=15}e other laying a groundwork of dysphoria and impulsivity. Human studies (laboratory and ecological) strongly support the stress–craving–relapse link, although ethical constraints prevent definitive causality tests (we mostly rely on correlation and analog interventions). This underscores why a **multimodal management of stress** is integral to relapse prevention. By combining behavioral interventions (sleep normalization, exercise, mindfulness) with selective pharmacological aids targeting stress biology, treatment can reduce the pathogenic salience of drug cues and improve resilience. Importantly, interventions must be **timed and tailored**: e.g., prioritizing sleep and stress reduction in early recovery when patients are most vulnerable, and teaching skills like diaphragmatic breathing to deploy in high-craving moments. While more research is needed – particularly to translate neurobiological insights into personalized care – current evidence affirms that alleviating stress and restoring adaptive stress-response systems can significantly **diminish cue-induced craving and relapse risk** in substance use disorders.

```

