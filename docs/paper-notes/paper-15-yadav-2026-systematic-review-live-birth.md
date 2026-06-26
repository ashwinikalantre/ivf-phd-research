# Paper 15: Systematic Review of AI-Based Live-Birth Prediction in IVF

## Citation

Yadav, R., Banerjee, D., & James Raj K. (2026). **AI-based live birth prediction in IVF cycles: a systematic review without meta-analysis of model performance and validation**. *Middle East Fertility Society Journal*, 31, Article 44.

DOI: [https://doi.org/10.1186/s43043-026-00334-0](https://doi.org/10.1186/s43043-026-00334-0)

Source checked: [Springer Nature article page](https://link.springer.com/article/10.1186/s43043-026-00334-0)

Evidence note:

This paper was published on **19 May 2026**, so it is outside the original 2021-2025 paper window. It is still useful as synthesis evidence because it reviews AI-based live-birth prediction studies up to January 2026 and directly summarizes validation and bias issues relevant to our PhD.

Related study terms:

- [Systematic review](../glossary/technical-glossary.md#systematic-review)
- [PRISMA](../glossary/technical-glossary.md#prisma)
- [PROSPERO](../glossary/technical-glossary.md#prospero)
- [QUADAS-2](../glossary/technical-glossary.md#quadas-2)
- [GRADE](../glossary/technical-glossary.md#grade)
- [Selection bias](../glossary/technical-glossary.md#selection-bias)
- [Internal validation overfitting](../glossary/technical-glossary.md#internal-validation-overfitting)
- [Noninferiority trial](../glossary/technical-glossary.md#noninferiority-trial)

## Why This Paper Matters

This paper is important because it systematically reviews AI models that predict **live birth**, which is one of the strongest IVF outcomes.

It is especially useful for our PhD because it does not only ask whether models have high AUC. It examines:

- model architecture
- input modality
- validation methodology
- risk of bias
- clinical utility
- prospective evidence

This supports our repeated gap: IVF-AI models often show promising retrospective performance, but clinical translation is limited by validation, bias and deployment evidence.

## Research Objective

The review aimed to evaluate diagnostic performance and validation methodologies of AI-based predictive models for achieving live birth after IVF cycles.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Systematic review without meta-analysis |
| Reporting guideline | PRISMA 2020 |
| Protocol registration | PROSPERO CRD420261298569 |
| Search period | January 2010 to January 2026 |
| Databases | PubMed/MEDLINE, Scopus, EMBASE, Web of Science, CENTRAL |
| Included studies | 23 primary clinical studies |
| Study designs included | 20 retrospective cohort studies, 2 prospective cohort studies, 1 randomized controlled trial |
| Validation datasets | Around 45,000 embryos/cycles across validation cohorts |
| Training datasets | More than 200,000 embryos/cycles |
| Risk of bias tool | QUADAS-2 |
| Certainty assessment | Modified GRADE approach |
| Meta-analysis | Not performed due to heterogeneity |

Confidence: **High**

## Inclusion and Exclusion Scope

Included studies:

- original research articles
- AI/ML models for embryo assessment or IVF outcome prediction
- patients undergoing IVF/ICSI with embryo transfer
- live birth as primary, secondary or follow-up outcome
- quantitative performance metrics reported

Excluded studies:

- reviews, commentaries, editorials
- conference abstracts without full text
- non-embryological AI applications unless directly linked to embryo-related live birth/pregnancy prediction
- animal, in vitro and simulation studies
- studies without clinical outcome data
- studies without quantitative predictive metrics

Confidence: **High**

## Data Extracted By Review Authors

The review extracted:

- study characteristics
- population characteristics
- sample size
- maternal age
- BMI
- infertility etiology
- IVF indications
- AI architecture
- input modality
- training data size
- number of centers
- validation approach
- outcome definitions
- diagnostic accuracy metrics
- comparator performance
- calibration, generalizability and subgroup analyses
- risk of bias

Confidence: **High**

## Main Findings

### Included study distribution

| Study Type | Count |
| --- | ---: |
| Retrospective cohort | 20 |
| Prospective cohort | 2 |
| Randomized controlled trial | 1 |

Geographic distribution:

- Asia: 12 studies, 52%
- Europe: 5 studies, 22%
- North America: 2 studies, 9%
- multicentre international collaborations: 3 studies, 13%
- Australia: 1 study, 4%

### Model-performance synthesis

| Model/Input Type | Reported Performance Summary |
| --- | --- |
| Multimodal models | Highest performance; up to AUC 0.97, accuracy 74-82% |
| Time-lapse models | AUC 0.64-0.97; accuracy 64-78% |
| Clinical-variable-only models | AUC 0.70-0.80; accuracy 76-78% |
| Static image models | Lowest accuracy range, 62-69% |
| Center-based models | Outperformed national registry-based models |

### Prospective/RCT evidence

The review notes that the single prospective double-blind randomized controlled trial comparing iDAScore with traditional morphology did **not** demonstrate noninferiority, with clinical pregnancy rates of 46.5% versus 48.2%.

Confidence: **High**

## Limitations / Cautions Stated By Authors

The authors conclude that:

| Limitation / caution | Meaning |
| --- | --- |
| Evidence heavily retrospective | Most included studies were retrospective cohorts. |
| Selection bias risk | Retrospective embryo studies may include only transferred embryos. |
| Internal validation overfitting | Some models may perform well internally but fail externally. |
| Heterogeneity | Models, datasets, outcomes and validation methods differ widely. |
| Prospective RCT evidence is weak | Independent clinical superiority/noninferiority is not proven. |
| AI should be supplementary | Current evidence supports AI as a supplementary embryologist tool only. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Outside original target window | Use as synthesis support, not as a core 2021-2025 paper. |
| Review focuses heavily on embryo assessment/live birth | It is highly relevant, but not a full CDSS implementation review. |
| No meta-analysis | Results are descriptive because studies are heterogeneous. |
| Some included studies extend beyond our period | Need careful citation if our review chapter says 2021-2025 only. |
| AI as supplementary tool | Supports conservative framing: decision support, not replacement. |

Confidence: **High/Medium**

## Future Work Suggested

The review supports future work in:

- prospective multicenter studies
- randomized controlled trials
- standardized outcome definitions
- better reporting of calibration and fairness
- external validation
- subgroup validation
- transparent and explainable model reporting
- avoiding selection bias in transferred-embryo datasets
- evaluating real clinical utility before deployment

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need external validation | Yes | Internal validation overfitting is a central issue. |
| Need prospective/RCT validation | Yes | RCT evidence is limited and not clearly positive. |
| Selection bias gap | Yes | Retrospective transferred-embryo datasets can bias conclusions. |
| Trustworthy AI gap | Yes | The review stresses validation and transparent reporting. |
| Need multimodal data | Yes | Multimodal models showed strongest performance. |
| Real-world deployment gap | Yes | Current evidence supports supplementary use only. |
| Clinical decision support gap | Partial | It supports decision-support framing but is focused on model evidence. |

## Usefulness For Our PhD

Relevance: **High as synthesis, outside original year window**

This paper is valuable because it confirms many repeated gaps we have already seen across individual papers:

- retrospective evidence dominates
- selection bias is common
- external validation is limited
- high AUC does not prove clinical utility
- multimodal models are promising but need stronger validation
- AI should currently support, not replace, embryologists

It is especially useful in the literature-review conclusion and gap-analysis section.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Yadav et al. (2026) systematically reviewed AI-based live-birth prediction models in IVF and found that multimodal approaches reported the strongest performance, but the evidence base was dominated by retrospective studies with heterogeneous validation methods and risk of selection bias.

Gap-support sentence:

> The review concluded that prospective RCT evidence has not yet established independent superiority or noninferiority of AI-based IVF prediction, supporting the need for externally validated, transparent and clinically evaluated decision-support frameworks.

## What This Paper Does Not Prove

This paper does not prove that:

- AI improves live-birth rates in routine IVF care.
- multimodal models are always better in every clinic.
- embryo AI should replace embryologists.
- retrospective AUC values are enough for deployment.
- the reviewed evidence directly applies to Indian IVF clinics.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Review design | High |
| Included study counts | High |
| Model-performance ranges | High |
| Limitations/conclusions | High |
| Dataset/model metrics for individual studies | Medium unless original studies are checked |
| Connection to our PhD | High |
