# Paper 29: Indian IVF Outcome Prediction Using Bayesian-Optimized Ensemble Learning

## Citation

Sengupta, A., Majumdar, G., Choudhury, A., Gupta, P., Modi, D., & Narad, P. (2025). **Artificial intelligence-enhanced in-vitro fertilization outcome prediction for the Indian subpopulation: integrating pre-treatment parameters and Bayesian-optimized ensemble techniques**. *International Journal of Community Medicine and Public Health*, 12(5), 2272-2279.

DOI: [https://doi.org/10.18203/2394-6040.ijcmph20251387](https://doi.org/10.18203/2394-6040.ijcmph20251387)

Source checked: [International Journal of Community Medicine and Public Health article page](https://www.ijcmph.com/index.php/ijcmph/article/view/13816)

Evidence note:

This paper is important for our PhD because it directly uses an Indian IVF dataset. However, the accessible source is mainly the journal article page and abstract-level information. The PDF endpoint was protected by a verification page during review, so detailed extraction beyond the article page is marked carefully.

Related study terms:

- [IVF](../glossary/clinical-glossary.md#ivf)
- [ICSI](../glossary/clinical-glossary.md#icsi)
- [Live Birth](../glossary/clinical-glossary.md#live-birth)
- [AMH](../glossary/clinical-glossary.md#amh)
- [BMI](../glossary/clinical-glossary.md#bmi)
- [Voting Classifier](../glossary/technical-glossary.md#voting-classifier)
- [Bayesian Optimization](../glossary/technical-glossary.md#bayesian-optimization)

## Why This Paper Matters

This paper matters because many IVF-AI studies use Western, Chinese, European, Australian or registry datasets. This study is different because it reports IVF-ICSI data from an Indian hospital.

For our PhD, the paper is useful for three reasons:

- it supports the need for Indian-context IVF prediction research
- it shows that pre-treatment parameters can be used before IVF treatment begins
- it still leaves a clear gap for external validation across more than one Indian clinic

Important caution:

This paper should not be cited as proof that the Indian IVF-AI gap is solved. It is better used as evidence that Indian work has started, but remains limited by single-center validation and incomplete real-world deployment evidence.

## Research Objective

The study aimed to develop and validate a Bayesian-optimized voting-ensemble machine learning model, named BoVe, for predicting live-birth outcomes in IVF using pre-treatment patient parameters.

Confidence: **High** for broad objective from the article page.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Original research article |
| Journal | International Journal of Community Medicine and Public Health |
| Published | 30 April 2025 |
| Dataset source | Centre of IVF and Human Reproduction, Sir Ganga Ram Hospital, New Delhi, India |
| Study population | IVF patients / IVF-ICSI clinical records |
| Dataset size | 2,908 IVF patients |
| Number of parameters | 79 parameters |
| Data period | 1 January 2018 to 31 October 2022, based on our existing source registry entry |
| Data split | 80:20 training-validation split |
| Outcome | Live birth outcome |
| External validation | Not confirmed from available source |
| Multi-center data | Not confirmed; available source indicates one Indian hospital |

Confidence: **High** for dataset size, 79 parameters, 80:20 split and hospital source from article page. **Medium** for exact date range because it comes from the existing project source registry, not the visible article-page abstract.

## Variables / Features Used

The article page confirms these variables:

- maternal age
- BMI
- AMH level
- number of IVF cycles
- infertility type
- sperm parameters

The article page states that 79 parameters were analyzed, but the full 79-variable list was not available from the accessible source during this review.

Confidence: **High** for listed variables. **Not confirmed** for full feature list.

## Method / Algorithm

| Component | Extracted Information |
| --- | --- |
| Main model | Bayesian-optimized voting-ensemble model |
| Model name | BoVe |
| Model family | Ensemble machine learning |
| Optimization approach | Bayesian optimization |
| Comparison | Evaluated against traditional machine learning models |
| Technology mentioned | Machine learning and cloud-based fertility guidance web application |

Confidence: **High** for model family and BoVe name from article page.

## Evaluation Metrics

The article page reports:

| Metric | Reported Value |
| --- | ---: |
| ROC-AUC | 0.93 |
| Accuracy | 0.87 |

Other metrics such as sensitivity, specificity, calibration, decision-curve analysis and confidence intervals were not confirmed from the accessible source.

Confidence: **High** for ROC-AUC and accuracy. **Not confirmed** for other metrics.

## Main Findings

The article page reports that BoVe achieved stronger predictive performance than conventional machine learning models.

Reported predictors associated with higher live-birth success included:

- AMH level greater than 3.5 ng/mL
- BMI less than 23
- maternal age less than 35 years
- male sperm parameters

The paper also reports development of an AI-powered web application for cloud-based fertility guidance and personalized recommendations.

Confidence: **High** for these headline findings from article page.

## Limitations Stated By Authors

The accessible article page did not provide a detailed limitation section.

Confidence: **Not confirmed from available source**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points, not necessarily author-stated limitations.

| Critical Point | Why It Matters |
| --- | --- |
| Single Indian hospital | The model may learn local patient, lab, clinic and treatment patterns. |
| External validation not confirmed | Performance may reduce when tested in another Indian clinic. |
| 80:20 split only | Internal validation is weaker than temporal, geographic or multi-center validation. |
| Full feature list not available from accessible source | We cannot confirm whether lifestyle, socioeconomic, embryo and longitudinal variables were included. |
| Calibration not confirmed | High AUC does not prove the predicted probability is clinically reliable. |
| Decision-support workflow not fully confirmed | A web application is mentioned, but real clinician use, safety checks and workflow evaluation are not confirmed. |
| Source quality caution | Useful Indian evidence, but should be supported by stronger indexed and externally validated studies. |

Confidence: **Medium-High** as critical interpretation based on available source details.

## Future Work Suggested

Based on the confirmed evidence and our review needs, this paper supports future work on:

- external validation across multiple Indian IVF clinics
- testing across different Indian regions and patient groups
- adding lifestyle and socioeconomic factors where ethically and clinically appropriate
- checking model calibration, fairness and explainability
- converting prediction into clinician-reviewed decision support
- prospective evaluation before clinical use

Confidence: **Medium** because these are inferred from study design limitations and our PhD direction.

## Gap Contribution

| Gap Category | Contribution |
| --- | --- |
| Indian population | Partially addressed by using Indian hospital data |
| External validation | Still open because multi-center validation is not confirmed |
| Personalized recommendation | Partially addressed by reported web application and personalized guidance |
| Clinical decision support | Partially addressed conceptually; real-world clinical workflow evidence not confirmed |
| Lifestyle data | Not confirmed from available source |
| Explainable AI | Not confirmed beyond reported predictor findings |
| Fairness analysis | Not confirmed |
| Real-world deployment | Not confirmed beyond web application mention |

## Usefulness For Our PhD

Usefulness: **High for Indian-context justification, Medium for final evidence strength**

This paper is useful because it gives direct Indian IVF-AI evidence. It helps us explain why an Indian-focused IVF prediction and decision-support study is realistic and relevant.

But it should not become the main proof of novelty. Its best use is to show that:

- Indian IVF prediction work exists
- current evidence is still limited
- single-center Indian evidence needs stronger validation
- a Pune/Maharashtra or multi-clinic Indian dataset would add value

## What This Paper Does Not Prove

This paper does not prove that:

- the model will generalize to all Indian IVF clinics
- lifestyle variables improve IVF prediction
- clinicians trust the model in real practice
- the web application improves live-birth rates
- the model is fair across age, socioeconomic or regional groups

## Thesis-Ready Citation Sentences

Sengupta et al. (2025) developed a Bayesian-optimized voting-ensemble model using Indian IVF patient data and reported strong live-birth prediction performance, with ROC-AUC of 0.93 and accuracy of 0.87.

The study is relevant to Indian IVF-AI research because it uses clinical records from Sir Ganga Ram Hospital, New Delhi; however, evidence of external multi-center validation, calibration, lifestyle-data integration and real-world clinician evaluation was not confirmed from the accessible source.

For this PhD, the paper supports the argument that Indian-context IVF prediction is emerging, but robust, explainable and externally validated clinical decision support remains an open research need.

## Source Confidence Summary

| Item | Confidence |
| --- | --- |
| Citation, authors, DOI, journal | High |
| Objective | High |
| Dataset size and broad feature categories | High |
| Full 79-variable list | Not confirmed |
| Method name and reported metrics | High |
| Author-stated limitations | Not confirmed |
| External validation status | Not confirmed |
| PhD gap interpretation | Medium-High |
