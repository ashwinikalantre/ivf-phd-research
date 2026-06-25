# Dataset Feasibility Decision

The final title depends on what data doctors and clinics can provide.

## Main Decision Questions

| Question | If Yes | If No |
| --- | --- | --- |
| Can we access IVF clinical data? | Basic study is feasible. | Topic cannot move forward yet. |
| Are embryo variables available? | We can use `multimodal clinical and embryological data`. | Use only `clinical data` in title. |
| Are lifestyle variables available? | We can include lifestyle personalization. | Keep lifestyle as future work. |
| Is more than one clinic available? | We can claim external validation. | Use internal validation only. |
| Can doctors review explanations? | We can evaluate CDSS usability. | Keep CDSS as proposed framework only. |

## Title Based on Dataset

| Dataset Available | Best Title Direction |
| --- | --- |
| Clinical data only | Explainable CDSS for IVF outcome prediction using clinical data |
| Clinical + embryo data | Explainable personalized CDSS using multimodal clinical and embryological data |
| Clinical + embryo + lifestyle data | Explainable multimodal CDSS using clinical, embryological and lifestyle data |
| Data from multiple clinics | Add external validation in Indian IVF settings |
| Clinician review possible | Add clinical usability evaluation objective |

## Minimum Dataset

Minimum required fields:

- patient age
- BMI
- infertility duration
- infertility diagnosis
- AMH
- AFC
- IVF/ICSI
- fresh/frozen transfer
- stimulation protocol
- endometrial thickness
- number of embryos transferred
- clinical pregnancy or live birth outcome

## Strong Dataset

Strong dataset includes minimum data plus:

- oocytes retrieved
- mature oocytes
- fertilization rate
- embryo grade
- blastocyst grade
- transfer day
- embryo freezing details

## Best Dataset

Best dataset includes strong dataset plus:

- lifestyle questionnaire
- stress/sleep/activity/diet data
- multiple clinics
- doctor review of model explanations

## Presentation Point

We are not fixing the final title today because data access is not confirmed.

We are presenting a strong working direction and a clear data-based decision plan.
