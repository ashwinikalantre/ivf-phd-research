# FET, Endometrial Receptivity, Ultrasound and Radiomics

## Papers in This Theme

| No | Year | Title | Method | Dataset | Gap Found |
| --- | --- | --- | --- | --- | --- |
| 10 | 2025 | Optimizing predictive features using machine learning for early miscarriage risk following single vitrified-warmed blastocyst transfer | Logistic Regression, Random Forest, Gradient Boosting, Voting Classifier. | Dual-center retrospective analysis of 1,664 SVBT cycles, including 308 early miscarriage cases. | Retrospective Design; Limited Multi-center Validation; Need Clinical Decision Support |
| 25 | 2025 | An explainable ultrasound-based machine learning model for predicting reproductive outcomes after frozen embryo transfer | Radiomics model, clinical logistic regression model, XGBoost fusion model, SHAP explanations. | Prospective study of 787 infertile females undergoing FET; train n=550, test n=237. | Single-center Study; Need External Validation; Need Multimodal Data; Manual/Subjective Workflow Bias |
| 33 | 2025 | Development of an explainable machine learning model to predict live birth versus miscarriage among IVF-ET pregnancies | XGBoost, LightGBM, Logistic Regression and soft-voting ensemble with SHAP explanations. | Public Yuan et al. dataset from Qingdao Women's and Children's Hospital, China; 1,017 singleton IVF-ET pregnancies with confirmed intrauterine pregnancy; 52-55 clinical, hormonal, immune, coagulation and treatment-related variables. | Need External Validation; Single-center Study; Retrospective Design; Need Clinical Decision Support; Trustworthy AI Gap; Real-world Deployment Gap |

## Existing Work

- Recent work uses ultrasound radiomics, endometrial features and clinical variables to predict FET outcomes, miscarriage or live birth.
- Fusion models combining imaging-derived scores with clinical data can outperform single-modality models.
- SHAP and other XAI tools are being used to provide individual-level explanation.

## Repeated Limitations

- Single-center datasets are common.
- Manual ROI drawing in ultrasound/radiomics may introduce subjectivity.
- FET-specific models may not generalize to fresh embryo transfer.
- External multicenter validation remains limited.

## Usable Research Gaps

- Multimodal endometrium plus clinical prediction with external validation.
- Automated or standardized imaging feature extraction.
- Explainable FET counseling support.

## Supervisor View

This theme is promising but narrower. It can support the multimodal framework, especially if ultrasound/endometrial data are available. Without such data, it should remain a supporting theme.
