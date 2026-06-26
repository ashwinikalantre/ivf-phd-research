# Faculty Panel Question Bank

Use this page before the faculty presentation. The aim is to answer clearly, with evidence, without claiming more than the literature and available data support.

## Answering Rule

For every question, answer in this order:

1. direct answer in simple English
2. one evidence point or statistic
3. limitation or caution
4. how it connects to the proposed PhD work

## Quick Defense Position

| Panel concern | Safe position |
| --- | --- |
| Is the title final? | No. It is a provisional direction. The final title depends on clinic data access. |
| Is the novelty only prediction? | No. Prediction alone is not enough. The stronger opportunity is explainable, validated and doctor-facing decision support. |
| Can AI replace doctors? | No. The proposed system is clinical decision support, not automated treatment decision-making. |
| Can lifestyle data be included? | Only if it can be collected reliably through a structured questionnaire or clinic record. |
| Can external validation be claimed? | Only if data from another clinic, time period or independent source is available. |

## High-Priority Questions

| Question | Short answer | Evidence to mention | Confidence | What not to claim |
| --- | --- | --- | --- | --- |
| Why choose IVF as a PhD area? | IVF is clinically important, costly and decision-heavy. Many couples face uncertainty across repeated cycles. | WHO estimates about 1 in 6 adults experience infertility globally. | High | Do not say IVF solves infertility for everyone. |
| Why AI in IVF? | IVF data contains many interacting clinical, hormonal, treatment and embryology variables. ML can help discover patterns and support counseling. | Literature from 2021-2025 shows many models for live birth, pregnancy, embryo selection and stimulation decisions. | High | Do not say AI will replace embryologists or doctors. |
| Why not only build a prediction model? | Many papers already predict IVF outcomes. The repeated gaps are explainability, validation and clinical decision-support translation. | In our 35-paper matrix, external validation and CDSS gaps appear repeatedly. | High | Do not present simple prediction as sufficient novelty. |
| What is the main research gap? | Existing studies often remain model-centric. They do not consistently become explainable, externally validated, clinician-usable decision-support systems. | Gap frequency table: external validation, CDSS translation, real-world deployment and trustworthy AI recur across multiple papers. | High | Do not treat every paper limitation as a PhD gap. |
| Why is explainability important? | Doctors need to know why a model gives a score before using it in counseling or treatment planning. | XAI methods such as SHAP and LIME are commonly used for feature-level explanation. | High | Do not say SHAP proves causality. |
| Why Indian validation? | Indian IVF patients, access, affordability, clinic workflows and diagnosis profiles may differ from international datasets. | Many AI-IVF studies are single-country or single-center. Indian data is underrepresented in the reviewed work. | Medium/High | Do not claim all foreign models fail in India without testing. |
| What is the provisional research direction? | An explainable and personalized clinical decision-support framework for IVF outcome prediction using available clinical and embryological data. | Direction comes from repeated gaps, not one paper. | High | Do not call the title final before data access is confirmed. |

## Statistics Questions

| Question | Simple answer | Number to quote | Source | Confidence |
| --- | --- | ---: | --- | --- |
| How common is infertility globally? | It is a major global reproductive-health issue. | About 1 in 6 adults, or 17.5%, experience infertility in their lifetime. | WHO | High |
| What is India’s fertility context? | India’s total fertility rate has declined, but infertility and delayed treatment remain important healthcare issues. | NFHS-5 TFR: 2.0; NFHS-4 TFR: 2.2. | NFHS-5 | High |
| What is the Indian infertility prevalence figure we can safely quote? | Use the peer-reviewed definition carefully. | 18.7 per 1,000 among currently married women in union for at least five years, 2019-20. | Peer-reviewed Indian study using NFHS-5 | Medium/High |
| What is a typical IVF success figure? | It depends on age and denominator. Always say success per what. | HFEA 2023: fresh embryo-transfer birth rate 35% for ages 18-34 and 5% for ages 43-44 using own eggs. | HFEA | High |
| What is the economic burden in India? | IVF is often expensive and paid out-of-pocket. | Public OOPE about Rs. 1.10 lakh; private OOPE about Rs. 2.38 lakh; catastrophic expenditure 85%. | HTAIn/ICMR-NIRRCH policy brief | High |
| How many IVF clinics are in India? | The official current registry should be checked directly before presentation. An older PIB figure reported 308 ICMR-enrolled ART clinics in 2015. | 308 in 2015, old figure. | PIB and National ART & Surrogacy Registry | Medium |

## Success-Rate Questions

| Question | Safe answer |
| --- | --- |
| What is IVF success rate? | There is no single IVF success rate. It depends on age, own eggs or donor eggs, fresh or frozen transfer, diagnosis, clinic practice and denominator. |
| Why do success rates differ across sources? | Some report pregnancy, some live birth, some per started cycle, some per retrieval, some per embryo transfer, and some cumulative success. |
| Can we compare natural pregnancy and IVF pregnancy directly? | Not directly. IVF patients usually already have infertility or subfertility, so the populations are different. |
| Which outcome should the PhD predict? | Live birth is strongest if available. Clinical pregnancy is acceptable if live birth is not reliably recorded. |
| Should miscarriage be included? | It can be a secondary outcome if records are complete enough. |

## Dataset Questions

| Question | Answer |
| --- | --- |
| What minimum data is needed? | Age, BMI, infertility diagnosis, infertility duration, AMH, AFC, IVF/ICSI, fresh/frozen transfer, stimulation protocol, endometrial thickness, embryos transferred and pregnancy/live-birth outcome. |
| What makes the dataset stronger? | Embryology variables such as oocytes retrieved, mature oocytes, fertilization, embryo grade, blastocyst grade and transfer day. |
| What makes it best for this topic? | Clinical + embryology + lifestyle variables, with a second clinic or external dataset for validation and clinician review of explanations. |
| What if embryo data is not available? | The title should be reduced to clinical-data-based explainable CDSS. |
| What if lifestyle data is not available? | Lifestyle should be kept as future work or a separate questionnaire-based sub-study. |
| What if only one clinic gives data? | Use internal validation and temporal validation. Do not claim multicentre external validation. |
| How many records are needed? | It depends on outcome frequency, missingness and number of predictors. The first step is to audit available cycles and outcome balance before fixing model complexity. |

## Methodology Questions

| Question | Safe answer |
| --- | --- |
| Which models will be used? | Start with logistic regression as a baseline, then compare Random Forest, XGBoost and LightGBM for tabular clinical data. |
| Why not deep learning first? | Deep learning usually needs larger datasets or image/time-lapse embryo data. For clinic tabular data, boosted trees and interpretable baselines are more realistic. |
| Which evaluation metrics? | AUC, sensitivity, specificity, precision, recall, F1, calibration and Brier score. Decision curve analysis can be added if clinically meaningful thresholds are available. |
| How will explainability be evaluated? | Use global feature importance and local patient-level explanations, then ask clinicians whether explanations are understandable and useful. |
| How will overfitting be handled? | Train/test split, cross-validation, careful feature selection, calibration testing and external or temporal validation where possible. |
| How will missing data be handled? | First report missingness. Then use clinically sensible imputation and compare model performance with transparent missing-data handling. |

## Ethics and Privacy Questions

| Question | Safe answer |
| --- | --- |
| Will patient identity be used? | No. Data should be anonymized or de-identified before analysis. |
| Is ethics approval needed? | Yes. Clinic permission and institutional ethics approval are required before using patient records. |
| Can the system advise treatment? | It should support counseling and risk understanding. Final treatment decisions remain with clinicians. |
| How will bias be checked? | Compare performance across age groups, diagnosis categories and other available subgroups. |
| Is lifestyle data sensitive? | Yes. It should be collected only with consent and with clear purpose, minimal variables and privacy protection. |

## Novelty Questions

| Question | Strong answer |
| --- | --- |
| What is new here? | The novelty is not "using ML in IVF". The research opportunity is an explainable, personalized and clinically reviewed decision-support framework, validated as far as the available data allows. |
| How is this different from existing prediction papers? | Existing papers often stop at model performance. This work aims to connect prediction, explanation, dataset feasibility, clinician review and decision-support presentation. |
| What if external validation is not possible? | Then the thesis should honestly present internal and temporal validation, and frame external validation as future work. |
| What if the model accuracy is moderate? | A moderate but well-calibrated and explainable model may still support counseling if used carefully. The goal is clinical usefulness, not only highest accuracy. |

## Questions To Ask Doctors

| Area | Question |
| --- | --- |
| Data access | How many IVF/ICSI cycles from 2021-2025 can be shared in anonymized form? |
| Outcomes | Are clinical pregnancy, live birth, miscarriage and cycle cancellation recorded reliably? |
| Embryology | Are embryo grades, blastocyst grades and transfer-day details available digitally? |
| Lifestyle | Are BMI, smoking, alcohol, sleep, stress, diet or activity recorded? If not, can a short questionnaire be used? |
| Validation | Can data be separated by year, doctor, protocol or clinic for validation? |
| Clinician review | Can doctors review sample model explanations and comment on usefulness? |
| Ethics | What permissions are required from the hospital, clinic and ethics committee? |

## Answers To Avoid

| Avoid saying | Say instead |
| --- | --- |
| AI will decide IVF treatment. | AI will support doctors with prediction and explanation. |
| Our model will increase IVF success. | The model may improve counseling and decision support; clinical effect needs prospective validation. |
| Lifestyle definitely causes IVF failure. | Lifestyle factors may influence fertility, but they must be measured carefully and interpreted cautiously. |
| This is the final title. | This is the current working direction. The final title depends on data feasibility. |
| We will prove the model works for India. | We will validate on available Indian clinic data and clearly state the limits. |

## Closing Answer For Faculty

The project has moved from a broad IVF interest to a literature-supported research direction. The strongest repeated gap is not only prediction, but the lack of explainable, validated and clinician-usable AI decision support in IVF. The next step is clinic data confirmation. After that, the final title, objectives and methodology can be fixed responsibly.
