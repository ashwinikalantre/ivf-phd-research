# Paper 07: ML Live-Birth Prediction for PCOS Fresh Embryo Transfer

## Citation

Zhu, S., Huang, Z., Chen, X., Jiang, W., Zhou, Y., Zheng, B., & Sun, Y. (2025). **Construction and evaluation of machine learning-based prediction model for live birth following fresh embryo transfer in IVF/ICSI patients with polycystic ovary syndrome**. *Journal of Ovarian Research*, 18, Article 70.

DOI: [https://doi.org/10.1186/s13048-025-01654-x](https://doi.org/10.1186/s13048-025-01654-x)

Source checked: [Springer Nature article page](https://link.springer.com/article/10.1186/s13048-025-01654-x)

Related study terms:

- [PCOS](../glossary/clinical-glossary.md#pcos)
- [Antagonist protocol](../glossary/clinical-glossary.md#antagonist-protocol)
- [Fresh embryo transfer](../glossary/clinical-glossary.md#fresh-embryo-transfer)
- [Blastocyst](../glossary/clinical-glossary.md#blastocyst)
- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [AMH](../glossary/clinical-glossary.md#amh)
- [AFC](../glossary/clinical-glossary.md#afc)
- [XGBoost](../glossary/technical-glossary.md#xgboost)
- [SHAP](../glossary/technical-glossary.md#shap)
- [Decision curve analysis](../glossary/technical-glossary.md#decision-curve-analysis)
- [Recursive feature elimination](../glossary/technical-glossary.md#recursive-feature-elimination)

## Why This Paper Matters

This paper is useful because it is a disease-specific IVF prediction study focused on PCOS patients.

It supports our personalization argument:

> IVF prediction may need subgroup-specific models because patient diagnosis and reproductive condition can affect treatment response and live-birth probability.

It is also useful because it uses SHAP to interpret model predictors, which connects to our explainable AI direction.

## Research Objective

The objective was to investigate determinants affecting live-birth outcomes after fresh embryo transfer among IVF/ICSI patients with PCOS and to construct machine-learning prediction models for this specific group.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Retrospective cohort prediction-model study |
| Country | China |
| Center | Fujian Provincial Maternal and Child Health Hospital |
| Study period | January 2019 to December 2023 |
| Population | Female PCOS patients undergoing antagonist protocol followed by fresh embryo transfer |
| Sample size | 1,062 fresh embryo-transfer cycles |
| Live births | 466 |
| Training group | 743 cycles |
| Validation/testing group | 319 cycles |
| Split ratio | 7:3 |
| Outcome | Live birth |
| Data availability | Available from corresponding authors on reasonable request |

Confidence: **High**

## Inclusion and Exclusion

Inclusion criteria:

- PCOS diagnosed by Rotterdam criteria or Chinese PCOS guideline criteria
- ovarian stimulation with antagonist protocol
- fresh embryo transfer cycles

Exclusion criteria included:

- uterine abnormalities
- adenomyosis
- submucosal fibroids
- endometriosis
- hydrosalpinx
- chromosomal abnormalities in either partner
- severe oligoasthenozoospermia in male partners
- loss to follow-up or missing outcome data

Confidence: **High**

## Variables / Features Used

The study collected demographic, biochemical, treatment and embryological variables.

Confirmed variables include:

- age
- BMI
- infertility duration
- number of treatment cycles
- basal FSH
- LH
- estradiol
- testosterone
- progesterone on HCG day
- gonadotropin dose
- number of transferred embryos
- type of transferred embryos
- blastocyst transfer
- number of high-quality cleavage-stage embryos
- AMH and AFC were discussed but were not strong predictors in this study

Significant differences between live-birth and control groups included:

- maternal age
- BMI
- infertility duration
- treatment frequency
- testosterone level
- initial gonadotropin dose
- FSH on HCG day
- progesterone on HCG day
- number of high-quality cleavage-stage embryos
- transferred embryo type
- number of transferred embryos

Confidence: **High**

## Method / Algorithm

Seven ML models were developed:

| Model | Role |
| --- | --- |
| Decision Tree | Comparison model |
| KNN | Comparison model |
| LightGBM | Comparison model |
| Naive Bayes | Comparison model |
| Random Forest | Comparison model |
| Support Vector Machine | Comparison model |
| XGBoost | Best-performing model |

Other methods:

- missing data handling using `missForest` in R
- LASSO regression for feature selection
- recursive feature elimination
- grid search for hyperparameter tuning
- fivefold cross-validation
- calibration curves
- decision curve analysis
- SHAP for interpretation of the best model

Confidence: **High**

## Evaluation Metrics

The study used:

- AUC
- accuracy
- specificity
- sensitivity
- positive predictive value
- negative predictive value
- F1 score
- Brier score
- calibration curve
- decision curve analysis

Confidence: **High**

## Main Findings

### Model performance

| Model | Training AUC | Testing AUC |
| --- | ---: | ---: |
| Decision Tree | 0.813 | 0.773 |
| KNN | 1.000 | 0.719 |
| LightGBM | 0.724 | 0.705 |
| Naive Bayes | 0.791 | 0.764 |
| Random Forest | 1.000 | 0.794 |
| SVM | 0.819 | 0.806 |
| XGBoost | 0.853 | 0.822 |

The XGBoost model was selected as the best overall model.

Validation-set performance for XGBoost:

| Metric | Value |
| --- | ---: |
| AUC | 0.822 |
| 95% CI | 0.777-0.867 |
| Accuracy | 0.752 |
| Specificity | 0.732 |
| Sensitivity | 0.772 |
| PPV | 0.682 |
| NPV | 0.812 |
| F1 score | 0.724 |
| Brier score | 0.172 |

### SHAP findings

Top predictors in descending SHAP importance:

1. number of transferred embryos
2. blastocyst transfer
3. female age
4. infertility duration >= 3
5. BMI >= 28
6. testosterone level
7. progesterone level on HCG day

The study found that higher female age, higher testosterone, higher progesterone on HCG day, infertility duration >= 3 and BMI >= 28 were linked with lower probability of live birth.

Confidence: **High**

## Limitations Stated by Authors

The authors state these limitations:

| Limitation | Meaning |
| --- | --- |
| Single-center data | Model applicability to other institutions may be limited. |
| Missing insulin and glucose metabolism parameters | Important metabolic variables for PCOS were absent from electronic records. |
| No external validation | Generalizability is uncertain. |
| Need external validation datasets | Authors plan to collect comprehensive external validation datasets. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Disease-specific scope | Useful for PCOS personalization, but not general IVF prediction. |
| Fresh embryo transfer only | Does not generalize to frozen embryo transfer or freeze-all strategies. |
| Antagonist protocol only | Protocol-specific population limits wider application. |
| Training AUC of 1.000 for KNN/RF | Suggests potential overfitting in some models. |
| No external validation | The model is not ready for broad clinical use. |
| SHAP but no clinician usability testing | Explainability is technical, not yet evaluated for doctor decision-making. |
| Lifestyle/metabolic data incomplete | Important PCOS variables such as insulin/glucose metabolism were missing. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- external validation across other institutions
- adding insulin and glucose metabolism variables
- improving robustness of PCOS-specific prediction models
- using prediction models to identify high-risk cases
- supporting informed treatment decisions for PCOS fresh embryo-transfer patients

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Disease-specific personalization | Yes | Focuses on PCOS fresh embryo-transfer patients. |
| Need external validation | Yes | Single-center model without external validation. |
| Explainability gap | Partial | SHAP is used, but clinician usability is not evaluated. |
| Need clinical decision support | Yes | Authors discuss treatment decision support, but no deployed CDSS is tested. |
| Lifestyle/metabolic data gap | Yes | Insulin/glucose metabolism variables were missing. |
| Generalization gap | Yes | PCOS, fresh transfer and antagonist protocol limit wider generalization. |
| Indian validation gap | Yes | China-only dataset; no Indian validation. |

## Usefulness For Our PhD

Relevance: **Medium-High**

This paper is useful because it supports subgroup-specific IVF prediction and shows that diagnosis-specific models may be important.

For our PhD, it suggests that if our dataset contains enough PCOS cases, subgroup analysis should be considered. However, it should not become the full PhD topic unless clinic data strongly supports a PCOS-specific direction.

It also strengthens the argument that XAI methods like SHAP can identify clinically meaningful predictors, but clinical decision-support usability still needs evaluation.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Zhu et al. (2025) developed seven machine-learning models to predict live birth after fresh embryo transfer among 1,062 IVF/ICSI patients with PCOS, identifying XGBoost as the best-performing model and using SHAP to highlight embryo-transfer count, blastocyst transfer, age, infertility duration, BMI, testosterone and progesterone as important predictors.

Gap-support sentence:

> Although the study supports diagnosis-specific and explainable IVF prediction, its single-center retrospective design, lack of external validation and missing metabolic variables limit its generalizability and clinical decision-support readiness.

## What This Paper Does Not Prove

This paper does not prove that:

- the model works for non-PCOS IVF patients.
- the model generalizes to Indian clinics.
- fresh-transfer findings apply to frozen-transfer cycles.
- SHAP explanations are sufficient for clinician trust.
- the model is ready for deployed clinical decision support.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Dataset | High |
| Inclusion/exclusion | High |
| Variables/features | High |
| Model list | High |
| Main findings | High |
| Author-stated limitations | High |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
