# Clinic Discussion Checklist

Use this page when discussing data access with IVF doctors, embryologists or clinic administrators.

## Purpose

We are not asking for identifiable patient data at the discussion stage.

The first goal is only to understand:

- what data exists
- what format it is stored in
- what outcomes are available
- whether anonymized research use is possible
- whether doctors can review AI explanations

## Core Questions

| Question | Why It Matters |
| --- | --- |
| How many IVF cycles are available? | Determines model feasibility. |
| Which years are available? | Determines time coverage and possible temporal validation. |
| Is the data digital or paper-based? | Determines extraction effort. |
| Is clinical pregnancy recorded? | Minimum outcome feasibility. |
| Is live birth recorded? | Stronger thesis outcome. |
| Are embryo grades recorded? | Determines whether embryological data can be included. |
| Are stimulation dose and trigger details recorded? | Determines whether ovarian stimulation CDSS is feasible. |
| Are lifestyle variables recorded? | Determines whether lifestyle can enter title/objectives. |
| Can a lifestyle questionnaire be added prospectively? | Alternative if historical lifestyle data are missing. |
| Is data from more than one clinic possible? | Determines external validation feasibility. |
| Can data be anonymized? | Required for ethics and privacy. |
| Can clinicians review model explanations? | Determines decision-support usability evaluation. |

## Minimum Data Request

Ask whether these fields are available:

- patient age
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
- clinical pregnancy outcome
- live-birth outcome if available

## Embryology Data Request

Ask whether these fields are available:

- number of oocytes retrieved
- number of mature oocytes
- fertilization rate
- embryo grade
- blastocyst grade
- transfer day
- number of embryos transferred
- embryo freezing details

## Lifestyle Data Request

Ask whether these are recorded or can be collected:

- smoking
- alcohol
- sleep
- stress
- physical activity
- diet pattern
- caffeine
- occupation
- environmental exposure

## Ethics and Privacy Questions

- Can all patient identifiers be removed?
- Who will approve data access?
- Is institutional ethics approval required?
- Can data be exported as Excel/CSV?
- Can a data-sharing agreement be signed?
- Can only anonymized cycle IDs be used?

## Doctor Review Questions

Ask whether clinicians can review sample AI outputs such as:

- predicted success probability
- top positive factors
- top negative factors
- modifiable factors
- non-modifiable factors
- uncertainty/caution note
- suggested counseling summary

## Decision After Discussion

| If Clinic Confirms | Then Use |
| --- | --- |
| Only clinical data | Clinical-data title |
| Clinical + embryo data | Multimodal clinical and embryological title |
| Clinical + embryo + lifestyle data | Lifestyle-data title |
| Multiple clinics | External validation title extension |
| Clinician review possible | CDSS usability evaluation objective |
