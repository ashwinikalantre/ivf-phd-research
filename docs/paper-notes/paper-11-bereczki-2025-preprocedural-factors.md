# Paper 11: IVF Outcome Prediction Using Female Preprocedural Factors

## Citation

Bereczki, K., Bukva, M., Vedelek, V., Nádasdi, B., Kozinszky, Z., Sinka, R., Bereczki, C., Vágvölgyi, A., & Zádori, J. (2025). **Machine Learning-Based Prediction of IVF Outcomes: The Central Role of Female Preprocedural Factors**. *Biomedicines*, 13(11), Article 2768.

DOI: [https://doi.org/10.3390/biomedicines13112768](https://doi.org/10.3390/biomedicines13112768)

Sources checked:

- [PubMed record](https://pubmed.ncbi.nlm.nih.gov/41301861/)
- [University of Szeged repository record](https://publicatio.bibl.u-szeged.hu/38446)
- Repository PDF text extracted locally from the University of Szeged source

Related study terms:

- [IVF](../glossary/clinical-glossary.md#ivf)
- [ICSI](../glossary/clinical-glossary.md#icsi)
- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [AMH](../glossary/clinical-glossary.md#amh)
- [FSH](../glossary/clinical-glossary.md#fsh)
- [XGBoost](../glossary/technical-glossary.md#xgboost)
- [Feature importance](../glossary/technical-glossary.md#feature-importance)
- [Same-centre external validation](../glossary/technical-glossary.md#same-centre-external-validation)
- [Negative predictive value](../glossary/technical-glossary.md#negative-predictive-value)

## Why This Paper Matters

This paper is useful because it focuses on **first-visit / preprocedural prediction**.

Many IVF prediction papers use variables collected during treatment, after stimulation or after embryo development. That can improve prediction performance but limits usefulness before treatment begins.

This paper is different because it uses routinely available baseline variables such as female age, AMH, BMI, FSH, LH, sperm parameters and infertility duration.

For our PhD, it supports the idea that early counseling models can be built from clinic variables available before or at treatment initiation.

## Research Objective

The study aimed to develop and validate a per-cycle IVF outcome prediction model using only preprocedural clinical variables available at the first consultation.

The broader goal was early individualized counseling and treatment planning before treatment begins.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Retrospective single-centre prediction-model study |
| Country | Hungary |
| Center | Institute of Reproductive Medicine, University of Szeged |
| Primary data period | 21 January 2022 to 12 December 2023 |
| Primary modeled dataset | 1,243 IVF/ICSI cycles |
| Dataset before listwise deletion | 1,422 patient observations and 15 variables |
| External validation cohort | 92 additional IVF/ICSI cycles |
| External validation period | January to March 2025 |
| Validation type | Independent same-centre external validation without refitting or recalibration |
| Target outcome | IVF success / clinical pregnancy definition in methods; abstract keywords include clinical pregnancy and live birth |
| Ethics | Not fully extracted in current note; source PDF should be consulted if needed |

Confidence: **High**, except ethics details not extracted.

## Variables / Features Used

The initial model used 14 baseline predictors.

Confirmed variables include:

- female age
- AMH
- BMI
- FSH
- LH
- sperm concentration
- sperm motility
- male age
- infertility duration
- number of births
- sperm diagnosis categories such as normozoospermia, asthenozoospermia, teratozoospermia and cryptozoospermia

The refined model used nine predictors:

1. female age
2. AMH
3. BMI
4. FSH
5. LH
6. sperm concentration
7. sperm motility
8. male age
9. infertility duration

Confidence: **High**

## Method / Algorithm

| Area | Method |
| --- | --- |
| Main model | XGBoost classifier |
| Software version | XGBoost version 1.7.7.1 |
| Full model | 14 baseline predictors |
| Refined model | 9-variable model based on feature importance |
| Missing data handling | Listwise deletion |
| Validation | Untouched test set plus same-centre external validation cohort |
| Recalibration in external validation | None |
| Feature interpretation | XGBoost Gain, Cover and Frequency metrics |

Confidence: **High**

## Evaluation Metrics

The study reported:

- AUC
- accuracy
- 95% confidence interval
- sensitivity
- specificity
- positive predictive value
- negative predictive value
- balanced accuracy
- confusion matrix
- feature importance by Gain, Cover and Frequency

Confidence: **High**

## Main Findings

### Internal test-set performance

The refined 9-variable model achieved:

| Metric | Value |
| --- | ---: |
| AUC | 0.876 |
| Accuracy | 81.70% |
| 95% CI for accuracy | 76.30-86.30% |
| Sensitivity | 75.60% |
| Specificity | 84.40% |
| PPV | 68.60% |
| NPV | 88.50% |

### Same-centre external validation

External validation cohort:

- 92 patients
- 63 unsuccessful outcomes
- 29 successful outcomes

Performance:

| Metric | Value |
| --- | ---: |
| Accuracy | 78.30% |
| Sensitivity | 68.90% |
| Specificity | 82.50% |
| PPV | 69.00% |
| NPV | 82.50% |

### Feature importance findings

- Female age was the dominant high-impact predictor.
- AMH and BMI acted as frequent “workhorse” predictors.
- FSH, LH, sperm motility, sperm concentration, male age and infertility duration added supportive value.
- Variables without strong univariate significance could still contribute through non-linear interactions.

Confidence: **High**

## Limitations Stated by Authors

The authors acknowledge:

| Limitation | Meaning |
| --- | --- |
| Retrospective design | Prospective value is not proven. |
| Single-centre design | Wider generalizability is limited. |
| Need larger multicentre cohorts | External validation across other institutions is needed. |
| IVF success varies by institution | Protocols, technology and expertise differ across clinics. |
| Need clinic-specific calibration | Model estimates may need correction using local success rates. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Same-centre external validation only | Better than simple internal testing, but not equivalent to multi-centre external validation. |
| Short external validation window | January-March 2025 cohort is small and temporally narrow. |
| Listwise deletion | Removing records with missing values may introduce selection bias. |
| Preprocedural-only data | Useful for early counseling, but cannot capture embryo quality or treatment response. |
| No Indian validation | Hungary-only data; local validation in Indian clinics remains necessary. |
| No deployed CDSS | Counseling potential is discussed, but no clinician-facing system is tested. |
| Limited XAI depth | Feature importance is used, but patient-level explanation and clinician usability are not deeply evaluated. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- larger multi-centre validation
- clinic-specific calibration
- prospective validation
- integration into early counseling workflows
- validating whether preprocedural prediction helps patient preparedness and shared decision-making
- combining baseline data with later treatment and embryology variables where appropriate

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Pre-treatment counseling gap | Yes | Uses first-consultation variables only. |
| Need external validation | Yes | Same-centre validation exists, but multi-centre validation is still needed. |
| Clinical decision support gap | Yes | Counseling utility is discussed, but no CDSS is deployed. |
| Calibration gap | Yes | Authors recommend clinic-specific calibration. |
| Indian validation gap | Yes | Hungary-only dataset. |
| Multimodal data gap | Partial | Preprocedural model does not include embryology or image data. |
| Explainability gap | Partial | Feature importance is reported, but no detailed XAI/usability evaluation. |

## Usefulness For Our PhD

Relevance: **Medium-High**

This paper is important because it supports a practical early-counseling direction. It shows that useful IVF prediction may be possible before treatment begins using routinely collected variables.

For our PhD, it helps separate two possible model purposes:

1. **Pre-treatment counseling model** using baseline variables.
2. **Treatment-cycle outcome model** using stimulation, embryo and transfer variables.

This distinction is important when we talk to doctors and clinics about available data.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Bereczki et al. (2025) developed an XGBoost-based IVF outcome prediction model using routinely available first-consultation variables from 1,243 IVF/ICSI cycles, showing that a refined nine-variable model achieved strong internal test-set discrimination and maintained performance in a same-centre external validation cohort.

Gap-support sentence:

> Although the study supports preprocedural IVF counseling using baseline clinical variables, its retrospective single-centre design, small same-centre external validation cohort and lack of multicentre or Indian validation limit generalizability for broader clinical decision-support use.

## What This Paper Does Not Prove

This paper does not prove that:

- the model generalizes across countries or clinics.
- baseline variables alone are sufficient for embryo-transfer or live-birth prediction in all settings.
- same-centre validation is equivalent to multicentre external validation.
- the model is ready as a deployed CDSS.
- feature importance alone is enough for clinician trust.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Dataset | High |
| Variables/features | High |
| Model and metrics | High |
| Same-centre external validation | High |
| Author-stated limitations | High |
| Ethics details | Not extracted in current note |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
