# Paper 01: Explainable AI for Follicle Optimization in IVF

## Citation

Hanassab, S., Nelson, S. M., Akbarov, A., Yeung, A. C., Hramyka, A., Alhamwi, T., Salim, R., Comninos, A. N., Trew, G. H., Kelsey, T. W., Heinis, T., Dhillo, W. S., & Abbara, A. (2025). **Explainable artificial intelligence to identify follicles that optimize clinical outcomes during assisted conception**. *Nature Communications*, 16, Article 296.

DOI: [https://doi.org/10.1038/s41467-024-55301-y](https://doi.org/10.1038/s41467-024-55301-y)

Source checked: [Nature Communications article page](https://www.nature.com/articles/s41467-024-55301-y)

Related study terms:

- [Follicle](../glossary/clinical-glossary.md#follicle)
- [Oocyte](../glossary/clinical-glossary.md#oocyte)
- [Mature oocyte / metaphase-II oocyte](../glossary/clinical-glossary.md#mature-oocyte-metaphase-ii-oocyte)
- [Ovarian stimulation](../glossary/clinical-glossary.md#ovarian-stimulation)
- [Trigger day](../glossary/clinical-glossary.md#trigger-day)
- [Gradient boosting](../glossary/technical-glossary.md#gradient-boosting)
- [SHAP](../glossary/technical-glossary.md#shap)
- [TreeSHAP](../glossary/technical-glossary.md#treeshap)
- [Leave-one-clinic-out cross-validation](../glossary/technical-glossary.md#leave-one-clinic-out-cross-validation)

## Why This Paper Matters

This is a strong paper for our research because it connects:

- IVF treatment decision-making
- explainable AI
- multi-center data
- ovarian stimulation and trigger timing
- clinical outcome optimization

It does not only predict an outcome. It uses explainable AI to identify follicle-size patterns that may help personalize ovarian stimulation decisions.

## Research Objective

The paper aimed to identify which follicle sizes on the day of trigger administration contribute most to mature oocyte retrieval and downstream IVF outcomes.

The clinical motivation was that IVF trigger timing is often guided by simple rules based on a few lead follicles, while the full follicle cohort contains richer information.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Retrospective multi-center cohort study |
| Population | Treatment-naive female IVF/ICSI patients |
| Sample size | 19,082 female participants |
| Centers | 11 IVF centers |
| Countries | United Kingdom and Poland |
| Study years | 2005 to 2023 |
| Age range | 18 to 49 years |
| Main inclusion condition | At least three follicles greater than 10 mm on the day of trigger administration |
| Primary outcome | Number of mature metaphase-II oocytes where maturity grading was available |
| Important secondary outcomes | All oocytes, 2PN zygotes, high-quality blastocysts, live birth association |
| Ethics | Health Research Authority approval reported; clinics licensed under UK or Polish ART regulation |

Confidence: **High**

## Variables / Features Used

The main input variables were individual follicle-size counts on the day of trigger administration.

Additional variables were also examined:

- age
- BMI
- days of stimulation
- IVF protocol type
- estradiol on day of trigger
- trigger type

The paper also analyzed follicle-size information from one and two days before the trigger day.

Confidence: **High**

## Method / Algorithm

| Area | Method |
| --- | --- |
| Main model | Histogram-based gradient boosting regression tree |
| Validation approach | Leave-one-clinic-out cross-validation |
| Hyperparameter tuning | Nested validation with Bayesian optimization |
| Explainability | Permutation importance and SHAP / TreeSHAP |
| Comparison / sensitivity | Multilayer perceptron model and restricted-data sensitivity analysis |
| Additional statistical analysis | Logistic regression for association with live birth rate |

Confidence: **High**

## Evaluation Metrics

| Metric | Use |
| --- | --- |
| Mean absolute error | Main model optimization and performance metric |
| R-squared | Reported for predictive performance |
| Permutation importance | Used to identify contributory follicle sizes |
| SHAP values | Used for model explanation |
| Logistic regression association | Used for live birth association analysis |

Confidence: **High**

## Main Findings

The most important findings were:

- Follicles sized **13-18 mm** on the day of trigger contributed most to mature oocyte retrieval.
- Follicles sized **13-18 mm** were also important for 2PN zygotes.
- Follicles sized **14-20 mm** were important for high-quality blastocysts.
- Larger follicles, especially those **greater than 18 mm**, were associated with premature progesterone elevation and possible negative impact on live birth rate in fresh embryo transfer.
- The authors suggest that considering the full follicle cohort may be better than relying only on the largest lead follicles.

Confidence: **High**

## Limitations Stated by Authors

The paper clearly states that the proposed approach requires **prospective randomized controlled trial evaluation** before it can be treated as a definitive clinical strategy.

The authors also frame the clinical decision-support use as potential, not already proven for routine deployment.

Confidence: **High**

## Hidden Limitations / Our Critical View

These are not accusations against the paper. They are points relevant to our PhD gap analysis.

| Critical Point | Why It Matters |
| --- | --- |
| European dataset only | Strong multi-center design, but not validated in Indian IVF population. |
| Retrospective design | Useful for discovery, but prospective clinical impact is not proven. |
| Focused clinical decision | It supports trigger-timing insight, not a complete IVF outcome CDSS. |
| Limited lifestyle integration | Lifestyle variables are not central to the model. |
| No patient-facing explanation evaluation | XAI is technical/clinical; patient-centered usefulness is not the focus. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- prospective evaluation
- randomized trial comparison of trigger strategies
- clinical decision-support use
- personalization of IVF ovarian stimulation decisions

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need prospective/RCT validation | Yes | Authors explicitly state the need for prospective evaluation. |
| Need clinical decision support | Yes | Paper points toward CDSS use but does not fully deploy a general CDSS. |
| External/Indian validation gap | Yes | Multi-center Europe, but no Indian validation. |
| Explainable AI relevance | Yes | Strong example of XAI in IVF. |
| Personalized treatment recommendation | Yes | Strongly connected to personalized ovarian stimulation and trigger timing. |
| Lifestyle data gap | Limited | Lifestyle is not a central feature group. |

## Usefulness For Our PhD

Relevance: **High**

This paper is useful because it proves that XAI can generate clinically interpretable IVF treatment insights from multi-center data. It supports our argument that the important research direction is not only prediction, but explainable and clinically usable decision support.

It also supports a careful gap: even a strong multi-center XAI paper still calls for prospective validation and does not solve Indian-context validation.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Hanassab et al. (2025) demonstrated that explainable machine learning can identify clinically meaningful follicle-size ranges associated with mature oocyte retrieval and downstream IVF outcomes using data from 19,082 treatment-naive patients across 11 European IVF centers.

Gap-support sentence:

> Although the study provides a strong example of XAI-supported personalization in ovarian stimulation, the authors highlight the need for prospective evaluation, and the findings still require validation in local clinical contexts before routine decision-support use.

## What This Paper Does Not Prove

This paper does not prove that:

- AI can independently decide IVF treatment.
- the approach is already validated for Indian IVF clinics.
- prospective clinical outcomes will improve without trial evidence.
- lifestyle variables are necessary or sufficient for IVF outcome prediction.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Dataset | High |
| Methods | High |
| Main findings | High |
| Limitations/future work | High |
| Hidden limitations | Medium/High |
| Connection to our PhD | High |
