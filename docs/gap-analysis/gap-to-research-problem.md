# Gap to Research Problem Mapping

This page maps repeated gaps to the research problem, research questions and objectives.

## Gap-to-Problem Chain

| Repeated Gap | What It Shows | Research Problem Element |
| --- | --- | --- |
| External validation and generalizability | Models often work only in the dataset where they were developed. | Need a framework that includes validation beyond internal train-test performance. |
| Clinical decision-support translation | Prediction outputs are not enough for IVF clinicians. | Need clinician-facing decision support, not only a probability score. |
| Trustworthy and explainable AI | Black-box IVF recommendations are difficult to trust. | Need explanations that clinicians and patients can understand. |
| Multimodal personalization | IVF outcomes depend on clinical, embryological, imaging and lifestyle/contextual factors. | Need integrated data modeling rather than isolated single-modality prediction. |
| Indian/contextual validation | Most evidence is not India-specific. | Need Indian population adaptation or validation strategy. |
| Prospective/real-world usability | Retrospective accuracy does not prove clinical usefulness. | Need usability/deployment-oriented evaluation. |

## Refined Research Problem

Current AI models in IVF show promise for predicting clinical pregnancy, live birth, embryo quality and treatment response. However, the literature repeatedly shows that many models are retrospective, internally validated, population-specific, insufficiently explainable and weakly translated into clinical decision-support workflows.

This creates a gap for an explainable, personalized and clinically usable IVF decision-support framework that integrates multimodal patient, clinical, embryology and contextual data, and evaluates generalizability for Indian IVF settings.

## Refined Research Questions

RQ1. Which clinical, embryological, imaging and contextual factors are most useful for personalized IVF outcome prediction?

RQ2. Can a multimodal ML model improve IVF outcome prediction compared with single-modality or conventional models?

RQ3. How can XAI methods provide clinician-usable and patient-understandable explanations for IVF predictions?

RQ4. How well does the proposed model generalize across patient subgroups, clinics or Indian population data?

RQ5. How can predictive outputs be translated into a clinical decision-support workflow without replacing clinician judgment?

## Refined Objectives

1. Build a structured literature matrix and identify repeated gaps in AI-enabled IVF research.
2. Design a multimodal IVF outcome prediction framework using clinical, embryology and contextual variables.
3. Integrate explainable AI methods to identify patient-specific outcome drivers.
4. Evaluate predictive performance, calibration, subgroup behavior and generalizability.
5. Propose and evaluate a clinician-facing decision-support workflow for personalized IVF counseling.

## Contribution Boundary

The contribution should not be:

- only comparing classifiers
- only reporting higher accuracy
- only building a black-box prediction model

The contribution should be:

- explainable
- personalized
- clinically usable
- validation-aware
- relevant to Indian IVF context
