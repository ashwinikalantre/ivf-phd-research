# Faculty Speaker Script

This script is for a 12-15 minute faculty presentation. Use simple language and keep the discussion focused on the research journey, not only the final topic.

## Opening

Good morning respected faculty members.

My broad research area is women’s healthcare, with primary focus on IVF. I started with the question: where can computer applications, especially AI and machine learning, make a scientifically useful contribution in IVF?

I have not fixed the final PhD title prematurely. I followed a step-by-step process: broad area, literature review, existing work, limitations, repeated gaps, research problem, research questions, objectives and then topic direction.

## Why IVF

IVF is important because infertility affects many couples and treatment decisions are complex, costly and emotionally difficult.

WHO estimates that about one in six adults experience infertility in their lifetime. In IVF, success depends on many factors such as age, ovarian reserve, diagnosis, treatment protocol, embryo quality and clinic workflow.

So this is not only a medical problem. It is also a data, prediction, explanation and decision-support problem.

## Literature Review Method

I focused mainly on papers from 2021 to 2025. I reviewed AI in IVF, machine learning, explainable AI, clinical decision support, personalized treatment recommendation, healthcare informatics and predictive analytics.

For each paper I extracted objective, dataset, features, method, evaluation metrics, findings, limitations and future work.

The purpose was not just to summarize papers. The purpose was to identify repeated gaps across many studies.

## What Existing Work Shows

Existing studies show that machine learning can predict IVF outcomes such as clinical pregnancy, live birth, embryo selection, ovarian response and stimulation decisions.

Common models include logistic regression, Random Forest, XGBoost, LightGBM and neural networks. Some studies also use explainable AI methods such as SHAP.

This means the field is active, but also that simple prediction alone is not enough for a PhD contribution.

## Repeated Gaps

After reviewing the papers, the strongest repeated gaps are:

- lack of external validation
- limited clinical decision-support translation
- limited real-world deployment evidence
- retrospective or single-center studies
- limited explainability and trust evaluation
- limited Indian population or local validation
- limited use of lifestyle data

The important point is that I am not treating every limitation as a research gap. I am focusing on gaps that appear repeatedly.

## Research Problem

The research problem can be stated like this:

Many IVF prediction models show promising performance, but they often remain model-centric. They are not always explainable, externally validated, personalized or translated into clinician-usable decision-support systems.

This creates a gap between AI model development and practical IVF decision support.

## Provisional Direction

Based on the repeated gaps, the current working direction is:

An explainable and personalized clinical decision-support framework for IVF outcome prediction using clinical and embryological data.

This is still conditional. If embryology data is not available, the title will be adjusted. If lifestyle data is available, it can be included. If more than one clinic is available, external validation can be added.

## Research Questions

The main research questions are:

1. Which clinical, treatment and embryological variables are most useful for IVF outcome prediction?
2. Which machine learning models provide good predictive performance and calibration?
3. How can explainable AI help clinicians understand patient-level predictions?
4. Can the model output be converted into a useful clinical decision-support format?
5. How well does the model generalize across time, subgroup or clinic data if available?

## Proposed Technical Approach

The technical plan is to start with structured IVF data.

First, clean and map the data. Then train baseline and advanced models. Logistic regression will be used as a baseline. Random Forest, XGBoost and LightGBM can be compared for stronger tabular-data performance.

The evaluation will include AUC, sensitivity, specificity, F1 score, calibration and possibly decision curve analysis.

Explainability will be added using SHAP or similar methods, and clinician review will be used if possible.

## Dataset Dependency

The next major step is clinic data confirmation.

There are five important feasibility questions:

1. What IVF dataset can be accessed?
2. Does the dataset include embryo variables?
3. Does it include lifestyle variables?
4. Is there more than one clinic or source for validation?
5. Can clinicians review explanation outputs?

These answers will decide the final title and methodology.

## Expected Contribution

The expected contribution is not only a machine learning model.

The expected contribution is a framework that connects IVF data, predictive modeling, explainable AI, validation and doctor-facing decision support.

The system will not replace doctors. It will support counseling and decision-making by showing probability, important positive and negative factors, and explanation of model output.

## Closing

At this stage, the work has produced a structured literature matrix, gap-frequency analysis, theme classification, research problem, provisional research questions and a technical blueprint.

The immediate next step is data collection discussion with IVF doctors and clinics. After dataset feasibility is confirmed, the final title, objectives and methodology can be fixed with stronger confidence.

## If Faculty Ask For The Final Title

Answer:

The final title should not be fixed before data access is confirmed. The current working title is:

**An Explainable and Personalized Clinical Decision Support Framework for IVF Outcome Prediction Using Multimodal Clinical and Embryological Data**

If the available data changes, the title will be adjusted responsibly.

## If Faculty Ask What Is New

Answer:

Using machine learning in IVF is not new. The contribution is to move from model-only prediction toward an explainable, personalized and clinician-reviewed decision-support framework, validated on available Indian clinic data as far as possible.
