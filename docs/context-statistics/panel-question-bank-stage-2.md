# Panel Question Bank Stage 2

This page converts selected high-priority panel questions into safe, evidence-based answers.

Stage 2 is not the final defense script. It is the evidence-backed answer bank that will later be shortened into spoken answers.

## Answer Confidence Labels

| Label | Meaning |
| --- | --- |
| Confident | Supported by reviewed papers, statistics pages or reliable sources. |
| Conditional | Depends on clinic data access, outcome availability or ethics approval. |
| Not yet claimable | Should not be stated as a conclusion at this stage. |

## How To Answer In Panel

Use this order:

1. give the direct answer
2. mention evidence
3. state the limitation
4. connect it to the PhD direction

Example:

> The literature supports IVF outcome prediction as an active AI area, but model accuracy alone is not enough. Across reviewed papers, repeated gaps include external validation, clinical decision-support translation and real-world deployment. Therefore, my current direction is explainable and validated decision support, not simply another prediction model.

## Core Position

| Panel concern | Safe position | Confidence |
| --- | --- | --- |
| Is the title final? | No. The current title is a working direction. Final title depends on clinic dataset confirmation. | Confident |
| Is the novelty only machine learning? | No. ML prediction already exists. The stronger gap is explainable, validated, clinician-usable decision support. | Confident |
| Can AI replace doctors? | No. The proposed work is clinical decision support. Doctors remain responsible for treatment decisions. | Confident |
| Can lifestyle data be promised? | Not yet. Lifestyle can be included only if collected reliably and ethically. | Conditional |
| Can external validation be promised? | Only if another clinic, time period or independent dataset is available. | Conditional |
| Can improved IVF success be claimed? | No. At this stage we can study prediction, explanation and decision support, not prove improved live-birth rates. | Not yet claimable |

## Domain Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| Why choose IVF as the healthcare domain? | IVF is clinically important, costly and emotionally sensitive. Patients and clinicians face uncertainty across stimulation, embryo selection, transfer and outcome prediction. | Context statistics pages; reviewed IVF-AI papers across prediction, stimulation, embryo selection and XAI. | Confident | I am not claiming IVF is the only important domain. I selected it because it has high decision complexity and a growing AI literature. |
| Why is IVF outcome prediction important? | It can support counseling, risk understanding and planning, especially when patients ask about chances of pregnancy or live birth. | Papers 5, 7, 8, 9, 17, 29, 30 and 31 study IVF/ART outcome prediction. | Confident | Prediction should support counseling. It should not be treated as a guarantee of success or failure. |
| Why is live birth stronger than clinical pregnancy? | Live birth is the final treatment outcome patients care about most. Clinical pregnancy occurs earlier and is useful, but it does not guarantee live birth. | Paper notes repeatedly distinguish clinical pregnancy and live birth; Paper 30 uses live birth, Paper 31 uses clinical pregnancy. | Confident | If live birth is not reliably recorded, clinical pregnancy may be used but must be stated as a limitation. |
| Why does age matter in IVF? | Female age is repeatedly used as an important predictor in IVF studies and is strongly linked to reproductive outcome. | Papers 7, 17, 29, 30, 31 and 33 include age-related predictors. | Confident | I should not reduce IVF outcome to age alone. It interacts with ovarian reserve, embryo quality, diagnosis and treatment factors. |
| Why separate fresh and frozen embryo transfer? | Fresh and frozen transfers can have different biological and treatment contexts, so outcome patterns may differ. | Papers 8 and 31 focus fresh transfer; Paper 25 focuses FET; Paper 10 focuses vitrified-warmed blastocyst transfer. | Confident | If dataset contains both, transfer type should be modeled or stratified. |

## Literature Review Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| How many papers have been reviewed so far? | Thirty-five paper notes have been prepared in the site. They include model-development papers, XAI papers, CDSS papers, reviews, RCT evidence and adoption survey evidence. | Paper Reading Notes index. | Confident | The number can increase, but current Stage 2 answers are based on the reviewed set. |
| Why use 2021-2025 papers? | This period captures recent AI-IVF work, especially modern ML, XAI, CDSS and validation discussions. Older foundational papers may still be cited if needed. | Project scope and literature matrix. | Confident | I am not excluding older science completely; the primary review window is recent literature. |
| Which papers are strongest evidence? | Stronger papers include multicenter or prospective studies, RCTs, high-quality reviews and full-text model papers. Examples: Paper 1, 2, 5, 21, 25, 28, 30, 31 and 33. | Paper notes and source registry. | Confident | Strength depends on the question. A review is strong for framing, while an RCT is stronger for clinical effect. |
| Which papers should be used cautiously? | Papers with limited full-text access, preprints, single-center retrospective data or non-indexed/less established venues should be used cautiously. | Paper 14 is preprint; Paper 29 source access is article-page limited; Paper 32 full-text details are limited. | Confident | Cautious does not mean useless. It means the claim should match the evidence level. |
| What are the major literature themes? | Major themes are IVF outcome prediction, embryo selection/grading, ovarian stimulation CDSS, FET/endometrium prediction, XAI/trustworthy AI, Indian/lifestyle data and clinical deployment. | Theme-wise review pages and paper notes. | Confident | The final PhD should select one focused theme, not attempt all themes. |

## Research Gap Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| What is the main research gap? | The main gap is not just prediction. Many studies stop at model performance and lack external validation, explainability, clinician usability and real-world decision-support evaluation. | Literature matrix and papers 12, 13, 26, 28, 32, 34 and 35. | Confident | I will avoid saying every paper has all gaps. The claim is based on repeated patterns across papers. |
| Why is external validation important? | A model can perform well in one clinic but fail in another because patient population, lab practice, protocols and data quality differ. | Papers 5, 29, 30, 31 and 33 highlight generalization/external-validation concerns. | Confident | If external validation is not available, I can use internal and temporal validation but must state the limitation. |
| Why is single-center data a limitation? | Single-center data may capture local practice and patient mix rather than a general IVF pattern. | Papers 6, 21, 25, 29, 30, 31 and 33 contain single-center or limited-source concerns. | Confident | Single-center studies are still useful, but they should not claim broad generalization. |
| Is explainability still a gap? | Yes, especially when models are intended for clinician counseling or decision support. XAI exists in several papers, but clinician-tested explanation remains limited. | Papers 17, 25, 27, 31 and 33 use XAI; Papers 26, 32 and 35 support trust/clinical-use concerns. | Confident | SHAP or LIME alone is not enough; clinical understandability should be evaluated. |
| Is lifestyle data a confirmed repeated gap? | It is a plausible and important gap, but it must be handled carefully. Many reviewed IVF prediction models focus on clinical, hormonal and embryology data, while lifestyle variables are often absent or not central. | Paper notes for 29, 30, 31 and 33; data collection framework. | Conditional | I should not claim lifestyle data improves prediction until tested with reliable data. |
| Is Indian population data missing? | Indian data is limited in the reviewed AI-IVF literature, but not completely absent. Paper 29 uses an Indian hospital dataset. The stronger gap is broader Indian external validation and regional generalization. | Paper 29 and literature matrix correction. | Confident | I should not say "no Indian data exists." The correct claim is limited Indian validation evidence. |

## Dataset And Feasibility Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| What dataset do you need? | Ideally, clinical, treatment, embryology and outcome data. Lifestyle data is useful if collected reliably. | Data collection framework; variables used across Papers 29, 30, 31 and 33. | Conditional | The exact dataset will be finalized only after clinic confirmation. |
| What is the minimum viable dataset? | A minimum dataset should include age, BMI, infertility diagnosis/duration, ovarian reserve markers if available, treatment type, transfer details and a reliable outcome. | Dataset questions page; features used in Papers 29 and 30. | Conditional | If key variables are missing, the topic scope must be reduced. |
| What is the ideal dataset? | Clinical plus embryology plus lifestyle data, with live-birth outcome and a second clinic or independent time period for validation. | Data collection framework and feasibility decision page. | Conditional | Ideal does not mean guaranteed. It is a target for clinic discussion. |
| What if only one clinic gives data? | Then the study can still be feasible, but it should use internal validation and preferably temporal validation. It cannot claim multicenter external validation. | Single-center limitations across Papers 29, 30, 31 and 33. | Conditional | I will clearly state this as a limitation rather than hide it. |
| What if live birth is unavailable? | Clinical pregnancy can be used carefully, but live birth should remain the preferred outcome where available. | Papers 16, 19 and 31 use clinical pregnancy; Papers 5, 7, 8, 9, 29 and 30 use live-birth-related outcomes. | Conditional | The final title and objectives should match the outcome actually available. |
| What if embryo variables are unavailable? | Then the study should not claim multimodal clinical-embryological prediction. It can become clinical-data-based explainable IVF outcome prediction. | Feasibility decision page; embryo-data papers 4, 24, 27 and 28. | Conditional | I should not keep "embryological data" in the title if those variables are unavailable. |
| What if lifestyle variables are unavailable? | Lifestyle should become future work or a separate questionnaire-based sub-study, not a core claim. | Data collection framework and previous clinic discussion planning. | Conditional | I should not invent lifestyle data or infer it from unrelated records. |

## Feasible Study Design Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| Can this PhD be done with retrospective data? | Yes, many IVF prediction studies are retrospective. But retrospective design limits causal claims and needs careful validation. | Papers 6, 9, 10, 29, 30, 31 and 33. | Confident | Retrospective model development is feasible; prospective clinical impact is a later step. |
| Can this PhD be done without clinical deployment? | Yes. A prototype CDSS and clinician review can be feasible without real deployment. But deployment impact cannot be claimed. | Papers 22 and 35 show deployment/adoption context; Paper 14 supports interface feedback ideas. | Conditional | I should say "prototype and clinician evaluation," not "implemented in hospital" unless it truly happens. |
| How will the scope remain manageable? | The scope should be fixed after data audit: one main outcome, one dataset level, clear model comparison, XAI, and clinician review if feasible. | Pipeline and feasibility framework. | Conditional | I should not try to include every IVF stage, every model and every data type in one PhD. |
| What will be excluded? | Treatment automation, replacing doctor decisions, proving improved live-birth rate, and claims beyond available data should be excluded. | Ethics/privacy page; Papers 26, 32 and 35. | Confident | Exclusion improves scientific credibility, not weakness. |

## Variables And Hypotheses Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| What is the dependent variable? | It depends on data availability. Preferred outcome is live birth. If unavailable, clinical pregnancy or miscarriage risk may be used with clear limitation. | Papers 30 and 33 use live-birth-related outcomes; Paper 31 uses clinical pregnancy. | Conditional | I will not finalize the outcome until clinic data is confirmed. |
| What are likely independent variables? | Clinical variables may include age, BMI, infertility duration/diagnosis, AMH, AFC, stimulation protocol, hormone values, transfer type and embryo variables if available. | Papers 29, 30, 31 and 33. | Conditional | The final variable list must come from actual clinic records. |
| Are hypotheses finalized? | No. Hypotheses should be tentative until dataset variables and outcome are confirmed. | Research pipeline and data feasibility decision page. | Confident | A hypothesis that cannot be tested with available data should be removed or rewritten. |
| Can we hypothesize that multimodal data improves prediction? | Only if the dataset has at least two meaningful modalities, such as clinical plus embryology or clinical plus imaging. | Papers 3, 4 and 25 support multimodal directions. | Conditional | If only clinical tabular data is available, the hypothesis is not valid. |
| Can we hypothesize that XAI improves clinician trust? | Only if clinicians actually review explanations using a structured evaluation. | Papers 14 and 35 support usability/trust context; Papers 25, 27, 31 and 33 use XAI methods. | Conditional | XAI output does not automatically prove trust or usefulness. |

## Methodology And Statistics Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| Which models will you use? | Start with interpretable baselines such as logistic regression, then compare tree-based models such as Random Forest, XGBoost and LightGBM if data size supports them. | Papers 17, 30, 31 and 33 compare classical and ML models. | Conditional | Model choice should match data size, missingness and outcome balance. |
| Why not deep learning first? | Deep learning is suitable for images, videos or very large datasets. For tabular clinic data, simpler baselines and boosted trees are more realistic. | Papers 3, 4 and 28 use image/video/deep learning contexts; Paper 30 shows logistic regression can be competitive. | Confident | I can include deep learning only if the data type justifies it. |
| Why compare with logistic regression? | Logistic regression is a transparent clinical baseline. If complex ML cannot beat it meaningfully, the simpler model may be preferable. | Paper 30 found logistic regression and Random Forest had similar performance. | Confident | A PhD model should be clinically useful, not complex for its own sake. |
| Which evaluation metrics matter? | AUC, sensitivity, specificity, precision, recall, F1, calibration, Brier score and confidence intervals. Accuracy alone is not enough. | Papers 30 and 33; technical glossary. | Confident | Metric choice should consider clinical thresholds and outcome imbalance. |
| How will overfitting be avoided? | Use train/test split, cross-validation, feature control, calibration, and external or temporal validation where possible. | Papers 30, 31 and 33; TRIPOD + AI glossary. | Confident | Internal validation reduces overfitting risk but does not prove generalization. |
| Will sample size be calculated? | Yes, after knowing outcome frequency, number of predictors and available records. Before data audit, exact sample size would be premature. | Statistical planning logic; dataset feasibility page. | Conditional | I should not invent sample size before clinic data availability is known. |

## Ethics And Responsible AI Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| Is ethics approval required? | Yes. IVF data is sensitive health data. Clinic permission and institutional ethics approval are required before analysis. | Ethics/privacy page and standard research practice. | Confident | Even anonymized retrospective data requires proper approval or exemption documentation. |
| How will patient privacy be protected? | Use de-identified/anonymized data, remove direct identifiers, restrict access and report aggregate results. | Ethics/privacy page. | Confident | I should not handle identifiable records unless explicitly approved. |
| What should AI not decide? | AI should not decide treatment, embryo value or patient eligibility independently. It should support clinicians with risk estimates and explanations. | Papers 26, 32 and 35. | Confident | Human oversight is mandatory in this type of clinical decision support. |
| Can AI create bias? | Yes. Bias can occur if training data underrepresents groups or if clinic-specific patterns are learned. Performance should be checked across available subgroups. | Papers 26, 32 and 35; external-validation gap. | Confident | Fairness analysis depends on whether subgroup variables are available. |

## Novelty And Contribution Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| What is new in this work? | The novelty should not be "using AI in IVF." The potential contribution is an explainable, personalized and clinic-feasible decision-support framework validated honestly on available data. | Papers 12, 13, 26, 32, 34 and 35 support translation/trust gaps. | Conditional | Final novelty depends on dataset access and exact scope. |
| Is XAI alone enough for novelty? | No. XAI methods already exist in IVF studies. The novelty must combine XAI with a meaningful clinical problem, validation and clinician-facing usefulness. | Papers 25, 27, 31 and 33 use SHAP/LIME-style explanations. | Confident | I should not present SHAP alone as a PhD contribution. |
| Is Indian data enough for novelty? | Not by itself. Indian data is valuable, but novelty also needs a clear research problem, method, validation and clinical relevance. | Paper 29 shows Indian data exists but with limitations. | Confident | I should avoid saying "Indian dataset" alone proves novelty. |
| What is the clinical contribution? | A clinician-facing explanation and risk-support framework may help counseling and structured decision discussion, if validated and reviewed. | Papers 14, 22, 25, 32 and 35. | Conditional | It cannot be claimed to improve patient outcomes without prospective clinical evidence. |

## Limitations Questions

| Question | Safe answer | Evidence basis | Confidence | If challenged |
| --- | --- | --- | --- | --- |
| What are expected limitations? | Possible limitations include small or single-center data, missing variables, incomplete live-birth follow-up, no external validation and no real deployment. | Repeated gaps across current literature matrix. | Confident | Stating limitations early makes the proposal stronger. |
| What if the model does not perform well? | Then the result is still useful if it shows which variables, data gaps or validation limits reduce predictive value. | Paper 30 shows modest AUC can still be informative. | Confident | The PhD should not depend only on achieving high accuracy. |
| What if external validation is not possible? | Then the thesis should state internal/temporal validation only and position external validation as future work. | Dataset feasibility page; external validation gap. | Conditional | I should not label internal testing as external validation. |
| What claims will you avoid? | I will avoid claiming that AI improves IVF success, replaces clinicians, proves causality, or generalizes to all Indian clinics without evidence. | Papers 26, 28, 32 and 35. | Confident | Conservative claims are more defensible in panel and thesis. |

## Stage 2 Completion Check

Stage 2 v1 is complete when:

- high-priority questions have safe answers
- every answer has a confidence label
- dataset-dependent answers are clearly marked conditional
- unsupported claims are explicitly avoided

## Stage 3 Preview

Stage 3 should convert the dataset-related answers into a feasibility framework:

| Dataset Situation | Feasible Direction |
| --- | --- |
| Clinical data only | Explainable clinical IVF outcome prediction |
| Clinical + embryology data | Multimodal clinical-embryology IVF prediction |
| Clinical + lifestyle data | Personalized IVF risk-factor and outcome modeling |
| One clinic only | Internal/temporal validation with single-center limitation |
| Two or more clinics | External validation and generalization analysis |
| No live birth outcome | Clinical pregnancy outcome with clear limitation |
