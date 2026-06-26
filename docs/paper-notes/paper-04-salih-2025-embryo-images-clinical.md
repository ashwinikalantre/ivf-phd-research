# Paper 04: Deep Learning With Embryo Images and Clinical Information

## Citation

Salih, M., Austin, C., Mantravadi, K., Seow, E., Jitanantawittaya, S., Reddy, S., Vollenhoven, B., Rezatofighi, H., & Horta, F. (2025). **Deep learning classification integrating embryo images with associated clinical information from ART cycles**. *Scientific Reports*, 15, Article 17585.

DOI: [https://doi.org/10.1038/s41598-025-02076-x](https://doi.org/10.1038/s41598-025-02076-x)

Source checked: [Scientific Reports article page](https://www.nature.com/articles/s41598-025-02076-x)

Related study terms:

- [Blastocyst](../glossary/clinical-glossary.md#blastocyst)
- [Embryo transfer](../glossary/clinical-glossary.md#embryo-transfer)
- [Single embryo transfer](../glossary/clinical-glossary.md#single-embryo-transfer)
- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [Miscarriage](../glossary/clinical-glossary.md#miscarriage)
- [Multimodal learning](../glossary/technical-glossary.md#multimodal-learning)
- [Convolutional neural network](../glossary/technical-glossary.md#convolutional-neural-network)
- [ResNet](../glossary/technical-glossary.md#resnet)
- [Fusion model](../glossary/technical-glossary.md#fusion-model)
- [ScoreCAM](../glossary/technical-glossary.md#scorecam)
- [Layer-wise relevance propagation](../glossary/technical-glossary.md#layer-wise-relevance-propagation)

## Why This Paper Matters

This paper is important because it directly studies whether prediction improves when embryo images are combined with patient clinical information.

It is useful for our PhD because it supports the idea that IVF prediction should not depend only on one data type. It also includes treatment cycles from India, Malaysia and Thailand, which gives it more relevance to our Indian-context discussion than many Europe- or China-only papers.

## Research Objective

The study aimed to develop and compare three AI models for predicting reproductive outcomes in ART cycles:

1. a clinical-data model
2. an embryo-image model
3. a fusion model combining clinical data and embryo images

The main outcomes were:

- clinical pregnancy
- live birth / miscarriage / not pregnant classification

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Retrospective model-development and testing study |
| Data source | International ART treatment-cycle database |
| Countries / groups | India, Malaysia and Thailand in the final described database; ethics section also mentions Australia involvement |
| Initial treatment cycles | 1,503 treatment cycles in abstract |
| Available IVF/ICSI cycle information after analysis | 1,394 cycles with clinical data and blastocyst images |
| Initial blastocyst images | 1,980 images |
| Single embryo transfer images | 1,190 samples |
| Discarded due to artifacts/incomplete data | 599 samples |
| Clinical pregnancy prediction samples | 1,503 samples |
| Live-birth prediction samples | 1,585 samples |
| Clinical pregnancy split | 1,048 train, 154 validation, 301 test |
| Live-birth split | 1,109 train, 159 validation, 137 blind test |
| Ethics | Monash Health ethics approval; clinic consent for unidentifiable samples |

Confidence: **High**

## Variables / Features Used

The paper groups clinical information into:

- clinical features
- treatment features
- ART and embryo transfer features

The model used clinical records and blastocyst still images taken at embryo transfer procedures.

Important clinical variables mentioned in the paper include:

- female age
- male age
- female BMI
- sperm motility
- IVF or ICSI treatment type
- fresh or frozen embryo transfer
- treatment-cycle information

The authors state that embryo quality grading followed the Istanbul consensus, but because these features required manual embryologist grading, they were **not included in the final models**.

Confidence: **High**

## Method / Algorithm

| Model | Input | Method |
| --- | --- | --- |
| Clinical model | Clinical data | Multi-layer perceptron |
| Image model | Blastocyst still images | CNN using ResNet34 backbone |
| Fusion model | Clinical data + blastocyst images | MLP + ResNet34 features concatenated into a final classifier |

Implementation details:

- Python
- PyTorch
- 70% training, 10% validation, 20% blind test
- Weighted batch sampling to manage class imbalance
- Cross-entropy loss
- AdamW optimizer
- LeakyReLU activation
- 400 epochs

Confidence: **High**

## Explainability / Visualization Methods

The paper used visualization methods to understand model behavior.

| Method | Purpose |
| --- | --- |
| ScoreCAM | Created saliency maps to identify image regions important for CNN predictions |
| Layer-wise Relevance Propagation | Estimated clinical feature importance in the clinical model |
| Bayesian inference | Tested whether heatmap patterns could help estimate prediction reliability |

Important finding:

The image model often focused on trophectoderm cells, but some examples showed flawed behavior where the model focused on background rather than embryo regions.

Confidence: **High**

## Evaluation Metrics

| Metric | Use |
| --- | --- |
| Accuracy | Overall correct classification |
| Average precision | Precision-recall-based performance |
| AUC | Discrimination performance |
| F1-score | Useful because dataset imbalance was present |
| ROC curve | Model comparison |
| Precision-recall curve | Model comparison |
| Fivefold cross-validation | Additional model consistency check |

Confidence: **High**

## Main Findings

### Abstract-level performance

| Model | Accuracy | Average Precision | AUC |
| --- | ---: | ---: | ---: |
| Clinical MLP | 81.76% | 90% | 0.91 |
| Image CNN | 66.89% | 74% | 0.73 |
| Fusion model | 82.42% | 91% | 0.91 |

### Pregnancy and live-birth reporting in results

| Outcome | Clinical Model | Image Model | Fusion Model |
| --- | ---: | ---: | ---: |
| Clinical pregnancy accuracy | 91% | 73% | 91% |
| Live-birth task accuracy | 87% | 80% | 88% |

Other important findings:

- The clinical model performed strongly.
- The image-only model performed weaker than the clinical model.
- The fusion model performed better than image-only models and slightly improved over clinical-only results in some comparisons.
- Female age and male age were highly important clinical factors.
- Trophectoderm was an important blastocyst image feature.
- The authors argue that integrating clinical information with embryo images can support more personalized embryo-selection decisions.

Confidence: **High**

## Limitations Stated by Authors

The authors clearly describe several limitations.

| Limitation | Meaning |
| --- | --- |
| Retrospective data | The study requires clinical-setting testing and prospective validation. |
| Class imbalance | The dataset had 69% positive pregnancy samples, which was higher than expected. |
| Transferred embryos only | The model did not include embryos that were not transferred, frozen or discarded. |
| Limited database | The authors state that AI is data-hungry and the model suffered from limited database size. |
| Need larger diverse dataset | Larger and more diverse data are needed for generalizability. |
| Need embryologist comparison | Future testing against embryologists is needed. |
| Need interpretability improvement | More work is needed on uncertainty estimation and active learning. |
| Data bias and shifting | Older samples and changing clinical practice may affect model behavior. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These points matter for our PhD gap analysis.

| Critical Point | Why It Matters |
| --- | --- |
| Image infrastructure requirement | Clinics without standardized embryo image capture may not be able to use this approach. |
| Fusion gain is modest | The fusion model did not show a drastic improvement over clinical data alone. |
| Transferred-embryo bias | If only transferred embryos are included, the model may not learn from embryos that were rejected or frozen. |
| No true real-time CDSS validation | The study suggests CDSS value, but actual clinician-facing deployment was not tested. |
| Limited explanation depth | ScoreCAM/LRP provide visualization, but clinician trust and usability were not deeply evaluated. |
| Indian data present but not separately validated | India is included as a data source, but the paper does not provide India-specific model validation. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- including time-lapse videos of transferred and non-transferred embryos
- using larger and more diverse datasets
- testing models in clinical settings
- comparing AI predictions against embryologists
- improving prediction uncertainty estimation
- using active learning
- exploring transformers and continuous learning
- integrating more biomarkers such as genetics, proteomics and metabolomics

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need multimodal data | Yes | Clinical + embryo image fusion is central to the paper. |
| Need clinical decision support | Yes | Authors position the model as a building block for CDSS, but deployment is not complete. |
| Need real-world deployment evidence | Yes | Clinical-setting testing remains future work. |
| Selection bias / transferred-embryo bias | Yes | Only transferred embryos were included. |
| Need larger external validation | Yes | Larger diverse datasets and clinical testing are needed. |
| Explainability/trust gap | Yes | Visualization is present, but deeper interpretability and trust evaluation remain. |
| Indian relevance | Partial | India is included in the dataset, but India-specific validation is not shown. |

## Usefulness For Our PhD

Relevance: **High**

This paper is useful because it supports the argument that IVF prediction can benefit from combining patient clinical data and embryology/image data. It is especially relevant to our provisional direction of multimodal clinical and embryological decision support.

However, it also teaches an important caution: multimodal AI is not automatically better in a clinically meaningful way. In this study, clinical data alone was already strong, and fusion provided only modest improvement in some results. Therefore, our future model should compare clinical-only, embryology-only and combined models rather than assuming multimodal integration will always be superior.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Salih et al. (2025) developed and compared clinical, embryo-image and fused deep learning models using ART treatment-cycle data and blastocyst images from international clinics, showing that integration of clinical information with embryo images can improve reproductive outcome prediction compared with image-only models.

Gap-support sentence:

> Despite demonstrating the value of multimodal clinical-image integration, the study was retrospective, used only transferred embryos, faced class imbalance and limited database size, and identified the need for larger diverse datasets, clinical-setting validation and stronger explainability before routine decision-support use.

## What This Paper Does Not Prove

This paper does not prove that:

- embryo images alone are sufficient for reliable IVF outcome prediction.
- multimodal fusion always gives large improvement over clinical-data models.
- the model is ready for clinical deployment.
- India-specific performance is established.
- clinician trust and patient acceptance are solved.
- non-transferred embryo ranking is solved.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Dataset | High |
| Methods | High |
| Main findings | High |
| Limitations/future work | High |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
