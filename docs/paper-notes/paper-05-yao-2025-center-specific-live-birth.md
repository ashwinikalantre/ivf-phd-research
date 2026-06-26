# Paper 05: Center-Specific ML Models for IVF Live-Birth Prediction

## Citation

Yao, M. W. M., Nguyen, E. T., Retzloff, M. G., Gago, L. A., Nichols, J. E., Payne, J. F., Ripps, B. A., Opsahl, M., Groll, J., Beesley, R., Neal, G., Adams, J., Nowak, L., Swanson, T., & Chen, X. (2025). **Machine learning center-specific models show improved IVF live birth predictions over US national registry-based model**. *Nature Communications*, 16, Article 3661.

DOI: [https://doi.org/10.1038/s41467-025-58744-z](https://doi.org/10.1038/s41467-025-58744-z)

Source checked: [Nature Communications article page](https://www.nature.com/articles/s41467-025-58744-z)

Related study terms:

- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [AMH](../glossary/clinical-glossary.md#amh)
- [Clinical decision support system](../glossary/technical-glossary.md#clinical-decision-support-system)
- [External validation](../glossary/technical-glossary.md#external-validation)
- [Calibration](../glossary/technical-glossary.md#calibration)
- [Brier score](../glossary/technical-glossary.md#brier-score)
- [Precision-recall AUC](../glossary/technical-glossary.md#precision-recall-auc)
- [F1 score](../glossary/technical-glossary.md#f1-score)
- [Data drift](../glossary/technical-glossary.md#data-drift)
- [Concept drift](../glossary/technical-glossary.md#concept-drift)
- [TRIPOD + AI](../glossary/technical-glossary.md#tripod-ai)

## Why This Paper Matters

This paper is important because it compares localized, center-specific IVF live-birth prediction models with a national registry-based model.

It is useful for our PhD because it supports a central argument:

> IVF prediction models may need local validation because patient characteristics, clinical workflows and treatment practices differ across centers.

This directly supports our Indian validation concern. A model trained on large national or international data may not be enough for a local clinic unless it is validated or recalibrated for that setting.

## Research Objective

The study aimed to compare:

1. machine learning, center-specific live-birth prediction models
2. the US Society for Assisted Reproductive Technology national registry-based model

The main question was whether center-specific ML models provide more clinically useful live-birth probability estimates than the SART national model for patients receiving IVF counseling at six US fertility centers.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Retrospective model validation study |
| Country | United States |
| Centers | Six unrelated small-to-midsize fertility centers |
| Geographic spread | 22 locations across 9 states and 4 US regions |
| Patient sample | 4,635 patients' first-IVF cycle data in abstract |
| Validation comparison set | DNMV1 test set with 4,645 first-IVF cycles |
| Comparator model | SART national registry-based model |
| Local model type | Machine learning center-specific models |
| Outcome | Live birth probability |
| Model lifecycle | MLCS1, MLCS2, internal cross-validation, external/live model validation, production validation |
| Ethics | IRB exempt status for secondary research using de-identified data |
| Data sharing | Clinical datasets not shareable because owned by six third-party entities |

Confidence: **High**

## Variables / Features Used

The paper refers to clinical variables and diagnostic frequencies used in IVF live-birth prediction.

Confirmed variables or variable groups include:

- female age
- AMH
- first IVF cycle information
- clinical diagnostic frequencies
- center-specific patient characteristics
- SART model usage criteria variables

The article states that 17 key clinical variables or diagnostic frequencies were used in data-drift analysis.

Full exact model feature list requires supplementary table review.

Confidence: **Medium/High**

## Method / Algorithm

| Area | Method |
| --- | --- |
| Main model | Machine learning center-specific live-birth prediction models |
| Model versions | MLCS1 and MLCS2 |
| Comparator | SART national registry-based prediction model |
| Validation | Internal cross-validation and external/live model validation |
| External validation type | Out-of-time test sets contemporaneous with clinical model usage |
| Drift testing | Clinical data drift and concept drift assessment |
| Reclassification | 4 x 4 prognostic-category reclassification table |
| Reporting | TRIPOD + AI / EQUATOR reporting guidance |

The exact ML algorithm family is not clearly stated in the visible main article text. Therefore, the paper should be described as **center-specific machine learning models**, not as a specific algorithm such as Random Forest or XGBoost unless the supplementary material confirms it.

Confidence: **High** for study method; **not confirmed** for exact algorithm family.

## Evaluation Metrics

| Metric | Meaning |
| --- | --- |
| ROC-AUC | Discrimination performance |
| PLORA | Predictive power compared with age-only model |
| Brier score | Calibration performance |
| Precision-recall AUC | Ability to balance precision and recall, useful for false positive/false negative minimization |
| F1 score | Harmonic mean of precision and recall at specific live-birth probability thresholds |
| Reclassification table | Shows how patients move across prognostic categories between MLCS and SART |
| Data-drift tests | Checked whether clinical variable distributions changed over time |

Confidence: **High**

## Main Findings

Important confirmed findings:

| Finding | Result |
| --- | --- |
| Sample | 4,635 first-IVF-cycle patients from six centers in abstract |
| MLCS vs age-only model | MLCS showed improved ROC-AUC over age models across centers |
| Updated MLCS2 vs MLCS1 | MLCS2 had improved PLORA while ROC-AUC was comparable |
| Live model validation | MLCS1 external/live validation did not significantly differ from internal cross-validation results |
| MLCS2 vs SART calibration | MLCS2 had significantly lower, better Brier scores than SART |
| F1 at 50% live-birth probability threshold | MLCS2 median 0.74 vs SART median 0.71; p < 0.05 |
| PR-AUC | MLCS2 median 0.75 vs SART median 0.69; p < 0.05 |
| Prognostic categorization | MLCS assigned more patients to live-birth probability >= 50% and >= 75% compared with SART |

The authors interpret MLCS as more useful for personalized prognostic counseling and cost-success transparency.

Confidence: **High**

## Limitations Stated by Authors

The paper discusses these limitations and next steps:

| Limitation / caution | Meaning |
| --- | --- |
| Six-center sample | The authors recommend evaluation across a wider range of fertility centers. |
| Small-to-midsize US centers | Findings may not represent larger centers, academic centers or publicly funded IVF systems. |
| Center-specific deployment context | The models were built around local workflows and provider collaboration. |
| Proprietary model pipeline | Full model pipeline and preprocessing code are not openly available. |
| Need broader collaborative research | Authors call for larger public-private research efforts, including racial disparities and molecular mechanisms. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| US-only validation | It supports local validation, but not Indian validation. |
| Proprietary/commercial context | Several authors were employed by or had interests in Univfy; this should be transparently noted. |
| Algorithm opacity | The visible article text does not clearly specify the exact ML algorithm family. |
| Local model advantage may depend on data quality | Center-specific models require enough clean local historical data. |
| Counseling focus, not full treatment CDSS | The model supports prognostic counseling, not ovarian stimulation or embryo-transfer treatment decisions. |
| Dataset not publicly shareable | Independent reproduction by other researchers is limited. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- evaluating MLCS models in more fertility centers
- including larger centers, academic centers and publicly funded IVF settings
- studying racial disparities in IVF prediction and access
- investigating molecular mechanisms of infertility and IVF failure
- scaling localized prognostic models across multiple settings
- improving patient-provider counseling and value-based IVF care

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need local/external validation | Yes | Strongly supports local center-specific validation rather than relying only on national models. |
| Need clinical decision support | Partial | Supports counseling workflow, but not a full treatment recommendation CDSS. |
| Indian validation gap | Yes | No Indian validation; local models may be needed in Indian clinics. |
| Calibration gap | Yes | Calibration and Brier score were central to comparing model usefulness. |
| Generalization gap | Yes | Center differences and data drift are explicitly discussed. |
| Explainability gap | Limited | The paper is more about model validation and counseling utility than XAI. |
| Deployment evidence | Yes | Discusses deployed clinical usage and live model validation, though in a commercial context. |

## Usefulness For Our PhD

Relevance: **High**

This paper is very useful for defending why our PhD should not rely only on models developed elsewhere.

The strongest lesson is:

> Local clinical context matters in IVF prediction.

For our work, this supports the need to validate any IVF prediction or CDSS model on Indian clinic data. It also reminds us that performance should not be judged only by AUC. Calibration, false positives/false negatives, patient counseling usefulness and threshold-based interpretation matter.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Yao et al. (2025) compared machine learning center-specific IVF live-birth prediction models with the US SART national registry-based model across six fertility centers and found that localized models improved calibration, precision-recall performance and threshold-based F1 scores relevant to clinical counseling.

Gap-support sentence:

> The study supports the importance of local validation and center-specific prognostic modeling in IVF, but its US-only setting, proprietary pipeline and counseling-focused application indicate that independent validation in Indian clinical settings remains necessary.

## What This Paper Does Not Prove

This paper does not prove that:

- the center-specific model generalizes to Indian IVF clinics.
- a national registry model is always inferior in every setting.
- live-birth prediction alone is enough for complete IVF decision support.
- the exact algorithm can be reproduced from the visible article text alone.
- calibration and counseling improvements automatically improve live-birth rates.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Study design and dataset | High |
| Main findings | High |
| Evaluation metrics | High |
| Author-stated limitations | High |
| Exact ML algorithm family | Not confirmed from visible main article text |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
