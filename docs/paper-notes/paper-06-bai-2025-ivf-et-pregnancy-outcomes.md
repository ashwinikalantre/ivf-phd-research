# Paper 06: Multiple ML Models for IVF-ET Pregnancy and Live-Birth Prediction

## Citation

Bai, R., Li, J.-W., Hong, X., Xuan, X.-Y., Li, X.-H., & Tuo, Y. (2025). **Predictive modeling of pregnancy outcomes utilizing multiple machine learning techniques for in vitro fertilization-embryo transfer**. *BMC Pregnancy and Childbirth*, 25, Article 316.

DOI: [https://doi.org/10.1186/s12884-025-07433-2](https://doi.org/10.1186/s12884-025-07433-2)

Source checked: [Springer Nature article page](https://link.springer.com/article/10.1186/s12884-025-07433-2)

Related study terms:

- [IVF](../glossary/clinical-glossary.md#ivf)
- [Embryo transfer](../glossary/clinical-glossary.md#embryo-transfer)
- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [2PN zygote](../glossary/clinical-glossary.md#2pn-zygote)
- [OHSS](../glossary/clinical-glossary.md#ohss)
- [XGBoost](../glossary/technical-glossary.md#xgboost)
- [LightGBM](../glossary/technical-glossary.md#lightgbm)
- [Random Forest](../glossary/technical-glossary.md#random-forest)
- [Support Vector Machine](../glossary/technical-glossary.md#support-vector-machine)
- [Feature selection](../glossary/technical-glossary.md#feature-selection)

## Why This Paper Matters

This paper is useful because it is a recent IVF-ET outcome prediction study using several common machine-learning models on structured clinical data.

It connects directly to our base theme:

> IVF outcome prediction using clinical and treatment-cycle variables.

It is also useful because it clearly shows a common limitation in many IVF prediction papers: high model performance is reported, but the study is single-center, retrospective and locally specific.

## Research Objective

The study aimed to:

1. identify factors influencing pregnancy outcomes in IVF-ET
2. construct multiple machine-learning prediction models
3. compare models for predicting clinical pregnancy and live birth
4. identify high-performing models that may have clinical use

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Retrospective single-center prediction-model study |
| Country | China |
| Center | Reproductive Center of the Affiliated Hospital of Inner Mongolia Medical University |
| Study years | 2016 to 2022 |
| Initial cohort | 3,880 women |
| Excluded / missing / lost to follow-up | 1,255 women |
| Final modeled cohort | 2,625 women |
| Treatment type | Fresh-cycle IVF-ET |
| Inclusion age | 20 to 40 years |
| Clinical pregnancy group | 2,031 |
| Non-clinical pregnancy group | 594 |
| Live birth group | 1,711 |
| Non-live birth group | 320 |
| Data availability | Available from corresponding author on reasonable request |

Confidence: **High**

## Inclusion and Exclusion

Inclusion criteria:

- age 20 to 40 years
- fresh embryo-transfer cycle

Exclusion criteria included:

- chronic systemic diseases such as hypertension, diabetes, heart disease
- IVF mainly due to male-factor infertility
- chromosomal abnormalities
- recurrent miscarriages
- decreased ovarian reserve function
- major missing medical records

Confidence: **High**

## Variables / Features Used

The study collected clinical, hormone, stimulation, embryology and transfer-related features.

Confirmed variables include:

- age
- BMI
- infertility factors
- infertility duration
- infertility type
- menstrual history
- disease and surgical history
- smoking and alcohol history
- LH
- FSH
- prolactin
- progesterone
- estradiol
- AMH
- gonadotropin starting dose
- gonadotropin stimulation duration
- total gonadotropin dose
- total follicle count
- HCG
- number of oocytes retrieved
- number of 2PN embryos
- number of transferable embryos
- number of high-quality embryos
- endometrial thickness
- number of embryos transferred

The article states that 30 observational indices were collected.

Confidence: **High**

## Method / Algorithm

Eight machine-learning models were constructed:

| Model | Role |
| --- | --- |
| SVM | Comparison model |
| KNN | Comparison model |
| Random Forest | Ensemble tree model |
| Extra Trees | Ensemble tree model |
| XGBoost | Gradient boosting model |
| Multilayer Perceptron | Neural-network comparison model |
| Logistic Regression | Baseline/statistical ML model |
| LightGBM | Gradient boosting model |

Other processing and analysis steps:

- SPSS 26.0 for statistical analysis
- Python 3.11 for model construction
- Z-score standardization
- Spearman correlation analysis
- exclusion of highly correlated features above 0.9
- Lasso regression with cross-validation for feature selection
- fivefold cross-validation
- independent test-set validation

Important source caution:

The abstract states that the dataset was divided into training and test sets in an **8:2 ratio**. Later, the article text appears to state that the test set consisted of 2,100 cases, or 80%, and the training set consisted of 525 cases, or 20%. This is internally inconsistent with standard wording and with the abstract. Therefore, the exact train-test direction should be treated carefully unless confirmed from the PDF/supplementary material or authors.

Confidence: **High** for models and preprocessing; **Medium** for exact train-test split direction because of article-text inconsistency.

## Evaluation Metrics

The paper reports or discusses:

- accuracy
- AUC
- 95% confidence interval
- sensitivity
- specificity
- recall
- precision
- positive prediction rate
- negative prediction rate
- F1 index
- ROC curve
- confusion matrix

Confidence: **High**

## Main Findings

### Best models

| Prediction Task | Best Model | Reported AUC |
| --- | --- | ---: |
| Clinical pregnancy | XGBoost | 0.999, 95% CI 0.999-1.000 |
| Live birth | LightGBM | 0.913, 95% CI 0.895-0.930 |

### Accuracy examples reported in article text

| Task | Model | Training Accuracy | Test Accuracy |
| --- | --- | ---: | ---: |
| Pregnancy | Random Forest | 0.997 | 0.964 |
| Pregnancy | XGBoost | 0.996 | 0.986 |
| Pregnancy | LightGBM | 0.999 | 0.990 |
| Live birth | XGBoost | 0.884 | 0.712 |
| Live birth | LightGBM | 0.857 | 0.744 |

The authors conclude that XGBoost performed best for pregnancy prediction and LightGBM performed best for live-birth prediction.

Confidence: **High**

## Limitations Stated by Authors

The authors identify several limitations and cautions:

| Limitation | Meaning |
| --- | --- |
| Local fresh day-3 transfer practice | Most women in this setting chose fresh day-3 embryo transfer, which differs from centers using blastocyst transfer or freeze-all cycles. |
| Limited generalizability | Findings are based on local IVF characteristics and may not generalize to other centers. |
| Preliminary study | The authors describe it as an exploratory/preliminary prediction-model study. |
| Need standard-category testing | Future work should test model performance in standard infertility categories. |
| Not ideal for pre-treatment counseling | The models included pre-treatment and during-treatment variables, so they do not fully support pre-treatment counseling before IVF begins. |
| Standardization and ethical issues | AI in assisted reproduction faces standardization, data collection and data breach concerns. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Very high pregnancy AUC | AUC of 0.999 is unusually high and should be interpreted cautiously, especially with during-treatment variables such as HCG and embryo-related variables. |
| Possible data leakage risk | Including variables collected after treatment starts may make prediction easier but less useful for early counseling. |
| Single-center China dataset | No external clinic validation or Indian validation. |
| Fresh day-3 transfer setting | Transfer practice differs from many clinics using blastocyst or frozen transfer. |
| Internal train-test inconsistency | The article contains conflicting train/test wording, so exact split direction needs caution. |
| No XAI or clinician usability evaluation | The study compares model performance but does not deeply evaluate explainability or CDSS workflow. |
| Missing data excluded | Excluding records with missing data may introduce selection bias. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- prediction models using only pre-treatment data
- models useful for counseling before IVF begins
- testing in standard infertility categories
- improving clinical decision-making support
- addressing AI standardization and data protection
- external validation across other centers and transfer practices

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need external validation | Yes | Single-center model with no independent clinic validation. |
| Need clinical decision support | Yes | Authors discuss clinical value, but no deployed CDSS is tested. |
| Retrospective design | Yes | Uses retrospective clinical records. |
| Pre-treatment counseling gap | Yes | Authors explicitly state that during-treatment variables limit pre-treatment counseling use. |
| Standardization gap | Yes | Authors discuss lack of AI standards and variation in data collection. |
| Explainability gap | Yes | No strong XAI or clinician-facing explanation layer. |
| Indian validation gap | Yes | China-only data, no Indian validation. |

## Usefulness For Our PhD

Relevance: **High**

This paper is useful as evidence that structured clinical and treatment-cycle data can produce strong IVF outcome prediction models.

However, it also strongly supports our careful PhD framing. A model can achieve high performance but still have limited clinical usefulness if it:

- uses variables available only after treatment begins
- lacks external validation
- lacks explainability
- is limited to one center and one transfer practice
- is not converted into a clinician-facing decision-support workflow

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Bai et al. (2025) developed multiple machine-learning models using clinical and treatment-cycle data from 2,625 fresh IVF-ET patients at a single Chinese reproductive center, reporting XGBoost as the best model for clinical pregnancy prediction and LightGBM as the best model for live-birth prediction.

Gap-support sentence:

> Although the study reported high predictive performance, its retrospective single-center design, local fresh day-3 transfer practice, use of during-treatment variables and lack of external validation limit direct translation into pre-treatment counseling or generalized clinical decision support.

## What This Paper Does Not Prove

This paper does not prove that:

- the model generalizes to Indian IVF clinics.
- high AUC automatically means clinical usefulness.
- the model can support pre-treatment counseling before IVF starts.
- the model is ready for real-world CDSS deployment.
- XGBoost or LightGBM is always best for IVF prediction in other datasets.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Dataset | High |
| Variables/features | High |
| Model list | High |
| Main findings | High |
| Author-stated limitations | High |
| Exact train-test split direction | Medium due to source inconsistency |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
