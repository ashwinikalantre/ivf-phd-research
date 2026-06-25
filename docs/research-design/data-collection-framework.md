# IVF Data Collection Framework

This page defines the data variables needed for the proposed IVF AI research.

The goal is to discuss feasibility with IVF doctors and clinics before finalizing the title.

## Data Collection Logic

Variables are grouped into four levels:

| Level | Meaning |
| --- | --- |
| Mandatory | Minimum variables required for any IVF outcome prediction model. |
| Recommended | Strongly useful for personalization and better model performance. |
| Optional | Useful if available, but not essential. |
| Sensitive | Can improve research but needs stronger privacy and ethics handling. |

## Outcome Variables

These are the target variables. At least one clear outcome is required.

| Variable | Priority | Notes |
| --- | --- | --- |
| Clinical pregnancy | Mandatory | Usually defined by gestational sac or fetal heartbeat. |
| Live birth | Recommended | Stronger outcome than pregnancy, but may be harder to collect. |
| Biochemical pregnancy | Optional | Useful as intermediate outcome. |
| Miscarriage | Optional | Useful for post-transfer risk modeling. |
| Implantation success | Optional | Useful when embryo-level data are available. |
| Cycle cancellation | Optional | Useful for ovarian stimulation modeling. |
| Number of oocytes retrieved | Recommended | Important for stimulation response. |
| Number of mature oocytes | Recommended | Important for ovarian response and trigger decisions. |
| Number of embryos formed | Recommended | Useful intermediate ART outcome. |
| Number of good-quality embryos/blastocysts | Recommended | Useful for embryo development prediction. |

## Patient Demographic Variables

| Variable | Priority | Notes |
| --- | --- | --- |
| Patient age | Mandatory | One of the strongest IVF predictors. |
| BMI | Mandatory | Important clinical and lifestyle-linked factor. |
| Height and weight | Recommended | Allows BMI verification. |
| Duration of infertility | Mandatory | Common predictor. |
| Type of infertility | Mandatory | Primary or secondary infertility. |
| Cause of infertility | Mandatory | Female factor, male factor, unexplained, tubal, endometriosis, PCOS etc. |
| Previous IVF attempts | Recommended | Important for prognosis. |
| Previous pregnancies | Recommended | Obstetric history. |
| Previous live births | Recommended | Prognostic and counseling relevance. |
| Previous miscarriages | Recommended | Useful for risk modeling. |
| Socioeconomic indicators | Optional/Sensitive | Education, occupation, income; useful but privacy-sensitive. |

## Female Clinical and Hormonal Variables

| Variable | Priority | Notes |
| --- | --- | --- |
| AMH | Mandatory | Key ovarian reserve marker. |
| AFC | Mandatory | Important ovarian reserve marker. |
| Basal FSH | Recommended | Ovarian reserve. |
| Basal LH | Recommended | Hormonal profile. |
| Estradiol/E2 | Recommended | Baseline or stimulation monitoring. |
| Progesterone | Recommended | Especially on trigger/HCG day. |
| TSH | Optional | Thyroid status may affect fertility. |
| Prolactin | Optional | Endocrine factor. |
| PCOS status | Recommended | Important subgroup. |
| Endometriosis status | Recommended | Important subgroup. |
| Tubal factor | Recommended | Infertility diagnosis. |
| Uterine abnormalities | Optional | Fibroids, polyps, congenital anomalies. |
| Menstrual cycle regularity | Optional | Useful clinical context. |

## Male Partner Variables

| Variable | Priority | Notes |
| --- | --- | --- |
| Male age | Recommended | May affect embryo and pregnancy outcomes. |
| Sperm concentration/count | Recommended | Semen parameter. |
| Sperm motility | Recommended | Semen parameter. |
| Sperm morphology | Recommended | Semen parameter. |
| Male factor infertility diagnosis | Mandatory if available | Important infertility cause. |
| DNA fragmentation index | Optional | Useful if available. |

## Treatment Cycle Variables

| Variable | Priority | Notes |
| --- | --- | --- |
| IVF or ICSI | Mandatory | Treatment type. |
| Fresh or frozen transfer | Mandatory | Major workflow difference. |
| Stimulation protocol | Mandatory | Agonist, antagonist, mild stimulation etc. |
| Gonadotropin starting dose | Recommended | Important for stimulation personalization. |
| Total gonadotropin dose | Recommended | Treatment burden and response. |
| Stimulation duration | Recommended | Ovarian response. |
| Trigger type | Recommended | HCG, GnRH agonist, dual trigger etc. |
| Trigger day | Recommended | Timing variable. |
| Follicle count by size | Recommended | Very useful for XAI stimulation modeling. |
| Estradiol on trigger day | Recommended | Ovarian response. |
| Progesterone on trigger day | Recommended | Fresh-transfer outcome relevance. |
| Endometrial thickness | Mandatory | Common predictor. |
| Endometrial pattern | Recommended | If available from ultrasound. |

## Embryology Variables

These decide whether the title can include `embryological data`.

| Variable | Priority | Notes |
| --- | --- | --- |
| Number of oocytes retrieved | Mandatory for embryology level | Basic lab outcome. |
| Number of mature oocytes/MII | Recommended | Oocyte maturity. |
| Fertilization method | Mandatory | IVF/ICSI/split. |
| Fertilization rate | Recommended | Lab performance variable. |
| Number of embryos formed | Recommended | Intermediate outcome. |
| Cleavage-stage embryo grade | Optional | If day-3 transfer data exist. |
| Blastocyst grade | Recommended | Important for blastocyst transfer. |
| Inner cell mass grade | Optional | Detailed blastocyst quality. |
| Trophectoderm grade | Optional | Detailed blastocyst quality. |
| Day of embryo transfer | Recommended | Day 3, day 5, day 6 etc. |
| Number of embryos transferred | Mandatory | Strong predictor and clinical decision variable. |
| Frozen embryo count | Optional | Cumulative outcome relevance. |
| PGT-A/ploidy status | Optional/Sensitive | Strong but ethically and practically sensitive. |
| Embryo image/time-lapse data | Optional/Sensitive | Useful for deep learning, but difficult to access and store. |

## FET and Endometrial Variables

| Variable | Priority | Notes |
| --- | --- | --- |
| FET protocol | Recommended | Natural, modified natural, HRT etc. |
| Endometrial preparation details | Recommended | Estrogen/progesterone regimen. |
| Progesterone exposure before transfer | Optional | Useful for implantation window. |
| Endometrial thickness before transfer | Mandatory if FET | Important predictor. |
| Ultrasound images | Optional/Sensitive | Required for radiomics; not mandatory. |

## Lifestyle and Contextual Variables

These decide whether the title can include `lifestyle data`.

| Variable | Priority | Notes |
| --- | --- | --- |
| Smoking status | Recommended | Important lifestyle risk factor. |
| Alcohol use | Optional/Sensitive | Needs careful wording and privacy. |
| Physical activity | Optional | Can be collected by questionnaire. |
| Sleep quality | Optional | Patient-reported variable. |
| Stress level | Optional | Use validated scale if possible. |
| Diet pattern | Optional | Broad self-report possible. |
| Caffeine intake | Optional | Patient-reported. |
| Occupational exposure | Optional/Sensitive | Heat, chemicals, shift work etc. |
| Environmental exposure | Optional/Sensitive | Pollution, toxins etc. |

## Clinic and Workflow Variables

These help with validation and real-world deployment.

| Variable | Priority | Notes |
| --- | --- | --- |
| Clinic ID | Recommended | Needed for multi-center validation; anonymized. |
| Doctor/consultant ID | Optional/Sensitive | Useful for workflow variation, but privacy-sensitive. |
| Embryologist ID | Optional/Sensitive | Useful for lab variation, but sensitive. |
| Year of treatment | Recommended | Temporal validation. |
| Protocol changes over time | Optional | Helps interpret model drift. |

## Minimum Dataset Scenario

If only a basic clinical dataset is available, minimum required fields are:

- age
- BMI
- infertility duration
- infertility diagnosis
- AMH
- AFC
- IVF/ICSI
- fresh/frozen transfer
- stimulation protocol
- endometrial thickness
- number of embryos transferred
- clinical pregnancy or live birth outcome

Possible safe title:

**An Explainable Clinical Decision Support Framework for IVF Outcome Prediction Using Clinical Data**

## Strong Dataset Scenario

If clinical and embryology data are available:

- all minimum clinical variables
- oocytes retrieved
- mature oocytes
- fertilization rate
- embryo grade
- blastocyst grade
- transfer day
- number of embryos transferred

Possible title:

**An Explainable and Personalized Clinical Decision Support Framework for IVF Outcome Prediction Using Multimodal Clinical and Embryological Data**

## Best Dataset Scenario

If clinical, embryology and lifestyle data are available:

- clinical variables
- embryology variables
- lifestyle questionnaire variables
- patient context variables

Possible title:

**An Explainable Multimodal Clinical Decision Support Framework for Personalized IVF Outcome Prediction Using Clinical, Embryological and Lifestyle Data**

## Multi-Center Scenario

If data are available from more than one clinic:

Possible title extension:

**with External Validation in Indian IVF Settings**

## Clinic Discussion Questions

Ask doctors or clinic administrators:

1. What IVF data fields are routinely recorded?
2. Are clinical and embryology data stored together?
3. Is live-birth outcome available, or only pregnancy outcome?
4. Is embryo grade available in structured format?
5. Is lifestyle information collected currently?
6. Can lifestyle data be collected by questionnaire?
7. Can data be anonymized for research?
8. How many years of historical IVF data are available?
9. Approximately how many IVF cycles are available?
10. Is data from more than one clinic possible?
11. Can clinicians review AI explanation outputs?
12. Is an ethics committee approval required, and who will support it?
