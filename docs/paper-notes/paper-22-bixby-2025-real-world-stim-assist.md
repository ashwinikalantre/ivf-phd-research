# Paper 22: Real-World Use of Stim Assist for Ovarian Stimulation

## Citation

Bixby, C. J., & Miller, B. (2025). **Real-world use of an artificial intelligence-powered clinical decision support tool for ovarian stimulation**. *F&S Reports*, 6(2), 140-146.

DOI: [https://doi.org/10.1016/j.xfre.2025.01.015](https://doi.org/10.1016/j.xfre.2025.01.015)

Source checked: [F&S Reports article page](https://www.fertstertreports.org/article/S2666-3341%2825%2900017-0/fulltext)

Evidence note:

The publisher page was identified, but direct full-text extraction was limited. The note uses publisher/search-indexed abstract details and cross-checks with the known Stim Assist methodology already documented in [Paper 02](paper-02-canon-2024-stim-assist.md).

Related study terms:

- [Ovarian stimulation](../glossary/clinical-glossary.md#ovarian-stimulation)
- [FSH](../glossary/clinical-glossary.md#fsh)
- [Mature oocyte / Metaphase-II oocyte](../glossary/clinical-glossary.md#mature-oocyte-metaphase-ii-oocyte)
- [Trigger day](../glossary/clinical-glossary.md#trigger-day)
- [AMH](../glossary/clinical-glossary.md#amh)
- [AFC](../glossary/clinical-glossary.md#afc)
- [Estradiol](../glossary/clinical-glossary.md#estradiol)
- [Clinical Decision Support System](../glossary/technical-glossary.md#clinical-decision-support-system)
- [Historical Control](../glossary/technical-glossary.md#historical-control)
- [Real-World Evidence](../glossary/technical-glossary.md#real-world-evidence)

## Why This Paper Matters

This paper is important because it evaluates real-world clinician use of Stim Assist, an AI-powered clinical decision-support tool for ovarian stimulation.

It is useful for our PhD because it addresses a repeated gap:

- many IVF-AI papers only report model accuracy
- fewer papers evaluate actual use in clinical workflow
- this paper studies changes in physician decisions and patient outcomes after AI-assisted use

It also helps us understand what real-world deployment evidence looks like in IVF-AI.

## Research Objective

The study aimed to understand how treatment decisions and patient outcomes changed when physicians used AI to help determine:

- starting FSH dose
- trigger injection timing during ovarian stimulation

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Research article |
| Journal | F&S Reports |
| Year | 2025 |
| Study design | Retrospective cohort study with historical controls |
| Setting | One IVF clinic in the United States |
| Treatment arm | 292 patients treated with adjunctive clinician use of AI |
| Treatment period | December 2022 to December 2023 |
| Control arm | 292 matched historical control patients |
| Control period | May 2019 to May 2022 |
| Clinicians | Multiple physicians at the same IVF clinic |
| Tool | Stim Assist clinical decision-support software |
| Main clinical area | Ovarian stimulation |

Confidence: **High for abstract-confirmed details**

## Variables / Features Used

The article evaluates Stim Assist, which includes two AI-supported tools:

| Tool | Purpose | Inputs / Basis |
| --- | --- | --- |
| Starting Dose Tool | Helps select starting FSH dose | Baseline patient characteristics such as age, BMI, AMH and AFC, using similar historical patients |
| Trigger Tool | Helps optimize trigger timing | Follicle growth and hormone data such as estradiol |

Full variable table for Paper 22:

**Not confirmed from available source**

Confidence: **High for Stim Assist tool purpose; Medium for full variable set in this article**

## Method / Algorithm

Confirmed:

- AI-powered clinical decision-support software
- adjunctive clinician use, not autonomous AI decision-making
- matched historical-control comparison
- same clinic and same physicians used for historical comparison

Stim Assist algorithm background from Paper 02:

- Starting Dose Tool uses a K-nearest-neighbors style comparison with similar historical patients.
- Trigger Tool uses interpretable linear regression models using follicle sizes and estradiol.

Confidence: **High for CDSS design and study comparison; Medium for algorithm detail in this specific article because full text was not directly extracted**

## Evaluation Metrics

Primary endpoints:

- starting FSH dose
- total FSH dose
- number of MII oocytes retrieved at the end of stimulation

Safety:

- adverse events

Confidence: **High**

## Main Findings

After matching, treatment and control groups had no statistically significant differences in:

- age
- BMI
- AMH
- AFC

Main outcome comparison:

| Outcome | AI Use Group | Historical Control |
| --- | ---: | ---: |
| Average MII oocytes | 11.17 | 11.25 |
| Average starting FSH dose | 397.09 IU | 443.84 IU |
| Average total FSH dose | 4,181.77 IU | 4,654.71 IU |

Interpretation:

- AI use helped reduce starting FSH dose.
- AI use helped reduce total FSH dose.
- MII oocyte outcome was not adversely affected.
- No adverse events were introduced by AI use.

Confidence: **High**

## Limitations Stated By Authors

Not confirmed from full text.

The abstract/source snippets do not provide a full limitations section.

Confidence: **Not confirmed**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points based on available evidence.

| Critical Point | Why It Matters |
| --- | --- |
| Retrospective design | Historical-control comparison can be affected by time-related practice changes. |
| Single IVF clinic | Results may not generalize to other clinics or countries. |
| Intermediate outcome focus | MII oocyte count is important but not pregnancy or live birth. |
| No confirmed randomized design | Randomized evaluation would be stronger for causality. |
| No confirmed patient-centered outcomes | Cost, stress, satisfaction and live birth were not confirmed as main endpoints. |
| Explainability/user trust not fully confirmed | The study measures use/outcomes, but clinician explanation evaluation is not confirmed. |
| Indian population not included | Indian clinic validation would still be needed. |

Confidence: **High/Medium**

## Future Work Suggested

Not confirmed from full text.

Our evidence-based extension:

- test Stim Assist-like tools in multicenter prospective Indian settings
- include pregnancy and live-birth outcomes, not only MII oocytes
- measure medication cost and patient burden
- evaluate clinician trust, override reasons and explanation quality
- compare AI-supported decisions with standard protocols in randomized or pragmatic trials

Confidence: **Medium**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Real-world deployment evidence | Yes | The paper evaluates clinical use of an AI CDSS in practice. |
| Need prospective/RCT validation | Yes | Retrospective historical-control design limits causal interpretation. |
| Single-center study | Yes | Study was at one US IVF clinic. |
| Need external validation | Yes | Other clinics and populations need validation. |
| Intermediate outcome limitation | Yes | MII oocytes, not live birth, were primary outcome. |
| Clinical decision support gap | Yes | It directly studies CDSS use. |
| Lack of Indian population | Yes | Study is US-based. |

## Usefulness For Our PhD

Relevance: **Very High**

This paper is valuable because it shows that a CDSS can influence actual physician prescribing behavior in ovarian stimulation.

It supports our direction toward:

- doctor-facing decision support
- ovarian stimulation personalization
- medication-dose optimization
- real-world workflow evaluation
- measuring whether AI changes decisions without harming clinical outcomes

It also gives us a practical model for future clinic discussions:

- what decision does the tool support?
- what variables are available before the decision?
- how often do doctors follow or override AI advice?
- does the tool reduce medication use, cost or burden?
- does it preserve or improve clinical outcomes?

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Bixby and Miller (2025) evaluated real-world use of the Stim Assist AI-powered clinical decision-support tool in 292 ovarian-stimulation patients matched to 292 historical controls at a US IVF clinic, reporting reduced starting and total FSH doses without an adverse effect on MII oocyte yield.

Gap-support sentence:

> Although the study provides rare real-world CDSS evidence in IVF ovarian stimulation, its retrospective single-clinic historical-control design and intermediate MII outcome support the need for prospective, multicenter validation using pregnancy and live-birth outcomes.

## What This Paper Does Not Prove

This paper does not prove that:

- AI improves clinical pregnancy or live-birth rates.
- the CDSS generalizes to Indian IVF clinics.
- historical-control comparisons fully remove bias.
- clinicians will trust or use the tool in all settings.
- reduced FSH dose always reduces total patient cost.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation and DOI | High |
| Study design | High |
| Sample size and periods | High |
| Primary endpoints | High |
| Main abstract results | High |
| Full limitations | Not confirmed |
| Full variable table | Not confirmed |
| Author-stated future work | Not confirmed |
