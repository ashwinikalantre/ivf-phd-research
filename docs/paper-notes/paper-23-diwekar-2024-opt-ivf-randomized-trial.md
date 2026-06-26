# Paper 23: Opt-IVF Decision Support in a Multicenter Randomized Trial

## Citation

Diwekar, U., Gupta, S. N., Gahlan, A., Hota, S., Murdia, K., Murdia, N., Chandra, V., Bhoi, N., & Joag, S. (2024). **A new decision-support tool in a multi-center randomized trial for personalized, optimized, and simplified fertility treatment in non-PCOS patients**. *Reproduction and Fertility*, 5(3), e240013.

DOI: [https://doi.org/10.1530/RAF-24-0013](https://doi.org/10.1530/RAF-24-0013)

Sources checked:

- [PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC11466266/)
- [Reproduction and Fertility article page](https://raf.bioscientifica.com/view/journals/raf/5/3/RAF-24-0013.xml)
- Search-indexed article abstract and repository excerpts

Evidence note:

The PMC page was blocked by browser verification, but indexed abstract excerpts and journal metadata confirm the core study details. Exact table-level values should be checked from the article PDF before final thesis use.

Related study terms:

- [Ovarian stimulation](../glossary/clinical-glossary.md#ovarian-stimulation)
- [Gonadotropin dosage](../glossary/clinical-glossary.md#gonadotropin-dosage)
- [Ultrasonogram](../glossary/clinical-glossary.md#ultrasonogram)
- [Blastocyst](../glossary/clinical-glossary.md#blastocyst)
- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [OHSS](../glossary/clinical-glossary.md#ohss)
- [Clinical Decision Support System](../glossary/technical-glossary.md#clinical-decision-support-system)
- [Physics-Based Model](../glossary/technical-glossary.md#physics-based-model)
- [Optimal Control Theory](../glossary/technical-glossary.md#optimal-control-theory)
- [Ovarian Sensitivity Index](../glossary/technical-glossary.md#ovarian-sensitivity-index)

## Why This Paper Matters

This paper is important because it evaluates a decision-support tool in a randomized multicenter IVF setting.

It is especially useful for our PhD because it is closer to clinical decision support than many prediction-only papers. It studies whether Opt-IVF can:

- personalize gonadotropin dosing
- reduce repeated ultrasound monitoring
- guide trigger date
- reduce total hormone dose
- improve embryo and pregnancy-related outcomes

It also matters for us because the study appears to be from Indian IVF centers, making it relevant to our Indian clinic-validation angle.

## Research Objective

The study aimed to evaluate whether Opt-IVF, a clinical decision-support tool, could reduce cumulative gonadotropin dosage and repeated ultrasonogram monitoring without compromising good-quality blastocyst outcomes in non-PCOS IVF patients.

Confidence: **Medium-High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Clinical trial article |
| Journal | Reproduction and Fertility |
| Year | 2024 |
| Study design | Multicenter randomized trial |
| Trial registration | ClinicalTrials.gov ID NCT05811065 |
| Registration date | 15 March 2023 |
| First subject enrollment | 20 March 2023 |
| Population | Women aged 25-45 years undergoing IVF |
| Patient scope | Non-PCOS patients |
| Total participants | 115 women |
| Intervention group | 55 women randomized to Opt-IVF |
| Control group | 60 women randomized to standard clinical care |
| Intervention | Opt-IVF decision-support tool guiding gonadotropin dosing and trigger dates |

Confidence: **High for abstract-confirmed study design and sample size**

## Variables / Features Used

Confirmed:

- follicle size distribution data
- gonadotropin dosage
- day 5 monitoring information
- trigger date recommendation
- oocyte and MII outcomes
- good-quality blastocyst outcomes
- clinical pregnancy outcome

Opt-IVF background:

- The tool is described as using a physics-based model and optimal control theory.
- It provides personalized dosage profiles.
- It reduces the need for ultrasound exams after day 5.

Full variable list:

**Not confirmed from available source**

Confidence: **Medium-High**

## Method / Technology

| Component | Extracted Information |
| --- | --- |
| Tool | Opt-IVF |
| Type | Clinical decision-support tool |
| Modeling basis | Physics-based follicle development model |
| Optimization basis | Optimal control theory |
| Decision supported | Gonadotropin dosing and trigger date |
| Workflow intent | Personalized, optimized and simplified ovarian stimulation |

Confidence: **Medium-High**

## Evaluation Metrics

The study evaluated:

- total cumulative gonadotropin dosage
- number of repeated ultrasonograms / ultrasound monitoring burden
- number of oocytes retrieved
- number of MII oocytes retrieved
- number of good-quality blastocysts
- good-quality blastocyst rate
- ovarian sensitivity index
- pregnancy rate

Confidence: **Medium-High**

## Main Findings

Confirmed findings from indexed abstract/repository excerpts:

| Finding | Extracted Information |
| --- | --- |
| Gonadotropin dosage | Opt-IVF group required significantly lower cumulative gonadotropin dosage |
| Monitoring burden | Opt-IVF eliminated the need for ultrasound exams after day 5 |
| Oocytes retrieved | Opt-IVF group had higher number of oocytes retrieved |
| MII oocytes | Opt-IVF group had higher number of MII oocytes |
| Good-quality blastocysts | Number and rate were significantly higher in the Opt-IVF group |
| Ovarian sensitivity index | Significantly higher in the Opt-IVF group |
| Pregnancy rate | Significantly higher in the Opt-IVF group |
| Overall conclusion | Opt-IVF outperformed clinical teams in most reported outcomes |

Confidence: **Medium-High**

## Limitations Stated By Authors

Not fully confirmed from accessible source.

Likely scope limitation from title and design:

- non-PCOS population only
- small randomized trial sample

Confidence: **Medium**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Small randomized sample | 115 patients is useful but still limited for broad claims. |
| Non-PCOS-only scope | Results may not apply to PCOS patients or poor responders unless separately tested. |
| Outcome not clearly live birth | Pregnancy and blastocyst outcomes are important but final live-birth effect needs confirmation. |
| Tool ownership / conflict details need full text | Commercial tool studies require careful conflict-of-interest reading. |
| Exact statistical tables need PDF check | Thesis claims should use exact values only after full article verification. |
| Generalizability beyond participating centers | Even multicenter Indian results may not generalize to all Indian IVF clinics. |
| Explainability not confirmed | The tool optimizes dose but clinician-facing explanation quality is not confirmed. |

Confidence: **Medium-High**

## Future Work Suggested

Not fully confirmed from available source.

Our evidence-based extension:

- verify full paper tables and limitations
- evaluate Opt-IVF or similar CDSS in larger Indian multicenter cohorts
- include PCOS and poor-responder groups separately
- evaluate live birth and cumulative live birth
- assess clinician trust, override behavior and explanation usability
- assess cost, patient burden and monitoring reduction in Indian clinics

Confidence: **Medium**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Clinical decision support gap | Yes | The paper evaluates a CDSS in IVF stimulation. |
| Personalized recommendation gap | Yes | Opt-IVF provides individualized dose/trigger recommendations. |
| Need randomized validation | Partially addressed | It is randomized, which is stronger than retrospective studies. |
| Small dataset | Yes | Trial included 115 women. |
| Limited population scope | Yes | Non-PCOS patients only. |
| Need broader external validation | Yes | Wider clinic and subgroup validation remains needed. |
| Need live-birth outcome | Likely | Live-birth outcome is not confirmed from available source. |
| Indian relevance | Yes | This paper is especially relevant if trial centers were Indian IVF centers. |

## Usefulness For Our PhD

Relevance: **Very High**

This paper is highly useful because it connects directly to:

- ovarian stimulation decision support
- personalized gonadotropin dosing
- reduced monitoring burden
- randomized clinical evaluation
- Indian IVF relevance

It supports our direction toward an explainable, clinician-facing IVF decision-support framework. It also shows that the final PhD topic could reasonably focus on decision support rather than only prediction.

For clinic discussions, this paper suggests asking:

- Can we access gonadotropin dose records?
- Are follicle measurements available on day 1/day 5 and later visits?
- Are ultrasound visits recorded clearly?
- Are trigger dates recorded?
- Are MII oocytes, blastocyst quality and pregnancy outcomes available?
- Can doctors evaluate whether suggested dose changes are clinically acceptable?

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Diwekar et al. (2024) evaluated Opt-IVF, a physics-based decision-support tool using optimal control theory, in a multicenter randomized trial of 115 non-PCOS IVF patients and reported reduced gonadotropin dosage, reduced ultrasound monitoring after day 5, and improved blastocyst and pregnancy-related outcomes in the intervention group.

Gap-support sentence:

> Although Opt-IVF provides comparatively strong randomized evidence for ovarian stimulation decision support, its small non-PCOS sample and limited confirmed live-birth evidence indicate the need for broader validation across patient subgroups and clinically final outcomes.

## What This Paper Does Not Prove

This paper does not prove that:

- Opt-IVF improves live-birth rates.
- the tool works equally well in PCOS or poor-responder patients.
- all Indian IVF clinics can adopt the same workflow.
- the model explanation is sufficient for clinician trust.
- a sample of 115 patients is enough for national-level deployment.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation and DOI | High |
| Trial design and sample size | High |
| Intervention/control allocation | High |
| Main abstract findings | Medium-High |
| Exact table values | Not confirmed |
| Limitations stated by authors | Medium |
| Conflict-of-interest details | Not confirmed |
| Future work stated by authors | Not confirmed |
