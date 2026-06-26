# Paper 25: Explainable Ultrasound Radiomics for FET Outcome Prediction

## Citation

Xu, F., Ma, Q., Lai, P., Hu, L., Gao, C., Xu, Q., Fang, Y., Guo, Y., Yao, W., & Zhang, C. (2025). **An explainable ultrasound-based machine learning model for predicting reproductive outcomes after frozen embryo transfer**. *Reproductive BioMedicine Online*, 50(5), 104743.

DOI: [https://doi.org/10.1016/j.rbmo.2024.104743](https://doi.org/10.1016/j.rbmo.2024.104743)

Sources checked:

- [PubMed record](https://pubmed.ncbi.nlm.nih.gov/40199653/)
- [Europe PMC record](https://europepmc.org/article/med/40199653)
- Search-indexed article metadata and abstract excerpts

Evidence note:

PubMed was browser-gated during direct extraction, but Europe PMC and indexed abstract excerpts confirmed the main study details. This note is high confidence for abstract-level study design, sample size, model type and main reported performance.

Related study terms:

- [Frozen embryo transfer](../glossary/clinical-glossary.md#frozen-embryo-transfer)
- [Endometrial thickness](../glossary/clinical-glossary.md#endometrial-thickness)
- [Endometrial receptivity](../glossary/clinical-glossary.md#endometrial-receptivity)
- [Junctional zone](../glossary/clinical-glossary.md#junctional-zone)
- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [Radiomics](../glossary/technical-glossary.md#radiomics)
- [Region of Interest](../glossary/technical-glossary.md#region-of-interest)
- [XGBoost](../glossary/technical-glossary.md#xgboost)
- [Fusion Model](../glossary/technical-glossary.md#fusion-model)
- [SHAP](../glossary/technical-glossary.md#shap)
- [AUC](../glossary/technical-glossary.md#auc)

## Why This Paper Matters

This paper is highly relevant because it combines ultrasound imaging, clinical data and explainable machine learning for frozen embryo transfer outcome prediction.

It supports several important directions for our PhD:

- multimodal IVF prediction
- ultrasound/radiomics data integration
- explainable AI using SHAP
- FET-specific outcome prediction
- endometrial receptivity assessment before transfer

It also gives a practical example of how model explanations can identify the most influential features, not only produce a probability.

## Research Objective

The study aimed to develop an explainable ultrasound-based machine-learning model for predicting reproductive outcomes after frozen embryo transfer using radiomics and clinical information.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Prospective study |
| Journal | Reproductive BioMedicine Online |
| E-publication date | 28 November 2024 |
| Issue | May 2025, volume 50, issue 5 |
| Participants | 787 infertile females undergoing FET |
| Training set | 550 patients |
| Test set | 237 patients |
| Setting | Single-center study |
| Outcome context | Reproductive outcomes after frozen embryo transfer |
| Imaging source | Ultrasound images of endometrium and junctional zone |
| Explainability method | SHAP |

Confidence: **High**

## Variables / Features Used

Confirmed feature groups:

| Feature Group | Examples / Meaning |
| --- | --- |
| Ultrasound radiomics | Quantitative imaging features from endometrium and junctional zone |
| Radiomics score | Combined imaging-derived score |
| Clinical data | Patient and cycle-level clinical factors |
| Endometrial thickness | Ultrasound-measured uterine lining thickness |
| Embryo grade | Embryo quality variable |
| Age | Patient age |

Most influential features reported in secondary indexed excerpts:

- radiomics score
- embryo grade
- age
- endometrial thickness

Confidence: **High for feature categories; Medium-High for ranked feature detail**

## Method / Algorithm

The study developed and compared:

| Model | Description |
| --- | --- |
| Radiomics model | Ultrasound radiomics-based prediction |
| Clinical model | Clinical feature-based model |
| Fusion model | Combined radiomics and clinical information |

The fusion model used:

- XGBoost
- ultrasound radiomics features
- clinical variables
- SHAP explanations

Confidence: **High**

## Evaluation Metrics

Confirmed metrics:

- AUC
- SHAP feature contribution/explanation

Other metrics:

**Not confirmed from available source**

Confidence: **Medium-High**

## Main Findings

| Finding | Extracted Information |
| --- | --- |
| Best model | Fusion model combining radiomics and clinical data |
| Training AUC | 0.861 |
| Test AUC | 0.793 |
| Main influential features | Radiomics score, embryo grade, age, endometrial thickness |
| Explainability | SHAP explained feature effects on predictions |
| Clinical implication | Ultrasound radiomics may help predict FET outcomes before transfer |

The fusion model outperformed radiomics-only and clinical-only models according to indexed summaries.

Confidence: **High for main model and AUC values; Medium-High for detailed comparative ranking**

## Limitations Stated By Authors

Not fully confirmed from available source.

Limitations strongly indicated by available indexed summaries and study design:

| Limitation | Meaning |
| --- | --- |
| Single-center study | Generalizability to other clinics is not established. |
| Manual ROI delineation | Manual selection of imaging regions may introduce subjectivity. |
| FET-specific population | Results may not generalize to fresh transfer cycles. |
| Outcome may not be live birth | Clinical pregnancy/reproductive outcome needs exact final endpoint verification from full text. |

Confidence: **Medium**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Ultrasound image availability | Many clinics may not store images in research-ready format. |
| Manual ROI workflow | Subjective region selection may reduce reproducibility. |
| Single-center data | Needs external validation across scanners, operators and clinics. |
| FET-only scope | Does not directly apply to fresh IVF transfer or ovarian stimulation decisions. |
| Clinical endpoint needs verification | We should not treat this as live-birth evidence unless full text confirms it. |
| SHAP is not clinical validation | Explanation helps interpretation but does not prove clinical utility. |
| Indian validation absent | Indian clinic ultrasound protocols and populations may differ. |

Confidence: **High/Medium**

## Future Work Suggested

Likely future directions supported by the study:

- external multicenter validation
- automated ROI segmentation
- scanner/operator robustness testing
- prospective clinical workflow testing
- evaluation of final outcomes such as live birth
- integration into clinician-facing decision-support tools

Confidence: **Medium**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need multimodal data | Yes | Combines ultrasound radiomics and clinical data. |
| XAI gap | Partially addressed | Uses SHAP for explanation. |
| Need external validation | Yes | Single-center study needs broader validation. |
| Manual/subjective workflow bias | Yes | ROI selection can introduce subjectivity. |
| Need clinical decision support | Yes | Model is not confirmed as deployed CDSS. |
| Lack of Indian population | Yes | Indian validation not established. |
| Need stronger endpoint verification | Yes | Exact reproductive endpoint should be checked from full text before thesis claims. |

## Usefulness For Our PhD

Relevance: **Very High for multimodal/XAI theme**

This paper is useful because it shows how clinical variables and imaging features can be combined with explainable ML.

For our proposed work, it supports collecting or asking about:

- ultrasound image availability
- endometrial thickness
- endometrial receptivity measurements
- embryo grade
- FET cycle type
- clinical outcome labels
- whether clinicians can review SHAP-style explanations

If our available dataset has no ultrasound images, this paper remains important as literature support for multimodal AI, but may not be part of our implemented method.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Xu et al. (2025) developed an explainable ultrasound radiomics and clinical-data fusion model for predicting reproductive outcomes after frozen embryo transfer in 787 patients, reporting that the XGBoost fusion model achieved AUC values of 0.861 in training and 0.793 in testing, with SHAP identifying radiomics score, embryo grade, age and endometrial thickness as key contributors.

Gap-support sentence:

> Although the study demonstrates the value of multimodal and explainable prediction for FET, its single-center design and manual ultrasound region selection indicate the need for external validation and more reproducible image-analysis workflows.

## What This Paper Does Not Prove

This paper does not prove that:

- ultrasound radiomics improves live-birth rates.
- the model generalizes to Indian IVF clinics.
- manual ROI-based radiomics is reproducible across operators.
- SHAP explanations are sufficient for clinician trust.
- the model is ready as a deployed clinical decision-support system.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation and DOI | High |
| Study design and sample size | High |
| Train/test split | High |
| Main model type | High |
| Main AUC values | High |
| Full limitation section | Not confirmed |
| Exact endpoint wording | Medium |
| Full metric table | Not confirmed |
