# Paper 10: ML Prediction of Early Miscarriage After Single Vitrified-Warmed Blastocyst Transfer

## Citation

Liu, L., Liu, B., Wu, H., Gan, Q., Huang, Q., & Li, M. (2025). **Optimizing predictive features using machine learning for early miscarriage risk following single vitrified-warmed blastocyst transfer**. *Frontiers in Endocrinology*, 16.

DOI: [https://doi.org/10.3389/fendo.2025.1557667](https://doi.org/10.3389/fendo.2025.1557667)

Source checked: [Frontiers in Endocrinology article page](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2025.1557667/full)

Related study terms:

- [Frozen embryo transfer](../glossary/clinical-glossary.md#frozen-embryo-transfer)
- [Single embryo transfer](../glossary/clinical-glossary.md#single-embryo-transfer)
- [Blastocyst](../glossary/clinical-glossary.md#blastocyst)
- [Vitrification](../glossary/clinical-glossary.md#vitrification)
- [Miscarriage](../glossary/clinical-glossary.md#miscarriage)
- [Endometrial thickness](../glossary/clinical-glossary.md#endometrial-thickness)
- [Inner cell mass](../glossary/clinical-glossary.md#inner-cell-mass)
- [Trophectoderm](../glossary/clinical-glossary.md#trophectoderm)
- [Voting Classifier](../glossary/technical-glossary.md#voting-classifier)
- [Stacking Classifier](../glossary/technical-glossary.md#stacking-classifier)
- [SMOTETomek](../glossary/technical-glossary.md#smotetomek)
- [Mutual Information](../glossary/technical-glossary.md#mutual-information)

## Why This Paper Matters

This paper is useful because it focuses on a narrower but clinically important IVF outcome: **early miscarriage after single vitrified-warmed blastocyst transfer**.

It supports a key point for our research:

> IVF outcome prediction is not only pregnancy or live birth. Some clinically useful models may focus on post-transfer risks such as early miscarriage.

It also fits our FET/endometrium/embryology theme because it uses parental, embryonic and endometrial factors.

## Research Objective

The objective was to develop and compare machine-learning models for predicting early miscarriage risk after single vitrified-warmed blastocyst transfer.

The study particularly aimed to identify predictive features and evaluate whether ensemble learning models improve risk prediction compared with traditional models.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Dual-center retrospective prediction-model study |
| Country | China |
| Centers | First Affiliated Hospital of Guangxi Medical University and Nanning Maternity and Child Health Hospital |
| Study period | June 2016 to December 2022 |
| Reviewed SVBT cycles | 3,375 |
| Included clinical pregnancy SVBT cycles | 1,664 |
| Early miscarriage cases | 308 |
| Non-early miscarriage cases | 1,356 |
| Train-test split | 70% training, 30% testing |
| Cross-validation | Repeated stratified 10-fold cross-validation |
| Primary outcome | Early miscarriage |
| Data quality | Dataset reported complete with no missing values |

Confidence: **High**

## Outcome Definition

Early miscarriage was defined as spontaneous pregnancy loss before **12 weeks and 6 days** of gestation.

Confidence: **High**

## Variables / Features Used

The initial dataset included more than 40 features. A panel of three reproductive medicine experts selected 32 features for model development.

Selected feature groups included:

- maternal age
- paternal age
- BMI
- basal FSH
- previous gravidity
- infertility duration
- gonadotropin duration
- total gonadotropin dose
- number of oocytes retrieved
- endometrial thickness
- basal LH
- trigger-day estradiol
- blastulation time
- blastocyst stage
- inner cell mass grade
- trophectoderm grade
- cleavage-stage fragmentation
- number of blastomeres at cleavage stage
- infertility type
- previous parity
- previous abortions
- previous transfers
- infertility cause
- controlled ovarian hyperstimulation protocol
- fertilization method
- endometrial preparation protocol

Confidence: **High**

## Method / Algorithm

The paper evaluated several models, including:

- Logistic Regression
- Random Forest
- Gradient Boosting
- CatBoost
- Voting Classifier
- Stacking Classifier

Feature optimization methods:

- Mutual Information
- Recursive Feature Elimination with Random Forest

Class imbalance handling:

- SMOTETomek, combining SMOTE and Tomek Links

Preprocessing:

- label encoding for categorical variables
- min-max scaling for continuous variables
- stratified train-test split

Confidence: **High**

## Evaluation Metrics

The models were evaluated using:

- AUC
- accuracy
- precision
- recall
- F1 score
- specificity

Confidence: **High**

## Main Findings

Important baseline findings:

- Advanced maternal and paternal ages were associated with higher miscarriage risk.
- Miscarriage group had thinner endometrial thickness.
- Delayed blastocyst development by day 5 was more common in miscarriage cases.
- Poorer inner cell mass quality was associated with miscarriage.
- Ovarian-related infertility was more common in the miscarriage group.

Model performance:

| Model | Key Result |
| --- | --- |
| Logistic Regression | AUC 0.584 |
| Voting Classifier | Best overall: AUC 0.836, accuracy 0.780, precision 0.914, specificity 0.942 |
| Gradient Boosting | Strong performance: AUC 0.831, accuracy 0.777 |

The authors concluded that ensemble models, especially Voting Classifier and Gradient Boosting, improved early miscarriage prediction after SVBT.

Confidence: **High**

## Limitations Stated by Authors

The article’s abstract and discussion emphasize the value of the model, but explicit limitations are less detailed than some other papers.

Limitations supported by the study design include:

| Limitation | Meaning |
| --- | --- |
| Retrospective design | Prospective clinical value is not proven. |
| Two-center regional dataset | Wider multicenter, national or international validation is still needed. |
| Specific transfer type | Findings apply to SVBT, not all IVF/FET cycles. |
| Clinical pregnancy subset | Model was built among SVBT cycles resulting in clinical pregnancy, not all transfer cycles. |

Confidence: **Medium/High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Narrow outcome and population | Useful for miscarriage risk, but not a general IVF outcome model. |
| Class imbalance | Only 308 early miscarriage cases among 1,664 cycles; balancing method was required. |
| Regional China-only validation | No Indian validation or broader population testing. |
| No deployed CDSS | Model performance is reported, but no clinician-facing workflow is tested. |
| No patient-centered explanation | Feature selection is described, but clinician/patient interpretability is not deeply evaluated. |
| Post-pregnancy risk model | It supports risk management after clinical pregnancy, not pre-IVF or pre-transfer counseling for all patients. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- broader external validation
- clinical decision-support tools for miscarriage-risk counseling
- integrating parental, embryonic and endometrial variables
- prospective testing in FET/SVBT workflows
- improving individualized post-transfer risk monitoring

Confidence: **Medium/High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need clinical decision support | Yes | Individual miscarriage-risk estimates could support post-transfer counseling, but no CDSS is deployed. |
| Need external validation | Yes | Two-center regional retrospective data; wider validation needed. |
| FET/SVBT subgroup gap | Yes | Focuses on a specific transfer context. |
| Retrospective design | Yes | No prospective testing. |
| Explainability/trust gap | Partial | Feature selection is used, but no strong clinician-facing XAI evaluation. |
| Indian validation gap | Yes | China-only data. |

## Usefulness For Our PhD

Relevance: **Medium**

This paper is useful as a supporting paper for the FET/endometrium/embryology theme. It shows that ML can predict a specific post-transfer risk using combined parental, endometrial and embryonic variables.

However, it is not central to our main PhD direction unless our available clinic data includes:

- frozen embryo transfer cycles
- blastocyst quality details
- pregnancy follow-up and miscarriage outcomes

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Liu et al. (2025) developed machine-learning models for early miscarriage prediction after single vitrified-warmed blastocyst transfer using 1,664 clinical pregnancy cycles from two Chinese reproductive centers, with ensemble models such as Voting Classifier and Gradient Boosting outperforming logistic regression.

Gap-support sentence:

> Although the study demonstrates the value of parental, embryonic and endometrial variables for individualized miscarriage-risk prediction, its retrospective regional design, narrow SVBT population and lack of deployed clinical decision-support evaluation limit broader translation.

## What This Paper Does Not Prove

This paper does not prove that:

- the model predicts live birth for all IVF patients.
- the model applies to fresh embryo transfer.
- the model generalizes to Indian clinics.
- ensemble methods are always better for all IVF tasks.
- the model is ready for routine clinical deployment.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Dataset | High |
| Feature groups | High |
| Model list | High |
| Main findings | High |
| Author-stated limitations | Medium |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
