# Paper 12: Review of AI for Personalized Assisted Reproductive Technology

## Citation

Hanassab, S., Abbara, A., Yeung, A. C., Voliotis, M., Tsaneva-Atanasova, K., Kelsey, T. W., Trew, G. H., Nelson, S. M., Heinis, T., & Dhillo, W. S. (2024). **The prospect of artificial intelligence to personalize assisted reproductive technology**. *npj Digital Medicine*, 7, Article 55.

DOI: [https://doi.org/10.1038/s41746-024-01006-x](https://doi.org/10.1038/s41746-024-01006-x)

Source checked: [npj Digital Medicine article page](https://www.nature.com/articles/s41746-024-01006-x)

Related study terms:

- [Assisted reproductive technology](../glossary/clinical-glossary.md#assisted-reproductive-technology)
- [Ovarian stimulation](../glossary/clinical-glossary.md#ovarian-stimulation)
- [FSH](../glossary/clinical-glossary.md#fsh)
- [Trigger day](../glossary/clinical-glossary.md#trigger-day)
- [OHSS](../glossary/clinical-glossary.md#ohss)
- [Clinical decision support system](../glossary/technical-glossary.md#clinical-decision-support-system)
- [Federated learning](../glossary/technical-glossary.md#federated-learning)
- [Human-in-the-loop AI](../glossary/technical-glossary.md#human-in-the-loop-ai)
- [Black-box AI](../glossary/technical-glossary.md#black-box-ai)
- [Prospective validation](../glossary/technical-glossary.md#prospective-validation)

## Why This Paper Matters

This is a review paper, not a primary dataset study.

It is highly useful because it gives a broad, clinically informed map of where AI may personalize assisted reproductive technology.

It supports our research direction by showing that AI in ART is not limited to one prediction task. It can support:

- pre-treatment counseling
- gonadotropin dosing
- cycle monitoring
- trigger timing
- gamete and embryo assessment
- endometrial and omics-based research
- clinical decision-support workflows

The paper strongly supports our position that the PhD topic should be framed around **explainable, validated and clinician-usable decision support**, not only model performance.

## Research Objective

The review aimed to examine current AI implementations within ART and future prospects for improving personalization, efficacy and safety.

The authors focused on how AI could optimize key ART decisions in a reproducible way.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Narrative review article |
| Dataset | Not applicable; no original dataset generated |
| Data availability | Not applicable |
| Publication date | 01 March 2024 |
| Journal | npj Digital Medicine |
| Main scope | AI methods and clinical applications across ART |

Confidence: **High**

## Review Scope

The review covers AI applications in:

- pre-treatment counseling
- ovarian stimulation
- gonadotropin dosing
- induction of oocyte maturation / trigger timing
- sperm assessment
- oocyte assessment
- embryo assessment
- endometrial receptivity
- omics approaches
- CDSS implementation
- trustworthiness and explainability
- prospective validation and regulation

Confidence: **High**

## Key Arguments

| Argument | Meaning For Our PhD |
| --- | --- |
| ART decisions are operator-dependent | AI may support reproducible and consistent decision-making. |
| ART generates large dynamic datasets | AI can handle temporal and multi-stage clinical data. |
| Human-in-the-loop CDSS is preferred | Doctors and embryologists should remain final decision-makers. |
| External and prospective validation are essential | Retrospective models alone are not enough for clinical adoption. |
| Transparent models can improve trust | Explainability matters for clinician and patient acceptance. |
| AI workflows must fit clinic practice | A useful model must not increase workload or disrupt clinical care. |
| Geography and population matter | Models may need validation across different treatment settings and patient groups. |

Confidence: **High**

## Methods / Algorithms Discussed

Because this is a review, it discusses multiple AI methods rather than building one model.

Methods discussed include:

- decision trees
- logistic regression
- K-nearest neighbors
- support vector machines
- Random Forest
- artificial neural networks
- convolutional neural networks
- unsupervised clustering
- generative adversarial networks
- large language models
- federated learning
- reinforcement learning
- human-in-the-loop CDSS frameworks

Confidence: **High**

## Evaluation Themes

The review emphasizes that AI evaluation in ART should include:

- independent test datasets
- temporally different test data
- clinic-level external validation
- prospective validation
- randomized controlled trials where appropriate
- clinically relevant outcomes
- workflow impact
- patient outcome impact
- trustworthiness and fairness

Confidence: **High**

## Main Findings / Synthesis

The review argues that AI has potential in ART because many decisions are complex, repeated and data-rich.

Important synthesis points:

- AI may personalize FSH dosing and reduce unnecessary medication burden.
- Trigger-day models need prospective validation in diverse populations.
- Embryology AI is promising because image and time-lapse data are suitable for computer vision.
- Transparent models are important in early clinical AI development.
- Black-box models require explainability, fairness and generalizability checks.
- AI-omics approaches are promising but still face standardization and clinical-evidence barriers.
- CDSS tools must integrate with EHR and clinic workflows.
- Prospective validation, including well-designed RCTs, is needed before claiming patient-outcome improvement.

Confidence: **High**

## Limitations / Cautions Stated By Authors

The review highlights several cautions:

| Caution | Meaning |
| --- | --- |
| Retrospective models need prospective validation | Many current AI studies are not enough for clinical adoption. |
| Geographic validation matters | Dosing and practice patterns vary by region. |
| Training/test leakage must be avoided | Cycles from the same patient should not appear across training and testing folds. |
| Black-box trust is a barrier | Clinicians prefer transparency, especially in healthcare decisions. |
| Workflow integration matters | CDSS must not reduce clinical efficiency. |
| AI conclusions may be correlational | Clinical inference must not be ignored. |
| Autonomous AI clinician remains contentious | AI should support, not replace, clinicians. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Review is broad | It supports framing but cannot prove one specific model gap alone. |
| No original dataset | It cannot be used as evidence of model performance. |
| Not India-specific | Indian validation remains unaddressed. |
| Review includes emerging ideas | Some areas such as LLMs and AI-omics are still experimental. |
| CDSS vision is future-oriented | It supports our direction but also shows that real deployment evidence is limited. |

Confidence: **High/Medium**

## Future Work Suggested

The review supports future work in:

- prospective validation of AI models in ART
- multicenter validation across geographies
- transparent and trustworthy CDSS development
- human-in-the-loop AI workflows
- EHR-integrated decision support
- federated learning for privacy-preserving multi-clinic collaboration
- clinically relevant outcome evaluation
- balancing automation with workforce training and clinical expertise

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need clinical decision support | Yes | CDSS and human-in-the-loop AI are central themes. |
| Need prospective validation | Yes | Review explicitly stresses prospective validation/RCTs. |
| Need external validation | Yes | Validation across geographies and clinics is emphasized. |
| Trustworthy AI gap | Yes | Black-box models, transparency, fairness and trust are discussed. |
| Workflow integration gap | Yes | CDSS must fit clinical workflow and EHR systems. |
| Multimodal/personalization gap | Yes | ART decisions involve multiple data types and sequential decisions. |
| Indian validation gap | Indirect | Review is not India-specific, but geographic validation argument supports local validation. |

## Usefulness For Our PhD

Relevance: **Very High**

This review is one of the strongest papers for justifying the overall PhD framing.

It supports the shift from:

> AI model for IVF prediction

to:

> explainable, personalized and clinically usable AI decision support for IVF.

It is especially useful in the thesis introduction and literature-review synthesis sections because it explains why validation, transparency, workflow integration and human oversight matter.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Hanassab et al. (2024) reviewed AI applications across assisted reproductive technology and argued that AI can support personalization across pre-treatment counseling, ovarian stimulation, trigger timing, gamete and embryo assessment, provided that models are validated, trustworthy and integrated into clinical workflows.

Gap-support sentence:

> The review emphasizes that retrospective AI models in ART require prospective and geographically diverse validation, transparent human-in-the-loop decision-support design and workflow integration before they can be responsibly adopted in routine fertility care.

## What This Paper Does Not Prove

This paper does not prove that:

- a specific IVF prediction model works better than another.
- AI improves live-birth rates in real clinics.
- AI-CDSS is already ready for autonomous clinical use.
- the reviewed evidence applies directly to Indian IVF clinics.
- black-box embryo AI is acceptable without explanation and validation.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Article type | High |
| Review scope | High |
| Key arguments | High |
| Future-work themes | High |
| Dataset/model metrics | Not applicable |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
