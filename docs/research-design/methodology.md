# Proposed Methodology

This methodology is proposal-level and should be refined after data access is confirmed.

## Stage 1: Literature Review and Gap Analysis

1. Search papers from 2021-2025.
2. Extract abstract, conclusion, limitations and future work.
3. Maintain Excel literature matrix.
4. Classify papers by theme.
5. Create gap-frequency table.
6. Shortlist repeated PhD-relevant gaps.

Output:

- literature review matrix
- gap frequency table
- theme-wise review
- finalized research gap

## Stage 2: Data Collection and Preparation

Possible data groups:

| Data Group | Examples |
| --- | --- |
| Demographic | age, BMI, infertility duration, prior cycles |
| Clinical | AMH, AFC, FSH, LH, estradiol, progesterone, diagnosis |
| Treatment | stimulation protocol, gonadotropin dose, trigger, oocytes retrieved |
| Embryology | embryo grade, blastocyst quality, oocyte quality, sperm parameters |
| Contextual/lifestyle | smoking, stress, sleep, diet, activity, occupation, socioeconomic context |

Data preparation:

- missing-value analysis
- outlier handling
- feature encoding
- class imbalance handling
- train/validation/test split
- external validation if a second dataset is available

## Stage 3: Model Development

Candidate models:

- Logistic Regression as baseline
- Random Forest
- XGBoost or LightGBM
- Support Vector Machine
- Neural network only if data volume supports it
- ensemble model if justified

Primary outcomes:

- clinical pregnancy
- live birth
- miscarriage or failed cycle, depending on data availability

## Stage 4: Explainability

Candidate XAI methods:

- SHAP
- LIME
- permutation importance
- partial dependence plots
- patient-level explanation cards

Explanation outputs should answer:

- What factors increased predicted success?
- What factors reduced predicted success?
- Which factors are modifiable?
- Which factors are non-modifiable?
- How confident is the prediction?

## Stage 5: Evaluation

Performance:

- AUC
- accuracy
- sensitivity
- specificity
- precision
- recall
- F1 score

Clinical reliability:

- calibration curve
- Brier score
- decision curve analysis if feasible

Generalizability:

- subgroup analysis
- clinic-wise validation if data permits
- Indian population validation if data permits

Explainability/usability:

- clinician review of explanation usefulness
- patient-understandability review if feasible
- qualitative feedback or structured questionnaire

## Stage 6: Decision-Support Framework

The final framework should provide:

- predicted IVF outcome probability
- patient-specific drivers
- caution flags
- explanation summary
- counseling support text
- clinician review step

The system should support decision-making, not replace the doctor.
