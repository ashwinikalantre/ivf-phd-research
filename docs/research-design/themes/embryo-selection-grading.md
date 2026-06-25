# Embryo Selection, Embryo Grading and Ploidy Prediction

## Papers in This Theme

| No | Year | Title | Method | Dataset | Gap Found |
| --- | --- | --- | --- | --- | --- |
| 3 | 2025 | Multimodal intelligent prediction model for in vitro fertilization | Multimodal deep learning model for post-transfer outcome prediction. | Chinese IVF data; day-3 transferred embryos only. | Need External Validation; Limited Population Diversity; No Pre-transfer Recommendation; Retrospective Design |
| 4 | 2025 | Deep learning classification integrating embryo images with associated clinical information from ART cycles | Deep learning image model with clinical-data fusion. | Embryo images and associated ART-cycle clinical data; transferred embryos only; limited database. | Small Dataset; Selection Bias; Need Multimodal Data; No Pre-transfer Recommendation |
| 24 | 2023 | Towards Automation in IVF: Pre-Clinical Validation of a Deep Learning-Based Embryo Grading System during PGT-A Cycles | iDAScore v1.0 deep learning model using 3D CNN. | Retrospective pre-clinical external validation including 3,604 blastocysts and 808 euploid transfers from 1,232 cycles. | Retrospective Design; Need External Validation; Need Prospective/RCT Validation; Black-box/Explainability Gap |
| 26 | 2021 | Interpretable, not black-box, artificial intelligence should be used for embryo selection | Ethical and methodological critique. | Commentary/review of embryo-selection AI literature. | Black-box/Explainability Gap; Trustworthy AI Gap; Need Prospective/RCT Validation; Patient-centered XAI Gap |
| 27 | 2024 | Beyond black-box models: explainable AI for embryo ploidy prediction and patient-centric consultation | RF, LDA, LR, SVM, AdaBoost and LightGBM with SHAP and LIME. | 1,908 blastocyst embryos with ploidy status, morphokinetic features, morphology grades and 11 clinical variables. | Black-box/Explainability Gap; Patient-centered XAI Gap; Need External Validation |
| 28 | 2024 | Deep learning versus manual morphology-based embryo selection in IVF: a randomized, double-blind noninferiority trial | Deep learning embryo selection using iDAScore compared with embryologist morphology-based selection. | Multicenter randomized double-blind noninferiority trial across 14 IVF clinics in Australia and Europe; 1,066 patients, 533 per arm. | Need Prospective/RCT Validation; Need Real-world Deployment Evidence; Trustworthy AI Gap; Clinical Utility Gap |

## Existing Work

- Deep learning is widely applied to embryo images, time-lapse data, morphology and ploidy-related prediction.
- Some systems aim to automate embryo ranking and reduce inter-observer variation.
- The 2024 Nature Medicine randomized trial is important because it tests AI embryo selection prospectively rather than relying only on retrospective model performance.

## Repeated Limitations

- Image-only or transferred-embryo-only datasets may introduce selection bias.
- Black-box embryo selection raises ethical and trust concerns.
- The Nature Medicine RCT did not demonstrate noninferiority for clinical pregnancy, though it improved evaluation time.
- Many models are not trained or validated for the actual clinical decision: choosing among embryos of similar apparent quality.

## Usable Research Gaps

- Explainable embryo-selection support rather than opaque automated ranking.
- Clinical utility evaluation, not only AUC/accuracy.
- Integration of embryo features with clinical and patient context.

## Supervisor View

Embryo AI is an important theme, but a thesis focused only on embryo image grading may become too laboratory-specific. It is better used as one component of a broader multimodal IVF decision-support framework.
