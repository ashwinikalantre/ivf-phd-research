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

## Feature

**Simple meaning:** An input variable used by a model.

**Example:** Age, BMI, AMH, AFC, follicle count, embryo grade or stimulation protocol.

**For our research:** Good feature definition is essential because IVF data comes from many clinical stages.

Deep reading:

- [Google ML Crash Course: numerical data](https://developers.google.com/machine-learning/crash-course/numerical-data)

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

## Calibration

**Simple meaning:** How closely predicted probabilities match actual observed outcomes.

**Example:** If a model predicts 60% pregnancy probability for many patients, about 60% of similar patients should actually become pregnant.

**For our research:** Calibration matters because IVF counseling depends on probability, not only ranking.

Deep reading:

- [scikit-learn probability calibration](https://scikit-learn.org/stable/modules/calibration.html)

## Bayesian Optimization

**Simple meaning:** A method for efficiently searching model settings by using previous results to choose better next trials.

**Why it matters:** It is used for hyperparameter tuning when there are many possible model settings.

**For our research:** It can improve model tuning, but it does not replace external validation.

Deep reading:

- [scikit-optimize Bayesian optimization](https://scikit-optimize.github.io/stable/auto_examples/bayesian-optimization.html)
