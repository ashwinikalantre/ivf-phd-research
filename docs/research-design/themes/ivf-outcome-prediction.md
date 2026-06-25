# IVF Outcome, Pregnancy and Live-Birth Prediction

## Papers in This Theme

| No | Year | Title | Method | Dataset | Gap Found |
| --- | --- | --- | --- | --- | --- |
| 5 | 2025 | Machine learning center-specific models show improved IVF live birth predictions over US national registry-based model | Center-specific machine learning live-birth prediction models. | 4,635 first-IVF-cycle patients from six centers. | Limited Population Diversity; No Indian Population; Generalization Gap; Need External Validation |
| 6 | 2025 | Predictive modeling of pregnancy outcomes utilizing multiple machine learning techniques for IVF-ET | Multiple ML models; 80:20 train-test split. | 2,625 women undergoing fresh IVF-ET cycles from 2016-2022 at Inner Mongolia Medical University affiliated hospital. | Single-center Study; Need External Validation; Retrospective Design; Need Clinical Decision Support |
| 7 | 2025 | Construction and evaluation of machine learning-based prediction model for live birth following fresh embryo transfer in IVF/ICSI patients with PCOS | Multiple ML algorithms; XGBoost best; SHAP for predictors. | 1,062 fresh embryo transfer cycles in PCOS patients; 466 live births. | Need External Validation; Disease-specific Generalization Gap; Need Clinical Decision Support |
| 8 | 2025 | Predictive models for live birth outcomes following fresh embryo transfer | Machine learning prediction models. | Fresh embryo-transfer cohort; exact size not extracted in first pass. | Need External Validation; Need Clinical Decision Support; Need Real-world Deployment Evidence |
| 9 | 2025 | A retrospective analysis of 48,514 IVF cycles and an evaluation of machine learning models for live birth prediction | CNN, Random Forest and other traditional ML models. | 48,514 IVF cycles from EMR data. | Retrospective Design; Need External Validation; Need Real-world Deployment Evidence |
| 10 | 2025 | Optimizing predictive features using machine learning for early miscarriage risk following single vitrified-warmed blastocyst transfer | Logistic Regression, Random Forest, Gradient Boosting, Voting Classifier. | Dual-center retrospective analysis of 1,664 SVBT cycles, including 308 early miscarriage cases. | Retrospective Design; Limited Multi-center Validation; Need Clinical Decision Support |
| 11 | 2025 | Machine learning-based prediction of IVF outcomes: the central role of female preprocedural factors | Machine learning prediction models. | IVF cycles; exact size not extracted in first pass. | Need Full-text Verification; Need External Validation; Need Clinical Decision Support |
| 15 | 2026 | AI-based live birth prediction in IVF cycles: a systematic review without meta-analysis of model performance and validation | Systematic review without meta-analysis. | Systematic review of live-birth prediction studies; included because it directly synthesizes 2021-2025 evidence though published after target window. | Retrospective Design; Selection Bias; Internal Validation Overfitting; Need External Validation |
| 16 | 2024 | Comparative study of machine learning approaches integrated with genetic algorithm for IVF success prediction | ANN, RPART, Random Forest, SVM and AdaBoost with Genetic Algorithm feature selection. | Single medical facility in Tehran, Iran; IVF clinical dataset. | Single-center Study; Need External Validation; Limited Population Diversity; Need Clinical Decision Support |
| 17 | 2024 | Catalyzing IVF outcome prediction: exploring advanced machine learning paradigms for enhanced success rate prognostication | Logistic Regression, Gaussian NB, SVM, MLP, KNN, Random Forest, AdaBoost, LogitBoost, RUSBoost and RSM. | Datasets from 2017-2018 and 2010-2016. | Retrospective Design; Need Prospective/RCT Validation; Need Clinical Decision Support |
| 18 | 2022 | Comparison of machine learning classification techniques to predict implantation success in an IVF treatment cycle | Machine learning classification techniques. | IVF treatment-cycle dataset; full dataset details require paper verification. | Need Full-text Verification; Need External Validation |
| 19 | 2022 | Predicting clinical pregnancy using clinical features and machine learning algorithms in in vitro fertilization | Random Forest and Logistic Regression. | IVF patients from 2007-2019. | Need Full-text Verification; Need External Validation; Need Clinical Decision Support |
| 20 | 2022 | Machine Learning Approach to Predict Clinical Pregnancy Potential in Women Undergoing IVF Program | Decision Tree and Random Forest. | Large practical IVF clinical database; exact size/source require verification. | Lack of Standardization; Need External Validation; Need Clinical Decision Support |
| 29 | 2025 | Artificial intelligence-enhanced in-vitro fertilization outcome prediction for the Indian subpopulation: integrating pre-treatment parameters and Bayesian-optimized ensemble techniques | Bayesian-optimized ensemble model, reported as BoVe. | Retrospective cohort using IVF-ICSI data from Sir Ganga Ram Hospital, Delhi, India, from 1 January 2018 to 31 October 2022; original dataset 2,908 records and 79 variables. | No Indian Population; Single-center Study; Need External Validation; Retrospective Design; Need Clinical Decision Support |
| 30 | 2024 | Machine learning algorithms in constructing prediction models for assisted reproductive technology related live birth outcomes | Statistical models and multiple ML algorithms; logistic regression recommended for simplicity in source summary. | Large Chinese ART patient sample; exact cohort size requires full paper extraction. | Need Full-text Verification; Need External Validation; Lack of Standardization; Need Clinical Decision Support |
| 31 | 2025 | Machine learning prediction of clinical pregnancy in endometriosis patients undergoing fresh embryo transfer | Naive Bayes, Logistic Regression, Random Forest, KNN, Neural Network and XGBoost with feature selection and cross-validation. | 1,752 endometriosis patients undergoing IVF/ICSI with fresh embryo transfer from 2014 to 2024. | Disease-specific Generalization Gap; Retrospective Design; Need External Validation; Need Clinical Decision Support |
| 33 | 2025 | Development of an explainable machine learning model to predict live birth versus miscarriage among IVF-ET pregnancies | XGBoost explainable model with interpretable tree/feature analysis. | IVF-ET pregnancies with confirmed pregnancy; exact cohort details require full extraction. | Need External Validation; Need Clinical Decision Support; Trustworthy AI Gap; Need Full-text Verification |

## Existing Work

- Most studies build predictive models for clinical pregnancy, implantation, miscarriage or live birth using routine clinical and treatment-cycle variables.
- Ensemble methods such as Random Forest, AdaBoost, XGBoost and voting classifiers frequently outperform simpler baselines, but several studies still show modest or context-dependent gains.
- Recent work is moving from general IVF prediction toward subgroup-specific prediction, including PCOS, endometriosis, male-factor infertility, FET and Indian subpopulation contexts.

## Repeated Limitations

- Many studies remain retrospective and single-center or geographically narrow.
- External validation is often missing or insufficient.
- Studies use different datasets, variables, outcomes and metrics, making direct comparison difficult.
- Prediction accuracy is often emphasized more than clinical workflow integration.

## Usable Research Gaps

- Externally validated IVF outcome prediction for Indian clinical settings.
- Standardized feature and reporting framework for IVF prediction studies.
- Explainable prediction outputs that can support counseling and treatment decisions.

## Supervisor View

This theme is the broad evidence base. It supports the need for prediction, but alone it is too common for a PhD topic. The topic becomes stronger only when prediction is combined with explainability, clinical decision support and Indian/multimodal validation.
