# Paper 17: Advanced Machine Learning for IVF Live-Birth Prediction

## Citation

Sadegh-Zadeh, S. A., Khanjani, S., Javanmardi, S., Bayat, B., Naderi, Z., & Hajiyavand, A. M. (2024). **Catalyzing IVF outcome prediction: exploring advanced machine learning paradigms for enhanced success rate prognostication**. *Frontiers in Artificial Intelligence*, 7, 1392611.

DOI: [https://doi.org/10.3389/frai.2024.1392611](https://doi.org/10.3389/frai.2024.1392611)

Source checked: [Frontiers full article](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1392611/full)

Evidence note:

This paper explicitly states that the objective is to predict **live-birth occurrences in IVF cycles**. It is therefore more directly relevant to final IVF success than papers using only clinical pregnancy or beta-hCG as outcomes.

Related study terms:

- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [HFEA dataset](../glossary/technical-glossary.md#hfea-dataset)
- [One-hot encoding](../glossary/technical-glossary.md#one-hot-encoding)
- [Standard scaling](../glossary/technical-glossary.md#standard-scaling)
- [SHAP](../glossary/technical-glossary.md#shap)
- [LogitBoost](../glossary/technical-glossary.md#logitboost)
- [RUSBoost](../glossary/technical-glossary.md#rusboost)
- [Random Subspace Method](../glossary/technical-glossary.md#random-subspace-method)
- [Clinical Decision Support System](../glossary/technical-glossary.md#clinical-decision-support-system)
- [Prospective validation](../glossary/technical-glossary.md#prospective-validation)
- [External validation](../glossary/technical-glossary.md#external-validation)

## Why This Paper Matters

This paper is useful because it uses a large IVF registry context and compares many classical, neural-network and ensemble machine-learning models for live-birth prediction.

It is especially relevant for our PhD because it connects three things we care about:

- live-birth prediction
- explainability using SHAP
- clinical decision-support potential

It also reinforces a repeated literature pattern: high retrospective performance is promising, but prospective studies, external validation and clinical integration are still needed before real-world adoption.

## Research Objective

The primary objective was to explore and compare advanced machine-learning algorithms to predict live-birth occurrences in IVF cycles, integrating gynecological expertise with data-driven modeling.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Original research article |
| Journal | Frontiers in Artificial Intelligence |
| Publication date | 5 November 2024 |
| Dataset source | HFEA-related IVF datasets |
| Dataset periods | 2017-2018 and 2010-2016 |
| Outcome focus | Live-birth occurrence in IVF cycles |
| Feature count mentioned | 37 fields in the dataset |
| Gamete scope | Cases where embryos were formed from couples' gametes, not donor gametes |
| Data type | Clinical, demographic and procedural IVF variables |
| Study nature | Retrospective data analysis |

Confidence: **High for article-level details; Medium for exact cohort size because it was not extracted from the visible article text used here**

## Variables / Features Used

The paper emphasizes:

- patient demographics
- infertility factors
- treatment protocols
- clinical variables
- procedural variables
- hormonal variables
- embryo-related variables

SHAP-ranked features reported in the article:

| Feature | SHAP Importance Score |
| --- | ---: |
| Maternal age | 0.245 |
| Previous IVF cycles | 0.198 |
| Luteinizing hormone | 0.153 |
| Gonadotropin dosage | 0.142 |
| Infertility type | 0.125 |
| Embryo count | 0.110 |
| Patient ethnicity | 0.075 |
| Partner ethnicity | 0.062 |
| Number of embryos transferred | 0.052 |

Infertility factors discussed:

- tubal disease
- ovulatory disorder
- male factor infertility
- unexplained infertility
- endometriosis infertility

Confidence: **High**

## Method / Algorithm

Models used:

| Model Group | Algorithms |
| --- | --- |
| Linear/probabilistic models | Logistic Regression, Gaussian Naive Bayes |
| Kernel/distance models | Support Vector Machine, K-Nearest Neighbors |
| Neural-network model | Multi-layer Perceptron |
| Ensemble models | Random Forest, AdaBoost, LogitBoost, RUSBoost, Random Subspace Method |

Preprocessing and interpretation:

- categorical features were encoded for machine learning
- feature scaling was used where needed
- SHAP was used for model interpretation
- model comparison included several classification metrics

Confidence: **High**

## Evaluation Metrics

The paper reports and discusses:

- accuracy
- precision
- recall
- F1-score
- ROC-AUC curves
- SHAP feature importance

Confidence: **High**

## Main Findings

| Finding | Extracted Information |
| --- | --- |
| Strongest model family | Ensemble learning methods |
| Best highlighted model | LogitBoost |
| Highest reported accuracy | 96.35% |
| Strong ensemble models | AdaBoost, LogitBoost and Random Forest |
| Important feature group | Infertility causes improved prediction performance |
| SHAP top feature | Maternal age |
| Clinical implication | Potential for decision support, patient counseling and personalized IVF treatment planning |

The article reports that ensemble methods showed strong performance and that infertility-factor variables contributed meaningfully to prediction.

For the 2017-2018 dataset, adding infertility causes improved reported metrics:

| Metric | Without Infertility Causes | With Infertility Causes |
| --- | ---: | ---: |
| Accuracy | 0.86 | 0.95 |
| Precision | 0.80 | 0.85 |
| Recall | 0.88 | 0.99 |
| F1 | 0.84 | 0.92 |

For the 2010-2016 dataset, adding infertility causes also improved reported metrics:

| Metric | Without Infertility Causes | With Infertility Causes |
| --- | ---: | ---: |
| Accuracy | 0.89 | 0.96 |
| Precision | 0.81 | 0.87 |
| Recall | 0.98 | 0.99 |
| F1 | 0.89 | 0.92 |

Confidence: **High**

## Limitations Stated By Authors

| Limitation / Need | Meaning |
| --- | --- |
| Retrospective nature | Unknown confounding factors cannot be fully controlled. |
| Need prospective studies | Controlled forward-looking studies are needed for stronger evidence. |
| Need external validation | Models should be tested on data from different IVF centers. |
| Need clinical integration | Future work should integrate models into clinical practice for real-time decision support. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Very high reported accuracy needs caution | Performance around 96% may not generalize without external prospective testing. |
| Retrospective registry modeling is not deployment evidence | It does not prove real clinical usefulness at point of care. |
| HFEA population may not match Indian IVF patients | Local validation would still be needed for Indian clinics. |
| SHAP is helpful but not enough alone | SHAP gives feature contribution, but clinician trust also needs usability and workflow testing. |
| Dataset-period differences may introduce temporal shift | 2010-2016 and 2017-2018 may reflect different clinical practices. |
| No real-time CDSS evaluation | The article discusses clinical decision support potential but does not deploy and evaluate a tool in practice. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- prospective studies
- external validation
- larger multi-center studies
- integration into clinical decision-support systems
- closer collaboration between gynecologists and data scientists
- real-time decision support during IVF treatment

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Retrospective design | Yes | Authors identify retrospective design as a limitation. |
| Need prospective validation | Yes | Prospective studies are explicitly suggested. |
| Need external validation | Yes | External validation across IVF centers is explicitly suggested. |
| Need clinical decision support | Yes | Clinical integration and real-time decision support are future directions. |
| Explainability gap | Partial | SHAP is included, but usability and clinician review are not deeply evaluated. |
| Lack of Indian population | Yes | HFEA data does not establish Indian clinic generalizability. |
| Temporal/generalization risk | Yes | Multiple historical periods may involve practice changes and data shift. |

## Usefulness For Our PhD

Relevance: **High**

This paper is useful because it strengthens the argument that:

- live birth is the preferred IVF outcome for clinically meaningful prediction
- infertility-cause variables should be included in the dataset if available
- ensemble models are strong baselines for tabular IVF data
- SHAP can support explainability for clinical variables
- high retrospective performance still requires prospective and external validation

For our dataset planning, this paper supports collecting:

- maternal age
- prior IVF cycles
- hormone levels
- gonadotropin dosage
- infertility type/cause
- embryo count
- number of embryos transferred
- ethnicity/population variables if ethically and legally appropriate

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Sadegh-Zadeh et al. (2024) compared multiple machine-learning paradigms for IVF live-birth prediction using HFEA-related datasets from 2010-2016 and 2017-2018, reporting strong ensemble-model performance and identifying maternal age, previous IVF cycles, hormone levels, infertility type and embryo-related variables as important predictors through SHAP analysis.

Gap-support sentence:

> Despite high retrospective performance, the authors emphasized the need for prospective studies, external validation and integration into clinical decision-support workflows, reinforcing the translational gap in IVF-AI research.

## What This Paper Does Not Prove

This paper does not prove that:

- the model will work equally well in Indian IVF clinics.
- high retrospective accuracy will remain high in prospective deployment.
- SHAP explanations alone are sufficient for clinician trust.
- the model has been tested as a real-time clinical decision-support system.
- ensemble methods are always superior for every IVF dataset.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Objective | High |
| Dataset periods | High |
| Outcome focus | High |
| Algorithms | High |
| Reported performance highlights | High |
| SHAP feature importance table | High |
| Exact cohort size | Not confirmed from extracted article text |
| Limitations and future work | High |
