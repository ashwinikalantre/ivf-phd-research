# Paper 20: Tree-Based Machine Learning for IVF Clinical Pregnancy Prediction

## Citation

Handayani, N., Louis, C. M., Erwin, A., Aprilliana, T., Polim, A. A., Sirait, B., Boediono, A., & Sini, I. (2022). **Machine Learning Approach to Predict Clinical Pregnancy Potential in Women Undergoing IVF Program**. *Fertility & Reproduction*, 4(2), 77-87.

DOI: [https://doi.org/10.1142/S2661318222500098](https://doi.org/10.1142/S2661318222500098)

Sources checked:

- [World Scientific article page](https://www.worldscientific.com/doi/10.1142/S2661318222500098)
- [Institutional repository record](https://repository.uki.ac.id/8721/)
- Search-indexed abstract snippets from World Scientific/ResearchGate/repository pages

Evidence note:

The World Scientific article page and repository metadata confirm the citation and abstract-level study details. The institutional PDF link was identified but could not be downloaded directly in this environment. Therefore, this note uses confirmed abstract-level information and marks deeper details as not confirmed.

Related study terms:

- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [Fresh embryo transfer](../glossary/clinical-glossary.md#fresh-embryo-transfer)
- [Cleavage-stage embryo](../glossary/clinical-glossary.md#cleavage-stage-embryo)
- [Blastocyst](../glossary/clinical-glossary.md#blastocyst)
- [Decision Tree](../glossary/technical-glossary.md#decision-tree)
- [Random Forest](../glossary/technical-glossary.md#random-forest)
- [Gradient Boosting](../glossary/technical-glossary.md#gradient-boosting)
- [Genetic Algorithm](../glossary/technical-glossary.md#genetic-algorithm)
- [Balanced Accuracy](../glossary/technical-glossary.md#balanced-accuracy)

## Why This Paper Matters

This paper is useful because it uses a relatively large multicenter IVF dataset and focuses on tree-based machine-learning models for clinical pregnancy prediction.

It is relevant for our PhD because it supports:

- use of practical clinical IVF data
- comparison of simple tree-based models before complex models
- Genetic Algorithm based optimization and variable selection
- the repeated finding that clinical-pregnancy prediction remains moderate, not perfect

It is also useful as a reminder that even multicenter retrospective datasets may produce only modest balanced accuracy.

## Research Objective

The study aimed to use machine-learning based data-mining techniques to construct a reliable prediction model for clinical pregnancy in IVF.

Confidence: **Medium-High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Research article |
| Journal | Fertility & Reproduction |
| Year | 2022 |
| Study design | Retrospective cohort multicenter study |
| Dataset size | 4,570 IVF cycles |
| Study period | January 2015 to December 2019 |
| Treatment scope | Fresh embryo transfer |
| Embryo stage | Cleavage-stage or blastocyst-stage transfer |
| Outcome | Clinical pregnancy |
| Country / clinic details | Not fully confirmed from available source |
| Full variable table | Not confirmed from available source |

Confidence: **Medium-High for abstract-confirmed details; Medium for full dataset context**

## Variables / Features Used

Confirmed:

- clinical IVF cycle variables were used
- Genetic Algorithm was used for variable selection
- female age was consistently included across prediction models

Not confirmed from available source:

- complete feature list
- exact number of variables
- missing-data handling
- final selected feature subsets for each classifier

Confidence: **Medium**

## Method / Algorithm

The study focused on tree-based classifiers:

| Algorithm | Role |
| --- | --- |
| Decision Tree | Tree-based classifier |
| Random Forest | Ensemble tree-based classifier |
| Gradient Boost | Boosting tree-based classifier |

Optimization / selection:

- Each classifier was optimized using Genetic Algorithm.
- Genetic Algorithm was also used for variable selection.

Confidence: **Medium-High**

## Evaluation Metrics

Confirmed metric:

- balanced accuracy

Other metrics:

**Not confirmed from available source**

Confidence: **Medium**

## Main Findings

| Finding | Extracted Information |
| --- | --- |
| Best-performing models | Decision Tree and Random Forest |
| Weaker model | Gradient Boost |
| Balanced accuracy | Roughly 0.62 for Decision Tree and Random Forest |
| Variable-selection insight | Different models worked best with different variable combinations |
| Consistently included variable | Female age |
| Conclusion | ML remained useful for data mining and knowledge extraction in IVF clinical datasets |

The study concluded that a relatively reliable clinical-pregnancy prediction system could be constructed if sufficient data is available.

Confidence: **Medium-High**

## Limitations Stated By Authors

Not fully confirmed from available source.

The accessible abstract-level information does not provide a detailed limitations section.

Confidence: **Not confirmed**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points based on confirmed information.

| Critical Point | Why It Matters |
| --- | --- |
| Outcome is clinical pregnancy, not live birth | Clinical pregnancy is an intermediate outcome. |
| Retrospective design | Practice patterns and confounders may influence results. |
| Moderate balanced accuracy | Around 0.62 suggests limited standalone clinical usefulness. |
| Full variable list unavailable in this review | Dataset planning cannot rely on this paper alone. |
| External validation not confirmed | Multicenter data helps, but independent external validation must still be checked. |
| No confirmed CDSS deployment | Prediction modeling is not the same as a clinical decision-support system. |
| No confirmed XAI method | GA feature selection gives some insight, but not patient-level explanation. |

Confidence: **Medium**

## Future Work Suggested

Not confirmed from available source.

Our evidence-based extension:

- obtain full paper/PDF for exact limitations and variable list
- check whether validation was internal, external or site-based
- compare clinical pregnancy prediction against live birth prediction
- add explainability if used for clinician-facing counseling
- test whether moderate balanced accuracy is clinically useful

Confidence: **Medium**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need full-text verification | Yes | Full paper details could not be completely extracted. |
| Need stronger outcome label | Yes | Outcome is clinical pregnancy, not live birth. |
| Retrospective design | Yes | Study is retrospective. |
| Need clinical decision support | Likely | No deployed CDSS was confirmed. |
| Lack of XAI | Likely | No patient-level explanation method was confirmed. |
| Need external validation | Likely | Independent validation was not confirmed from available source. |
| Moderate model performance | Yes | Balanced accuracy was roughly 0.62. |

## Usefulness For Our PhD

Relevance: **Medium-High**

This paper is useful because it shows that:

- multicenter clinical IVF datasets are possible
- tree-based models can be used for clinical pregnancy prediction
- Genetic Algorithm can support model optimization and feature selection
- moderate performance should make us cautious about clinical deployment claims

It is useful for the literature matrix, but we should not use it as a major thesis-gap source until the full text is checked.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Handayani et al. (2022) used a retrospective multicenter cohort of 4,570 IVF cycles to compare tree-based machine-learning classifiers for clinical-pregnancy prediction, reporting that Decision Tree and Random Forest models achieved similar balanced accuracy of approximately 0.62 after Genetic Algorithm based optimization.

Gap-support sentence:

> The moderate balanced accuracy reported in this multicenter clinical-pregnancy study suggests that IVF-AI prediction models require richer variables, stronger validation and careful clinical evaluation before decision-support use.

## What This Paper Does Not Prove

This paper does not prove that:

- clinical pregnancy prediction is equivalent to live-birth prediction.
- the model is ready for clinical deployment.
- Decision Tree or Random Forest will generalize to Indian IVF clinics.
- Genetic Algorithm feature selection provides sufficient explainability.
- balanced accuracy around 0.62 is enough for clinical decision support.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation and DOI | High |
| Abstract-level objective | High |
| Dataset size and study period | Medium-High |
| Algorithms | Medium-High |
| Main performance summary | Medium-High |
| Full feature list | Not confirmed |
| Full limitations | Not confirmed |
| Author-stated future work | Not confirmed |
