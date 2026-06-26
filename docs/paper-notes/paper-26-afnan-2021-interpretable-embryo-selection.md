# Paper 26: Interpretable AI Should Be Used for Embryo Selection

## Citation

Afnan, M. A. M., Liu, Y., Conitzer, V., Rudin, C., Mishra, A., Savulescu, J., & Afnan, M. (2021). **Interpretable, not black-box, artificial intelligence should be used for embryo selection**. *Human Reproduction Open*, 2021(4), hoab040.

DOI: [https://doi.org/10.1093/hropen/hoab040](https://doi.org/10.1093/hropen/hoab040)

Source checked: [Oxford Academic full text](https://academic.oup.com/hropen/article/2021/4/hoab040/6415831)

Evidence note:

This is a conceptual, ethical and methodological paper. It does not develop a dataset or train a new prediction model. Its value for our PhD is in framing why IVF-AI systems should be interpretable, rigorously evaluated and responsibly governed before clinical use.

Related study terms:

- [Embryo grading](../glossary/technical-glossary.md#embryo-grading)
- [Black-Box AI](../glossary/technical-glossary.md#black-box-ai)
- [Explainable AI](../glossary/technical-glossary.md#explainable-ai)
- [Interpretable Model](../glossary/technical-glossary.md#interpretable-model)
- [Trustworthy AI](../glossary/technical-glossary.md#trustworthy-ai)
- [Shared Decision-Making](../glossary/technical-glossary.md#shared-decision-making)
- [Responsibility Gap](../glossary/technical-glossary.md#responsibility-gap)
- [Regulatory Oversight](../glossary/technical-glossary.md#regulatory-oversight)
- [Long-Term Follow-Up](../glossary/technical-glossary.md#long-term-follow-up)

## Why This Paper Matters

This paper is very important for our PhD because it explains why high AI accuracy is not enough in embryo selection.

The authors argue that black-box embryo-selection AI raises:

- trust problems
- poor generalization risk
- hidden confounding
- bias and value-misalignment risks
- economic concerns for clinics
- shared decision-making concerns
- responsibility gaps when decisions go wrong
- risk of more paternalistic decision-making

This paper helps us justify why our final work should include explainability, clinician oversight and validation, not only prediction performance.

## Research Objective

The paper aimed to argue that AI used for embryo selection should be interpretable rather than black-box, and should be rigorously evaluated before implementation.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Conceptual / ethical / methodological review |
| Journal | Human Reproduction Open |
| Published | 2 November 2021 |
| Dataset | No original dataset |
| Model training | No new model trained |
| Literature search | MEDLINE, Embase and Google Scholar up to February 2021 |
| Main domain | AI for embryo selection in IVF |
| Main recommendation | Use interpretable models and evaluate rigorously before implementation |

Confidence: **High**

## Variables / Features Used

Not applicable.

The paper discusses embryo-selection AI generally, including:

- embryo images
- time-lapse imaging
- embryo morphology
- embryo quality categories
- implantation, fetal heartbeat and live birth as possible outcomes
- patient values and ethical considerations

Confidence: **High**

## Method / Algorithm

Not applicable as an implementation paper.

The paper discusses:

- black-box computer vision models
- neural networks
- interpretable machine-learning models
- interpretable feature-based approaches
- limitations of post-hoc explanations for black-box models

Confidence: **High**

## Evaluation Metrics

The paper critiques overreliance on:

- accuracy
- ROC-AUC
- agreement with embryologist grading

The authors emphasize that the clinically relevant task is not simply separating clearly good and clearly poor embryos. The real clinical need is choosing between embryos of similar apparent quality.

Confidence: **High**

## Main Findings / Arguments

| Argument | Meaning |
| --- | --- |
| No RCTs were published at the time | AI embryo selection lacked strong clinical-trial evidence up to February 2021. |
| High AUC can be misleading | Some models distinguish obvious good/poor embryos rather than the difficult clinical decision among similar-quality embryos. |
| Most models were black-box | Opaque models create epistemic and ethical problems. |
| Black-box AI may generalize poorly | Confounders and setting-specific artifacts may not be detected. |
| Post-hoc explanations may be unreliable | Explaining a black-box model is not the same as using an inherently interpretable model. |
| Shared decision-making may be harmed | Patients and clinicians may not understand why an embryo is selected. |
| Long-term follow-up is needed | Child health and well-being after AI-selected embryo transfer should be monitored. |
| Data/code transparency is recommended | Public data and code can support independent validation. |

Confidence: **High**

## Limitations Stated / Scope Limits

This paper is not designed to:

- provide a new predictive model
- provide a quantitative meta-analysis
- provide new clinical outcome data
- test a deployed embryo-selection system
- evaluate Indian IVF data

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Conceptual paper | It supports framing but cannot be used as empirical performance evidence. |
| Embryo-selection focus | It does not directly address ovarian stimulation or FET CDSS, though principles transfer. |
| Published in 2021 | Later RCT evidence now exists, so we must combine it with newer trials such as Paper 28. |
| Strong interpretability preference | In some settings, accurate black-box models plus strong validation may still be debated; we should present this as an ethical argument, not universal proof. |

Confidence: **High**

## Future Work Suggested

The authors recommend:

- use of interpretable AI models for embryo selection
- rigorous randomized controlled trials before implementation
- long-term follow-up of children born after AI-assisted embryo selection
- regulatory oversight
- public availability of data and code
- independent reproduction and validation of models

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Black-box / explainability gap | Yes | Central argument of the paper. |
| Trustworthy AI gap | Yes | Covers trust, bias, oversight, responsibility and governance. |
| Need prospective/RCT validation | Yes | Authors explicitly recommend RCTs. |
| Patient-centered XAI gap | Yes | Shared decision-making and patient values are discussed. |
| Need regulatory oversight | Yes | Authors recommend regulatory oversight before implementation. |
| Need long-term follow-up | Yes | Child outcomes after AI-selected embryos should be followed. |
| Data/code transparency gap | Yes | Authors recommend public availability for independent validation. |

## Usefulness For Our PhD

Relevance: **Very High for conceptual framing**

This paper helps us defend why our PhD should not be only:

- model accuracy
- AUC comparison
- black-box prediction
- embryo or patient ranking

It supports designing a system that includes:

- explainable outputs
- clinician oversight
- patient-value awareness
- transparent limitations
- validation before deployment
- clear responsibility boundaries

Even if our final topic focuses on IVF treatment recommendation rather than embryo selection, the same trustworthy-AI principles apply.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Afnan et al. (2021) argued that black-box AI for embryo selection raises epistemic and ethical concerns, including poor generalization, hidden confounding, compromised shared decision-making, responsibility gaps and patient-value misrepresentation, and therefore recommended interpretable models, RCT evaluation, regulatory oversight and long-term follow-up before clinical implementation.

Gap-support sentence:

> This critique supports the need for trustworthy and explainable IVF-AI systems that assist clinicians without replacing transparent clinical reasoning or patient-centered decision-making.

## What This Paper Does Not Prove

This paper does not prove that:

- interpretable models always outperform black-box models.
- any specific IVF-AI model is unsafe.
- embryo-selection AI cannot be useful.
- an empirical CDSS has been validated.
- the argument directly applies to Indian clinics without local context.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation and DOI | High |
| Article type | High |
| Main arguments | High |
| Recommendations | High |
| Dataset/model details | Not applicable |
| Empirical performance evidence | Not applicable |
