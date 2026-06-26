# Paper 03: Multimodal IVF Prediction Using Time-Lapse Videos and Clinical Data

## Citation

Gao, Q., Yao, S., Du, D., Yang, F., Yu, P., Quan, S., Hua, R., Zhao, L., Shang, A., Lu, H., & Yue, C. (2026). **Multimodal intelligent prediction model for in vitro fertilization**. *npj Digital Medicine*, 9, Article 147.

DOI: [https://doi.org/10.1038/s41746-025-02331-5](https://doi.org/10.1038/s41746-025-02331-5)

Source checked: [npj Digital Medicine article page](https://www.nature.com/articles/s41746-025-02331-5)

Important note:

This paper was initially present in our matrix as **2025**, but the publisher page shows **published 10 January 2026**. Therefore, it is outside the original 2021-2025 target window. It is still useful as a high-relevance support paper because it directly addresses multimodal IVF prediction.

Related study terms:

- [Time-lapse system](../glossary/clinical-glossary.md#time-lapse-system)
- [Embryo transfer](../glossary/clinical-glossary.md#embryo-transfer)
- [Single embryo transfer](../glossary/clinical-glossary.md#single-embryo-transfer)
- [Double embryo transfer](../glossary/clinical-glossary.md#double-embryo-transfer)
- [Fetal heartbeat](../glossary/clinical-glossary.md#fetal-heartbeat)
- [Miscarriage](../glossary/clinical-glossary.md#miscarriage)
- [Multimodal learning](../glossary/technical-glossary.md#multimodal-learning)
- [Deep learning](../glossary/technical-glossary.md#deep-learning)
- [Pretraining](../glossary/technical-glossary.md#pretraining)
- [Multi-task learning](../glossary/technical-glossary.md#multi-task-learning)
- [Cross-attention](../glossary/technical-glossary.md#cross-attention)

## Why This Paper Matters

This paper is highly relevant because it directly supports the idea that IVF outcome prediction can be improved by integrating more than one data type.

It combines:

- embryo time-lapse videos
- tabular clinical variables
- multimodal deep learning
- multi-task prediction
- external testing across hospitals

This is close to our provisional research direction because our topic also depends on multimodal clinical and embryological data. However, this paper is more technically complex and focused on embryo-video data.

## Research Objective

The study proposed **VaTEP**, a Video and Table model for Embryo Prediction.

The objective was to integrate embryo time-lapse video data with clinical table variables to predict three IVF-related outcomes:

1. fetal heartbeat
2. singleton pregnancy vs. multiple pregnancy
3. miscarriage vs. live birth

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Retrospective multimodal model development and validation study |
| Country | China |
| Hospitals | Three hospitals |
| Initial participant source | 9,786 participants across three hospitals |
| Internal training/validation source | Hospital 1 |
| External testing source | Hospitals 2 and 3 |
| Data type | Embryo TLS videos plus clinical information tables |
| Transfer type | Day-3 embryo transfers only after filtering |
| Internal dataset after quality control | 1,012 participants |
| External dataset after quality control | 221 participants |
| Internal videos | 1,767 videos |
| External videos | 388 videos |
| Clinical variables | 39 clinical variables selected by clinical expertise |
| Ethics | IRB approval from participating hospitals; written informed consent; anonymized videos and clinical data |

Confidence: **High**

## Data Filtering and Quality Control

Participants were excluded if they had:

- missing clinical information tables
- unavailable embryo time-lapse videos
- absent pregnancy outcome records
- transfer of more than three embryos
- non-day-3 embryo transfer

Video quality control removed:

- non-transferred embryos
- out-of-focus frames
- black frames
- frozen frames
- resolution below 300 x 300
- videos with fewer than 576 frames
- duplicates

Clinical table quality control removed:

- incomplete records
- incorrectly recorded data
- outliers

The videos and tables were matched using unique IDs.

Confidence: **High**

## Variables / Features Used

The paper used two main data modalities.

| Modality | Information Used |
| --- | --- |
| Video modality | Embryo time-lapse videos showing embryo development over time |
| Table modality | Clinical variables including demographic, hormonal, treatment and transfer-related information |

The article mentions variables such as:

- BMI
- endometrial thickness
- FSH
- LH
- estradiol
- progesterone
- testosterone
- AMH
- prolactin
- thyroid-stimulating hormone
- gonadotropin
- HCG

Female and male age were highlighted as significantly different between fetal-heartbeat and non-fetal-heartbeat groups in both internal and external datasets.

Confidence: **High**

## Method / Algorithm

| Area | Method |
| --- | --- |
| Model name | VaTEP: Video and Table model for Embryo Prediction |
| Video preprocessing | YOLOv8 object detection to extract embryo regions |
| Video pretraining tasks | TLS video reconstruction and embryo developmental phase prediction |
| Video encoder | 3D convolutional blocks and Temporal Transformer |
| Tabular-data encoder | Heterogeneous encoding of categorical and continuous variables |
| Table interaction | Table Transformer |
| Multimodal fusion | Cross-attention between video embeddings and clinical variable embeddings |
| Learning framework | Multi-task collaborative learning |
| Prediction branches | Fully connected task-specific classifier branches |
| Loss function | Weighted cross-entropy; masked weighted cross-entropy for selected downstream tasks |

Confidence: **High**

## Evaluation Metrics

| Metric | Use |
| --- | --- |
| Accuracy | Classification performance |
| AUC | Discrimination performance |
| F1 score | Balance between precision and recall |
| ROC curves | Compared classification performance |
| Precision, recall, mAP | Object detection evaluation |
| Expert comparison | Compared VaTEP with embryologist predictions |

Confidence: **High**

## Main Findings

The full VaTEP model used pretrained video representation, video+table multimodal fusion and multi-task learning.

| Prediction Task | Accuracy | AUC | F1 |
| --- | ---: | ---: | ---: |
| Fetal heartbeat | 0.7403 ± 0.0079 | 0.8000 ± 0.0130 | 0.7413 ± 0.0432 |
| Singleton vs. multiple pregnancy | 0.8636 ± 0.0163 | 0.8823 ± 0.0268 | 0.8013 ± 0.0281 |
| Miscarriage vs. live birth | 0.9145 ± 0.0148 | 0.9258 ± 0.0220 | 0.9494 ± 0.0094 |

Other important findings:

- Multimodal video+table models outperformed unimodal versions.
- Pretraining improved model performance.
- Multi-task learning improved overall performance compared with single-task learning.
- VaTEP was externally tested using data from Hospitals 2 and 3.
- The model was compared with embryologist predictions.
- Performance for irregularly developing embryos still required improvement.

Confidence: **High**

## Limitations Stated by Authors

The authors clearly state these limitations:

| Limitation | Meaning |
| --- | --- |
| Retrospective data | The model cannot replace prospective clinical validation. |
| Need prospective trials | Future multi-center prospective trials are needed. |
| Pre-transfer recommendation not fully solved | A true pre-transfer preference recommendation system needs broader inclusion of non-transferred embryos. |
| Irregular embryo performance needs improvement | The model performed less strongly for irregularly developing embryos, likely because such cases were limited in training data. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our literature-review observations based on the paper design.

| Critical Point | Why It Matters |
| --- | --- |
| Published outside 2021-2025 target window | It should be used as current support evidence, not counted as a core 2021-2025 paper unless the review window is expanded. |
| China-only hospitals | External testing was across hospitals, but not across countries or Indian clinics. |
| Day-3 transfer restriction | Findings may not generalize to other embryo-transfer timings or blastocyst-stage transfer. |
| Requires time-lapse video infrastructure | Many clinics may not have TLS data, limiting practical use in resource-constrained settings. |
| Deep model complexity | Strong performance, but clinical explanation and interpretability are limited compared with simpler XAI/CDSS approaches. |
| Transfer-selection bias risk | The model used transferred embryo videos after filtering; true ranking among all available embryos needs broader non-transferred embryo data. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- multi-center prospective clinical trials
- real-world clinical utility evaluation
- collaborative decision-making between senior experts and model output
- broader datasets including non-transferred embryos
- improving performance for irregularly developing embryos
- developing true pre-transfer preference recommendation systems

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need multimodal data | Yes | Strong example of video + clinical table integration. |
| Need external validation | Partial | External hospital testing exists, but international/Indian validation is absent. |
| Need prospective validation | Yes | Authors explicitly call for prospective trials. |
| No pre-transfer recommendation | Yes | Authors state broader non-transferred embryo data are needed for true pre-transfer recommendation. |
| Explainability gap | Yes | Deep multimodal model performance is strong, but explanation for clinical decision-making is limited. |
| Deployment gap | Yes | Real-world clinical utility is not established. |
| Lifestyle data gap | Limited | Lifestyle variables are not a central component. |

## Usefulness For Our PhD

Relevance: **High**, but **outside the original 2021-2025 window**.

This paper is useful because it supports the idea that multimodal IVF prediction can outperform single-modality prediction.

It also shows why our PhD direction should be practical and data-dependent. If our clinic data does not include time-lapse videos, we should not claim a video-based multimodal model. Instead, our multimodal scope may need to focus on clinical, hormonal, treatment-cycle and embryology table variables.

This paper strengthens our argument that future IVF-AI systems should integrate multiple data sources, but it also highlights the need for explainability, prospective validation and local clinical feasibility.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Gao et al. (2026) developed VaTEP, a multimodal deep learning model that integrated embryo time-lapse videos with 39 clinical variables to predict fetal heartbeat, singleton versus multiple pregnancy, and miscarriage versus live birth across internal and external hospital datasets.

Gap-support sentence:

> Although VaTEP achieved strong predictive performance and demonstrated the value of multimodal fusion, the study was retrospective, restricted to day-3 transfers, and the authors identified the need for broader non-transferred embryo data and prospective multi-center validation before routine clinical decision-support use.

## What This Paper Does Not Prove

This paper does not prove that:

- multimodal deep learning is feasible in clinics without time-lapse video systems.
- the model generalizes to Indian IVF populations.
- the model can already recommend embryo transfer choices in real clinical practice.
- high AUC alone is enough for clinician trust.
- all IVF clinics should use deep video-based AI instead of simpler clinical models.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Publication year correction | High |
| Study design and dataset | High |
| Methods | High |
| Main findings | High |
| Limitations/future work | High |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
