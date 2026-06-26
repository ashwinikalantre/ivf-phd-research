# Paper 30: ART Live-Birth Prediction Using Clinical Indicators

## Citation

Peng, J., Geng, X., Zhao, Y., Hou, Z., Tian, X., Liu, X., Xiao, Y., et al. (2024). **Machine learning algorithms in constructing prediction models for assisted reproductive technology (ART) related live birth outcomes**. *Scientific Reports*, 14, Article 32083.

DOI: [https://doi.org/10.1038/s41598-024-83781-x](https://doi.org/10.1038/s41598-024-83781-x)

Source checked: [Scientific Reports full text](https://www.nature.com/articles/s41598-024-83781-x)

Evidence note:

This is a full-text, open-access Scientific Reports paper. Extraction confidence is high because the abstract, methods, results, discussion, limitations and data availability sections were available.

Related study terms:

- [ART](../glossary/clinical-glossary.md#assisted-reproductive-technology)
- [IVF](../glossary/clinical-glossary.md#ivf)
- [ICSI](../glossary/clinical-glossary.md#icsi)
- [Live Birth](../glossary/clinical-glossary.md#live-birth)
- [FSH](../glossary/clinical-glossary.md#fsh)
- [Estradiol](../glossary/clinical-glossary.md#estradiol)
- [Progesterone](../glossary/clinical-glossary.md#progesterone)
- [LH](../glossary/clinical-glossary.md#lh)
- [HCG Day](../glossary/clinical-glossary.md#hcg-day)
- [Random Forest](../glossary/technical-glossary.md#random-forest)
- [XGBoost](../glossary/technical-glossary.md#xgboost)
- [LightGBM](../glossary/technical-glossary.md#lightgbm)
- [Calibration](../glossary/technical-glossary.md#calibration)
- [Brier Score](../glossary/technical-glossary.md#brier-score)
- [TRIPOD + AI](../glossary/technical-glossary.md#tripod-ai)

## Why This Paper Matters

This paper is useful because it compares traditional logistic regression with multiple machine learning algorithms for ART-related live-birth prediction in a large Chinese dataset.

The important lesson is not that complex ML always wins. In this study, logistic regression and Random Forest had similar performance, and the authors recommended logistic regression because it was simpler to fit.

For our PhD, this supports a careful research position:

- model complexity must be justified
- simple models should be strong baselines
- live birth is the preferred IVF outcome
- internal validation is not enough for clinical decision support
- important missing variables can limit prediction even in large datasets

## Research Objective

The study aimed to develop and internally validate prognostic prediction models for live birth among patients receiving ART, using easily obtainable demographic and clinical features at the beginning of IVF treatment.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Retrospective prediction-model study |
| Journal | Scientific Reports |
| Published | 30 December 2024 |
| Country | China |
| Institution | Second Affiliated Hospital of Kunming Medical University, Yunnan Province |
| Data period | January 2015 to December 2022 |
| Initial database | 13,620 patients who initiated first and subsequent IVF with ICSI treatment |
| Final analysis sample | 11,486 couples with complete information |
| Exclusions | ART initiation before study period, restarted ART after live birth, missing vital information, lost to follow-up for at least one year |
| Outcome | Live birth during a single ART cycle |
| Live-birth count | 3,097 couples |
| Live-birth rate | 26.96% |
| Reporting guideline | TRIPOD + AI |
| Data availability | Not publicly available for ethical reasons; available from corresponding authors on reasonable request |

Confidence: **High**

## Variables / Features Used

Candidate predictors included:

- couple's age
- ethnicity
- maternal BMI
- duration of infertility
- type of infertility
- cause of infertility
- previous ART cycles
- insemination method
- starting gonadotropin dosage
- duration of gonadotropin treatment
- total gonadotropin dosage
- basal FSH
- basal estradiol
- basal LH
- progressive sperm motility
- non-progressive sperm motility
- estradiol on HCG day
- LH on HCG day
- progesterone on HCG day

Final selected predictors:

| Predictor | Meaning |
| --- | --- |
| Maternal age | Female age at treatment |
| Duration of infertility | Years of infertility |
| Basal FSH | Ovarian reserve / stimulation-related hormone marker |
| Progressive sperm motility | Male-factor semen quality indicator |
| Progesterone on HCG day | Hormone value near trigger day |
| Estradiol on HCG day | Ovarian response-related hormone value |
| LH on HCG day | Hormone value near trigger day |

Confidence: **High**

## Method / Algorithm

The study used:

- descriptive statistics
- univariate logistic regression
- multivariate logistic regression
- Random Forest
- XGBoost
- LightGBM
- binary logistic regression prediction model
- tenfold cross-validation
- 500-times bootstrap validation

The authors first screened candidate predictors using logistic regression and variable importance scores from machine learning models. Variables ranked in the top six in at least two of three ML algorithms were selected.

Confidence: **High**

## Evaluation Metrics

The study used:

- AUROC for discrimination
- Brier score for calibration
- cross-validation
- bootstrap validation

Key reported performance:

| Model | Validation | AUROC | Brier Score |
| --- | --- | --- | --- |
| Logistic Regression | Tenfold cross-validation | 0.671, 95% CI 0.630-0.713 | 0.183, 95% CI 0.170-0.196 |
| Logistic Regression | Bootstrap | 0.671, 95% CI 0.662-0.683 | 0.183, 95% CI 0.179-0.187 |
| Random Forest | Cross-validation / bootstrap | Similar discrimination and calibration to logistic regression | Similar to logistic regression |

The abstract reports Random Forest AUROC 0.671 and logistic regression AUROC 0.674, with both Brier scores 0.183.

Confidence: **High**

## Main Findings

The study identified seven promising predictors for live birth:

- maternal age
- duration of infertility
- basal FSH
- progressive sperm motility
- progesterone on HCG day
- estradiol on HCG day
- LH on HCG day

Maternal age had the strongest association with live-birth outcome, followed by progesterone and estradiol on HCG day.

Random Forest performed slightly better than other ML models, but logistic regression performed similarly in discrimination and calibration. The authors recommended logistic regression because it is simpler and easier to fit.

The overall model discrimination was fair, not excellent.

Confidence: **High**

## Limitations Stated By Authors

| Limitation | Meaning |
| --- | --- |
| Overall discrimination was not high | AUROC around 0.67 suggests missing predictors and limited predictive strength. |
| AMH unavailable | An important ovarian reserve marker could not be included. |
| Embryo quality unavailable | A clinically important predictor was missing. |
| Baseline-only indicators | The model did not include time-varying factors across the IVF treatment pathway. |
| Single institution | Results may reflect one hospital's population and practice. |
| Retrospective design | Information bias and selection bias could not be avoided. |
| External validation needed | Authors recommend multicenter prospective studies. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| No Indian population | Findings may not transfer directly to Indian IVF clinics. |
| Modest AUROC despite large sample | Clinical variables alone may not be enough for strong live-birth prediction. |
| No lifestyle variables | Lifestyle, stress, sleep, diet, occupation and socioeconomic factors were not part of the final model. |
| No embryo-quality data | Missing embryo variables may reduce prediction quality. |
| No external validation | Internal validation cannot prove generalization. |
| No XAI workflow | Variable importance was used, but clinician-facing explanations were not the main focus. |
| No deployed CDSS | The study supports prediction, not full clinical decision-support implementation. |

Confidence: **High**

## Future Work Suggested

The authors recommend:

- longitudinal designs
- inclusion of more meaningful indicators
- multicenter prospective studies
- external validation of the findings

For our PhD, the paper also supports:

- adding AMH, embryo variables and lifestyle variables where available
- comparing simple and complex models fairly
- evaluating calibration, not only AUROC
- designing clinician-readable explanations
- testing generalization across Indian clinic settings

Confidence: **High** for author-stated future work and **Medium-High** for PhD interpretation.

## Gap Contribution

| Gap Category | Contribution |
| --- | --- |
| Need external validation | Strongly supported |
| Single-center study | Strongly supported |
| Retrospective design | Strongly supported |
| Missing embryo variables | Strongly supported |
| Missing AMH | Strongly supported |
| Lack of lifestyle data | Supported by absence from final model and candidate list |
| Lack of Indian population | Supported for Indian-context research |
| Need clinical decision support | Supported because model was not deployed as CDSS |
| Model complexity caution | Strongly supported because logistic regression matched ML performance |

## Usefulness For Our PhD

Usefulness: **High**

This paper is useful because it gives a strong methodological caution. A large dataset and several ML algorithms still produced only fair discrimination, and a simpler model was recommended.

For our thesis, this supports the argument that the research problem is not only “try a better algorithm.” The stronger problem is to build a clinically useful, explainable and validated decision-support framework using appropriate variables and proper validation.

## What This Paper Does Not Prove

This paper does not prove that:

- complex ML is superior to simpler statistical models
- the model works outside the source hospital
- the model works in Indian IVF populations
- baseline clinical variables alone are enough
- the model can guide treatment decisions in real clinical workflow

## Thesis-Ready Citation Sentences

Peng et al. (2024) developed and internally validated ART-related live-birth prediction models using 11,486 couples from a single Chinese medical institution and compared logistic regression, Random Forest, XGBoost and LightGBM.

The study found that logistic regression and Random Forest had similar predictive performance, with AUROC around 0.67 and Brier score 0.183, leading the authors to recommend logistic regression because of its simplicity.

The paper strengthens the gap for this PhD by showing that live-birth prediction remains limited by missing predictors, single-center retrospective design, lack of external validation and absence of important variables such as AMH and embryo quality.

## Source Confidence Summary

| Item | Confidence |
| --- | --- |
| Citation, authors, DOI, journal | High |
| Objective | High |
| Dataset and study design | High |
| Variables and final predictors | High |
| Algorithms and validation methods | High |
| Metrics and findings | High |
| Limitations and future work | High |
| PhD gap interpretation | High |
