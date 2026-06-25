# Conceptual Framework

## Working Framework

```mermaid
flowchart TD
    A["Patient and Clinical Data"] --> D["Data Integration"]
    B["Embryology and Laboratory Data"] --> D
    C["Lifestyle and Context Data"] --> D
    U["Ultrasound / Imaging / Radiomics"] --> D
    D --> E["Preprocessing and Feature Engineering"]
    E --> F["Predictive ML Model"]
    F --> G["Calibration and Validation"]
    G --> H["Explainability Layer"]
    H --> I["Clinician Decision Support"]
    H --> J["Patient-Centered Explanation"]
    I --> K["Personalized IVF Recommendation"]
    J --> K
```

## Input Data Groups

| Group | Examples |
| --- | --- |
| Demographic | age, BMI, infertility duration, prior cycles |
| Clinical | AMH, AFC, FSH, LH, progesterone, estradiol, PCOS/endometriosis status |
| Treatment cycle | stimulation protocol, gonadotropin dose, trigger timing, retrieved oocytes |
| Embryology | embryo grade, blastocyst quality, oocyte quality, sperm parameters |
| Imaging | embryo images, time-lapse videos, ultrasound/radiomics |
| Lifestyle | smoking, diet, physical activity, sleep, stress, occupation, environmental factors |

## Model Outputs

- predicted clinical pregnancy probability
- predicted live-birth probability
- predicted ovarian response
- key positive and negative drivers
- personalized treatment or counseling suggestion
- uncertainty and caution notes

## Evaluation Dimensions

- AUC, accuracy, sensitivity, specificity, precision, recall and F1
- calibration
- external validation
- subgroup/fairness analysis
- explanation quality
- clinician usability
- patient understandability
