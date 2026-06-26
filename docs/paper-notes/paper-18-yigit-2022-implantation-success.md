# Paper 18: Machine Learning for Implantation Success Prediction in IVF

## Citation

Yigit, P., Bener, A., & Karabulut, S. (2022). **Comparison of machine learning classification techniques to predict implantation success in an IVF treatment cycle**. *Reproductive BioMedicine Online*, 45(5), 923-934.

DOI: [https://doi.org/10.1016/j.rbmo.2022.06.022](https://doi.org/10.1016/j.rbmo.2022.06.022)

Source checked:

- [PubMed record](https://pubmed.ncbi.nlm.nih.gov/36088224/)
- [Reproductive BioMedicine Online abstract page](https://www.rbmojournal.com/article/S1472-6483%2822%2900481-3/abstract)

Evidence note:

The full article text was not fully accessible during this review. Extraction is therefore based on bibliographic records and accessible abstract-level information. Details that require full-table verification are marked carefully.

Related study terms:

- [Implantation success](../glossary/clinical-glossary.md#implantation-success)
- [Embryo transfer](../glossary/clinical-glossary.md#embryo-transfer)
- [Estradiol](../glossary/clinical-glossary.md#estradiol)
- [Gonadotropin dosage](../glossary/clinical-glossary.md#gonadotropin-dosage)
- [Super Learner](../glossary/technical-glossary.md#super-learner)
- [Random Forest](../glossary/technical-glossary.md#random-forest)
- [XGBoost](../glossary/technical-glossary.md#xgboost)
- [Specificity](../glossary/technical-glossary.md#specificity)
- [Repeated Cross-Validation](../glossary/technical-glossary.md#repeated-cross-validation)
- [AUROC / AUC](../glossary/technical-glossary.md#auc)

## Why This Paper Matters

This paper is useful because it focuses on **implantation success**, a clinically important intermediate outcome after embryo transfer.

It helps us understand:

- which classical and ensemble ML models have been tested for implantation prediction
- which variables may matter for implantation after IVF
- how embryo-transfer timing and stimulation-related variables may contribute to outcome prediction

It is not as strong as live-birth prediction evidence, but it is useful for the IVF outcome pathway because implantation comes before clinical pregnancy and live birth.

## Research Objective

The study asked:

- Which machine-learning model predicts the implantation outcome better in an IVF cycle?
- What is the importance of each variable in predicting implantation outcome in an IVF cycle?

Confidence: **Medium-High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Retrospective cohort study |
| Journal | Reproductive BioMedicine Online |
| Year | 2022 |
| Country/setting | IVF center in Turkey |
| Study period | 2014-2018 |
| Dataset | 939 transferred embryos |
| Feature count | 17 selected features |
| Outcome | Implantation success |
| Full dataset details | Not fully confirmed from available source |

Confidence: **Medium-High for visible abstract-level details; Medium for unverified full dataset details**

## Variables / Features Used

Top features reported in accessible abstract-level information:

| Feature | Why It Matters |
| --- | --- |
| Maternal age | Strong known predictor of IVF success |
| Embryo transfer day | Transfer timing/development stage can affect implantation |
| Total gonadotropin dose | Reflects stimulation protocol and ovarian response |
| E2 level | Estradiol level may reflect ovarian stimulation response |

Other selected features:

**Not confirmed from available source**

Confidence: **Medium**

## Method / Algorithm

Algorithms reported:

| Algorithm | Role |
| --- | --- |
| Logistic Regression | Baseline statistical/ML classifier |
| Decision Tree | Tree-based classifier |
| Naive Bayes | Probabilistic classifier |
| Random Forest | Ensemble classifier |
| Support Vector Machine | Margin-based classifier |
| Neural Network | Non-linear classifier |
| Gradient Boost Decision Tree | Boosting classifier |
| XGBoost | Gradient boosting classifier |
| Super Learner | Ensemble/meta-learning approach |

Confidence: **High for algorithm list from accessible abstract-level information**

## Evaluation Metrics

The study evaluated model performance using:

- F1 score
- specificity
- accuracy
- AUROC
- 10-fold cross-validation repeated ten times

Confidence: **High**

## Main Findings

| Finding | Extracted Information |
| --- | --- |
| Best-performing models | Random Forest and Super Learner |
| F1 score | 74% |
| Specificity | 94% |
| Accuracy | 89% |
| AUROC | 83% |
| Most important predictor | Maternal age |
| Other important features | Embryo transfer day, total gonadotropin dose, E2 level |

The study concluded that machine-learning algorithms successfully predicted implantation rates in an IVF attempt.

Confidence: **Medium-High**

## Limitations Stated By Authors

Not confirmed from available source.

The abstract-level information available to us did not provide a full limitations section.

Confidence: **Not confirmed**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points based on the available information.

| Critical Point | Why It Matters |
| --- | --- |
| Full-text limitations not available | We should not overuse this paper for thesis gap claims until full text is checked. |
| Single IVF center | Generalizability to other clinics and populations is likely limited. |
| Outcome is implantation, not live birth | Implantation is important but does not guarantee live birth. |
| Retrospective cohort | Confounding and practice-pattern bias may remain. |
| No confirmed external validation | Model performance may be internal only. |
| No confirmed clinical deployment | The paper compares models but does not confirm a deployed CDSS. |
| No confirmed XAI method | Variable importance is reported, but patient-level explanation is not confirmed. |

Confidence: **Medium**

## Future Work Suggested

Not confirmed from available source.

Our evidence-based extension:

- full-text verification is needed
- external validation should be checked or performed
- implantation models should be compared with clinical pregnancy and live-birth prediction
- patient-level explainability should be added if used in clinical counseling
- model usefulness should be tested in clinician workflow before CDSS claims

Confidence: **Medium**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need full-text verification | Yes | Limitations and full dataset details were not accessible in this review. |
| Need external validation | Likely | No external validation was confirmed from accessible information. |
| Single-center study | Likely | Abstract-level information refers to one IVF center in Turkey. |
| Outcome-label limitation | Yes | Implantation success is not the same as live birth. |
| No clinical decision support | Likely | No deployed CDSS was confirmed. |
| Lack of XAI | Likely | No SHAP/LIME or patient-level explanation was confirmed. |
| Lack of Indian population | Yes | Study setting was Turkey, not India. |

## Usefulness For Our PhD

Relevance: **Medium-High**

This paper is useful for understanding intermediate IVF outcome prediction, especially implantation after embryo transfer.

It supports the importance of collecting:

- maternal age
- embryo transfer day
- gonadotropin dose
- estradiol level
- embryo-transfer related variables

However, because the full text was not fully accessible, we should use this paper cautiously. It is helpful for the literature matrix, but not yet strong enough for final thesis claims about limitations unless the full paper is obtained.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Yigit et al. (2022) compared multiple machine-learning classifiers for implantation-success prediction using 939 transferred embryos from a Turkish IVF center and reported the strongest performance for Random Forest and Super Learner models, with maternal age identified as the most important predictor.

Gap-support sentence:

> Because the available evidence confirms a retrospective single-center implantation-prediction study rather than externally validated live-birth decision support, the paper supports the need for broader validation and stronger clinically meaningful outcome labels.

## What This Paper Does Not Prove

This paper does not prove that:

- implantation prediction is equivalent to live-birth prediction.
- the model will generalize to Indian IVF clinics.
- the model has been externally validated.
- a clinical decision-support system is ready for use.
- patient-level explainability has been evaluated.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| DOI and journal details | High |
| Study design and sample size | Medium-High |
| Algorithms | High |
| Reported best performance | Medium-High |
| Full limitations | Not confirmed |
| Full feature list | Not confirmed |
| Future work stated by authors | Not confirmed |
