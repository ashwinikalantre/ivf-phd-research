# Panel Question Bank Stage 5

Stage 5 creates tentative research questions and hypotheses.

These are not final thesis commitments. They are dataset-dependent templates for panel discussion.

## Stage 5 Rule

Do not present a hypothesis unless the required data exists.

Use this wording:

> These are tentative research questions and hypotheses. The final set will be selected after clinic data access, outcome availability and variable completeness are confirmed.

## Research Question Selection Logic

| Step | Decision |
| --- | --- |
| 1 | Confirm available outcome: live birth, clinical pregnancy, miscarriage or other. |
| 2 | Confirm available predictors: clinical, embryology, lifestyle, imaging or mixed. |
| 3 | Confirm validation option: internal, temporal, external or multi-center. |
| 4 | Confirm whether clinician review is possible. |
| 5 | Select only research questions that can be tested with available data. |

## Core Research Questions

| RQ | Research Question | Required Data | Confidence |
| --- | --- | --- | --- |
| RQ1 | Which clinical variables are associated with IVF outcome prediction in the available clinic dataset? | Clinical variables + reliable outcome | Conditional |
| RQ2 | Can machine learning models predict IVF outcome better than a baseline statistical model? | Enough records, outcome balance, clinical predictors | Conditional |
| RQ3 | Does adding embryology variables improve prediction compared with clinical variables alone? | Clinical + embryology variables + same outcome | Conditional |
| RQ4 | Does adding lifestyle/contextual data improve prediction or personalization beyond clinical variables? | Reliable lifestyle/contextual variables + clinical variables + outcome | Conditional |
| RQ5 | Which variables most influence individual model predictions according to XAI methods? | Trained model + interpretable features | Conditional |
| RQ6 | Are model predictions well calibrated for clinical counseling? | Predicted probabilities + observed outcomes | Conditional |
| RQ7 | Does model performance differ across patient subgroups such as age, PCOS, endometriosis or transfer type? | Subgroup variables + sufficient subgroup size | Conditional |
| RQ8 | Does the model generalize to a second clinic, time period or independent source? | External clinic/source or temporal validation split | Conditional |
| RQ9 | Are clinician-facing explanations understandable and useful to IVF doctors? | Clinician review protocol + explanation outputs | Conditional |
| RQ10 | What minimum variable set can provide clinically useful IVF outcome prediction? | Full candidate variable set + feature-selection comparison | Conditional |

## Research Questions By Dataset Scenario

| Dataset Scenario | Suitable RQs | RQs To Avoid |
| --- | --- | --- |
| Clinical data only | RQ1, RQ2, RQ5, RQ6, RQ10 | RQ3, unless embryology variables exist |
| Clinical + embryology data | RQ1, RQ2, RQ3, RQ5, RQ6, RQ10 | Lifestyle claims unless lifestyle data exists |
| Clinical + lifestyle data | RQ1, RQ2, RQ4, RQ5, RQ6, RQ10 | Embryology claims unless embryo data exists |
| Multi-clinic or independent validation data | RQ8 plus relevant model RQs | Broad generalization claims beyond available sources |
| Clinician review possible | RQ9 plus XAI RQs | Claims of clinician usefulness without review |
| Live birth unavailable | Use clinical pregnancy version of RQs | Live-birth prediction claims |

## Tentative Hypotheses

These hypotheses are safe only when their data conditions are met.

| H | Tentative Hypothesis | Null Hypothesis | Required Data | Test / Evaluation | Confidence |
| --- | --- | --- | --- | --- | --- |
| H1 | Clinical variables can predict IVF outcome better than chance. | Clinical variables do not predict IVF outcome better than chance. | Clinical predictors + outcome | AUC with CI; logistic regression/ML comparison | Conditional |
| H2 | A machine learning model will outperform logistic regression for IVF outcome prediction. | ML performance is not significantly better than logistic regression. | Adequate sample size + outcome balance | AUC comparison, calibration, Brier score | Conditional |
| H3 | Adding embryology variables improves prediction compared with clinical variables alone. | Clinical + embryology model does not improve over clinical-only model. | Clinical + embryology variables | AUC, calibration, net benefit, nested model comparison | Conditional |
| H4 | Adding lifestyle variables improves personalization or prediction beyond clinical variables. | Lifestyle variables do not add predictive value beyond clinical variables. | Reliable lifestyle data | Model comparison, feature contribution, calibration | Conditional |
| H5 | XAI explanations identify clinically meaningful predictors for individual IVF outcome predictions. | XAI explanations do not provide clinically meaningful predictor information. | Trained model + XAI outputs + clinician review or expert interpretation | SHAP/LIME analysis; clinician rating if available | Conditional |
| H6 | Model performance varies across clinically important subgroups. | Model performance does not differ across subgroups. | Subgroup variables + sufficient sample size | Stratified AUC/calibration; interaction terms | Conditional |
| H7 | A model validated on an independent clinic/source will show acceptable generalization. | The model does not maintain acceptable performance on independent validation data. | Second clinic/source or temporal validation | External/temporal AUC, calibration, sensitivity/specificity | Conditional |
| H8 | Clinician-facing explanations improve perceived usefulness of the model output. | Clinician-facing explanations do not improve perceived usefulness. | Clinician review study | Survey/rating comparison; qualitative feedback | Conditional |

## Hypotheses To Avoid For Now

| Avoid Hypothesis | Why It Is Unsafe Now | Safer Version |
| --- | --- | --- |
| The model will increase IVF success rate. | Requires prospective clinical intervention and outcome testing. | The model may support counseling; clinical impact requires future prospective validation. |
| Lifestyle causes IVF failure. | Causality cannot be assumed from observational data. | Lifestyle variables may be associated with outcomes if measured reliably. |
| XAI will make doctors trust the model. | Trust must be measured, not assumed. | Clinicians can be asked to rate explanation usefulness and understandability. |
| The model works for all Indian IVF clinics. | Requires broad multi-center Indian validation. | The model can be tested on available Indian clinic data and limitations stated. |
| Deep learning will be superior. | Depends on data type and sample size. | Deep learning may be considered only for image/video or very large datasets. |

## Objective To RQ Mapping

| Objective | Related RQs | Evidence / Data Requirement |
| --- | --- | --- |
| Identify useful IVF outcome predictors | RQ1, RQ5, RQ10 | Clinical variables and outcome |
| Compare baseline and ML models | RQ2, RQ6 | Model-development dataset |
| Test value of embryology data | RQ3 | Structured embryology variables |
| Test value of lifestyle/contextual data | RQ4 | Reliable lifestyle data |
| Build explainable model outputs | RQ5 | XAI method such as SHAP/LIME |
| Evaluate validation/generalization | RQ6, RQ8 | Internal, temporal or external validation |
| Evaluate subgroup behavior | RQ7 | Sufficient subgroup sample |
| Evaluate clinician-facing explanation | RQ9 | Doctor review and rating protocol |

## Statistical And ML Test Map

| Question Type | Suitable Analysis | Notes |
| --- | --- | --- |
| Group comparison | Chi-square, t-test, Mann-Whitney U | Depends on variable type and distribution |
| Association with binary outcome | Logistic regression | Useful baseline and interpretable model |
| Model discrimination | AUC/ROC, PR-AUC | AUC alone is not enough |
| Probability accuracy | Calibration curve, Brier score | Important for counseling |
| Imbalanced outcome | Precision, recall, F1, PR-AUC | Especially if live birth or miscarriage class is imbalanced |
| Model comparison | Cross-validation, test-set metrics, DeLong test if appropriate | Must avoid data leakage |
| Feature contribution | SHAP, permutation importance | Explanation, not causality |
| Subgroup behavior | Stratified metrics, interaction terms | Needs sufficient sample size |
| Clinical utility | Decision curve analysis | Use only if meaningful thresholds exist |
| Clinician review | Likert-scale survey, thematic feedback | Requires review protocol |

## Final RQ Set Options

### Option A: Clinical Data Only

Use this if no embryo or lifestyle data is available.

1. Which clinical variables are associated with IVF outcome?
2. Can ML improve prediction over logistic regression?
3. Are model predictions calibrated enough for counseling?
4. Which clinical variables explain individual predictions?
5. What minimum clinical variable set is useful?

Suitable title:

**An Explainable Clinical Decision Support Framework for IVF Outcome Prediction Using Clinical Data**

### Option B: Clinical + Embryology Data

Use this if structured embryology data is available.

1. Which clinical and embryology variables predict IVF outcome?
2. Does adding embryology data improve performance over clinical data alone?
3. Which embryo-related variables influence patient-level predictions?
4. Is the model calibrated for counseling?
5. Can clinicians understand and use explanation outputs?

Suitable title:

**An Explainable and Personalized Clinical Decision Support Framework for IVF Outcome Prediction Using Multimodal Clinical and Embryological Data**

### Option C: Clinical + Embryology + Lifestyle Data

Use this only if lifestyle data is reliable.

1. Do lifestyle variables add predictive value beyond clinical and embryology variables?
2. Which lifestyle/contextual variables are associated with IVF outcome?
3. Can personalized explanations combine clinical, embryology and lifestyle factors?
4. Does model performance differ across lifestyle or demographic subgroups?
5. Can clinicians interpret lifestyle-inclusive explanations responsibly?

Suitable title:

**An Explainable Multimodal Clinical Decision Support Framework for Personalized IVF Outcome Prediction Using Clinical, Embryological and Lifestyle Data**

### Option D: Multi-Clinic Data

Use this if more than one clinic/source is available.

1. Does the model generalize across clinics?
2. Which variables remain stable predictors across clinics?
3. Does calibration differ by clinic?
4. Does XAI reveal clinic-specific prediction patterns?
5. What data-standardization issues affect validation?

Suitable title extension:

**with External Validation in Indian IVF Settings**

## Safe Panel Answers

Question:

> What is your main hypothesis?

Answer:

> The main hypothesis is not finalized. A safe tentative hypothesis is that an explainable model using available IVF clinical variables can predict the selected outcome better than chance and provide interpretable patient-level explanations. If embryology data is available, an additional hypothesis will test whether embryology variables improve performance over clinical variables alone.

Confidence: **Conditional**

Question:

> Why are your hypotheses not final?

Answer:

> Because hypotheses must match the actual dataset. If live birth, embryo variables, lifestyle variables or external validation data are not available, those hypotheses cannot be tested honestly.

Confidence: **Confident**

Question:

> Can you prove your model improves IVF success?

Answer:

> Not at this stage. That would require a prospective clinical intervention study. My current work can evaluate prediction, explanation, calibration and clinician usefulness, but not claim improved live-birth rates unless future prospective validation is done.

Confidence: **Confident**

## Stage 5 Completion Check

Stage 5 is complete when:

- every research question is tied to required data
- every hypothesis is conditional and testable
- unsafe hypotheses are explicitly blocked
- final RQs can be selected after clinic data audit

## Next Stage

Stage 6 should create the methodology blueprint:

- data collection
- preprocessing
- missing data handling
- model comparison
- validation
- XAI
- clinician review
- reporting metrics
