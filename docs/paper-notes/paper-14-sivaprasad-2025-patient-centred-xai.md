# Paper 14: Patient-Centred Explainability in IVF Outcome Prediction

## Citation

Sivaprasad, A., Reiter, E., McLernon, D., Tintarev, N., Bhattacharya, S., & Oren, N. (2025). **Patient-Centred Explainability in IVF Outcome Prediction**. arXiv preprint.

DOI: [https://doi.org/10.48550/arXiv.2506.18760](https://doi.org/10.48550/arXiv.2506.18760)

Source checked:

- [arXiv abstract page](https://arxiv.org/abs/2506.18760)
- arXiv PDF downloaded and text extracted locally

Evidence note:

This is an **arXiv preprint** submitted on 23 June 2025. The paper states that the version of record was accepted for presentation at AIIH 2025, but it should still be treated as lower evidence strength than a fully peer-reviewed journal article.

Related study terms:

- [Patient-centred explainability](../glossary/technical-glossary.md#patient-centred-explainability)
- [Human-centred AI](../glossary/technical-glossary.md#human-centred-ai)
- [Dialogue-based explanation](../glossary/technical-glossary.md#dialogue-based-explanation)
- [Risk communication](../glossary/technical-glossary.md#risk-communication)
- [Data shift](../glossary/technical-glossary.md#data-shift)
- [Model exclusion](../glossary/technical-glossary.md#model-exclusion)
- [Retrieval-Augmented Generation](../glossary/technical-glossary.md#retrieval-augmented-generation)

## Why This Paper Matters

This paper is important because it does not focus mainly on model accuracy.

It asks a different and highly relevant question:

> Do IVF patients or potential patients understand and trust prediction-tool outputs?

This is directly useful for our PhD because our proposed CDSS should be explainable not only to developers, but also to clinicians and possibly patients during counseling.

## Research Objective

The study evaluated the user interface of an IVF outcome prediction tool, focusing on understandability for patients or potential patients.

The authors aimed to identify explanation needs beyond standard model-feature explanations and explore whether dialogue-based interfaces could support personalized explanations.

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Human-computer interaction / XAI preprint |
| Tool evaluated | OPIS pre-IVF outcome prediction tool |
| Prediction target of OPIS | Probability of live birth following IVF at treatment stages |
| Feedback period | May 2020 to October 2024 |
| Feedback responses analysed | 62 responses from OPIS users |
| Feedback user types | 48 patients and 14 healthcare professionals |
| Final textual feedback analysis | 31 responses from 22 unique patients |
| Survey participants | 13 took survey; 2 excluded for no IVF experience |
| Included survey participants | 11 |
| Interview participants | 4 selected participants |
| Countries in survey | UK 9, Spain 1, India 1 |
| Data collected | Anonymous feedback, survey responses, semi-structured interviews |
| Medical data collected | No medical data collected in survey/interviews |

Confidence: **High**

## Tool Context

The study focused on the **pre-IVF OPIS tool**.

OPIS uses a discrete-time logistic regression model and considers factors such as:

- woman’s age
- infertility duration
- treatment type: IVF or ICSI
- year
- tubal factor infertility
- male factor infertility
- unexplained infertility
- anovulation
- previous pregnancy

The model had been externally validated with more recent data, but the user interface had not been evaluated or revised.

Confidence: **High**

## Method / Evaluation Design

The study had three parts:

| Part | Purpose |
| --- | --- |
| User feedback analysis | Analysed existing anonymous OPIS user feedback from 2020-2024 |
| Survey Part 1 | Evaluated understandability and trust in current OPIS UI |
| Survey Part 2 | Explored user explanation needs using an adapted XAI question bank |
| Semi-structured interviews | Collected deeper feedback on trust, probability interpretation and dialogue-based explanation expectations |

Additional details:

- participants were recruited through fertility support groups in the UK
- trust was measured using a three-point scale
- understandability was measured through perceived ratings and task-based questions
- demographic and numeracy information were collected
- interview responses were manually analysed for data security

Confidence: **High**

## Evaluation Metrics / Measures

The study evaluated:

- perceived understandability
- task-based understandability
- trust score
- user-friendliness
- explanation needs
- qualitative concerns about model reasoning and exclusions
- interview themes

Confidence: **High**

## Main Findings

### OPIS feedback analysis

| User Type | UF Description | UF Input | UF Result | Understandability |
| --- | ---: | ---: | ---: | ---: |
| Healthcare professionals | 92% | 77% | 100% | 100% |
| Patients | 91% | 89% | 85% | 78% |

Important finding:

- 15% of patients rated result presentation as not user-friendly.
- 22% of patients reported difficulty understanding results.

### Survey findings

Included survey participants:

- 11 participants after excluding two without IVF experience
- 9 from UK, 1 from Spain, 1 from India
- numeracy levels varied from high to low

Reported measures:

- normalized perceived understandability: 0.86
- task-based understandability score: 0.76
- perceived understandability had positive correlation with trust score: 0.75

The authors did not report demography-specific analysis because the sample size was low.

### Explanation needs

Users wanted explanations beyond model feature importance. They asked about:

- model accuracy
- whether the tool works for standard versus non-standard cases
- data shifts
- who was excluded from the model
- why some factors were not included
- how to interpret probability outputs
- whether the model was relevant to their individual circumstances

Confidence: **High**

## Limitations Stated / Evident From Paper

| Limitation | Meaning |
| --- | --- |
| Preprint status | Not yet equivalent to a peer-reviewed journal article. |
| Small survey sample | Only 11 survey participants after exclusions. |
| Low interview sample | Four interview participants. |
| Recruitment through support groups | Participants may not represent all IVF patients. |
| Mobile compatibility issues | Lower participation and accessibility problems were reported. |
| No medical data collected | Study evaluates explanation needs, not prediction accuracy. |
| UI-specific study | Findings are tied to OPIS and may not directly generalize to all IVF tools. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Patient-centered, not clinician-centered | Useful for patient explanations, but our CDSS may first need clinician-facing evaluation. |
| Preprint evidence level | Use carefully as supporting evidence, not as a core clinical-effectiveness paper. |
| Small and educated sample | Many participants had bachelor/master/PhD education, which may overestimate understandability. |
| Mostly UK participants | Only one participant from India; Indian patient understanding is not established. |
| Interface-level evaluation | Does not validate a new IVF prediction model. |
| RAG/dialogue proposal is future work | Dialogue-based explanation is proposed, not fully validated as a deployed solution. |

Confidence: **High/Medium**

## Future Work Suggested

The paper supports future work in:

- dialogue-based explanation interfaces
- personalized explanations for IVF prediction tools
- user-centered XAI evaluation
- explanation beyond model feature space
- better communication of data shift and model exclusions
- grounding LLM/RAG explanations in curated factual data
- evaluating trust and understandability with larger and more diverse patient groups

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Patient-centered XAI gap | Yes | This is the central contribution. |
| Need personalized explanations | Yes | Users wanted explanations relevant to their situation. |
| Trustworthy AI gap | Yes | Trust was affected by data shift, exclusions and explainability limitations. |
| Need usability evaluation | Yes | UI understandability and trust were evaluated directly. |
| Clinical decision support gap | Partial | Focus is patient-facing prediction interface, not full clinical CDSS. |
| Indian validation gap | Limited | One survey participant from India, but no India-specific evaluation. |

## Usefulness For Our PhD

Relevance: **Medium-High**

This paper is very useful for the explainability and trust part of our PhD.

It shows that users need explanations beyond:

> “Feature X increased your score.”

They also want to know:

- whether the model applies to people like them
- what data the model used
- who was excluded
- how accurate the model is
- what the probability means in real life

For our work, this suggests that if we build a CDSS prototype, the explanation layer should include not only SHAP-style feature importance but also plain-language model scope, uncertainty, limitations and data applicability.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Sivaprasad et al. (2025) evaluated the understandability and trust of a patient-facing IVF outcome prediction interface using OPIS feedback, survey responses and interviews, finding that users require explanations beyond model feature importance, including information about data shifts, exclusions and applicability to individual circumstances.

Gap-support sentence:

> The study supports the need for patient-centred and dialogue-oriented explainability in IVF prediction tools, but its preprint status, small survey/interview sample and UK-dominant participant group mean that broader validation is still required.

## What This Paper Does Not Prove

This paper does not prove that:

- a new IVF prediction model performs well.
- dialogue-based explainers improve clinical outcomes.
- patient-centered explanations work equally well in Indian IVF settings.
- SHAP or feature importance alone is enough for patient trust.
- all IVF patients understand prediction probabilities similarly.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Preprint status | High |
| Feedback/survey/interview counts | High |
| OPIS model description | High |
| Main findings | High |
| Limitations/future work | High |
| Generalizability to Indian patients | Low |
| Connection to our PhD | High |
