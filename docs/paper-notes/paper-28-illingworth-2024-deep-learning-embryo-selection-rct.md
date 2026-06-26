# Paper 28: Deep Learning Versus Manual Morphology for Embryo Selection

## Citation

Illingworth, P. J., Venetis, C., Gardner, D. K., Nelson, S. M., Berntsen, J., Larman, M. G., Agresta, F., Ahitan, S., Ahlström, A., Cattrall, F., Cooke, S., Demmers, K., Gabrielsen, A., Hindkjær, J., Kelley, R. L., Knight, C., Lee, L., Lahoud, R., Mangat, M., Park, H., Price, A., Trew, G., Troest, B., Vincent, A., Wennerström, S., Zujovic, L., & Hardarson, T. (2024). **Deep learning versus manual morphology-based embryo selection in IVF: a randomized, double-blind noninferiority trial**. *Nature Medicine*, 30, 3114-3120.

DOI: [https://doi.org/10.1038/s41591-024-03166-5](https://doi.org/10.1038/s41591-024-03166-5)

Source checked: [Nature Medicine full text](https://www.nature.com/articles/s41591-024-03166-5)

Evidence note:

This is one of the strongest empirical papers in our review because it is a multicenter randomized double-blind noninferiority trial. It is especially important because it tests AI embryo selection prospectively rather than relying on retrospective performance.

Related study terms:

- [Blastocyst](../glossary/clinical-glossary.md#blastocyst)
- [Time-lapse system](../glossary/clinical-glossary.md#time-lapse-system)
- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [Live birth](../glossary/clinical-glossary.md#live-birth)
- [Frozen embryo transfer](../glossary/clinical-glossary.md#frozen-embryo-transfer)
- [Embryo grading](../glossary/technical-glossary.md#embryo-grading)
- [Noninferiority Trial](../glossary/technical-glossary.md#noninferiority-trial)
- [Double-Blind Trial](../glossary/technical-glossary.md#double-blind-trial)
- [Intention-to-Treat Analysis](../glossary/technical-glossary.md#intention-to-treat-analysis)
- [Per-Protocol Analysis](../glossary/technical-glossary.md#per-protocol-analysis)
- [Hawthorne Effect](../glossary/technical-glossary.md#hawthorne-effect)

## Why This Paper Matters

This paper is highly important because it tests whether deep-learning embryo selection can perform at least as well as standard embryologist morphology assessment in a real randomized clinical trial.

It is useful for our PhD because it shows:

- retrospective AI performance is not enough
- prospective randomized evidence can give different conclusions
- AI may improve workflow speed without improving pregnancy/live-birth outcomes
- clinical utility must be tested directly
- embryo-selection AI should be discussed carefully, not assumed superior

This paper strongly supports our cautious thesis stance: AI should support clinical decision-making only after strong validation.

## Research Objective

The study aimed to determine whether selection of a single blastocyst for transfer using the iDAScore deep-learning algorithm was noninferior to trained embryologists using standard morphology criteria and a predefined prioritization scheme.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Randomized clinical trial |
| Trial design | Multicenter, randomized, double-blind, noninferiority, parallel-group trial |
| Journal | Nature Medicine |
| Published | 9 August 2024 |
| Clinics | 14 IVF clinics |
| Countries/regions | Australia and Europe |
| Participants included | 1,066 patients |
| iDAScore group | 533 patients |
| Morphology control group | 533 patients |
| Per-protocol analysis | 1,002 participants after excluding 64 protocol violations |
| Eligibility | Women under 42 years with at least two early-stage blastocysts on day 5 |
| Trial registration | Australian New Zealand Clinical Trials Registry, 379161 |
| Primary endpoint | Clinical pregnancy rate with 5% noninferiority margin |

Confidence: **High**

## Variables / Features Used

The iDAScore system used:

- time-lapse embryo images
- spatial/morphological patterns
- temporal/morphokinetic patterns
- blastocyst development information up to day 5/day 6

Control arm used:

- standard morphology-based embryo assessment
- predefined prioritization scheme based on Gardner grading

Confidence: **High**

## Method / Algorithm

| Component | Extracted Information |
| --- | --- |
| AI system | iDAScore |
| Method type | Deep learning embryo selection |
| Comparator | Manual morphology-based assessment by embryologists |
| AI input | Time-lapse embryo images and development patterns |
| Transfer approach | Selection of a single blastocyst for transfer |
| Human input | iDAScore reduces need for manual input compared with traditional morphology workflow |

Confidence: **High**

## Evaluation Metrics

The study evaluated:

- clinical pregnancy rate
- risk difference and confidence interval
- rate ratio
- positive hCG rate
- nonviable intrauterine pregnancy
- ongoing pregnancy rate
- live-birth rate
- evaluation time
- adverse medical events
- subgroup and sensitivity analyses

Confidence: **High**

## Main Findings

Primary outcome:

| Outcome | iDAScore Group | Morphology Group |
| --- | ---: | ---: |
| Clinical pregnancy rate | 46.5% (248/533) | 48.2% (257/533) |
| Risk difference | -1.7 percentage points | 95% CI: -7.7 to 4.3 |
| Rate ratio | 0.96 | 95% CI: 0.85 to 1.10 |
| P value | 0.62 |  |
| Noninferiority conclusion | Not demonstrated |  |

Secondary outcomes:

| Outcome | iDAScore Group | Morphology Group |
| --- | ---: | ---: |
| Live-birth rate | 39.8% (212/533) | 43.5% (232/533) |
| Live-birth risk difference | -3.9% | 95% CI: -9.9 to 2.2; p = 0.24 |
| Evaluation time | 21.3 ± 18.1 seconds | 208.3 ± 144.7 seconds |
| Evaluation time p value | p < 0.001 |  |
| Medical adverse events | None recorded |  |

Additional findings:

- Results were similar in intention-to-treat, per-protocol and adjusted analyses.
- Clinical pregnancy outcomes varied by fresh versus freeze-all cycles.
- iDAScore and morphology selected the same embryo in 65.8% of study-arm participants.
- Where different embryos were selected, clinical pregnancy rates were 48.3% for same-selection cases and 44.7% for different-selection cases.
- No significant difference in male-to-female ratio was found.

Confidence: **High**

## Limitations Stated By Authors

| Limitation / Issue | Meaning |
| --- | --- |
| Noninferiority not demonstrated | The trial could not conclude iDAScore was noninferior for clinical pregnancy. |
| Control pregnancy rate higher than expected | Control group clinical pregnancy rate was 48.2%, higher than expected 35.4%, affecting trial power. |
| Primary outcome was clinical pregnancy | Live birth was reported as secondary, not primary. |
| Fresh vs frozen inconsistency | iDAScore performed differently between fresh and freeze-all cycles. |
| Cost-effectiveness not established | Workflow time savings need formal economic evaluation. |
| Future trials may require very large sample sizes | Authors estimated around 7,800 participants may be needed for similar noninferiority detection under observed rates. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Strong RCT but negative/non-confirmatory result | This balances retrospective AI optimism. |
| AI improved speed, not outcome | Workflow efficiency is useful but different from clinical success. |
| Live birth was not the primary endpoint | Clinical pregnancy is useful but not the final IVF outcome. |
| Deep learning remains relatively black-box | Trial evidence helps, but explainability/trust remains relevant. |
| Time-lapse infrastructure required | Not all clinics, especially smaller Indian clinics, may have compatible infrastructure. |
| Fresh/frozen subgroup uncertainty | FET behavior may differ and needs further investigation. |
| No Indian population | Generalization to Indian IVF clinics is not established. |

Confidence: **High**

## Future Work Suggested

The paper supports:

- future RCTs with appropriate sample size
- subgroup investigation for fresh versus frozen embryo transfer
- formal cost-effectiveness analysis
- continued evaluation of clinical utility beyond retrospective grading performance
- assessment of how standardized embryo assessment affects outcomes
- further validation before broad routine deployment

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need prospective/RCT validation | Yes | This paper provides RCT evidence and shows why it matters. |
| Clinical utility gap | Yes | Deep learning did not demonstrate noninferiority for clinical pregnancy. |
| Real-world deployment evidence | Partial | Trial context is stronger than retrospective evidence but still not routine deployment. |
| Trustworthy AI gap | Yes | Results show that AI claims need rigorous evaluation. |
| Cost-effectiveness gap | Yes | Time savings require formal economic evaluation. |
| Fresh/FET generalization issue | Yes | Performance differed across fresh and freeze-all subgroups. |
| Lack of Indian population | Yes | Trial was in Australia and Europe. |

## Usefulness For Our PhD

Relevance: **Very High**

This paper is essential for our literature review because it prevents overclaiming. It shows that even a mature AI embryo-selection system can fail to demonstrate noninferiority in a rigorous trial.

For our PhD, it supports:

- careful distinction between retrospective AUC and clinical utility
- need for clinician-facing validation
- conservative framing of AI as decision support
- importance of final clinical outcomes
- need for subgroup and workflow analysis
- need to evaluate efficiency separately from success rate

It also strengthens our argument that a PhD topic should focus on trustworthy, explainable, validated decision support rather than simply “AI improves IVF.”

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Illingworth et al. (2024) conducted a multicenter randomized double-blind noninferiority trial across 14 IVF clinics comparing iDAScore deep-learning embryo selection with standard morphology assessment in 1,066 patients and found clinical pregnancy rates of 46.5% versus 48.2%, failing to demonstrate noninferiority of deep learning.

Gap-support sentence:

> Although iDAScore reduced embryo evaluation time nearly tenfold, live-birth rates were similar and noninferiority for clinical pregnancy was not established, demonstrating that IVF-AI systems require prospective clinical validation before claims of clinical benefit.

## What This Paper Does Not Prove

This paper does not prove that:

- deep learning embryo selection improves clinical pregnancy or live birth.
- iDAScore is superior to trained embryologists.
- AI embryo selection is useless in all contexts.
- time savings alone justify clinical adoption.
- the results generalize to Indian IVF clinics.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation and DOI | High |
| Study design | High |
| Dataset/sample size | High |
| Primary and secondary outcomes | High |
| Limitations/discussion | High |
| Relevance to our gap analysis | High |
