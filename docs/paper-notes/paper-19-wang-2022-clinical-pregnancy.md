# Paper 19: Clinical Pregnancy Prediction Using IVF Clinical Features

## Citation

Wang, C.-W., Kuo, C.-Y., Chen, C.-H., Hsieh, Y.-H., & Su, E. C.-Y. (2022). **Predicting clinical pregnancy using clinical features and machine learning algorithms in in vitro fertilization**. *PLOS ONE*, 17(6), e0267554.

DOI: [https://doi.org/10.1371/journal.pone.0267554](https://doi.org/10.1371/journal.pone.0267554)

Source checked: [PLOS ONE full article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0267554)

Evidence note:

This paper predicts **clinical pregnancy**, not live birth. It is useful for IVF outcome modeling and variable interpretation, but it should not be cited as live-birth prediction evidence.

Related study terms:

- [Clinical pregnancy](../glossary/clinical-glossary.md#clinical-pregnancy)
- [IVF](../glossary/clinical-glossary.md#ivf)
- [ICSI](../glossary/clinical-glossary.md#icsi)
- [Frozen embryo transfer](../glossary/clinical-glossary.md#frozen-embryo-transfer)
- [Ovarian stimulation](../glossary/clinical-glossary.md#ovarian-stimulation)
- [Random Forest](../glossary/technical-glossary.md#random-forest)
- [Logistic Regression](../glossary/technical-glossary.md#logistic-regression)
- [missForest](../glossary/technical-glossary.md#missforest)
- [Partial Dependence Plot](../glossary/technical-glossary.md#partial-dependence-plot)
- [Mean Decrease Accuracy](../glossary/technical-glossary.md#mean-decrease-accuracy)
- [Sensitivity](../glossary/technical-glossary.md#sensitivity)
- [Specificity](../glossary/technical-glossary.md#specificity)
- [AUC](../glossary/technical-glossary.md#auc)

## Why This Paper Matters

This paper is useful because it uses a large hospital-linked IVF/ICSI dataset and compares Random Forest with Logistic Regression for clinical pregnancy prediction.

It is especially relevant for our work because it:

- uses routinely collected clinical and treatment variables
- reports an independent later test set from 2020-2021
- uses Random Forest variable importance
- uses partial dependence plots to interpret variable effects
- explicitly identifies missing lifestyle and clinical details as limitations

This makes it useful for both dataset planning and gap analysis.

## Research Objective

The study aimed to use machine-learning algorithms to construct prediction models for clinical pregnancy in IVF and to explore how each clinical variable affects the outcome.

Confidence: **High**

## Study Design and Dataset

| Item | Extracted Information |
| --- | --- |
| Article type | Peer-reviewed research article |
| Journal | PLOS ONE |
| Country/setting | Taipei Medical University Hospital, Taiwan |
| Source system | Health Promotion Administration, Ministry of Health and Welfare, Taiwan, linked with TMUH data |
| Original records | 24,730 IVF/ICSI patients with clinical pregnancy outcomes |
| Analytical cohort | 17,288 women |
| Independent later test set | 3,352 new samples from 2020-2021 |
| Study period for model development | 2007-2019 |
| Age range | Women aged 21-55 years |
| Outcome | Clinical pregnancy |
| Outcome definition | Pregnancy lasting 6 weeks/42 days after last menstrual period and confirmed by hCG assay |
| Pregnancy proportion | 37.88% achieved clinical pregnancy |
| Exclusion noted | Cycles with simultaneous fresh and freeze-thawed embryo transfer were excluded because embryo origin could not be defined |
| Public data availability | Not public due to TMUH IRB regulation; access requires institutional approval |

Confidence: **High**

## Variables / Features Used

The study used 12 variables for analysis.

Important variables discussed:

| Variable | Direction / Interpretation Reported |
| --- | --- |
| Ovarian stimulation protocol | Most important variable; long and ultra-long protocols showed positive effects |
| Total number of frozen embryos | Positive effect, peaking around eight and then flattening |
| Female age | Negative nonlinear effect; clinical pregnancy probability declined strongly after age 40 |
| Fresh vs freeze-thawed embryo transfer | Freeze-thawed group was more likely to achieve pregnancy in this dataset |
| Cause of infertility | Ovary factor, male factor and unexplained causes were more likely to achieve pregnancy than tubal factor |
| Number of embryos transferred | Higher transfer number increased probability of clinical pregnancy |
| Duration of infertility | Negative effect; longer infertility duration reduced probability |

Variables missing or limited according to authors:

- BMI
- embryo grading
- detailed stimulation protocol information beyond drug dose and timing
- AMH
- basic hormone data
- semen analysis
- lifestyle-related factors
- disease status

Confidence: **High**

## Method / Algorithm

The study compared:

| Method | Role |
| --- | --- |
| Logistic Regression | Baseline prediction model |
| Random Forest | Main machine-learning model |

Technical details:

- Missing ovarian-stimulation protocol values were imputed using missForest.
- The original dataset was divided 50% training and 50% test.
- Random Forest used 1,000 trees.
- Variable importance was measured using mean decrease accuracy.
- Partial dependence plots were used to visualize variable effects.
- Hyperparameter tuning used `tuneRF` and `caret`.
- Analysis used RStudio and SAS.

Confidence: **High**

## Evaluation Metrics

The study used:

- accuracy
- sensitivity
- specificity
- AUC
- ROC curves

Confidence: **High**

## Main Findings

| Finding | Extracted Information |
| --- | --- |
| Best model | Random Forest |
| Logistic Regression AUC | 0.6766 |
| Random Forest AUC | 0.7208 |
| Random Forest interpretation | Variable importance plus partial dependence plots |
| Most important variable | Ovarian stimulation protocol |
| Important positive factor | Total frozen embryos, up to a flattening point |
| Important negative factor | Female age, especially after 40 |
| Other important factors | Infertility cause, number of embryos transferred, duration of infertility |

The authors concluded that Random Forest outperformed Logistic Regression and helped identify important clinical variables affecting clinical pregnancy.

Confidence: **High**

## Limitations Stated By Authors

| Limitation | Meaning |
| --- | --- |
| Data integrity limitations | Some variables had missingness or incomplete information. |
| Missing BMI | BMI was not available for further discussion. |
| Missing embryo grading | Embryo quality details were not included. |
| Limited stimulation detail | Detailed stimulation protocol information was lacking except drug dose and timing. |
| Missing AMH/basic hormones | Important ovarian reserve and hormone features were unavailable. |
| Missing semen analysis | Male-factor detail was limited. |
| Limited lifestyle data | Lifestyle-related factors were not sufficiently available. |
| Limited disease-status data | Disease status information was limited. |

Confidence: **High**

## Hidden Limitations / Our Critical View

These are our PhD-analysis points.

| Critical Point | Why It Matters |
| --- | --- |
| Outcome is clinical pregnancy, not live birth | Clinical pregnancy does not guarantee live birth. |
| Single-country/hospital-linked dataset | Taiwan results may not generalize to Indian IVF clinics. |
| Moderate AUC | Random Forest AUC 0.7208 is useful but not enough for confident clinical decision-making alone. |
| Missing embryo and lifestyle variables | This directly supports our proposed data-collection gap. |
| Imputation-heavy variable | 42.58% missingness in ovarian stimulation protocol required imputation, so interpretation needs caution. |
| No deployed CDSS | The study suggests clinical usefulness but does not test a decision-support tool in practice. |
| No patient-level XAI | PDP and variable importance help interpretation, but they are not individualized explanations like SHAP. |

Confidence: **High**

## Future Work Suggested

The authors state that future work should include:

- embryo image characteristics
- hormone profiles
- embryo grading
- combined clinical variables plus embryo images and grading
- improved prediction of clinical pregnancy

Confidence: **High**

## Gap Contribution

| Gap Category | Supported? | Explanation |
| --- | --- | --- |
| Need richer clinical variables | Yes | BMI, AMH, hormones, semen analysis and disease status were missing/limited. |
| Lack of lifestyle data | Yes | Authors explicitly state lifestyle-related factors were limited. |
| Need embryo data integration | Yes | Authors propose embryo image characteristics and embryo grading. |
| No clinical decision support | Yes | Prediction model was not deployed as a CDSS. |
| Need stronger outcome label | Yes | Outcome was clinical pregnancy, not live birth. |
| Lack of Indian population | Yes | Study was based in Taiwan. |
| Need personalized explanation | Partial | PDP gives model-level interpretation, but not patient-level explanation. |

## Usefulness For Our PhD

Relevance: **High**

This paper is particularly useful for data collection planning. It confirms that strong IVF prediction datasets should include:

- clinical treatment variables
- stimulation protocol details
- embryo transfer information
- embryo grading/images where possible
- hormone profiles
- AMH and ovarian reserve markers
- semen analysis
- BMI and lifestyle data
- disease status

It also supports the idea that a model should not only predict but also explain how variables influence outcomes.

## How We Can Cite This Paper In Thesis

Thesis-ready sentence:

> Wang et al. (2022) developed clinical-pregnancy prediction models using 17,288 IVF/ICSI records from Taipei Medical University Hospital and found that Random Forest outperformed Logistic Regression, with AUC values of 0.7208 and 0.6766, respectively.

Gap-support sentence:

> The study identified ovarian stimulation protocol, frozen embryos, female age, infertility cause and embryo-transfer variables as important predictors, but also reported missing BMI, AMH, hormone, semen, embryo-grading, lifestyle and disease-status data, supporting the need for richer multimodal IVF datasets.

## What This Paper Does Not Prove

This paper does not prove that:

- clinical pregnancy prediction is equivalent to live-birth prediction.
- the model generalizes to Indian IVF clinics.
- Random Forest is always superior for all IVF datasets.
- variable importance proves causality.
- the model is ready as a deployed clinical decision-support system.
- lifestyle and embryo variables are unnecessary.

## Source Confidence Summary

| Section | Confidence |
| --- | --- |
| Citation | High |
| Dataset and cohort size | High |
| Outcome definition | High |
| Methods and algorithms | High |
| Evaluation metrics | High |
| Main findings | High |
| Limitations and future work | High |
