# Panel Question Bank Stage 9

Stage 9 is the final claim audit before faculty or doctor discussion.

The purpose is to remove weak claims, stale numbers and unsupported promises.

## Stage 9 Rule

If a statement cannot be supported by a reviewed paper, reliable statistics source or confirmed clinic data, do not present it as fact.

Use one of these labels:

- **Confirmed**
- **Conditional**
- **Not yet claimable**
- **Needs re-check before presentation**

## Final Claim Audit

| Claim | Status | Safe Wording |
| --- | --- | --- |
| IVF is an important healthcare domain. | Confirmed | IVF is clinically important and decision-heavy. |
| AI/ML is actively studied in IVF. | Confirmed | Recent literature includes AI/ML for IVF outcome prediction, embryo selection, stimulation and XAI. |
| Prediction alone is not enough for novelty. | Confirmed | Many studies already perform prediction; the stronger gap is explainable, validated and clinician-usable support. |
| External validation is a repeated gap. | Confirmed | External validation appears repeatedly across the reviewed matrix, but exact count should be re-checked before presentation. |
| Indian validation is limited. | Confirmed | Indian IVF-AI evidence is limited, but not absent. Paper 29 uses Indian data. |
| Lifestyle data improves IVF prediction. | Not yet claimable | Lifestyle data can be tested only if reliable variables are available. |
| XAI improves doctor trust. | Not yet claimable | XAI can be evaluated for clinician usefulness if doctors review explanation outputs. |
| AI will improve IVF success rate. | Not yet claimable | AI may support prediction and counseling; outcome improvement requires prospective validation. |
| The model will work for all Indian IVF clinics. | Not yet claimable | Generalization can be claimed only if independent validation data supports it. |
| The final title is fixed. | Not yet claimable | The current title is provisional and depends on data access. |

## Numbers To Re-Check Before Presentation

| Number / Statistic | Current Use | Re-check Source |
| --- | --- | --- |
| Total reviewed papers | Used to say "35 paper notes" | Paper Reading Notes index |
| Gap frequency counts | Used for repeated-gap discussion | Latest literature matrix and gap-frequency page |
| IVF clinic count in India | Used only cautiously | Official National ART & Surrogacy Registry or current government source |
| IVF success rate by age | Used for age/success questions | HFEA/CDC/SART or selected official source |
| Indian infertility prevalence | Used for context | Peer-reviewed NFHS-based source |
| IVF cost/economic burden | Used for access discussion | HTAIn/ICMR-NIRRCH or reliable policy source |

## Known Audit Cautions

| Area | Caution |
| --- | --- |
| Gap-frequency table | Some counts may reflect earlier labels. Before final presentation, regenerate or manually re-check against the latest literature matrix. |
| Paper 29 Indian data | Do not say "no Indian data exists." Say Indian evidence is limited and needs broader validation. |
| Paper 32 and Paper 34 | Use mainly for framing because full-text details were limited or subscription-gated during review. |
| Lifestyle claims | Keep conditional unless lifestyle data is collected and analyzed. |
| External validation | Do not claim it unless independent data exists. |
| Clinical deployment | Do not claim deployment unless the system is actually used in a clinic under approval. |

## Final Title Audit

Before finalizing the title, check:

| Title Phrase | Allowed Only If |
| --- | --- |
| `multimodal` | At least two meaningful data modalities are available. |
| `embryological data` | Structured embryo/oocyte/fertilization variables are available. |
| `lifestyle data` | Lifestyle variables are reliably collected and ethically approved. |
| `external validation` | Independent clinic/source/time validation is available. |
| `Indian IVF settings` | Indian clinic data is used. |
| `clinical decision support` | Output is framed for doctors and not only model metrics. |
| `clinician-reviewed` | Doctors actually review outputs. |
| `live birth prediction` | Live-birth follow-up is reliable. |

## Final Hypothesis Audit

| Hypothesis Type | Safe Only If |
| --- | --- |
| Clinical variables predict outcome | Clinical variables and reliable outcome exist. |
| Embryology improves prediction | Clinical-only and clinical+embryology models can be compared. |
| Lifestyle improves prediction | Reliable lifestyle variables exist. |
| XAI improves clinician usefulness | Clinician review is performed. |
| External validation succeeds | Independent validation data exists. |
| Model improves IVF success | Prospective intervention study is performed. |

## Final Methodology Audit

| Method Claim | Audit Question |
| --- | --- |
| Logistic regression baseline | Is it included before complex ML? |
| ML comparison | Are model choices justified by data size/type? |
| Deep learning | Is image/video or large-scale data available? |
| Calibration | Are predicted probabilities checked, not only AUC? |
| Missing data | Is missingness reported before imputation? |
| Data leakage | Are future/post-outcome variables excluded from early prediction tasks? |
| External validation | Is the validation source truly independent? |
| XAI | Is it described as interpretation, not causality? |
| CDSS | Is it framed as doctor support, not decision automation? |

## Final Defense Checklist

Before the panel, the student should be able to answer:

| Question | Ready? |
| --- | --- |
| Why IVF? | Yes |
| Why AI in IVF? | Yes |
| Why not only prediction? | Yes |
| What are the repeated gaps? | Yes, with count re-check |
| What is the working direction? | Yes |
| Why is the title provisional? | Yes |
| What dataset is needed? | Yes |
| What if embryo data is missing? | Yes |
| What if lifestyle data is missing? | Yes |
| What if external validation is impossible? | Yes |
| What is the methodology? | Yes |
| What are unsafe claims? | Yes |

## Stop Or Continue Decision

| Situation | Decision |
| --- | --- |
| Faculty presentation is near | Stop adding new pages; practice Stage 7. |
| Doctor meeting is next | Use Stage 3, Stage 4 and data collection framework. |
| More literature questions expected | Review paper notes and literature matrix. |
| More statistics questions expected | Review key statistics and source-quality pages. |
| Data access is confirmed | Move from panel preparation to final title/objective refinement. |

## Final Safe Closing

Use this if the panel asks whether the PhD is ready:

> The literature-backed direction is ready, but the final PhD title should be fixed only after clinic data feasibility is confirmed. I have identified the repeated gaps, prepared dataset scenarios, mapped variables, created conditional research questions and planned a methodology that avoids unsupported claims.

## Stage 9 Completion Check

Stage 9 is complete when:

- unsupported claims are blocked
- stale numbers are marked for re-check
- title words are tied to data availability
- hypotheses are tied to testable data
- methodology claims are tied to validation level
- the student knows when to stop polishing and move to clinic confirmation
