# Variable and Outcome Map

This page organizes variables and outcomes so panel answers stay precise.

The goal is to avoid vague answers like "we will collect many IVF variables." Instead, every variable should have a role, source, timing and feasibility status.


## Outcome Map

| Outcome | Role | Strength | Limitation | Use If |
| --- | --- | --- | --- | --- |
| Live birth | Preferred dependent variable | Strongest patient-centered IVF outcome | Requires follow-up until delivery | Live-birth records are reliable |
| Clinical pregnancy | Backup dependent variable | Commonly available earlier | Not equivalent to live birth | Live birth is missing or incomplete |
| Biochemical pregnancy | Intermediate outcome | Early signal after transfer | Weak endpoint for final success | Only early pregnancy data exists |
| Miscarriage | Secondary outcome | Useful for post-pregnancy risk | Different prediction stage | Pregnancy is already confirmed |
| Implantation success | Secondary/embryo-level outcome | Useful with embryo-level data | May not map directly to live birth | Embryo-specific records exist |
| Oocytes retrieved | Intermediate outcome | Useful for stimulation response | Not final IVF success | Research focuses on stimulation |
| Mature oocytes | Intermediate outcome | Stronger than total oocytes for stimulation | Still not final outcome | Maturity data is recorded |
| Cycle cancellation | Secondary outcome | Useful for treatment-risk modeling | Not pregnancy outcome | Cancellation is reliably recorded |

## Preferred Outcome Position

Panel answer:

> Live birth is the preferred outcome because it is the most meaningful endpoint for patients. However, if live-birth follow-up is not reliably available, clinical pregnancy can be used with a clear limitation. The final dependent variable will be fixed only after checking clinic records.

Confidence: **Conditional**

## Variable Role Map

| Variable Role | Simple Meaning | IVF Examples | Why It Matters |
| --- | --- | --- | --- |
| Dependent variable | Outcome to be predicted | Live birth, clinical pregnancy, miscarriage | Defines the model target |
| Independent variable | Predictor used by model/statistics | Age, BMI, AMH, embryo grade | Explains or predicts outcome |
| Confounder | Variable that affects both predictor and outcome | Age, infertility cause, previous IVF attempts | Must be adjusted or stratified |
| Moderator | Variable that changes relationship strength | PCOS, endometriosis, age group, transfer type | Helps subgroup/personalization analysis |
| Mediator | Variable on the pathway between predictor and outcome | Oocytes retrieved, embryos formed, embryo quality | Helps understand treatment pathway |
| Control variable | Variable included to reduce bias | Clinic year, stimulation protocol, diagnosis | Improves fair comparison |

## Variable Timing Map

| Timing | Variables | Can Be Used For | Caution |
| --- | --- | --- | --- |
| Before IVF starts | Age, BMI, infertility duration, diagnosis, AMH, AFC, semen parameters | Pre-treatment counseling | Cannot include future treatment response |
| During stimulation | gonadotropin dose, follicle count, trigger-day hormones | Stimulation response and cycle monitoring | Not available at first consultation |
| At retrieval/lab stage | oocytes retrieved, mature oocytes, fertilization, embryos formed | Oocyte/embryology prediction | Occurs after treatment starts |
| At embryo transfer | embryo grade, blastocyst grade, transfer day, endometrial thickness | Transfer outcome prediction | Cannot be used for pre-treatment prediction |
| After pregnancy confirmation | hCG, ultrasound pregnancy status, immune/coagulation markers | Miscarriage/live-birth risk after pregnancy | Different clinical question |
| Lifestyle/context | smoking, sleep, stress, diet, activity, occupation | Personalization and risk-factor analysis | Needs reliable questionnaire and consent |

## Mandatory Clinical Variables

These are the minimum candidate variables for a basic clinical model.

| Variable | Type | Measurement | Possible Source | Role |
| --- | --- | --- | --- | --- |
| Female age | Continuous / grouped | Years | Clinic record | Predictor/confounder |
| BMI | Continuous / grouped | kg/m2 | Height/weight or record | Predictor/confounder |
| Infertility duration | Continuous | Years | Clinical history | Predictor |
| Infertility type | Categorical | Primary/secondary | Clinical history | Predictor/control |
| Infertility cause | Categorical | PCOS, tubal, male factor, unexplained etc. | Diagnosis record | Predictor/moderator |
| AMH | Continuous | ng/mL or pmol/L | Lab record | Predictor |
| AFC | Count | Follicle count | Ultrasound record | Predictor |
| IVF/ICSI | Categorical | IVF, ICSI, split | Treatment record | Control/predictor |
| Fresh/frozen transfer | Categorical | Fresh/FET | Treatment record | Moderator/control |
| Endometrial thickness | Continuous | mm | Ultrasound record | Predictor |
| Number of embryos transferred | Count | 1, 2 etc. | Transfer record | Predictor/control |
| Outcome | Binary/multiclass | Clinical pregnancy/live birth etc. | Follow-up record | Dependent variable |

## Embryology Variables

These decide whether the title can honestly include `embryological data`.

| Variable | Type | Source | Role | Required For Multimodal Claim |
| --- | --- | --- | --- | --- |
| Oocytes retrieved | Count | Embryology/lab record | Mediator/predictor | Yes |
| Mature oocytes | Count | Embryology/lab record | Mediator/predictor | Strongly useful |
| Fertilization method | Categorical | Lab record | Control/predictor | Yes |
| Fertilization count/rate | Count/percentage | Lab record | Mediator/predictor | Strongly useful |
| Embryos formed | Count | Lab record | Mediator/predictor | Strongly useful |
| Embryo grade | Ordinal/categorical | Embryology record | Predictor | Strongly useful |
| Blastocyst grade | Ordinal/categorical | Embryology record | Predictor | Strongly useful |
| Transfer day | Categorical/count | Transfer record | Control/predictor | Useful |
| Embryo image/time-lapse | Image/video | Incubator/imaging system | Deep learning input | Optional/sensitive |

Panel answer:

> If embryo variables are not available, I will remove "embryological data" from the title. I will not claim multimodal clinical-embryology prediction unless the dataset supports it.

Confidence: **Confident**

## Lifestyle Variables

These should be treated as conditional, not guaranteed.

| Variable | Type | Source | Risk | Use |
| --- | --- | --- | --- | --- |
| Smoking | Categorical | Questionnaire/record | Underreporting | Lifestyle predictor |
| Alcohol | Categorical/frequency | Questionnaire | Sensitive | Optional predictor |
| Sleep quality | Scale | Questionnaire | Self-report bias | Personalization |
| Stress | Validated scale | Questionnaire | Subjective | Personalization |
| Physical activity | Scale/frequency | Questionnaire | Self-report bias | Lifestyle predictor |
| Diet pattern | Categorical/score | Questionnaire | Hard to measure accurately | Exploratory |
| Occupation/exposure | Categorical | Questionnaire | Privacy-sensitive | Optional context |

Panel answer:

> Lifestyle data is useful only if it is collected reliably and ethically. If it is not available in clinic records, it can be collected through a short validated questionnaire or kept as future work.

Confidence: **Conditional**

## AI And Model Variables

These are not clinical predictors; they describe model behavior and evaluation.

| Variable / Measure | Meaning | Use |
| --- | --- | --- |
| Model type | Logistic regression, Random Forest, XGBoost, LightGBM etc. | Compare baseline and ML models |
| Predicted probability | Estimated risk/chance of outcome | Counseling and CDSS output |
| AUC | Discrimination metric | Ranking ability |
| Sensitivity | True positive rate | Identifying likely positive outcomes |
| Specificity | True negative rate | Identifying likely negative outcomes |
| Precision | Positive predictive value | Reliability of positive predictions |
| F1-score | Balance of precision and recall | Imbalanced outcome evaluation |
| Calibration | Whether probabilities match reality | Counseling usefulness |
| Brier score | Probability error metric | Calibration assessment |
| SHAP/LIME output | Explanation of prediction | XAI and clinician review |
| Clinician usefulness rating | Doctor feedback | CDSS usability evaluation |

## Confounders To Watch

| Confounder | Why It Matters |
| --- | --- |
| Female age | Strongly related to ovarian reserve, embryo quality and outcome |
| Infertility diagnosis | Different diagnoses have different prognosis |
| Previous IVF attempts | Prior failure may indicate difficult prognosis |
| Clinic/lab protocol | Outcomes may differ by clinic practice |
| Transfer type | Fresh and frozen cycles differ |
| Number of embryos transferred | Strongly affects pregnancy chance and risk |
| Embryo quality | May mediate or confound transfer outcome |
| Year of treatment | Protocols and lab practice may change over time |

## Moderator Candidates

Use moderators only if subgroup size is sufficient.

| Moderator | Possible Question |
| --- | --- |
| Age group | Does model performance differ by age group? |
| PCOS status | Does prediction differ in PCOS patients? |
| Endometriosis status | Does prediction differ in endometriosis patients? |
| Fresh/FET | Does transfer type change predictor importance? |
| IVF/ICSI | Does insemination method affect model behavior? |
| Clinic/source | Does the model generalize across clinics? |

## Mediator Candidates

These help explain the IVF pathway, but should not be casually treated as baseline predictors.

| Mediator | Possible Pathway |
| --- | --- |
| Oocytes retrieved | Ovarian reserve/stimulation -> oocyte yield -> embryo availability |
| Mature oocytes | Follicle response -> mature oocytes -> fertilization |
| Fertilization count | Sperm/oocyte quality -> fertilization -> embryo formation |
| Embryo quality | Clinical/lab factors -> embryo quality -> pregnancy outcome |
| Endometrial thickness | Treatment/endometrial preparation -> receptivity -> implantation |

## Required Vs Optional Decision

| If This Is Missing | Impact On Study |
| --- | --- |
| Outcome variable | Outcome prediction is not feasible |
| Female age | Dataset is too weak for serious IVF modeling |
| AMH/AFC | Ovarian-reserve interpretation becomes weaker |
| Embryo variables | Remove multimodal embryology claim |
| Lifestyle variables | Remove lifestyle personalization claim |
| Second clinic/source | Remove external validation claim |
| Clinician review | Remove clinician-usability claim |
| Live birth | Use clinical pregnancy only with limitation |

## Variables And Claims

| Claim | Required Variables / Evidence |
| --- | --- |
| Clinical IVF prediction | Clinical predictors + pregnancy/live-birth outcome |
| Live-birth prediction | Reliable live-birth outcome |
| Multimodal prediction | At least two data modalities, such as clinical + embryology |
| Lifestyle personalization | Reliable lifestyle variables collected ethically |
| External validation | Independent clinic/source/time split |
| Clinician-usable XAI | Clinician review of explanation outputs |
| Deep learning | Image/video or very large suitable dataset |
| Treatment recommendation | Treatment decision variable + clinical safety validation |

## Safe Panel Answers

Question:

> What is your dependent variable?

Answer:

> The preferred dependent variable is live birth. If live-birth follow-up is incomplete, clinical pregnancy will be used with a clear limitation. The final dependent variable will be decided after checking clinic records.

Confidence: **Conditional**

Question:

> What are your independent variables?

Answer:

> Candidate independent variables include age, BMI, infertility duration and diagnosis, AMH, AFC, treatment type, transfer type, endometrial thickness and embryo variables if available. The final list will come from the clinic data dictionary.

Confidence: **Conditional**

Question:

> Are lifestyle variables part of the main study?

Answer:

> Only if they are available or can be collected reliably through an approved questionnaire. Otherwise lifestyle will remain future work or a separate sub-study.

Confidence: **Conditional**

Question:

> Why do you need embryo variables?

Answer:

> Embryo variables can add information about fertilization and embryo development, which clinical baseline variables alone may miss. But I will include them only if structured embryology records are available.

Confidence: **Conditional**
