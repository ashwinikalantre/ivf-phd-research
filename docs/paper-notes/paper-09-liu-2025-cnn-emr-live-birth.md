# Paper 09: CNN and Traditional ML for IVF Live-Birth Prediction From EMR Data

## Citation

Liu, Y., Wang, Y., Huang, K., Shi, H., Xin, H., Dai, S., Liu, J., Yang, X., Song, J., Zhang, F., & Guo, Y. (2025). **Comparative analysis of convolutional neural networks and traditional machine learning models for IVF live birth prediction: a retrospective analysis of 48514 IVF cycles and an evaluation of deployment feasibility in resource-constrained settings**. *Frontiers in Endocrinology*, 16.

DOI: [https://doi.org/10.3389/fendo.2025.1556681](https://doi.org/10.3389/fendo.2025.1556681)

Source checked: [Frontiers in Endocrinology article page](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2025.1556681/full)

Related study terms:

- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [Electronic medical record](../glossary/technical-glossary.md#electronic-medical-record)
- [Convolutional neural network](../glossary/technical-glossary.md#convolutional-neural-network)
- [Feedforward Neural Network](../glossary/technical-glossary.md#feedforward-neural-network)
- [Naive Bayes](../glossary/technical-glossary.md#naive-bayes)
- [Random Forest](../glossary/technical-glossary.md#random-forest)
- [SHAP](../glossary/technical-glossary.md#shap)
- [One-hot encoding](../glossary/technical-glossary.md#one-hot-encoding)
- [Min-max scaling](../glossary/technical-glossary.md#min-max-scaling)
- [Early stopping](../glossary/technical-glossary.md#early-stopping)

## Why This Paper Matters

This paper is important because it uses a large IVF electronic medical record dataset and compares a convolutional neural network with traditional machine-learning models.

It is useful for our PhD because it addresses two practical questions:

1. Can deep learning be applied to structured IVF clinical data?
2. Can such models be deployed in resource-constrained reproductive centers?

It also reinforces a key caution: even large single-center datasets still need external validation before clinical use.

## Research Objective

The objective was to evaluate a CNN for analyzing structured EMR data in assisted reproductive therapy and compare its performance and interpretability with traditional ML models for IVF live-birth prediction.

The study also explored deployment feasibility in resource-limited clinical settings.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Retrospective cohort prediction-model study |
| Country | China |
| Center | First Affiliated Hospital of Zhengzhou University |
| Study period | August 2009 to May 2018 |
| Population | Fresh IVF cycles |
| Dataset size | 48,514 IVF cycles |
| Main outcome | Live birth |
| Final selected features | 39 high-quality clinical and laboratory features in final curated dataset |
| CNN input features | 42 selected features arranged as 6 x 7 pseudo-image input |
| Train-test split | 80% training, 20% testing, stratified by outcome |
| Cross-validation | Stratified fivefold cross-validation |
| Ethics | Ethics approval reported; written informed consent reported |
| Data availability | Original data not publicly disclosed due to patient privacy; requests can be made to author |

Confidence: **High**

## Variables / Features Used

The article lists many clinical indicators selected for live-birth prediction, including:

- female age
- infertility type
- infertility duration
- menstrual cycle length
- BMI
- basal FSH
- basal estradiol
- basal LH
- basal testosterone
- FT3
- FT4
- TSH
- unexplained infertility
- PCOS
- advanced age
- decreased ovarian function
- premature ovarian failure
- chronic anovulation
- pelvic factor
- immunologic factors
- abnormal AMH
- tubal factor
- endometrial factor
- chromosome abnormality
- sperm origin
- oocyte origin
- period type
- number of treatment attempts
- treatment solutions
- starting gonadotropin dose
- total gonadotropin dose
- days of gonadotropin injection
- number of retrieved oocytes
- number of 2PN oocytes
- number of 2PN cleavage oocytes
- number of transferable embryos
- number of high-quality embryos

Confidence: **High**

## Method / Algorithm

Five prediction models were compared:

| Model | Role |
| --- | --- |
| Random Forest | Best-performing traditional ML model |
| Decision Tree | Comparison model |
| Naive Bayes | Comparison model |
| Feedforward Neural Network | Comparison model |
| Convolutional Neural Network | Deep learning model adapted for structured EMR data |

Preprocessing and implementation:

- missing continuous variables imputed using mean
- categorical variables excluded if missingness exceeded 50%
- one-hot encoding for categorical variables
- min-max scaling to range -1 to 1 for numerical variables
- EMR features reshaped into single-channel pseudo-images
- CNN input shape: 1 x 6 x 7
- two convolutional layers with 16 and 32 filters
- ReLU activation
- max pooling
- dropout rate 0.5
- fully connected layers with 64 and 1 units
- sigmoid output
- binary cross-entropy loss
- Adam optimizer
- early stopping
- PyTorch 2.5, scikit-learn 1.6.0, SHAP 0.39.0

Confidence: **High**

## Evaluation Metrics

The study used:

- accuracy
- AUC
- precision
- recall
- F1 score
- ROC curves
- training loss curve
- SHAP-based feature importance

Confidence: **High**

## Main Findings

| Model | Accuracy | AUC | Precision | Recall | F1 Score |
| --- | ---: | ---: | ---: | ---: | ---: |
| Random Forest | 0.9406 ± 0.0017 | 0.9734 ± 0.0012 | 0.9356 ± 0.0018 | 0.9997 ± 0.0002 | 0.9666 ± 0.0009 |
| Decision Tree | 0.9387 ± 0.0026 | 0.8249 ± 0.0051 | 0.9478 ± 0.0014 | 0.9829 ± 0.0022 | 0.9650 ± 0.0015 |
| Naive Bayes | 0.4889 ± 0.0138 | 0.8795 ± 0.0034 | 0.9892 ± 0.0032 | 0.4103 ± 0.0173 | 0.5798 ± 0.0171 |
| Feedforward Neural Network | 0.9315 ± 0.0029 | 0.8896 ± 0.0041 | 0.9426 ± 0.0018 | 0.9801 ± 0.0037 | 0.9610 ± 0.0017 |
| CNN | 0.9394 ± 0.0013 | 0.8899 ± 0.0032 | 0.9348 ± 0.0018 | 0.9993 ± 0.0012 | 0.9660 ± 0.0007 |

Key findings:

- Random Forest had the highest AUC and F1 score.
- CNN performance was comparable to Random Forest in accuracy and F1.
- CNN had near-perfect recall.
- Naive Bayes had poor accuracy and recall.
- SHAP highlighted maternal age, BMI, AFC and gonadotropin dosage as important predictors in the abstract.
- The paper argues CNN models can be deployed locally without GPU acceleration, using about 80-100 MB memory and less than 0.05 seconds per prediction on tested Apple M1/M2 systems.

Confidence: **High**

## Limitations Stated by Authors

The authors state these limitations:

| Limitation | Meaning |
| --- | --- |
| Single medical center | Generalizability to other populations and settings is limited. |
| No multimodal data | Imaging and other modalities were not included. |
| Socioeconomic factors missing | Financial status and education were not considered. |
| Need multicenter validation | Future studies should validate across multiple centers. |
| Need multimodal integration | Future work should investigate multimodal data to improve performance and generalizability. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| High recall may reflect class imbalance or threshold behavior | Near-perfect recall should be interpreted with class distribution and false-positive burden. |
| CNN on tabular pseudo-images is methodologically debatable | Reshaping tabular features into a grid may impose artificial spatial structure. |
| Random Forest outperformed CNN in AUC | Deep learning was not clearly superior to traditional ML. |
| No external validation | Large sample size does not solve population and clinic generalization. |
| No calibration metrics reported in the main table | Counseling requires reliable probabilities, not only discrimination. |
| No clinician usability testing | Deployment feasibility was discussed technically, not tested as a real CDSS workflow. |
| No Indian validation | China-only data; local Indian validation still needed. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- multicenter validation
- multimodal data integration
- testing imaging, ultrasound, embryo morphokinetics and time-lapse videos
- improving generalizability
- evaluating real-world deployment in resource-limited reproductive centers
- adding socioeconomic factors where available

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need external validation | Yes | Single-center dataset despite large sample size. |
| Need multimodal data | Yes | Authors explicitly state multimodal data were not included. |
| Resource-constrained deployment | Yes | Paper directly discusses low-resource deployment feasibility. |
| Need clinical decision support | Partial | Deployment feasibility is discussed, but no clinician workflow trial is shown. |
| Explainability gap | Partial | SHAP used, but clinical usability of explanations is not evaluated. |
| Socioeconomic/lifestyle data gap | Yes | Financial and educational factors were not included. |
| Indian validation gap | Yes | No Indian data or validation. |

## Usefulness For Our PhD

Relevance: **High**

This paper is useful because it shows that large EMR-based IVF datasets can support live-birth prediction and that deployment feasibility should be considered, especially in resource-limited settings.

It also gives a strong caution for our methods chapter:

> Deep learning is not automatically better. Random Forest outperformed CNN on AUC, and CNN required artificial transformation of tabular data into pseudo-images.

For our PhD, this supports starting with strong tabular models such as Logistic Regression, Random Forest, XGBoost and LightGBM before considering deep learning.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Liu et al. (2025) analyzed 48,514 fresh IVF cycles from electronic medical records and compared CNN, Random Forest, Decision Tree, Naive Bayes and feedforward neural network models for live-birth prediction, finding that Random Forest achieved the highest AUC while CNN achieved comparable accuracy and high recall.

Gap-support sentence:

> Although the study demonstrates the feasibility of EMR-based IVF prediction and low-resource deployment, its single-center design, absence of multimodal and socioeconomic data, and lack of clinical workflow validation limit generalizability and decision-support readiness.

## What This Paper Does Not Prove

This paper does not prove that:

- CNN is superior to traditional ML for IVF tabular data.
- pseudo-image transformation of EMR variables is clinically meaningful.
- the model generalizes to Indian IVF clinics.
- low-resource technical deployment equals clinical adoption.
- SHAP output is sufficient for clinician trust.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Dataset | High |
| Variables/features | High |
| Model architecture | High |
| Main findings | High |
| Limitations/future work | High |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
