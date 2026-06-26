# Paper 02: AI Decision Support for FSH Dose and Trigger Timing

## Citation

Canon, C., Leibner, L., Fanton, M., Chang, Z., Suraj, V., Lee, J. A., Loewke, K., & Hoffman, D. (2024). **Optimizing oocyte yield utilizing a machine learning model for dose and trigger decisions, a multi-center, prospective study**. *Scientific Reports*, 14, Article 18721.

DOI: [https://doi.org/10.1038/s41598-024-69165-1](https://doi.org/10.1038/s41598-024-69165-1)

Source checked: [Scientific Reports article page](https://www.nature.com/articles/s41598-024-69165-1)

Related study terms:

- [Oocyte](../glossary/clinical-glossary.md#oocyte)
- [Mature oocyte / metaphase-II oocyte](../glossary/clinical-glossary.md#mature-oocyte-metaphase-ii-oocyte)
- [Ovarian stimulation](../glossary/clinical-glossary.md#ovarian-stimulation)
- [Trigger day](../glossary/clinical-glossary.md#trigger-day)
- [AMH](../glossary/clinical-glossary.md#amh)
- [AFC](../glossary/clinical-glossary.md#afc)
- [Clinical decision support system](../glossary/technical-glossary.md#clinical-decision-support-system)
- [K-nearest neighbors](../glossary/technical-glossary.md#k-nearest-neighbors)
- [Propensity matching](../glossary/technical-glossary.md#propensity-matching)

## Why This Paper Matters

This paper is highly relevant because it evaluates an AI-powered clinical decision-support tool in actual IVF ovarian stimulation practice.

It is important for our PhD because it connects:

- ovarian stimulation
- starting FSH dose selection
- trigger timing
- clinician use of AI predictions
- prospective post-market evaluation
- clinical decision support

This paper is closer to real-world CDSS use than many purely retrospective prediction studies.

## Research Objective

The objective was to evaluate clinical outcomes for IVF patients when clinicians used an AI platform to help decide:

1. starting FSH dose
2. timing of trigger injection

The main comparison was between patients treated with AI-assisted clinician decision-making and historical matched controls treated by the same physicians without AI assistance.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Study design | Prospective observational post-market study with historical control arm |
| Country | United States |
| Centers | Two assisted reproductive technology treatment centers |
| Physicians | Four physicians |
| Treatment arm | 291 autologous IVF cycles where Stim Assist was used |
| Treatment period | December 2022 to April 2023 |
| Control arm | Historical matched patients treated by the same doctors without AI |
| Control period | September 2021 to September 2022 |
| Patient type | Conventional autologous IVF cycles |
| Excluded use context | Not intended for minimal stimulation IVF or natural cycle IVF |
| Model training data | LILY study data were not used for training or testing the AI models |
| Ethics | WCG IRB approval; patient information deidentified; consent waiver obtained |

Confidence: **High**

## AI Platform / Intervention

The study evaluated **Stim Assist**, a clinical decision-support software.

Stim Assist contains two tools:

| Tool | Purpose | Model Approach |
| --- | --- | --- |
| Starting Dose Tool | Helps choose starting FSH dose before ovarian stimulation | K-nearest-neighbors approach using similar historical patients |
| Trigger Tool | Helps decide whether to trigger today, tomorrow or in two days | Interpretable linear regression models using follicle sizes and estradiol |

The software did not force decisions. Clinicians could follow, ignore or use the prediction only as confirmation.

Confidence: **High**

## Variables / Features Used

### Starting Dose Tool

The Starting Dose Tool used:

- age
- BMI
- AMH
- AFC
- starting FSH dose
- historical patient-cycle data

It identified the 100 most similar historical patients from a dataset of more than 20,000 ovarian stimulation cycles.

### Trigger Tool

The Trigger Tool used:

- current estradiol level
- follicle measurements
- follicle-size bins
- timing options: trigger today, tomorrow or in two days

### Study Variables Collected

The study also recorded:

- MII oocytes
- total oocytes
- cycle length
- daily follicle sizes
- daily medications
- trigger injections
- total FSH used

Confidence: **High**

## Method / Algorithm

| Area | Method |
| --- | --- |
| Starting dose model | K-nearest-neighbors model using similar historical patients |
| Trigger model | Interpretable linear regression models |
| Missing baseline AMH/AFC imputation | KNN imputer trained on 23,000 prior IVF patients from the Starting Dose Tool dataset |
| Matching | 1-to-1 matching of treatment-arm patients to historical controls by physician |
| Matching variables | Age, baseline AMH, baseline AFC |
| Statistical comparison | Average outcomes compared between matched groups |
| Significance test | t-test |

Confidence: **High**

## Evaluation Metrics / Outcomes

| Outcome / Metric | Meaning |
| --- | --- |
| Average number of MII oocytes | Main outcome measure |
| Average number of oocytes retrieved | Secondary laboratory outcome |
| Total FSH used | Medication-use outcome |
| Trigger day | Timing-related outcome |
| p-value | Used to assess statistical significance between groups |
| Clinician agreement/disagreement survey | Measured whether predictions confirmed, changed or were ignored in clinician decisions |
| Adverse events / OHSS | Safety-related reporting |

Confidence: **High**

## Main Findings

The main treatment-versus-control findings were:

| Finding | Result |
| --- | --- |
| MII oocytes | 12.20 vs 11.24; improvement 0.96; p = 0.16 |
| Total oocytes retrieved | 16.01 vs 14.54; improvement 1.47; p = 0.08 |
| Total FSH used | 3671.95 IU vs 3846.29 IU; reduction 174.35 IU; p = 0.13 |
| Trigger day | 10.27 vs 10.00; treatment arm stimulated 0.27 days longer; p = 0.07 |
| Trigger Tool aligned subgroup | MII improvement 2.57; p = 0.02 |
| Safety | No reported OHSS cases in either treatment or control group |

Important interpretation:

The overall improvements showed a positive trend but were mostly **not statistically significant**. The subgroup triggered in accordance with Trigger Tool predictions showed a statistically significant MII improvement.

Confidence: **High**

## Clinician Use Findings

The study collected clinician feedback during tool use.

| Tool | Confirmed or changed decision | Disagreed / ignored | Prediction unavailable |
| --- | ---: | ---: | ---: |
| Starting Dose Tool | 63.1% | 32.4% | 4.5% |
| Trigger Tool | 78.4% | 17.0% | 4.6% |

In 55.7% of cycles, clinicians agreed with every Stim Assist prediction shown during the cycle. In 44.3% of cycles, clinicians disagreed with at least one prediction.

This is useful for our PhD because it shows that clinician interaction with AI output is not automatic acceptance. Clinical judgment remains active.

Confidence: **High**

## Limitations Stated by Authors

The authors clearly state these limitations:

| Limitation | Meaning |
| --- | --- |
| Only two clinics and four physicians | Generalizability is limited. |
| Limited sample size | Outcome differences did not reach statistical significance overall. |
| Historical control arm | Not the same strength as randomized concurrent control. |
| Future prospective studies needed | Larger multi-site studies with more physicians are needed. |
| Combined software evaluation | The study could not separate the individual effect of the Starting Dose Tool and Trigger Tool. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our research-analysis points, not unsupported criticism.

| Critical Point | Why It Matters |
| --- | --- |
| Not randomized | Prospective use is strong, but historical controls can introduce temporal and practice-change bias. |
| Commercial platform context | The study was funded by Alife Health, and several authors were employees or consultants. This does not invalidate the study, but should be transparently noted. |
| Intermediate outcome focus | MII oocyte count is important, but live birth was not the main endpoint. |
| No Indian validation | The study was conducted in two US clinics, so local Indian validation is not established. |
| Clinician usability measured only in limited form | Agreement/disagreement was collected, but broader usability, trust and explanation quality were not deeply evaluated. |
| Prescriptive AI not tested | Clinicians retained final decisions; the study did not test AI-set treatment decisions. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- larger prospective studies
- more sites and more physicians
- isolating the separate impact of Starting Dose Tool and Trigger Tool
- evaluating more prescriptive AI use
- studying medication dosing, patient complications such as OHSS, and patient outcomes when AI guidance is used differently

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need clinical decision support | Yes | This is a direct CDSS study in ovarian stimulation. |
| Need real-world deployment evidence | Yes | It provides prospective post-market evidence, but still early and limited. |
| Need larger prospective validation | Yes | Authors state larger future studies are needed. |
| Limited multi-center validation | Yes | Only two US clinics and four physicians. |
| Personalized treatment recommendation | Yes | Starting dose and trigger timing were personalized using patient data. |
| Indian validation gap | Yes | No Indian clinic validation. |
| Explainability/trust gap | Partial | The tools are described as interpretable, but clinician-facing explanation and trust evaluation are limited. |

## Usefulness For Our PhD

Relevance: **High**

This paper is very useful because it moves beyond retrospective model development and shows AI being used as adjunctive clinical decision support during IVF ovarian stimulation.

It strengthens our argument that the next research opportunity is not only building a prediction model, but designing and validating a clinician-usable AI decision-support framework.

It also gives a realistic caution: even prospective AI-CDSS use may show only trends unless sample size, outcome choice and validation design are strong.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Canon et al. (2024) prospectively evaluated the Stim Assist AI decision-support platform across two US IVF centers and reported that clinician use of AI-assisted FSH-dose and trigger-timing predictions showed trends toward improved mature oocyte yield and reduced FSH use compared with matched historical controls.

Gap-support sentence:

> Although the study provides important early real-world evidence for AI-assisted ovarian stimulation, its limited sample size, two-clinic setting, historical control design and intermediate outcome focus indicate that larger prospective validation and broader clinical utility evaluation remain necessary.

## What This Paper Does Not Prove

This paper does not prove that:

- AI independently improves IVF live-birth rates.
- AI should replace clinician decision-making.
- the tool generalizes to Indian IVF clinics.
- the Starting Dose Tool and Trigger Tool each independently caused the observed trends.
- clinician trust and patient acceptance are fully solved.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Study design and dataset | High |
| AI platform details | High |
| Variables/features | High |
| Methods/statistical analysis | High |
| Main findings | High |
| Author-stated limitations | High |
| Hidden limitations / our critical view | Medium/High |
| Connection to our PhD | High |
