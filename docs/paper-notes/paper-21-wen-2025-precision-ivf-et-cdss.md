# Paper 21: AI-Driven Precision Treatment for IVF-ET Ovarian Stimulation Protocol Choice

## Citation

Wen, L., Wu, D., Ruan, J., Wang, R., Long, R., Chen, R., Hu, C., Tian, C., Zhang, Y., Pan, W., Jin, L., & Liao, S. (2025). **Artificial intelligence-driven precision treatment of reproductive medicine-related diseases: the optimal protocol choice for IVF-ET**. *Journal of Advanced Research*.

DOI: [https://doi.org/10.1016/j.jare.2025.10.040](https://doi.org/10.1016/j.jare.2025.10.040)

Source checked: [PubMed record](https://pubmed.ncbi.nlm.nih.gov/41139020/)

Evidence note:

The paper was **e-published on 23 October 2025** and is listed in the **July 2026 issue** of *Journal of Advanced Research*, volume 85, pages 919-933. For our 2021-2025 review window, it should be treated as a 2025 online publication but noted carefully because the issue publication is 2026.

Related study terms:

- [IVF](../glossary/clinical-glossary.md#ivf)
- [ICSI](../glossary/clinical-glossary.md#icsi)
- [Embryo transfer](../glossary/clinical-glossary.md#embryo-transfer)
- [Ovarian stimulation](../glossary/clinical-glossary.md#ovarian-stimulation)
- [Antagonist protocol](../glossary/clinical-glossary.md#antagonist-protocol)
- [Estradiol](../glossary/clinical-glossary.md#estradiol)
- [Progesterone](../glossary/clinical-glossary.md#progesterone)
- [Endometrial thickness](../glossary/clinical-glossary.md#endometrial-thickness)
- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [Clinical Decision Support System](../glossary/technical-glossary.md#clinical-decision-support-system)
- [Precision Medicine](../glossary/technical-glossary.md#precision-medicine)
- [Cost-Effectiveness](../glossary/technical-glossary.md#cost-effectiveness)
- [ICER](../glossary/technical-glossary.md#icer)

## Why This Paper Matters

This is one of the most important papers for our PhD direction because it moves beyond simple outcome prediction.

It directly studies:

- ovarian stimulation protocol selection
- personalized treatment recommendation
- AI-assisted clinical decision support
- cost and time reduction
- evaluation using a later dataset

This is close to our target idea of an explainable, clinically useful IVF decision-support framework.

## Research Objective

The study proposed an AI system that analyzes IVF-ET cycles to uncover relationships between ovarian stimulation choices and pregnancy outcomes, enabling personalized treatment recommendations while improving success rates and reducing unnecessary cost.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Research article |
| Journal | Journal of Advanced Research |
| E-publication date | 23 October 2025 |
| Issue listing | July 2026, volume 85, pages 919-933 |
| Clinical site | Tongji Hospital |
| Country | China |
| Training/development dataset | 17,791 patients |
| Study period | May 2015 to May 2019 |
| Treatment scope | Ovarian stimulation and IVF/ICSI |
| New evaluation dataset | 4,251 patients |
| Main intervention idea | AI-assisted CDSS for ovarian stimulation protocol selection |
| Outcome focus | Clinical pregnancy and pregnancy grading |

Confidence: **High from PubMed abstract**

## Variables / Features Used

The adaptive AI model integrated:

- personal characteristics
- ovarian reserve factors
- etiological factors

Key predicted/used indicators on hCG day:

| Indicator | Meaning |
| --- | --- |
| Progesterone (P) | Hormone linked with endometrial readiness and stimulation response |
| Number of oocytes retrieved (NOR) | Ovarian response and oocyte yield |
| Estradiol (E2) | Hormonal response during stimulation |
| Endometrial thickness (EMT) | Uterine lining measurement |

Full variable list:

**Not confirmed from available abstract-level source**

Confidence: **High for key indicators; Medium for full feature set**

## Method / Algorithm

Confirmed method-level description:

- adaptive AI model
- AI-assisted CDSS
- personalized ovarian stimulation selection
- pregnancy outcome grading system
- cost-effectiveness evaluation

The local matrix/student extraction mentions an adaptive ensemble/ACA-FI framework using Random Forest, XGBoost and SOIL feature-selection approaches. These details require full-text confirmation before being used as thesis claims.

Confidence: **High for PubMed-confirmed adaptive AI/CDSS details; Medium for exact algorithm names beyond abstract**

## Evaluation Metrics

The study evaluated:

- clinical pregnancy rate
- pregnancy grading levels
- number of patients moved to better pregnancy-probability levels after optimization
- recommended protocol distribution
- time savings
- cost reduction
- ICER / cost-effectiveness dominance
- statistical significance of clinical pregnancy and cost changes

Confidence: **High**

## Main Findings

Pregnancy grading system:

| Level | Total Score | Pregnancy Rate |
| --- | --- | ---: |
| Level IV | 15-16 | 0.55 |
| Level III | 13-14 | 0.44 |
| Level II | 11-12 | 0.24 |
| Level I | 4-10 | 0.07 |

Optimization movement:

| Initial Level | Improved After OS Optimization |
| --- | ---: |
| Level I | 1,355 patients improved |
| Level II | 2,290 of 2,341 patients improved |
| Level III | 1,448 of 3,839 patients improved |

CDSS protocol and economic findings:

| Finding | Value |
| --- | ---: |
| Patients prioritized for GnRH antagonist regimen | 54.64% |
| Per-patient time savings | 15.39-33.48 days |
| Per-patient cost reduction | ¥989-¥2,623 |
| Projected national direct savings in China | ¥0.54-1.43 billion/year |

New evaluation dataset:

| Outcome | Without / Before CDSS | With CDSS Recommendations |
| --- | ---: | ---: |
| Clinical pregnancy rate | 0.452 | 0.512 |
| Mean per-cycle cost | ¥7,385 | ¥7,242 |
| ICER | Saving of ¥2,383 per additional clinical pregnancy |

The increase in clinical pregnancy rate was statistically significant (p < 0.001), and the cost reduction was also statistically significant (p = 0.018).

Confidence: **High**

## Limitations Stated By Authors

Not confirmed from available abstract-level source.

The PubMed abstract does not provide a detailed limitations section.

Confidence: **Not confirmed**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points based on confirmed information.

| Critical Point | Why It Matters |
| --- | --- |
| Outcome is clinical pregnancy, not live birth | Clinical pregnancy is useful but not the final IVF success outcome. |
| Single hospital development dataset | Tongji Hospital data may not generalize to other clinics or countries. |
| China-specific cost model | Cost savings may not transfer to Indian IVF economics. |
| Full algorithm details not confirmed from abstract | We need full text before citing exact model architecture. |
| Real-world implementation details need checking | Abstract says CDSS recommendations were evaluated, but full workflow and clinician adherence require full-text review. |
| Explainability not confirmed | CDSS recommendation is useful, but explanation method for clinicians is not confirmed from abstract. |
| Indian population not included | Indian validation would still be required. |

Confidence: **High/Medium**

## Future Work Suggested

Not confirmed from available abstract-level source.

Our evidence-based extension:

- obtain and read full article for limitations and algorithm architecture
- verify whether the evaluation was prospective, retrospective, temporal or quasi-deployment
- assess clinician-facing explanation and usability
- test whether the approach can generalize to Indian IVF clinics
- adapt cost-effectiveness evaluation to Indian clinic pricing and patient affordability
- consider live-birth or cumulative live-birth outcome if available

Confidence: **Medium**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Personalized recommendation gap | Yes | The paper directly recommends ovarian stimulation protocols. |
| Clinical decision support gap | Yes | It develops an AI-assisted CDSS. |
| Cost-effectiveness gap | Yes | It evaluates time and cost savings. |
| Need external validation | Likely | Development data are from Tongji Hospital; cross-country validation is not confirmed. |
| Lack of Indian population | Yes | Study is China-based. |
| Need explainability | Likely | Clinician-facing explanation is not confirmed from abstract. |
| Stronger outcome label gap | Yes | Clinical pregnancy is used, not live birth. |

## Usefulness For Our PhD

Relevance: **Very High**

This paper strongly supports shifting our topic from only “prediction” toward:

- personalized treatment recommendation
- ovarian stimulation decision support
- clinical pregnancy outcome grading
- cost-aware IVF decision support
- clinician-facing CDSS

It also helps us ask doctors better data-access questions:

- Are ovarian stimulation protocol details available?
- Are hormone levels on hCG day available?
- Are oocyte retrieval counts available?
- Are endometrial thickness values available?
- Are treatment costs and time-to-treatment variables available?
- Can clinicians evaluate whether AI protocol suggestions are reasonable?

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Wen et al. (2025) developed an AI-assisted clinical decision-support system using 17,791 IVF/ICSI patients from Tongji Hospital to personalize ovarian stimulation protocol selection, using hCG-day progesterone, oocyte number, estradiol and endometrial thickness to construct pregnancy grading and cost-aware treatment recommendations.

Gap-support sentence:

> Although the study reported improved clinical pregnancy rate and reduced per-cycle cost in a new evaluation dataset, its China-based clinical and economic setting indicates the need for local validation and adaptation before application in Indian IVF clinics.

## What This Paper Does Not Prove

This paper does not prove that:

- the CDSS improves live-birth rate.
- the model generalizes to Indian IVF clinics.
- the same cost savings apply in India.
- clinicians will trust the recommendations without explainability.
- the exact algorithm architecture can be cited without full-text confirmation.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation and DOI | High |
| E-publication and issue timing | High |
| Dataset size and site | High |
| Objective and CDSS purpose | High |
| Main abstract results | High |
| Exact algorithm architecture | Medium |
| Full limitations | Not confirmed |
| Author-stated future work | Not confirmed |
