# Paper 27: XAI for Embryo Ploidy Prediction and Patient-Centric Consultation

## Citation

Luong, T.-M.-T., Ho, N.-T., Hwu, Y.-M., Lin, S.-Y., Ho, J. Y.-P., Wang, R.-S., Lee, Y.-X., Tan, S.-J., Lee, Y.-R., Huang, Y.-L., Hsu, Y.-C., Le, N.-Q.-K., & Tzeng, C.-R. (2024). **Beyond black-box models: explainable AI for embryo ploidy prediction and patient-centric consultation**. *Journal of Assisted Reproduction and Genetics*, 41, 2349-2358.

DOI: [https://doi.org/10.1007/s10815-024-03178-7](https://doi.org/10.1007/s10815-024-03178-7)

Source checked: [Springer Nature article page](https://link.springer.com/article/10.1007/s10815-024-03178-7)

Evidence note:

The Springer page provides the title, authors, publication details, abstract, dataset description, model list and main performance values. Full article access is subscription-limited, so detailed tables beyond the abstract are not fully extracted here.

Related study terms:

- [Blastocyst](../glossary/clinical-glossary.md#blastocyst)
- [PGT-A](../glossary/clinical-glossary.md#pgt-a)
- [Euploid embryo](../glossary/clinical-glossary.md#euploid-embryo)
- [Aneuploid embryo](../glossary/clinical-glossary.md#aneuploid-embryo)
- [Ploidy](../glossary/clinical-glossary.md#ploidy)
- [Morphokinetics](../glossary/clinical-glossary.md#morphokinetics)
- [Embryo grading](../glossary/technical-glossary.md#embryo-grading)
- [SHAP](../glossary/technical-glossary.md#shap)
- [LIME](../glossary/technical-glossary.md#lime)
- [Linear Discriminant Analysis](../glossary/technical-glossary.md#linear-discriminant-analysis)
- [LightGBM](../glossary/technical-glossary.md#lightgbm)
- [AUC](../glossary/technical-glossary.md#auc)

## Why This Paper Matters

This paper is important because it combines embryo ploidy prediction with explainable AI.

It is useful for our PhD because it directly addresses:

- black-box embryo AI concerns
- SHAP and LIME explanations
- patient-centric consultation
- embryo and clinical feature integration
- embryo ploidy as an intermediate biological outcome

It also connects well with Paper 26, which argues that embryo-selection AI should be interpretable rather than opaque.

## Research Objective

The study aimed to determine whether an explainable AI model can improve the accuracy and transparency of predicting embryo ploidy status from embryonic characteristics and clinical data.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Retrospective study |
| Journal | Journal of Assisted Reproduction and Genetics |
| Published | 4 July 2024 |
| Dataset size | 1,908 blastocyst embryos |
| Data included | Ploidy status, morphokinetic features, morphology grades and 11 clinical variables |
| Dataset groups | High-grade embryos, low-grade embryos and all-grade embryos |
| High-grade embryo dataset | HGE, n = 1,107 |
| Low-grade embryo dataset | LGE, n = 364 |
| All-grade embryo dataset | AGE, n = 1,471 |
| Mean maternal age | 38.5 ± 3.85 years |
| Clinical setting | Taipei Fertility Centre / Taiwan-linked research group |

Confidence: **High**

## Variables / Features Used

Confirmed feature groups:

- embryo ploidy status
- morphokinetic features
- morphology grades
- 11 clinical variables

Important SHAP-highlighted features:

| Feature | Meaning |
| --- | --- |
| Maternal age | Age of female partner/patient |
| Paternal age | Age of male partner |
| Time to blastocyst (tB) | Embryo development timing |
| Day 5 morphology grade | Embryo morphology assessment |

Confidence: **High**

## Method / Algorithm

Models trained:

| Model | Role |
| --- | --- |
| Random Forest | Tree-based ensemble model |
| Linear Discriminant Analysis | Linear classification model |
| Logistic Regression | Baseline statistical/ML model |
| Support Vector Machine | Margin-based classifier |
| AdaBoost | Boosting ensemble model |
| LightGBM | Gradient boosting model |

Explainability methods:

- SHAP for global feature impact analysis
- LIME for local case-level explanation and case-ploidy prediction probabilities

Confidence: **High**

## Evaluation Metrics

The paper reports:

- accuracy
- AUC
- 95% confidence interval for external test AUC
- SHAP feature impact
- LIME case-level explanations

Confidence: **High**

## Main Findings

| Finding | Extracted Information |
| --- | --- |
| Best-performing model | Random Forest |
| RF accuracy for all-grade embryos | 0.749 |
| RF AUC for all-grade embryos | 0.808 |
| External test accuracy | 0.714 |
| External test AUC | 0.750 |
| External test AUC 95% CI | 0.702-0.796 |
| Top SHAP features | Maternal age, paternal age, time to blastocyst, day 5 morphology grade |
| LIME contribution | Case-specific ploidy prediction probability and variable contribution ranges |
| Claimed value | More transparent ploidy prediction and patient-centric consultation |

Confidence: **High**

## Limitations Stated By Authors

Not fully confirmed from abstract-level source.

The Springer abstract does not list a detailed limitations section.

Confidence: **Not confirmed**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Outcome is ploidy, not live birth | Euploidy is important but does not guarantee implantation, pregnancy or live birth. |
| Retrospective design | Performance may not translate directly into prospective embryo-selection decisions. |
| Moderate external test AUC | AUC 0.750 is useful but not strong enough alone for clinical decision-making. |
| External validation details need full-text check | Abstract reports external test performance, but exact source/split should be verified. |
| No deployed CDSS | XAI outputs support consultation, but workflow deployment is not confirmed. |
| Patient-centric claim needs user evaluation | LIME/SHAP do not automatically prove patient understanding or trust. |
| No Indian population | Local validation would be needed for Indian IVF clinics. |

Confidence: **High/Medium**

## Future Work Suggested

Not fully confirmed from abstract-level source.

Our evidence-based extension:

- verify full limitation and validation details from full text
- test model on external multicenter populations
- evaluate whether SHAP/LIME explanations improve clinician and patient understanding
- connect ploidy prediction with clinical pregnancy and live-birth outcomes
- integrate explanation into a real consultation workflow

Confidence: **Medium**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Black-box / explainability gap | Partially addressed | SHAP and LIME are used. |
| Patient-centered XAI gap | Partially addressed | The paper targets patient-centric consultation, but user testing is not confirmed. |
| Need external validation | Yes | External test AUC is reported, but broader validation is still needed. |
| Outcome-label limitation | Yes | Ploidy is not live birth. |
| Need clinical decision support | Yes | No deployed CDSS workflow is confirmed. |
| Lack of Indian population | Yes | Dataset is not Indian. |
| Moderate performance | Yes | External AUC 0.750 suggests room for improvement. |

## Usefulness For Our PhD

Relevance: **High for XAI and embryo-selection theme**

This paper is useful because it gives a practical example of applying SHAP and LIME in IVF-related embryo assessment.

It supports our methodological thinking:

- use SHAP for global and patient-level feature contribution
- use local explanation methods for case-specific counseling
- do not treat intermediate biological labels as final IVF success
- separate technical explainability from actual user understanding

If our final project uses tabular clinical data rather than embryo ploidy data, this paper remains useful as XAI justification rather than direct method replication.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Luong et al. (2024) developed explainable machine-learning models for embryo ploidy prediction using 1,908 blastocysts with ploidy status, morphokinetic features, morphology grades and clinical variables, reporting that Random Forest achieved an all-grade embryo AUC of 0.808 and external test AUC of 0.750.

Gap-support sentence:

> Although SHAP and LIME improved transparency by identifying features such as maternal age, paternal age, time to blastocyst and day 5 morphology grade, ploidy prediction remains an intermediate outcome and requires broader validation and clinical workflow evaluation before patient-facing use.

## What This Paper Does Not Prove

This paper does not prove that:

- ploidy prediction improves live-birth rates.
- SHAP/LIME explanations are understood by patients.
- the model generalizes to Indian IVF clinics.
- embryo-selection decisions should be automated.
- ploidy prediction alone is enough for a clinical decision-support system.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation and DOI | High |
| Dataset size and groups | High |
| Model list | High |
| Main performance values | High |
| XAI methods | High |
| Full limitations | Not confirmed |
| Full validation design details | Medium |
