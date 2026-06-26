# Technical Glossary

This page explains AI, machine-learning and evaluation terms used in the literature review.

## Artificial Intelligence

**Simple meaning:** Computer systems designed to perform tasks that normally need human intelligence, such as recognizing patterns or supporting decisions.

**Why it matters:** IVF-AI research uses AI to support prediction, embryo assessment, treatment planning and counseling.

**For our research:** We should use the term AI broadly, but be specific when a paper actually uses machine learning, deep learning or explainable AI.

Deep reading:

- [NIH artificial intelligence overview](https://www.nih.gov/about-nih/what-we-do/science-health-public-trust/perspectives/artificial-intelligence)

## Machine Learning

**Simple meaning:** A type of AI where models learn patterns from data instead of being manually programmed with every rule.

**Why it matters:** Most IVF prediction papers use machine learning on clinical, embryology or imaging data.

**For our research:** ML is suitable for structured IVF datasets when we have enough clean records and meaningful outcome labels.

Deep reading:

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

## Deep Learning

**Simple meaning:** A machine-learning approach using neural networks with many layers.

**Why it matters:** Deep learning is often used for embryo images, time-lapse videos and complex multimodal data.

**For our research:** Deep learning should be used only if dataset size and data type justify it. For tabular clinic data, simpler models may be better.

Deep reading:

- [IBM deep learning overview](https://www.ibm.com/topics/deep-learning)

## Multimodal Learning

**Simple meaning:** A machine-learning approach that combines more than one type of data.

**Example:** Clinical table data plus embryo images or videos.

**For our research:** Multimodal learning is central if our dataset includes clinical, embryology and lifestyle data.

Deep reading:

- [Nature Medicine article on multimodal AI in healthcare](https://www.nature.com/articles/s41591-023-02448-8)

## Pretraining

**Simple meaning:** Training a model first on a related task before training it on the final prediction task.

**Why it matters:** It can help a model learn useful representations, especially for image or video data.

**For our research:** Pretraining may be relevant if embryo images or videos are available, but it is less central for simple tabular data.

Deep reading:

- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)

## Multi-Task Learning

**Simple meaning:** Training one model to predict more than one related outcome at the same time.

**Why it matters:** Related IVF outcomes may share useful information, such as fetal heartbeat, miscarriage and live birth.

**For our research:** Multi-task learning is promising, but only if enough high-quality labels are available for multiple outcomes.

Deep reading:

- [Multi-task learning overview, Stanford CS330 notes](https://cs330.stanford.edu/)

## Cross-Attention

**Simple meaning:** A neural-network mechanism where one data source learns which parts of another data source are relevant.

**Example:** Embryo-video features attending to clinical-variable features.

**For our research:** Cross-attention is useful for advanced multimodal deep learning, but may be too complex unless image/video data is available.

Deep reading:

- [Google Transformer model overview](https://developers.google.com/machine-learning/glossary#transformer)

## Transformer

**Simple meaning:** A neural-network architecture based on attention mechanisms.

**Why it matters:** Transformers are used in language, vision, time-series and tabular-data models.

**For our research:** Transformer-based models may be relevant for embryo video or complex multimodal data, but simpler models should be considered first for clinic tabular data.

Deep reading:

- [Google ML glossary: Transformer](https://developers.google.com/machine-learning/glossary#transformer)

## Object Detection

**Simple meaning:** A computer-vision task that locates objects inside images or videos.

**Example:** Detecting the embryo region in time-lapse images.

**For our research:** Object detection is relevant only if embryo image or video data is available.

Deep reading:

- [Ultralytics YOLO documentation](https://docs.ultralytics.com/)

## Convolutional Neural Network

**Simple meaning:** A deep-learning model commonly used for image analysis.

**Why it matters:** CNNs can learn visual patterns from embryo images.

**For our research:** CNNs are relevant only if embryo image data is available. For tabular clinic data, they are usually not needed.

Deep reading:

- [IBM convolutional neural networks overview](https://www.ibm.com/topics/convolutional-neural-networks)

## ResNet

**Simple meaning:** Residual Network. A CNN architecture that uses skip connections to make deep image models easier to train.

**Why it matters:** ResNet is commonly used as an image-model backbone.

**For our research:** Paper 04 used ResNet34 for blastocyst image classification.

Deep reading:

- [PyTorch ResNet documentation](https://pytorch.org/vision/main/models/resnet.html)

## Fusion Model

**Simple meaning:** A model that combines information from two or more input sources.

**Example:** Combining clinical data features with embryo image features.

**For our research:** Fusion models are central to testing whether multimodal IVF data improves prediction over single-modality models.

Deep reading:

- [Nature Medicine article on multimodal AI in healthcare](https://www.nature.com/articles/s41591-023-02448-8)

## ScoreCAM

**Simple meaning:** A visualization method that highlights image regions that influence a CNN prediction.

**Why it matters:** It can help detect whether an embryo-image model is focusing on meaningful embryo regions or irrelevant background.

**For our research:** Visualization can support trust, but it is not the same as full clinical explainability.

Deep reading:

- [Score-CAM paper](https://openaccess.thecvf.com/content_CVPRW_2020/html/w1/Wang_Score-CAM_Score-Weighted_Visual_Explanations_for_Convolutional_Neural_Networks_CVPRW_2020_paper.html)

## Layer-Wise Relevance Propagation

**Simple meaning:** A method that traces a model prediction backward to estimate which input features contributed most.

**Why it matters:** It can be used to explain clinical feature importance in neural-network models.

**For our research:** LRP is one possible explainability method, but SHAP may be easier to communicate for tabular clinical models.

Deep reading:

- [LRP overview from Explainable AI literature](https://doi.org/10.1371/journal.pone.0130140)

## Class Imbalance

**Simple meaning:** A dataset problem where one outcome class is much more common than another.

**Example:** Many more pregnant than non-pregnant samples.

**For our research:** IVF datasets often have imbalance, so metrics such as F1, sensitivity, specificity and calibration must be checked carefully.

Deep reading:

- [Google ML Crash Course: classification and imbalanced datasets](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)

## Blind Test Set

**Simple meaning:** A test dataset kept hidden from the model during training and tuning.

**Why it matters:** It gives a more honest estimate of model performance than testing on training data.

**For our research:** A blind test set is useful, but external clinic validation is still stronger.

Deep reading:

- [Google ML Crash Course: training and test sets](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets)

## Explainable AI

**Simple meaning:** AI methods that help users understand why a model gives a prediction.

**Why it matters:** In healthcare, doctors need to understand model reasoning before trusting or using it.

**For our research:** Explainability is one of the central gaps. The output should show important positive and negative factors, not only a probability score.

Deep reading:

- [NIST explainable AI overview](https://www.nist.gov/artificial-intelligence/explainable-ai)

## Clinical Decision Support System

**Simple meaning:** A system that helps clinicians make decisions by showing relevant information, predictions, alerts or recommendations.

**Why it matters:** A prediction model alone is not enough. It becomes clinically useful only when translated into a decision-support workflow.

**For our research:** CDSS framing helps connect ML output to doctor-facing counseling and treatment planning.

Deep reading:

- [AHRQ clinical decision support overview](https://digital.ahrq.gov/clinical-decision-support)

## Human-in-the-Loop AI

**Simple meaning:** An AI workflow where a human expert reviews, interprets or controls the final decision.

**Why it matters:** In IVF, doctors and embryologists should remain responsible for treatment decisions.

**For our research:** The proposed CDSS should support clinicians, not replace them.

Deep reading:

- [NIST human-centered AI resources](https://www.nist.gov/artificial-intelligence)

## Black-Box AI

**Simple meaning:** An AI model whose internal reasoning is difficult for humans to understand.

**Why it matters:** Black-box systems can reduce trust in healthcare if users cannot understand or challenge predictions.

**For our research:** Explainability is needed because IVF decisions affect patient counseling, cost and treatment choices.

Deep reading:

- [NIST explainable AI overview](https://www.nist.gov/artificial-intelligence/explainable-ai)

## Prospective Validation

**Simple meaning:** Testing a model forward in time on new patients after the model has been developed.

**Why it matters:** It gives stronger evidence than retrospective testing.

**For our research:** Prospective validation would be ideal, but feasibility depends on clinic cooperation and study timeline.

Deep reading:

- [TRIPOD statement](https://www.tripod-statement.org/)

## Federated Learning

**Simple meaning:** A method where multiple institutions train a shared model without directly sharing raw patient data.

**Why it matters:** It can support multi-clinic collaboration while protecting data privacy.

**For our research:** Federated learning may be future work if multiple IVF clinics cannot share raw data centrally.

Deep reading:

- [Google federated learning overview](https://research.google/blog/federated-learning-collaborative-machine-learning-without-centralized-training-data/)

## Digital Twin

**Simple meaning:** A digital representation of a real-world person, process or system that can be used to simulate possible outcomes.

**Why it matters:** In future IVF research, digital twins may allow virtual testing of treatment options before clinical decisions.

**For our research:** This is a future-facing concept. It should not be claimed unless the project actually builds a simulation model.

Deep reading:

- [FDA digital health and digital twins discussion](https://www.fda.gov/medical-devices/digital-health-center-excellence)

## Synthetic Data

**Simple meaning:** Artificially generated data designed to resemble real data.

**Why it matters:** Synthetic data may help model development when real IVF datasets are limited or privacy-restricted.

**For our research:** Synthetic data can be future work, but real clinical validation remains necessary.

Deep reading:

- [NIST synthetic data guidance resources](https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/collaboration-space/focus-topics/synthetic-data)

## Trustworthy AI

**Simple meaning:** AI that is reliable, transparent, fair, secure and accountable.

**Why it matters:** Healthcare AI must be trusted by clinicians and patients before it can be used responsibly.

**For our research:** Trustworthy AI includes explainability, validation, privacy, fairness and clinical oversight.

Deep reading:

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

## Model Generalizability

**Simple meaning:** How well a model works on new patients, clinics or populations beyond the data used to build it.

**Why it matters:** IVF models may perform well in one clinic but poorly elsewhere.

**For our research:** Generalizability is one reason Indian clinic validation is important.

Deep reading:

- [TRIPOD statement](https://www.tripod-statement.org/)

## Data Bias

**Simple meaning:** A problem where the data used to train a model does not fairly represent the population where the model will be used.

**Why it matters:** Biased IVF datasets can produce unreliable or unfair predictions for underrepresented groups.

**For our research:** We should check subgroup performance where data permits.

Deep reading:

- [NIST AI bias resources](https://www.nist.gov/artificial-intelligence/ai-fundamental-research/bias-ai)

## Clinical Validation

**Simple meaning:** Testing whether a model works in a clinically meaningful setting and population.

**Why it matters:** Good retrospective performance is not enough for patient-facing or clinician-facing use.

**For our research:** Clinical validation may include external validation, temporal validation and clinician review.

Deep reading:

- [TRIPOD statement](https://www.tripod-statement.org/)

## Post-Market Study

**Simple meaning:** A study done after a medical software or product is already available for clinical use.

**Why it matters:** It can show how a tool performs in real practice, but it may not be as controlled as a randomized trial.

**For our research:** Paper 02 is useful because it gives prospective post-market evidence for IVF AI-CDSS use.

Deep reading:

- [FDA real-world evidence overview](https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence)

## Feature

**Simple meaning:** An input variable used by a model.

**Example:** Age, BMI, AMH, AFC, follicle count, embryo grade or stimulation protocol.

**For our research:** Good feature definition is essential because IVF data comes from many clinical stages.

Deep reading:

- [Google ML Crash Course: numerical data](https://developers.google.com/machine-learning/crash-course/numerical-data)

## K-Nearest Neighbors

**Simple meaning:** A method that finds the most similar previous cases and uses them to support prediction or comparison.

**Why it matters:** It is intuitive for clinical examples because it asks: what happened to similar patients before?

**For our research:** Paper 02 used a K-nearest-neighbors approach in the Starting Dose Tool and for matching/imputation steps.

Deep reading:

- [scikit-learn nearest neighbors](https://scikit-learn.org/stable/modules/neighbors.html)

## KNN Imputer

**Simple meaning:** A missing-data method that fills a missing value using values from similar records.

**Why it matters:** IVF clinic data often has missing AMH, AFC or BMI values.

**For our research:** Missing-data handling must be reported clearly because it affects trust and reproducibility.

Deep reading:

- [scikit-learn KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html)

## Outcome / Target Variable

**Simple meaning:** The result that the model tries to predict.

**Example:** Clinical pregnancy, live birth, mature oocyte count or miscarriage.

**For our research:** The final outcome must depend on what clinic data records reliably.

Deep reading:

- [Google ML Crash Course: labels](https://developers.google.com/machine-learning/crash-course/framing/ml-terminology)

## Regression

**Simple meaning:** A prediction task where the output is a number.

**Example:** Predicting number of mature oocytes.

**For our research:** Paper 01 used a regression model because the main outcome was mature oocyte count.

Deep reading:

- [scikit-learn supervised learning](https://scikit-learn.org/stable/supervised_learning.html)

## Classification

**Simple meaning:** A prediction task where the output is a category.

**Example:** Pregnancy yes/no, live birth yes/no, miscarriage yes/no.

**For our research:** Many IVF outcome models are classification models.

Deep reading:

- [scikit-learn supervised learning](https://scikit-learn.org/stable/supervised_learning.html)

## Gradient Boosting

**Simple meaning:** A machine-learning method that builds many small decision trees step by step, where each new tree tries to improve previous errors.

**Why it matters:** Gradient boosting often performs well on structured clinical data.

**For our research:** XGBoost, LightGBM and histogram-based gradient boosting are candidate models for tabular IVF data.

Deep reading:

- [scikit-learn gradient boosting regression example](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)
- [scikit-learn GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)

## Histogram-Based Gradient Boosting

**Simple meaning:** A faster type of gradient boosting that groups continuous values into bins before building trees.

**Why it matters:** It can be efficient for larger tabular datasets.

**For our research:** Paper 01 used a histogram-based gradient boosting regression tree model.

Deep reading:

- [scikit-learn ensemble methods](https://scikit-learn.org/stable/modules/ensemble.html)

## Logistic Regression

**Simple meaning:** A statistical model often used for binary outcomes such as yes/no prediction.

**Why it matters:** It is easy to explain and often used as a baseline in medical prediction.

**For our research:** Logistic regression should be included as a baseline before using more complex models.

Deep reading:

- [scikit-learn LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

## Support Vector Machine

**Simple meaning:** A supervised machine-learning model that tries to separate classes using a boundary with maximum margin.

**Why it matters:** SVM is often used as a comparison model in medical prediction studies.

**For our research:** SVM can be tested, but tree-based models often perform better on mixed clinical tabular data.

Deep reading:

- [scikit-learn SVM](https://scikit-learn.org/stable/modules/svm.html)

## Random Forest

**Simple meaning:** An ensemble model made from many decision trees.

**Why it matters:** It can capture non-linear relationships and is commonly used in IVF prediction papers.

**For our research:** Random Forest is a useful baseline before more complex boosting models.

Deep reading:

- [scikit-learn RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

## Extra Trees

**Simple meaning:** Extremely Randomized Trees. An ensemble method similar to Random Forest but with more randomization in tree construction.

**Why it matters:** It is often used as a comparison ensemble model.

**For our research:** Extra Trees may be useful for benchmarking, but clinical interpretability still needs attention.

Deep reading:

- [scikit-learn ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html)

## AdaBoost

**Simple meaning:** Adaptive Boosting. An ensemble method that gives more attention to samples that previous models classified incorrectly.

**Why it matters:** It is often used as a comparison boosting model.

**For our research:** AdaBoost may be useful for benchmarking, but stronger models such as XGBoost, LightGBM or Random Forest may perform better on IVF tabular data.

Deep reading:

- [scikit-learn AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)

## Artificial Neural Network

**Simple meaning:** A machine-learning model inspired by connected layers of artificial neurons.

**Why it matters:** ANNs can learn non-linear patterns but may overfit if the dataset is not large or balanced enough.

**For our research:** Use ANN as a comparison model only if sample size and validation design support it.

Deep reading:

- [scikit-learn neural network models](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)

## Feedforward Neural Network

**Simple meaning:** A neural network where information moves in one direction from input to output.

**Why it matters:** It is a common comparison model for structured clinical prediction.

**For our research:** It can model non-linear relationships but needs careful validation to avoid overfitting.

Deep reading:

- [IBM neural networks overview](https://www.ibm.com/topics/neural-networks)

## Naive Bayes

**Simple meaning:** A probabilistic classification model based on Bayes’ theorem and a simplifying assumption that features are conditionally independent.

**Why it matters:** It is simple and fast, but often weak when clinical features are correlated.

**For our research:** Use mainly as a comparison baseline, not as the main model.

Deep reading:

- [scikit-learn Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)

## Electronic Medical Record

**Simple meaning:** A digital record of patient clinical information collected during care.

**Why it matters:** EMR data is a common source for retrospective IVF prediction studies.

**For our research:** Clinic EMR data may be useful, but missingness, inconsistent coding and privacy must be handled carefully.

Deep reading:

- [HealthIT.gov electronic medical records overview](https://www.healthit.gov/faq/what-are-electronic-medical-records-emrs)

## One-Hot Encoding

**Simple meaning:** A way to convert categories into numeric columns so machine-learning models can use them.

**Example:** Infertility type becomes separate yes/no columns for PCOS, tubal factor, male factor, etc.

**For our research:** Needed for categorical IVF variables, but categories should be clinically meaningful.

Deep reading:

- [scikit-learn OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)

## Min-Max Scaling

**Simple meaning:** A method that rescales numeric values to a fixed range.

**Why it matters:** Some models train better when numeric features are on similar scales.

**For our research:** Scaling should be fitted only on training data to avoid data leakage.

Deep reading:

- [scikit-learn MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)

## Early Stopping

**Simple meaning:** A training method that stops model training when validation performance stops improving.

**Why it matters:** It helps reduce overfitting in neural networks.

**For our research:** Useful for deep learning or boosting models, but validation design must be correct.

Deep reading:

- [Keras early stopping documentation](https://keras.io/api/callbacks/early_stopping/)

## XGBoost

**Simple meaning:** A powerful gradient-boosting tree algorithm often used for structured tabular data.

**Why it matters:** Many IVF prediction studies report strong XGBoost performance.

**For our research:** XGBoost is a strong candidate model, but it must be calibrated, explained and externally validated.

Deep reading:

- [XGBoost documentation](https://xgboost.readthedocs.io/)

## LightGBM

**Simple meaning:** A fast gradient-boosting framework designed for efficient training on large or structured datasets.

**Why it matters:** LightGBM often performs well on clinical tabular datasets.

**For our research:** LightGBM is a strong candidate model, but high performance must be interpreted with validation and explainability.

Deep reading:

- [LightGBM documentation](https://lightgbm.readthedocs.io/)

## Feature Selection

**Simple meaning:** Choosing the most useful input variables for a model.

**Why it matters:** Too many weak or redundant variables can reduce model reliability and interpretability.

**For our research:** Feature selection should be clinically sensible, not only mathematically optimized.

Deep reading:

- [scikit-learn feature selection](https://scikit-learn.org/stable/modules/feature_selection.html)

## Feature Importance

**Simple meaning:** A method for estimating which input variables contribute most to model predictions.

**Why it matters:** It helps researchers and clinicians understand which variables drive model behavior.

**For our research:** Feature importance is useful, but it should be interpreted carefully because it does not prove causality.

Deep reading:

- [scikit-learn permutation importance](https://scikit-learn.org/stable/modules/permutation_importance.html)

## Same-Centre External Validation

**Simple meaning:** Testing a model on a later or separate dataset from the same clinic or institution.

**Why it matters:** It is stronger than only testing on a random internal split, but weaker than validation in a different clinic.

**For our research:** We should clearly distinguish same-centre validation from true multicentre external validation.

Deep reading:

- [TRIPOD statement](https://www.tripod-statement.org/)

## Positive Predictive Value

**Simple meaning:** Among patients predicted as positive, the proportion who actually had the positive outcome.

**Why it matters:** It helps judge how reliable positive predictions are.

**For our research:** PPV depends on outcome prevalence, so it may change across clinics.

Deep reading:

- [MedlinePlus diagnostic test definitions](https://medlineplus.gov/lab-tests/how-to-understand-your-lab-results/)

## Negative Predictive Value

**Simple meaning:** Among patients predicted as negative, the proportion who actually did not have the positive outcome.

**Why it matters:** It helps judge how reliable negative predictions are.

**For our research:** High NPV may be useful for counseling, but it must be interpreted carefully to avoid discouraging patients unfairly.

Deep reading:

- [MedlinePlus diagnostic test definitions](https://medlineplus.gov/lab-tests/how-to-understand-your-lab-results/)

## Recursive Feature Elimination

**Simple meaning:** A feature-selection method that repeatedly removes less useful variables until a smaller feature set remains.

**Why it matters:** It can help reduce model complexity and improve interpretability.

**For our research:** RFE can be used, but selected features should still make clinical sense.

Deep reading:

- [scikit-learn recursive feature elimination](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html)

## Decision Curve Analysis

**Simple meaning:** A method for evaluating whether a prediction model gives useful clinical benefit across decision thresholds.

**Why it matters:** A model can have good AUC but still be less useful for clinical decisions at realistic thresholds.

**For our research:** Decision curve analysis may help show whether an IVF prediction model supports counseling or decision support.

Deep reading:

- [Decision curve analysis overview](https://www.mskcc.org/departments/epidemiology-biostatistics/biostatistics/decision-curve-analysis)

## Voting Classifier

**Simple meaning:** An ensemble model that combines predictions from multiple models and chooses the final class by voting or averaged probabilities.

**Why it matters:** It can improve stability when different models capture different patterns.

**For our research:** Voting classifiers may be useful for comparison, but explainability and calibration still matter.

Deep reading:

- [scikit-learn VotingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html)

## Stacking Classifier

**Simple meaning:** An ensemble method where predictions from several base models are used as inputs to another model.

**Why it matters:** It can improve performance but may become harder to explain.

**For our research:** Stacking should be used cautiously in healthcare because transparency and overfitting risk must be controlled.

Deep reading:

- [scikit-learn StackingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html)

## SMOTETomek

**Simple meaning:** A class-balancing method that combines SMOTE oversampling with Tomek Links cleaning.

**Why it matters:** It helps when one outcome class is much smaller than another.

**For our research:** Class balancing must be applied only to training data to avoid leakage.

Deep reading:

- [imbalanced-learn SMOTETomek](https://imbalanced-learn.org/stable/references/generated/imblearn.combine.SMOTETomek.html)

## Mutual Information

**Simple meaning:** A statistic that measures how much knowing one variable reduces uncertainty about another variable.

**Why it matters:** It can identify useful predictors even when relationships are non-linear.

**For our research:** Mutual information can support feature selection, but clinical relevance should still be checked.

Deep reading:

- [scikit-learn mutual_info_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html)

## Multilayer Perceptron

**Simple meaning:** A feedforward neural network with one or more hidden layers.

**Why it matters:** It can model non-linear patterns but may need more data and careful tuning.

**For our research:** It can be a comparison model, but should not be the first choice if clinic data is small.

Deep reading:

- [scikit-learn neural network models](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)

## Cross-Validation

**Simple meaning:** A validation method where the dataset is split multiple times so model performance is tested more reliably.

**Why it matters:** It helps reduce dependence on one lucky train-test split.

**For our research:** Cross-validation is important, but it is still internal validation unless tested on separate clinic/time data.

Deep reading:

- [scikit-learn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)

## Propensity Matching

**Simple meaning:** A method for making comparison groups more similar based on important baseline variables.

**Why it matters:** It is useful when a randomized control group is not available.

**For our research:** Paper 02 matched AI-treated patients to historical control patients using age, AMH and AFC.

Deep reading:

- [NIH/NLM overview of propensity score analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3144483/)

## Historical Control

**Simple meaning:** A comparison group from an earlier time period rather than a concurrent randomized control group.

**Why it matters:** It can be practical, but changes over time in clinic workflow or patient population may affect comparisons.

**For our research:** Historical controls should be treated cautiously when judging real clinical impact.

Deep reading:

- [ICH E10 guideline on choice of control group](https://www.ich.org/page/efficacy-guidelines)

## Leave-One-Clinic-Out Cross-Validation

**Simple meaning:** A validation approach where data from one clinic is held out for testing while the model is trained on the remaining clinics.

**Why it matters:** It tests whether the model generalizes across clinics better than random splitting.

**For our research:** This is stronger than simple internal validation, but it still depends on the diversity and quality of included clinics.

Deep reading:

- [scikit-learn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)

## External Validation

**Simple meaning:** Testing a model on data from a different clinic, population, time period or source not used in model development.

**Why it matters:** Many AI-IVF papers lack external validation, which weakens clinical trust.

**For our research:** External validation can be claimed only if genuinely independent data is available.

Deep reading:

- [TRIPOD statement for prediction model reporting](https://www.tripod-statement.org/)

## SHAP

**Simple meaning:** SHapley Additive exPlanations. A method that estimates how much each feature contributes to a model prediction.

**Why it matters:** SHAP can give both global feature importance and patient-level explanation.

**For our research:** SHAP is useful for explaining IVF predictions, but it does not prove causality.

Deep reading:

- [SHAP documentation](https://shap.readthedocs.io/)

## TreeSHAP

**Simple meaning:** A SHAP method optimized for tree-based models.

**Why it matters:** It is commonly used with Random Forest, XGBoost, LightGBM and gradient-boosted trees.

**For our research:** Paper 01 used SHAP/TreeSHAP-style explanation for a tree-based model.

Deep reading:

- [SHAP TreeExplainer documentation](https://shap.readthedocs.io/en/latest/generated/shap.TreeExplainer.html)

## Permutation Importance

**Simple meaning:** A method that measures how much model performance drops when one feature is randomly shuffled.

**Why it matters:** If shuffling a feature reduces performance a lot, the model depends strongly on that feature.

**For our research:** It helps identify important clinical features, but correlated features can make interpretation difficult.

Deep reading:

- [scikit-learn permutation importance](https://scikit-learn.org/stable/modules/permutation_importance.html)

## Partial Dependence Plot

**Simple meaning:** A plot showing how a model prediction changes as one feature changes, while averaging over other features.

**Why it matters:** It can help explain feature effects, but may mislead when features are highly correlated.

**For our research:** PDPs can support global explanation, but local patient-level explanations and clinician interpretation are also needed.

Deep reading:

- [scikit-learn partial dependence plots](https://scikit-learn.org/stable/modules/partial_dependence.html)

## Accumulated Local Effects

**Simple meaning:** A model-interpretation method that shows feature effects while reducing some problems caused by correlated features.

**Why it matters:** IVF variables are often correlated, such as hormones, follicles and oocytes.

**For our research:** ALE can complement SHAP and PDP in explainability analysis.

Deep reading:

- [Interpretable Machine Learning: Accumulated Local Effects](https://christophm.github.io/interpretable-ml-book/ale.html)

## Mean Absolute Error

**Simple meaning:** Average absolute difference between predicted and actual numeric values.

**Why it matters:** It is used for regression tasks.

**For our research:** Paper 01 used it for mature-oocyte-count prediction.

Deep reading:

- [scikit-learn mean_absolute_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html)

## R-Squared

**Simple meaning:** A metric showing how much variation in a numeric outcome is explained by the model.

**Why it matters:** It is commonly reported for regression performance.

**For our research:** R-squared should be interpreted with MAE and clinical meaning, not alone.

Deep reading:

- [scikit-learn r2_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)

## AUC

**Simple meaning:** Area under the ROC curve. A metric for how well a model separates positive and negative cases.

**Why it matters:** Common in IVF pregnancy/live-birth prediction.

**For our research:** AUC is useful, but calibration and clinical usefulness are also important.

Deep reading:

- [scikit-learn ROC and AUC](https://scikit-learn.org/stable/modules/model_evaluation.html#roc-metrics)

## Precision-Recall AUC

**Simple meaning:** Area under the precision-recall curve. It shows how well a model balances correct positive predictions and detection of actual positives.

**Why it matters:** It is useful when false positives and false negatives are clinically important.

**For our research:** IVF counseling should consider false reassurance and unnecessary discouragement, not only ROC-AUC.

Deep reading:

- [scikit-learn precision-recall metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)

## F1 Score

**Simple meaning:** A metric that combines precision and recall into one value.

**Why it matters:** It helps evaluate whether a model balances false positives and false negatives.

**For our research:** F1 can be useful at clinically meaningful thresholds, but it should not replace calibration.

Deep reading:

- [scikit-learn F1 score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)

## Calibration

**Simple meaning:** How closely predicted probabilities match actual observed outcomes.

**Example:** If a model predicts 60% pregnancy probability for many patients, about 60% of similar patients should actually become pregnant.

**For our research:** Calibration matters because IVF counseling depends on probability, not only ranking.

Deep reading:

- [scikit-learn probability calibration](https://scikit-learn.org/stable/modules/calibration.html)

## Brier Score

**Simple meaning:** A metric that measures how close predicted probabilities are to actual outcomes.

**Why it matters:** Lower Brier score usually means better probability calibration.

**For our research:** Brier score is useful because IVF counseling often gives patients probability estimates.

Deep reading:

- [scikit-learn brier_score_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html)

## Data Drift

**Simple meaning:** A change in the distribution of input data over time.

**Example:** A clinic’s patient age, diagnosis profile or treatment protocols change over years.

**For our research:** IVF models may need monitoring and updating if clinic populations or practices change.

Deep reading:

- [Evidently AI data drift guide](https://www.evidentlyai.com/ml-in-production/data-drift)

## Concept Drift

**Simple meaning:** A change in the relationship between input features and the outcome.

**Example:** A treatment protocol changes, so a variable predicts live birth differently than before.

**For our research:** Concept drift matters if a model is deployed over time in a real clinic.

Deep reading:

- [Evidently AI concept drift guide](https://www.evidentlyai.com/ml-in-production/concept-drift)

## TRIPOD + AI

**Simple meaning:** Reporting guidance for clinical prediction models that use regression or machine learning.

**Why it matters:** It helps make prediction-model studies transparent and reproducible.

**For our research:** TRIPOD + AI can guide how we report dataset, model, validation and limitations in the thesis.

Deep reading:

- [TRIPOD statement](https://www.tripod-statement.org/)

## Bayesian Optimization

**Simple meaning:** A method for efficiently searching model settings by using previous results to choose better next trials.

**Why it matters:** It is used for hyperparameter tuning when there are many possible model settings.

**For our research:** It can improve model tuning, but it does not replace external validation.

Deep reading:

- [scikit-optimize Bayesian optimization](https://scikit-optimize.github.io/stable/auto_examples/bayesian-optimization.html)
