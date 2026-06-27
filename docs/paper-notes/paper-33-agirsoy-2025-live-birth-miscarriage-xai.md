# Paper 33: Explainable Prediction of Live Birth Versus Miscarriage After IVF-ET Pregnancy

## Citation

Agirsoy, M., & Oehlschlaeger, M. A. (2025). **Development of an explainable machine learning model to predict live birth versus miscarriage among in vitro fertilization-embryo transfer pregnancies**. *Journal of Medical Artificial Intelligence*, 9, Article 3.

DOI: [https://doi.org/10.21037/jmai-25-75](https://doi.org/10.21037/jmai-25-75)

Source checked: [Journal of Medical Artificial Intelligence full text](https://jmai.amegroups.org/article/view/10224/html)

Evidence note:

This is a full-text open-access article. Extraction confidence is high for objective, dataset, variables, methods, performance, SHAP findings and limitations.

Related study terms:

- [IVF](../glossary/clinical-glossary.md#ivf)
- [Embryo Transfer](../glossary/clinical-glossary.md#embryo-transfer)
- [Clinical Pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [Live Birth](../glossary/clinical-glossary.md#live-birth)
- [Miscarriage](../glossary/clinical-glossary.md#miscarriage)
- [AMH](../glossary/clinical-glossary.md#amh)
- [FSH](../glossary/clinical-glossary.md#fsh)
- [LH](../glossary/clinical-glossary.md#lh)
- [ESR](../glossary/clinical-glossary.md#esr)
- [ANA](../glossary/clinical-glossary.md#ana)
- [Prolactin](../glossary/clinical-glossary.md#prolactin)
- [Coagulation Markers](../glossary/clinical-glossary.md#coagulation-markers)
- [XGBoost](../glossary/technical-glossary.md#xgboost)
- [LightGBM](../glossary/technical-glossary.md#lightgbm)
- [SHAP](../glossary/technical-glossary.md#shap)
- [TRIPOD + AI](../glossary/technical-glossary.md#tripod-ai)

## Why This Paper Matters

This paper is useful because it studies a narrower and clinically different question from many IVF prediction papers.

Most IVF-AI studies ask:

**Will IVF lead to pregnancy or live birth?**

This paper asks:

**If pregnancy is already confirmed after IVF-ET, can we predict live birth versus miscarriage?**

For our PhD, this is important because prediction timing matters. A model used before treatment, after embryo transfer, after positive pregnancy confirmation or during early pregnancy has different input variables, clinical purpose and counseling risk.

## Research Objective

The study aimed to develop and validate an interpretable machine learning model for predicting live birth versus miscarriage among patients with confirmed clinical pregnancy after IVF-ET.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Retrospective secondary analysis / prediction-model study |
| Journal | Journal of Medical Artificial Intelligence |
| Published online | 25 July 2025 |
| Dataset source | Publicly available dataset from Yuan et al. (2022) |
| Original clinical source | Reproductive Center of Qingdao Women's and Children's Hospital |
| Country | China |
| Data collection period | September 2019 to May 2022 |
| Sample size | 1,017 singleton IVF-ET pregnancies |
| Study population | Infertile women who underwent IVF-ET and achieved singleton intrauterine pregnancy confirmed by ultrasound |
| Exclusions | Donor sperm/egg, ectopic or multiple pregnancy, pregnancy loss due to trauma or medication, severe organ disorders, incomplete clinical data |
| Primary outcome | Live birth versus miscarriage among patients with confirmed pregnancy |
| Train-test split | 80% training, 20% testing |
| Reporting checklist | TRIPOD |

Confidence: **High**

## Variables / Features Used

The abstract reports 55 clinical, hormonal, immune and treatment-related features. The methods section later states that 52 clinical, biochemical, hormonal, immunologic and treatment-related variables were included.

Feature domains included:

- demographic variables
- ovarian reserve markers such as AMH, FSH and LH
- thyroid hormones such as TSH, FT3 and FT4
- immune markers such as ANA and ESR
- coagulation parameters such as D-dimer, PT and APTT
- infection screening
- uterine and ovarian morphology
- embryo transfer characteristics
- treatment-stage variables

Engineered variables included:

- AMH x age
- FSH/LH ratio
- endometrial quality

Important caution:

The article has a small inconsistency between 55 features in the abstract and 52 variables in the methods section. Use the broader wording "52-55 features/variables" unless the supplementary table is being cited directly.

Confidence: **High**

## Method / Algorithm

The study developed and compared:

| Model | Role |
| --- | --- |
| XGBoost | Standalone classifier and best-performing model |
| LightGBM | Included in soft-voting ensemble |
| Logistic Regression | Included in soft-voting ensemble |
| Soft-voting ensemble | Combined XGBoost, LightGBM and Logistic Regression |

Interpretability:

- SHAP global explanations
- SHAP feature contribution analysis
- individualized interpretation of prediction drivers

Other methodological details:

- class imbalance handling
- threshold optimization
- regularization
- TRIPOD reporting checklist

Confidence: **High**

## Evaluation Metrics

The study used:

- AUC
- precision
- F1-score
- accuracy
- sensitivity
- specificity
- confidence intervals
- SHAP-based interpretability

Key reported results:

| Model / Metric | Result |
| --- | ---: |
| XGBoost training AUC | 0.99, 95% CI 0.98-1.00 |
| XGBoost test AUC | 0.91, 95% CI 0.86-0.96 |
| XGBoost test F1-score | 0.93, 95% CI 0.89-0.96 |
| XGBoost test accuracy | 0.89, 95% CI 0.85-0.93 |
| Ensemble AUC | 0.89 |
| Ensemble sensitivity at optimized threshold | 0.96 |
| Ensemble specificity at optimized threshold | 0.66 |
| Optimized ensemble threshold | 0.16 |

Confidence: **High**

## Main Findings

The standalone XGBoost model outperformed the soft-voting ensemble in key metrics such as precision, F1-score and accuracy.

SHAP analysis identified important contributors including:

- AMH
- prolactin
- FSH
- ESR
- ANA
- BMI
- years of infertility
- immune and coagulation markers
- total oocytes retrieved
- number of high-quality embryos

The study also found that engineered features such as AMH x age, FSH/LH ratio and endometrial quality were not globally dominant, but may be useful in subgroups.

Confidence: **High**

## Limitations Stated By Authors

| Limitation | Meaning |
| --- | --- |
| Single-center China dataset | Generalizability may be limited. |
| External validation needed | Testing in geographically and ethnically diverse cohorts is required. |
| Retrospective analysis | Unmeasured confounding and data-quality issues may influence results. |
| Large feature set | 52 features may be difficult for routine clinical use. |
| Feature reduction needed | A smaller practical feature set is needed for real-world deployment. |
| Governance and transparency needed | Broader clinical implementation needs data transparency and governance. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Model applies after confirmed pregnancy | It cannot be used for pre-treatment IVF success prediction. |
| No Indian population | Generalization to Indian IVF patients is not established. |
| No independent external validation | Test split is not the same as testing another clinic. |
| High training AUC suggests overfitting risk must be watched | Training AUC 0.99 is strong, but needs external testing. |
| Many immune/coagulation features may not be routinely available | Practical clinic adoption may require a reduced feature set. |
| No clinician usability study | SHAP was used, but clinician trust and interpretation were not evaluated. |
| No lifestyle data | Lifestyle and socioeconomic factors were not central to the model. |

Confidence: **High**

## Future Work Suggested

The paper supports future work on:

- prospective validation
- external validation across diverse clinical settings
- streamlined feature sets for real-world implementation
- clinical workflow integration
- post-conception risk stratification
- individualized counseling after confirmed IVF pregnancy
- governance and data transparency for AI deployment

Confidence: **High**

## Gap Contribution

| Gap Category | Contribution |
| --- | --- |
| Explainable AI | Partially addressed using SHAP |
| Need external validation | Strongly supported |
| Single-center study | Strongly supported |
| Retrospective design | Strongly supported |
| Need clinical decision support | Supported; no deployed workflow tested |
| Real-world deployment gap | Strongly supported through feature-burden and validation needs |
| Indian population gap | Supported for our context |
| Lifestyle data gap | Supported by absence from key model features |
| Prediction timing gap | Strongly supported because the model is post-pregnancy-confirmation |

## Usefulness For Our PhD

Usefulness: **High for XAI and prediction-timing clarity**

This paper is useful because it helps separate different IVF prediction tasks:

- pre-treatment success prediction
- embryo-transfer outcome prediction
- pregnancy confirmation prediction
- live birth versus miscarriage prediction after pregnancy is confirmed

For our PhD, this distinction is important. If doctors give us a dataset, we must first identify which stage the available variables belong to. We should not mix pre-treatment counseling, embryo transfer support and post-conception risk prediction as if they are one model.

## What This Paper Does Not Prove

This paper does not prove that:

- the model works in Indian IVF clinics
- the model works before treatment starts
- SHAP explanations are trusted by doctors
- the model improves live-birth outcomes
- the large feature set is feasible in routine practice
- lifestyle factors are unnecessary

## Thesis-Ready Citation Sentences

Agirsoy and Oehlschlaeger (2025) developed an interpretable XGBoost model to predict live birth versus miscarriage among 1,017 singleton IVF-ET pregnancies with confirmed intrauterine pregnancy, using clinical, hormonal, immune, coagulation and treatment-related variables.

The model achieved test AUC of 0.91, F1-score of 0.93 and accuracy of 0.89, while SHAP analysis identified AMH, prolactin, FSH, ESR and ANA among the important contributors.

For this PhD, the study supports explainable post-transfer risk stratification, but it also strengthens the need for external validation, Indian population testing, clinician usability evaluation and careful separation of prediction tasks by IVF stage.

## Source Confidence Summary

| Item | Confidence |
| --- | --- |
| Citation, authors, DOI, journal | High |
| Objective | High |
| Dataset and study design | High |
| Variables and engineered features | High |
| Algorithms and validation approach | High |
| Metrics and SHAP findings | High |
| Limitations and future work | High |
| PhD gap interpretation | High |
