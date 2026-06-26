# Paper 08: Fresh Embryo Transfer Live-Birth Prediction With ML and Web Tool

## Citation

Wu, S., Wang, X., Liu, Y., Ren, Y., Zhao, M., Song, H., Shen, H., Wu, Y., Wei, Z., Lu, H., & Li, K. (2025). **Predictive models for live birth outcomes following fresh embryo transfer in assisted reproductive technologies using machine learning**. *Journal of Translational Medicine*, 23, Article 1004.

DOI: [https://doi.org/10.1186/s12967-025-07045-6](https://doi.org/10.1186/s12967-025-07045-6)

Correction note:

A correction was published on 07 October 2025 for an authorship equal-contribution omission. The correction did not change the study results.

Correction DOI: [https://doi.org/10.1186/s12967-025-07248-x](https://doi.org/10.1186/s12967-025-07248-x)

Source checked: [Springer Nature article page](https://link.springer.com/article/10.1186/s12967-025-07045-6)

Related study terms:

- [Fresh embryo transfer](../glossary/clinical-glossary.md#fresh-embryo-transfer)
- [Cleavage-stage embryo](../glossary/clinical-glossary.md#cleavage-stage-embryo)
- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [Endometrial thickness](../glossary/clinical-glossary.md#endometrial-thickness)
- [AMH](../glossary/clinical-glossary.md#amh)
- [Random Forest](../glossary/technical-glossary.md#random-forest)
- [XGBoost](../glossary/technical-glossary.md#xgboost)
- [AdaBoost](../glossary/technical-glossary.md#adaboost)
- [Artificial Neural Network](../glossary/technical-glossary.md#artificial-neural-network)
- [Permutation Importance](../glossary/technical-glossary.md#permutation-importance)
- [Partial Dependence Plot](../glossary/technical-glossary.md#partial-dependence-plot)

## Why This Paper Matters

This paper is useful because it moves beyond model comparison and includes a web-based prediction tool for clinicians.

It supports our clinical decision-support argument:

> A useful IVF-AI study should not stop at AUC. It should consider implementation, explainability, subgroup performance and decision support.

However, it also shows that a web tool alone does not solve generalizability, ethical implementation or clinician validation.

## Research Objective

The study aimed to develop machine-learning models to predict live-birth outcomes following fresh embryo transfer in assisted reproductive technology and to support clinician counseling before embryo transfer.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Retrospective single-center prediction-model study |
| Country | China |
| Center | Shanghai First Maternity and Infant Hospital |
| Study period | 2016 to 2023 |
| Original records | 51,047 ART records |
| Focused dataset after filtering | 13,362 records with fresh embryos and tracked outcomes |
| Final modeled dataset | 11,728 records |
| Outcome | Live birth following pregnancy / fresh embryo transfer |
| Live birth records | 3,971, 33.86% |
| Non-live birth records | 7,757, 66.14% |
| Initial features | 75 pre-pregnancy features |
| Refined feature set | 55 clinically and statistically validated predictors |
| Data/code availability | Code available on GitHub; additional data available on request |
| Ethics | Ethics approval from Shanghai First Maternity and Infant Hospital; anonymized data |

Confidence: **High**

## Inclusion and Filtering

The final dataset focused on:

- fresh embryo transfer
- tracked outcomes
- female age <= 55
- male age <= 60
- sperm from husband
- cleavage-stage embryo transfer

Missing values were imputed using `missForest`.

Confidence: **High**

## Variables / Features Used

The final refined model used 55 predictors from clinical, reproductive and embryo-transfer information.

Important features identified included:

- female age
- transferred embryo grades
- number of usable embryos
- endometrial thickness
- male age
- AMH
- estradiol on trigger day
- progesterone
- testosterone
- FSH on trigger day

The paper highlights female age and transferred embryo grades as the top two influential predictors.

Confidence: **High**

## Method / Algorithm

Six machine-learning models were evaluated:

| Model | Role |
| --- | --- |
| Random Forest | Best-performing model |
| XGBoost | Strong comparison model |
| Gradient Boosting Machine | Comparison model |
| AdaBoost | Comparison model |
| LightGBM | Comparison model |
| Artificial Neural Network | Comparison model |

Additional methods:

- grid search for hyperparameter optimization
- fivefold cross-validation
- training-testing ratios of 60:40, 70:30 and 80:20
- feature refinement from 75 to 55 variables
- sensitivity analysis by subgroup
- perturbation analysis for stability
- permutation-based feature importance
- partial dependence, local dependence and accumulated local profiles
- web-tool deployment through BMAP

Confidence: **High**

## Evaluation Metrics

The paper reports:

- AUC
- accuracy
- Cohen’s kappa
- sensitivity
- specificity
- precision
- recall
- F1 score
- positive likelihood ratio
- negative likelihood ratio
- calibration curves
- Brier score
- subgroup AUC

Confidence: **High**

## Main Findings

Key model findings:

- Random Forest and XGBoost consistently outperformed other methods.
- With 80% training data, Random Forest achieved AUC 0.808 with 95% CI 0.791-0.826.
- XGBoost achieved AUC 0.804 with 95% CI 0.786-0.822.
- Random Forest also showed the best calibration among models using the 55-feature subset.
- ANN was the weakest model in this framework.

Subgroup analysis:

- The optimal Random Forest model showed AUC >= 0.80 in most subgroups.
- Lower performance was observed in high-quality embryo-transfer patients with AUC 0.703.
- Sensitivity was low in younger women <= 35 years, reported as 0.492.

Top important predictors:

1. female age
2. transferred embryo grades
3. number of usable embryos
4. endometrial thickness
5. male age
6. AMH

The paper also deployed a web tool allowing clinicians to upload patient data and receive live-birth chance estimates plus explanatory feature profiles.

Confidence: **High**

## Limitations Stated by Authors

The authors state these limitations and cautions:

| Limitation | Meaning |
| --- | --- |
| Single-center dataset | Limits generalizability. |
| Need multicenter external validation | Additional datasets from multiple centers are needed. |
| Embryo quality assessment is subjective | Embryo grading relied on visual morphology and practitioner experience. |
| Specific to cleavage-stage fresh embryo transfer | Immediate applicability to frozen cycles and blastocyst transfers is limited. |
| Decision-support only | Model outputs should not be treated as definitive predictors. |
| Ethical implementation required | Patient autonomy, informed consent and clinician judgment must remain central. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Web tool does not equal clinical validation | A deployed web interface is useful, but real-world clinician outcome evaluation is still needed. |
| Single-center China data | No Indian validation or multicenter generalization. |
| Cleavage-stage fresh transfer only | The model may not apply to blastocyst transfer, frozen transfer or freeze-all strategies. |
| Moderate AUC | AUC around 0.808 is useful but not decisive alone; calibration and clinical thresholds matter. |
| Embryo grading subjectivity | Manual morphology grading may introduce observer variability. |
| Subgroup performance variation | Lower performance in favorable prognosis groups shows that model utility may differ by patient type. |
| Ethical deployment unresolved | The paper discusses ethics, but structured clinician and patient acceptance evaluation is not reported. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- multicenter external validation
- objective AI-assisted embryo morphological grading
- separate models for fresh, frozen, cleavage-stage and blastocyst-transfer cycles
- clinical deployment with decision-support safeguards
- informed consent and ethical implementation
- clinician-facing tools that preserve clinical judgment

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need clinical decision support | Yes | The paper includes a clinician-facing web tool. |
| Need external validation | Yes | Single-center model; authors call for multicenter datasets. |
| Real-world deployment gap | Partial | Web implementation exists, but real-world clinical effectiveness is not proven. |
| Explainability gap | Partial | Feature-importance and profile explanations are provided, but clinician usability is not deeply evaluated. |
| Generalization gap | Yes | Model is specific to cleavage-stage fresh transfers. |
| Indian validation gap | Yes | China-only data. |
| Embryo assessment subjectivity | Yes | Manual embryo grading may limit objectivity. |

## Usefulness For Our PhD

Relevance: **High**

This paper is useful because it shows a more complete direction than many prediction-only studies: model development, feature importance, subgroup analysis, calibration and web-tool implementation.

For our PhD, it supports the idea that a clinical decision-support framework should include:

- transparent input variables
- calibrated probability output
- feature-level explanation
- subgroup validation
- practical doctor-facing interface
- careful ethical framing

It also supports our caution that a model must be validated beyond one center and one treatment setting.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Wu et al. (2025) developed machine-learning models for live-birth prediction after fresh embryo transfer using 11,728 ART records and 55 refined pre-pregnancy features, with Random Forest achieving the best performance and a web-based tool implemented to support clinician use.

Gap-support sentence:

> Although the study advances IVF prediction toward clinical decision support through calibration, interpretation, subgroup analysis and web implementation, its single-center design, restriction to cleavage-stage fresh embryo transfer and lack of multicenter external validation limit generalizability.

## What This Paper Does Not Prove

This paper does not prove that:

- the model works for frozen embryo transfer or blastocyst transfer.
- the model generalizes to Indian IVF clinics.
- the web tool improves live-birth rates in practice.
- manual embryo grading is sufficiently objective for all settings.
- clinician and patient trust are fully established.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Correction note | High |
| Dataset | High |
| Feature set | High |
| Model list | High |
| Main findings | High |
| Author-stated limitations | High |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
