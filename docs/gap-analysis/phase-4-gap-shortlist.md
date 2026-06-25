# Phase 4 Gap Shortlist

Phase 4 reduces the raw gap-frequency table into a smaller set of PhD-relevant gaps.

The goal is not to list every limitation. The goal is to identify repeated gaps that can support a defensible research problem.

## Raw Gap Pattern

The current matrix has 35 papers. The strongest raw gap frequencies are:

| Raw Gap | Frequency |
| --- | ---: |
| Need external validation | 26 |
| Need clinical decision support | 18 |
| Need real-world deployment evidence | 9 |
| Retrospective design | 9 |
| Trustworthy AI gap | 8 |
| Need prospective/RCT validation | 7 |
| Single-center study | 6 |
| Lack of standardization | 4 |
| Need multimodal data | 3 |
| Patient-centered XAI gap | 3 |
| Black-box/explainability gap | 3 |
| Clinical utility gap | 3 |

## Normalized PhD-Relevant Gaps

| Shortlisted Gap | Evidence Strength | Related Raw Gaps | Why It Matters |
| --- | --- | --- | --- |
| External validation and generalizability gap | Very strong | Need external validation, single-center study, limited multi-center validation, limited population diversity, Indian validation gap | Most IVF AI models cannot be trusted clinically unless they generalize beyond the source clinic/population. |
| Clinical decision-support translation gap | Very strong | Need clinical decision support, clinical utility gap, real-world deployment evidence gap, clinician usability evaluation | Many studies stop at prediction scores and do not become usable clinician-facing decision support. |
| Trustworthy and explainable AI gap | Strong | Trustworthy AI gap, black-box/explainability gap, patient-centered XAI gap, personalized explanation gap | IVF decisions are high-stakes, emotionally sensitive and expensive; opaque models are difficult to justify. |
| Multimodal personalization gap | Moderate-strong | Need multimodal data, personalized recommendation gap, no pre-transfer recommendation, selection bias | IVF outcomes depend on interacting clinical, embryology, imaging and contextual factors, but many models use narrow data. |
| Indian/contextual population gap | Moderate but locally important | No Indian population, limited population diversity, Indian subpopulation evidence, external validation gap | This gives the PhD local relevance, but needs careful data feasibility checking. |
| Prospective and real-world validation gap | Strong | Retrospective design, need prospective/RCT validation, real-world deployment evidence gap | Retrospective performance is not enough for clinical adoption or treatment recommendation. |

## Gaps to Use Carefully

| Gap | Reason |
| --- | --- |
| Small dataset | Important in some papers, but not enough alone for a PhD topic. |
| Lack of standardization | Useful for review framing, but too broad as the main implementation problem. |
| Disease-specific generalization | Useful for PCOS/endometriosis discussion, but too narrow unless data access exists. |
| Manual/subjective workflow bias | Useful in embryo grading and ultrasound themes, but should support the XAI/CDSS argument. |
| Need full-text verification | Workflow task, not a research gap. |

## Final Shortlist for Topic Development

The final gap shortlist should be:

1. External validation and generalizability.
2. Explainable and trustworthy AI.
3. Clinical decision-support translation.
4. Multimodal personalization.
5. Indian/contextual validation.
6. Prospective or real-world usability evaluation.

## Supervisor Interpretation

The evidence does not support a narrow title such as:

> Machine learning model for IVF success prediction.

That would only address a common prediction task.

The evidence supports a stronger and more defensible problem:

> IVF AI models often predict outcomes but are not sufficiently explainable, externally validated, personalized or translated into clinically usable decision support, especially for Indian/context-specific IVF settings.
