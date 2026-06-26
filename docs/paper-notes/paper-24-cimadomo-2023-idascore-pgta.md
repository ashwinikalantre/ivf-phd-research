# Paper 24: Pre-Clinical Validation of iDAScore for Embryo Grading during PGT-A Cycles

## Citation

Cimadomo, D., Chiappetta, V., Innocenti, F., Saturno, G., Taggi, M., Marconetto, A., Casciani, V., Albricci, L., Maggiulli, R., Coticchio, G., Ahlström, A., Berntsen, J., Larman, M., Borini, A., Vaiarelli, A., Ubaldi, F. M., & Rienzi, L. (2023). **Towards Automation in IVF: Pre-Clinical Validation of a Deep Learning-Based Embryo Grading System during PGT-A Cycles**. *Journal of Clinical Medicine*, 12(5), 1806.

DOI: [https://doi.org/10.3390/jcm12051806](https://doi.org/10.3390/jcm12051806)

Sources checked:

- [MDPI article page](https://www.mdpi.com/2077-0383/12/5/1806)
- [PubMed record](https://pubmed.ncbi.nlm.nih.gov/36902592/)
- [PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC10002983/)

Evidence note:

The MDPI/PMC pages triggered browser challenge during direct extraction, but PubMed and indexed full-text excerpts confirm the key study details. This note is high confidence for the abstract-confirmed data and medium-high for detailed interpretation.

Related study terms:

- [Blastocyst](../glossary/clinical-glossary.md#blastocyst)
- [PGT-A](../glossary/clinical-glossary.md#pgt-a)
- [Euploid embryo](../glossary/clinical-glossary.md#euploid-embryo)
- [Aneuploid embryo](../glossary/clinical-glossary.md#aneuploid-embryo)
- [Single embryo transfer](../glossary/clinical-glossary.md#single-embryo-transfer)
- [Time-lapse system](../glossary/clinical-glossary.md#time-lapse-system)
- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [Embryo grading](../glossary/technical-glossary.md#embryo-grading)
- [3D Convolutional Neural Network](../glossary/technical-glossary.md#3d-convolutional-neural-network)
- [Pre-Clinical Validation](../glossary/technical-glossary.md#pre-clinical-validation)
- [External Validation](../glossary/technical-glossary.md#external-validation)
- [AUC](../glossary/technical-glossary.md#auc)

## Why This Paper Matters

This paper is useful because it evaluates an automated deep-learning embryo grading system before clinical deployment.

It is relevant for our PhD because it shows:

- embryo image/video AI can objectify embryo ranking
- AI embryo grading may be reproducible compared with embryologist assessment
- good retrospective association does not automatically prove clinical value
- randomized trials are required before replacing or guiding embryo selection decisions

It also helps us understand the difference between embryo-quality ranking and final IVF outcome prediction.

## Research Objective

The study aimed to externally and pre-clinically validate iDAScore v1.0, a deep-learning embryo grading/ranking system, during PGT-A cycles.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Retrospective pre-clinical validation study |
| Journal | Journal of Clinical Medicine |
| Year | 2023 |
| Tool evaluated | iDAScore v1.0 |
| Model type | Deep learning model based on 3D convolutional neural network |
| Dataset | 3,604 blastocysts |
| Euploid transfer subset | 808 euploid transfers |
| Cycles | 1,232 cycles |
| Clinical context | PGT-A cycles |
| Decision influence | Retrospective scoring only; did not influence embryologist decisions |

Confidence: **High**

## Variables / Features Used

Confirmed:

- time-lapse blastocyst videos/images
- embryo morphology comparison
- PGT-A/euploidy status
- euploid blastocyst transfer outcomes
- live-birth outcome after euploid single embryo transfer

The iDAScore model:

- was trained on time-lapse videos from implanted and non-implanted blastocysts
- ranks blastocysts without manual input
- was retrospectively applied in this validation study

Confidence: **High**

## Method / Algorithm

| Component | Extracted Information |
| --- | --- |
| AI system | iDAScore v1.0 |
| Architecture | 3D convolutional neural network |
| Task | Automated blastocyst ranking / embryo grading |
| Human comparator | Embryologist morphology assessment |
| Validation design | Retrospective pre-clinical external validation |
| Deployment status | Not used to make actual clinical decisions in this study |

Confidence: **High**

## Evaluation Metrics

The study evaluated:

- association with embryo morphology
- association with euploidy
- association with live birth after euploid blastocyst single embryo transfer
- AUC for euploidy prediction
- AUC for live-birth prediction
- retrospective simulations of embryo-ranking decisions

Confidence: **High**

## Main Findings

| Finding | Extracted Information |
| --- | --- |
| Association with morphology | iDAScore v1.0 was significantly associated with embryo morphology |
| Euploidy prediction AUC | 0.60 |
| Live-birth prediction AUC | 0.66 |
| Euploid ranking simulation | iDAScore ranked the euploid blastocyst top in 63% of cases with one or more euploid and aneuploid blastocysts |
| Disagreement simulation | iDAScore would have questioned embryologists' ranking in 48% of cases with at least two euploid blastocysts and one or more live birth |
| Reproducibility | iDAScore is objective and reproducible compared with subjective embryologist evaluation |
| Clinical conclusion | Randomized controlled trials are required to assess clinical value |

The main message is not that iDAScore solves embryo selection. The main message is that it may standardize embryo assessment, but its clinical value requires prospective/randomized testing.

Confidence: **High**

## Limitations Stated By Authors / Review Process

Confirmed or strongly indicated:

| Limitation | Meaning |
| --- | --- |
| Retrospective validation | iDAScore did not guide actual embryo selection decisions. |
| Pre-clinical study | It validates association, not clinical benefit. |
| Modest AUC values | Euploidy AUC 0.60 and live-birth AUC 0.66 are limited. |
| RCT needed | Randomized controlled trials are required to assess clinical value. |
| Cost-effectiveness unclear | Review comments noted uncertainty about whether iDAScore is cost-effective for IVF laboratories. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Black-box risk | 3D CNN ranking may be difficult for embryologists/patients to understand. |
| Modest discrimination | AUC 0.66 for live birth is not strong enough alone for clinical confidence. |
| PGT-A cycle focus | Findings may not apply to non-PGT-A IVF cycles. |
| Retrospective simulation | Simulated ranking changes are not the same as improved outcomes. |
| No Indian population | Generalization to Indian IVF labs is not established. |
| No full CDSS workflow | It is an embryo ranking system, not a complete clinical decision-support pathway. |
| Requires time-lapse infrastructure | Clinics without compatible embryo imaging systems may not use this approach. |

Confidence: **High**

## Future Work Suggested

The paper supports future work in:

- randomized controlled trials
- prospective clinical validation
- evaluation of clinical value before routine use
- cost-effectiveness assessment
- comparison with embryologists and other AI models
- assessment of generalizability across IVF laboratories and patient populations

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Black-box / explainability gap | Yes | 3D CNN ranking is not clearly explainable to users. |
| Need prospective/RCT validation | Yes | Authors conclude RCTs are required. |
| Retrospective design | Yes | iDAScore was applied retrospectively. |
| Clinical utility gap | Yes | Association does not prove improved outcomes. |
| Infrastructure dependency | Yes | Requires time-lapse embryo imaging. |
| Lack of Indian population | Yes | Dataset is not Indian. |
| Moderate performance | Yes | AUCs for euploidy and live birth were modest. |

## Usefulness For Our PhD

Relevance: **High for embryo-grading theme; Medium for our likely final CDSS topic**

This paper is useful because it shows how embryo image/video AI is being validated and where the limitations remain.

For our work, it tells us:

- embryo data can add value if available
- embryo image/video AI needs infrastructure
- black-box embryo ranking is not enough for clinical trust
- retrospective performance must not be overstated
- live birth remains the stronger outcome than morphology or euploidy alone

If our clinic dataset does not include embryo images or time-lapse videos, this paper becomes background evidence rather than a core method paper.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Cimadomo et al. (2023) externally validated iDAScore v1.0, a 3D CNN-based embryo grading system, using 3,604 blastocysts and 808 euploid transfers from 1,232 PGT-A cycles, finding significant association with morphology and embryo competence but modest AUC values of 0.60 for euploidy and 0.66 for live birth.

Gap-support sentence:

> The study concluded that although automated embryo grading may improve objectivity and reproducibility, randomized controlled trials are required to establish clinical value, reinforcing the need for prospective validation and trustworthy embryo-selection AI.

## What This Paper Does Not Prove

This paper does not prove that:

- iDAScore improves live-birth rate in routine IVF care.
- embryo AI should replace embryologists.
- AUC 0.66 is sufficient for clinical deployment.
- the tool generalizes to non-PGT-A cycles or Indian IVF clinics.
- black-box embryo ranking is acceptable without explanation and clinician review.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation and DOI | High |
| Dataset size | High |
| Tool and architecture | High |
| Main AUC values | High |
| Retrospective/pre-clinical design | High |
| Limitations and RCT need | High |
| Full table-level extraction | Medium |
