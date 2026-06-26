# Paper 16: Genetic Algorithm Feature Selection for IVF Clinical Pregnancy Prediction

## Citation

Dehghan, S., Rabiei, R., Choobineh, H., Maghooli, K., Nazari, M., & Vahidi-Asl, M. (2024). **Comparative study of machine learning approaches integrated with genetic algorithm for IVF success prediction**. *PLOS ONE*, 19(10), e0310829.

DOI: [https://doi.org/10.1371/journal.pone.0310829](https://doi.org/10.1371/journal.pone.0310829)

Source checked: [PLOS ONE article page](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0310829)

Evidence note:

The title uses the broader phrase **IVF success prediction**, but the paper defines the primary outcome as **clinical pregnancy**, measured by positive beta-hCG after the treatment cycle. Therefore, this paper should be cited as clinical-pregnancy prediction evidence, not live-birth prediction evidence.

Related study terms:

- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [Beta-hCG](../glossary/clinical-glossary.md#beta-hcg)
- [AMH](../glossary/clinical-glossary.md#amh)
- [AFC](../glossary/clinical-glossary.md#afc)
- [Endometrial thickness](../glossary/clinical-glossary.md#endometrial-thickness)
- [Genetic algorithm](../glossary/technical-glossary.md#genetic-algorithm)
- [SMOTE](../glossary/technical-glossary.md#smote)
- [Feature selection](../glossary/technical-glossary.md#feature-selection)
- [AdaBoost](../glossary/technical-glossary.md#adaboost)
- [Support Vector Machine](../glossary/technical-glossary.md#support-vector-machine)
- [AUC](../glossary/technical-glossary.md#auc)
- [External validation](../glossary/technical-glossary.md#external-validation)

## Why This Paper Matters

This paper is useful because it studies a practical tabular-data IVF prediction problem using common machine-learning models and feature selection.

It supports an important direction for our PhD:

- clinic record data can be used for IVF outcome prediction
- feature selection is important because IVF datasets contain many clinical, laboratory and treatment variables
- ensemble models such as AdaBoost and Random Forest can perform strongly on structured IVF data
- single-center performance is not enough for clinical generalization

It is also helpful for our future dataset planning because the selected features include patient, ovarian-reserve, semen, follicle, oocyte and embryo-quality variables.

## Research Objective

The study aimed to compare five machine-learning algorithms for predicting IVF outcome and to examine whether Genetic Algorithm based feature selection improves model performance.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Peer-reviewed research article |
| Journal | PLOS ONE |
| Country | Iran |
| Clinical site | Royesh clinics, Helal-e-Iran Hospital, Tehran |
| Dataset source | Medical records of couples undergoing IVF cycles |
| Sample size | 812 patients |
| Cycle scope | Fresh ovarian-stimulation cycle for each couple |
| Exclusions | Donor oocytes/embryos, frozen oocytes/embryos, PGD/PGS cycles |
| Initial variables | 26 variables: 25 predictors and 1 target class |
| Final predictors for modeling | 22 predictors after preprocessing |
| Outcome label | Clinical pregnancy |
| Outcome definition | Positive beta-hCG test result after the treatment cycle |
| Class balance | 189 clinical-pregnancy yes, 623 clinical-pregnancy no |
| Public data availability | Dataset not publicly shared due to hospital ownership constraints; access may be requested through named contacts in the article |

Confidence: **High**

## Variables / Features Used

Confirmed feature categories:

- demographic data
- medical and reproductive history of both partners
- baseline information
- test results
- clinical diagnosis
- treatment procedure variables
- ovarian-reserve and hormone variables
- semen variables
- oocyte and embryo-quality variables

Important selected features reported by the authors:

| Feature | Meaning |
| --- | --- |
| Female age | Patient age |
| AMH | Ovarian reserve marker |
| Endometrial thickness | Uterine lining measurement |
| Follicle size | Ovarian stimulation response marker |
| Number of oocytes | Retrieved oocyte count |
| Quality of retrieved oocytes, MI | Oocyte maturity/quality category |
| Quality of retrieved oocytes, MII | Mature oocyte quality category |
| Sperm count | Semen parameter |
| Sperm morphology | Semen quality parameter |
| Embryo quality | Embryology quality variable |

Preprocessing decisions:

- smoking was excluded because values were constant in more than 90% of cases
- type of infertility and PCOs were excluded because their correlation was about zero
- missing numerical values were handled using average imputation
- missing categorical values were handled using mode imputation
- FSH, LH, AMH, AFC and vitamin D3 were converted into high, low and normal categories

Confidence: **High**

## Method / Algorithm

The study compared five machine-learning models:

| Algorithm | Role |
| --- | --- |
| Random Forest | Tree-based ensemble classifier |
| Artificial Neural Network | Neural-network classifier |
| Support Vector Machine | Margin-based classifier |
| RPART | Recursive partitioning and regression tree method |
| AdaBoost | Boosting ensemble classifier |

Feature selection:

- Genetic Algorithm was used as the feature-selection method.
- The selected feature subsets were then used as inputs for the classifiers.

Class imbalance handling:

- SMOTE was used to oversample the minority class.
- The paper states that balancing was performed only on the training set.
- Kolmogorov-Smirnov testing was used to compare original minority-class distributions with SMOTE-generated synthetic samples.

Implementation technology:

- Python
- Scikit-learn

Confidence: **High**

## Evaluation Metrics

The paper used:

- accuracy
- precision
- recall
- F-measure
- AUC
- 10-fold cross-validation
- random allocation into training and test sets

Confidence: **High**

## Main Findings

| Finding | Extracted Information |
| --- | --- |
| Best model | AdaBoost with Genetic Algorithm feature selection |
| Best reported accuracy | 89.8% |
| Second strong model | Random Forest with Genetic Algorithm feature selection |
| Random Forest reported accuracy | 87.4% |
| Best AUC | AdaBoost AUC 0.910 |
| Random Forest AUC | 0.903 |
| Effect of SMOTE | Improved classifier accuracy across all models |
| Effect of Genetic Algorithm | Improved performance measures for all classifiers |
| Most consistently selected feature | Female age |

The authors reported that Genetic Algorithm feature selection improved all classifiers, and that AdaBoost and Random Forest were the strongest models in this dataset.

Confidence: **High**

## Limitations Stated By Authors

| Limitation | Meaning |
| --- | --- |
| Single medical facility | Data came from one facility in Tehran, Iran. |
| Limited demographic/setting generalizability | Findings may not apply to other populations or healthcare systems. |
| Need external validation | Authors state that models should be externally validated in other studies. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Outcome is clinical pregnancy, not live birth | Clinical pregnancy is an intermediate outcome and may not translate to live birth. |
| Dataset is small compared with recent IVF-AI studies | 812 patients may limit stable model estimation and subgroup analysis. |
| Single-country, single-center evidence | Direct transfer to Indian IVF clinics is not justified without validation. |
| No explicit XAI method | Feature selection identifies variables, but it is not the same as patient-level explanation. |
| No clinical decision-support interface | The paper builds models but does not deploy or test a clinician-facing CDSS. |
| Lifestyle data is limited | Smoking appears in preprocessing, but broader lifestyle variables are not central. |
| Fairness/subgroup performance not reported | Performance across age groups, infertility causes or socioeconomic groups is not clearly evaluated. |
| SMOTE may inflate apparent performance if not carefully validated | The paper states training-only balancing, but independent external testing is still needed. |

Confidence: **High/Medium**

## Future Work Suggested

The paper directly supports:

- external validation on other datasets
- testing reliability and generalizability in other settings
- clinical use only after further validation

Our extension:

- validate on Indian IVF clinic data if available
- add explainability beyond global feature selection
- compare clinical-pregnancy prediction with stronger outcomes such as ongoing pregnancy and live birth
- evaluate whether the model can be used inside a clinician-facing decision-support workflow
- include lifestyle and longitudinal treatment variables if available

Confidence: **High for author-stated validation need; Medium for our extension**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need external validation | Yes | Authors explicitly state that external validation is needed. |
| Single-center study | Yes | Dataset came from one medical facility in Tehran. |
| Limited population diversity | Yes | Generalizability to other demographics/settings is limited. |
| Lack of XAI | Yes | No patient-level explainability method such as SHAP/LIME was reported. |
| No clinical decision support | Yes | No deployed CDSS or clinician workflow evaluation was reported. |
| Lack of lifestyle data | Partial | Smoking was considered but dropped; broader lifestyle features were not central. |
| Need stronger outcome labels | Yes | Outcome was clinical pregnancy, not live birth. |
| Lack of Indian population | Yes | Study population was Iranian, not Indian. |

## Usefulness For Our PhD

Relevance: **High for tabular IVF prediction and feature-selection evidence**

This paper helps us justify why IVF datasets should include:

- female age
- AMH
- endometrial thickness
- follicle measures
- oocyte quantity and quality
- semen parameters
- embryo quality

It also supports our plan to compare classical ML models before moving to complex deep-learning models, especially if the available clinic dataset is structured/tabular rather than image or video based.

However, this paper alone cannot justify a final PhD topic because it does not solve explainability, external validation, Indian population relevance or clinical decision-support deployment.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Dehghan et al. (2024) compared Random Forest, ANN, SVM, RPART and AdaBoost models with Genetic Algorithm based feature selection for IVF clinical-pregnancy prediction using 812 patient records from a Tehran IVF clinic, reporting the highest performance for AdaBoost with 89.8% accuracy and AUC 0.910.

Gap-support sentence:

> Although Genetic Algorithm based feature selection improved model performance, the study was limited to a single medical facility and the authors emphasized the need for external validation, reinforcing the generalizability gap in IVF-AI prediction research.

## What This Paper Does Not Prove

This paper does not prove that:

- AI improves live-birth rates.
- the model generalizes to Indian IVF patients.
- clinical-pregnancy prediction is sufficient for final IVF success counseling.
- Genetic Algorithm feature selection is always superior in every IVF dataset.
- a clinical decision-support system is ready for deployment.
- patient-level explanations are available.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Dataset source and sample size | High |
| Outcome definition | High |
| Algorithms and preprocessing | High |
| Main performance values | High |
| Stated limitations | High |
| Full detailed table values from images | Medium unless manually extracted from table images |
| Connection to our PhD gaps | High |
