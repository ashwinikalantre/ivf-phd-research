# Paper 31: Clinical-Pregnancy Prediction in Endometriosis Patients After Fresh IVF/ICSI-ET

## Citation

Wan, X., Yu, M., Wu, X., Huang, Z., & Tan, J. (2025). **Machine learning prediction of clinical pregnancy in endometriosis patients following fresh IVF/ICSI-ET**. *European Journal of Medical Research*, 30, Article 838.

DOI: [https://doi.org/10.1186/s40001-025-03113-1](https://doi.org/10.1186/s40001-025-03113-1)

Source checked: [Publisher PDF](https://eurjmedres.biomedcentral.com/counter/pdf/10.1186/s40001-025-03113-1.pdf)

Evidence note:

This is a full-text publisher PDF. Extraction confidence is high for dataset, variables, methods, metrics, limitations and future work.

Related study terms:

- [Endometriosis](../glossary/clinical-glossary.md#endometriosis)
- [IVF](../glossary/clinical-glossary.md#ivf)
- [ICSI](../glossary/clinical-glossary.md#icsi)
- [Fresh Embryo Transfer](../glossary/clinical-glossary.md#fresh-embryo-transfer)
- [Clinical Pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [AMH](../glossary/clinical-glossary.md#amh)
- [HCG Day](../glossary/clinical-glossary.md#hcg-day)
- [XGBoost](../glossary/technical-glossary.md#xgboost)
- [SHAP](../glossary/technical-glossary.md#shap)
- [Recursive Feature Elimination](../glossary/technical-glossary.md#recursive-feature-elimination)
- [Precision-Recall AUC](../glossary/technical-glossary.md#precision-recall-auc)
- [F1 Score](../glossary/technical-glossary.md#f1-score)

## Why This Paper Matters

This paper matters because it studies a disease-specific IVF subgroup: endometriosis patients undergoing fresh IVF/ICSI embryo transfer.

For our PhD, it is useful because it shows:

- personalization may need subgroup-specific models
- clinical and embryology features can be combined
- SHAP can be used to explain model predictions
- good-looking model design can still produce only modest external-like test performance
- disease-specific factors may be missing from routine clinic data

The main caution is that the model's testing AUC was only 0.622. So this paper supports the need for explainable subgroup prediction, but it does not prove strong clinical readiness.

## Research Objective

The study aimed to develop an interpretable machine learning model to predict clinical pregnancy in endometriosis patients undergoing fresh embryo transfer after IVF/ICSI.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Retrospective prediction-model study |
| Journal | European Journal of Medical Research |
| Published | 2025 |
| Country | China |
| Institution | Reproductive Medicine Center, Jiangxi Maternal and Child Health Hospital, Nanchang |
| Initial patients identified | 2,043 endometriosis patients |
| Final included sample | 1,752 endometriosis patients |
| Data period | 1 January 2014 to 25 September 2024 |
| Treatment | IVF or ICSI with fresh embryo transfer |
| Diagnosis of endometriosis | Laparoscopic visualization or histological confirmation |
| Training set | 1,226 patients |
| Testing set | 526 patients |
| Split ratio | 7:3 |
| Clinical pregnancy events | 1,082 |
| Clinical pregnancy rate | 61.76% |
| Outcome | Clinical pregnancy |

Confidence: **High**

## Inclusion and Exclusion Criteria

Inclusion criteria:

- endometriosis confirmed by operative laparoscopy
- fresh IVF/ICSI-ET cycles with oocyte retrieval between 1 January 2014 and 25 September 2024
- infertility etiology including male factors, tubal infertility or intrauterine adhesions

Exclusion criteria:

- comorbid PCOS
- adenomyosis
- anatomical uterine anomalies affecting implantation
- sperm donation cycles
- oocyte donation cycles
- PGT cycles

Confidence: **High**

## Variables / Features Used

The study included 24 features:

- female age
- male age
- female infertility type
- female infertility duration
- female BMI
- female basal FSH
- female basal estradiol
- female basal LH
- female AMH
- male BMI
- controlled ovarian stimulation protocol
- startup dose of gonadotropins
- total dose of gonadotropins
- dosing days of gonadotropins
- HCG day estradiol
- HCG day LH
- HCG day progesterone
- HCG day endometrial thickness
- number of oocytes retrieved
- fertilization method
- number of normal fertilizations
- number of high-quality day-3 embryos
- stage of transferred embryos
- number of transferred embryos

The outcome was clinical pregnancy, defined using beta-hCG evidence plus intrauterine gestational sac with cardiac activity on ultrasound.

Confidence: **High**

## Missing Data Handling

The paper reports missing values in:

- female BMI
- basal FSH
- basal estradiol
- basal LH
- female AMH
- HCG day estradiol
- HCG day LH
- HCG day progesterone
- HCG day endometrial thickness

Features with more than 25% missing values were excluded. HCG-day hormones were handled using last observation carried forward. Remaining variables such as BMI, AMH and basal hormones were imputed using random forest regression through the `mice` package.

Confidence: **High**

## Method / Algorithm

The study compared six models:

| Model | Type |
| --- | --- |
| Naive Bayes | Probabilistic classifier |
| Logistic Regression | Linear statistical model |
| Random Forest | Tree ensemble |
| K-Nearest Neighbors | Instance-based classifier |
| Neural Network | Nonlinear model |
| XGBoost | Gradient-boosted tree model |

Feature selection used:

- univariate logistic regression
- multivariate logistic regression
- Random Forest recursive feature elimination
- tenfold cross-validation

Interpretability used:

- SHAP global explanations
- SHAP individual force plots
- SHAP dependence plots

Confidence: **High**

## Evaluation Metrics

The study used:

- ROC-AUC
- accuracy
- precision
- recall
- F1-score
- precision-recall curve / AUPRC
- tenfold cross-validation

Key reported performance:

| Model / Metric | Result |
| --- | ---: |
| Best model | XGBoost |
| XGBoost training AUC | 0.764 |
| XGBoost testing AUC | 0.622 |
| AUPRC | 0.692 |
| Baseline prevalence | 0.639 |

Confidence: **High**

## Main Findings

Logistic regression identified these significant predictors:

| Predictor | Reported Association |
| --- | --- |
| Male age | OR 0.96, 95% CI 0.93-0.98, p < 0.001 |
| Normal fertilization count | OR 1.07, 95% CI 1.03-1.11, p = 0.001 |
| Transferred embryo count | OR 1.61, 95% CI 1.24-2.08, p < 0.001 |

SHAP identified important predictors including:

- female age
- progesterone on HCG day
- AMH
- number of embryos transferred
- number of normal fertilizations
- female BMI

The authors state that SHAP helped provide both global and individual-level interpretation.

Confidence: **High**

## Limitations Stated By Authors

| Limitation | Meaning |
| --- | --- |
| Retrospective design | Selection bias may be present. |
| Single-center data | Generalizability is limited. |
| Prospective multicenter validation needed | Current evidence is not enough for broad clinical use. |
| Missing endometriosis-specific characteristics | rASRM stage, surgical history and lesion location were not included. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Outcome is clinical pregnancy, not live birth | Clinical pregnancy is useful but not the final IVF outcome. |
| Testing AUC is modest | AUC 0.622 limits clinical confidence. |
| Single disease subgroup | Useful for personalization, but not directly general IVF prediction. |
| No Indian population | Findings may not generalize to Indian endometriosis patients. |
| No lifestyle variables | Lifestyle and social determinants are not modeled. |
| Some variables are treatment-cycle variables | HCG-day hormones and embryo variables are not available before IVF starts. |
| No real deployment evidence | SHAP explanations were produced, but clinical workflow testing was not shown. |
| Data availability statement is unclear | The paper states no datasets were generated or analyzed, which conflicts with the retrospective analysis description. |

Confidence: **High**

## Future Work Suggested

The paper supports future work on:

- prospective multicenter validation
- validating the model across diverse populations
- testing impact on patient psychological outcomes
- testing impact on decision-making quality
- testing impact on treatment efficiency
- including endometriosis-specific variables such as rASRM stage, surgical history and lesion location

For our PhD, it also supports:

- subgroup-specific prediction models
- explaining model outputs to clinicians
- separating first-consultation predictors from treatment-cycle predictors
- validating models in Indian clinic data

Confidence: **High**

## Gap Contribution

| Gap Category | Contribution |
| --- | --- |
| Disease-specific personalization | Strongly supported |
| Explainable AI | Partially addressed using SHAP |
| Need external validation | Strongly supported |
| Single-center study | Strongly supported |
| Retrospective design | Strongly supported |
| Lack of Indian population | Supported for our context |
| Lack of lifestyle data | Supported |
| Need clinical decision support | Supported because no deployed workflow was evaluated |
| Outcome limitation | Supported because outcome was clinical pregnancy, not live birth |

## Usefulness For Our PhD

Usefulness: **High for personalization and XAI, Medium for model-strength evidence**

This paper is useful because it shows how a model can be built for a specific IVF subgroup and explained using SHAP.

However, the model's modest testing AUC shows why our PhD should not promise very high prediction accuracy too early. The stronger research direction is explainable, validated decision support using the right variables and clear clinical boundaries.

## What This Paper Does Not Prove

This paper does not prove that:

- XGBoost is clinically ready for endometriosis IVF counseling
- the model predicts live birth
- the model works outside the source hospital
- the model works for Indian patients
- SHAP explanations are understandable or trusted by clinicians
- lifestyle variables are unnecessary

## Thesis-Ready Citation Sentences

Wan et al. (2025) developed an interpretable XGBoost-based model to predict clinical pregnancy among 1,752 endometriosis patients undergoing fresh IVF/ICSI embryo transfer at a single Chinese reproductive medicine center.

The study used 24 clinical and embryology variables and found that the best model achieved training AUC of 0.764 and testing AUC of 0.622, while SHAP highlighted progesterone on HCG day, AMH and embryology-related variables as important predictors.

For this PhD, the paper supports disease-specific IVF prediction and explainable modeling, but also strengthens the need for external validation, live-birth outcomes, Indian population data, lifestyle-variable integration and clinician-tested decision support.

## Source Confidence Summary

| Item | Confidence |
| --- | --- |
| Citation, authors, DOI, journal | High |
| Objective | High |
| Dataset and study design | High |
| Inclusion/exclusion criteria | High |
| Variables and missing-data handling | High |
| Methods and algorithms | High |
| Metrics and findings | High |
| Limitations and future work | High |
| PhD gap interpretation | High |
