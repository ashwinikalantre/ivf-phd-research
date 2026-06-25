# Research Implementation Roadmap

This roadmap shows how the actual PhD work may proceed after data access is confirmed.

## Roadmap Summary

```mermaid
flowchart LR
    A["Clinic Data Access"] --> B["Data Cleaning"]
    B --> C["EDA"]
    C --> D["Baseline Models"]
    D --> E["Advanced Models"]
    E --> F["Explainable AI"]
    F --> G["Validation"]
    G --> H["CDSS Prototype"]
    H --> I["Clinician Review"]
    I --> J["Thesis and Publication"]
```

## Phase 1: Data Access

Goal:

Get anonymized IVF data from one or more clinics.

Key work:

- ethics permission
- data-sharing approval
- variable list confirmation
- anonymization plan

Main risk:

Data may be incomplete or not available in digital format.

## Phase 2: Data Preparation

Goal:

Prepare a clean research dataset.

Key work:

- missing-value handling
- duplicate record removal
- variable mapping
- outcome definition
- train-test split

Main risk:

Outcome fields may be missing or inconsistent.

## Phase 3: Exploratory Data Analysis

Goal:

Understand the dataset before modeling.

Key work:

- patient age distribution
- diagnosis distribution
- pregnancy/live-birth rate
- missing data pattern
- relation between key variables and outcome

Main risk:

Class imbalance may be high.

## Phase 4: Model Development

Goal:

Build baseline and advanced prediction models.

Suggested order:

1. Logistic Regression
2. Random Forest
3. XGBoost or LightGBM

Main risk:

High accuracy may not mean clinical usefulness.

## Phase 5: Explainable AI

Goal:

Explain model predictions.

Possible methods:

- SHAP
- LIME
- permutation importance

Main output:

- global feature importance
- patient-level explanation
- modifiable and non-modifiable factor list

## Phase 6: Validation

Goal:

Check whether the model is reliable.

Validation options:

- train-test validation
- cross-validation
- temporal validation
- subgroup validation
- external validation if another clinic is available

Main risk:

Model may perform well internally but poorly on another clinic.

## Phase 7: CDSS Prototype

Goal:

Convert model output into doctor-friendly decision support.

Prototype should show:

- predicted outcome probability
- key positive factors
- key negative factors
- explanation summary
- caution note
- doctor review step

## Phase 8: Clinician Review

Goal:

Check whether the output is useful and understandable for doctors.

Possible review method:

- structured questionnaire
- short interview
- expert feedback form

Main question:

Would this help counseling without replacing clinical judgment?

## Final Output

Expected final outputs:

- cleaned IVF dataset structure
- prediction model
- explainability module
- validation results
- CDSS prototype
- clinician feedback
- thesis and research papers
