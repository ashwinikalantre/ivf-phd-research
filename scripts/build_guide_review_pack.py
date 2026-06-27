from pathlib import Path
import csv
import io

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "guide_review_pack"


def load_literature_rows():
    matrix = ROOT / "docs" / "evidence-base" / "literature-matrix.md"
    rows = []
    for line in matrix.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "):
            continue
        if line.startswith("| No ") or line.startswith("| ---"):
            continue
        raw = line.strip().strip("|")
        parsed = next(csv.reader(io.StringIO(raw), delimiter="|", skipinitialspace=True))
        cells = [cell.strip() for cell in parsed]
        if len(cells) != 9:
            continue
        rows.append(
            {
                "no": cells[0],
                "year": cells[1],
                "title": cells[2],
                "journal": cells[3],
                "objective": cells[4],
                "method": cells[5],
                "dataset": cells[6],
                "gap": cells[7],
                "relevance": cells[8],
            }
        )
    return rows


def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_cell_text(cell, text, bold=False, font_size=9):
    cell.text = ""
    paragraph = cell.paragraphs[0]
    paragraph.paragraph_format.space_after = Pt(0)
    run = paragraph.add_run(str(text))
    run.bold = bold
    run.font.name = "Calibri"
    run.font.size = Pt(font_size)


def add_table(doc, headers, rows, widths=None):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    for i, header in enumerate(headers):
        set_cell_text(hdr[i], header, bold=True)
        set_cell_shading(hdr[i], "F2F4F7")
        hdr[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        if widths:
            hdr[i].width = Inches(widths[i])
    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            set_cell_text(cells[i], value)
            cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if widths:
                cells[i].width = Inches(widths[i])
    doc.add_paragraph()
    return table


def add_compact_paper_table(doc, rows):
    headers = ["Paper", "Focus and Method", "Dataset / Evidence", "Main Gap / Use"]
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    for i, header in enumerate(headers):
        set_cell_text(table.rows[0].cells[i], header, bold=True, font_size=8)
        set_cell_shading(table.rows[0].cells[i], "F2F4F7")
    for row in rows:
        cells = table.add_row().cells
        values = [
            f'Paper {row["no"]} ({row["year"]})\n{row["title"]}\n{row["journal"]}',
            f'{row["objective"]}\nMethod: {row["method"]}',
            row["dataset"],
            f'{row["gap"]}\nRelevance: {row["relevance"]}',
        ]
        for i, value in enumerate(values):
            set_cell_text(cells[i], value, font_size=8)
            cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    doc.add_paragraph()
    return table


def add_bullets(doc, items):
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(item)


def add_numbered(doc, items):
    for item in items:
        p = doc.add_paragraph(style="List Number")
        p.add_run(item)


def setup_doc(title, subtitle):
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

    styles = doc.styles
    styles["Normal"].font.name = "Calibri"
    styles["Normal"].font.size = Pt(11)
    styles["Normal"].paragraph_format.space_after = Pt(6)
    styles["Normal"].paragraph_format.line_spacing = 1.1

    for style_name, size, color in [
        ("Heading 1", 16, RGBColor(46, 116, 181)),
        ("Heading 2", 13, RGBColor(46, 116, 181)),
        ("Heading 3", 12, RGBColor(31, 77, 120)),
    ]:
        style = styles[style_name]
        style.font.name = "Calibri"
        style.font.size = Pt(size)
        style.font.color.rgb = color
        style.paragraph_format.space_before = Pt(8)
        style.paragraph_format.space_after = Pt(4)

    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    title_run = title_p.add_run(title)
    title_run.bold = True
    title_run.font.name = "Calibri"
    title_run.font.size = Pt(20)
    title_run.font.color.rgb = RGBColor(11, 37, 69)

    sub_p = doc.add_paragraph()
    sub_run = sub_p.add_run(subtitle)
    sub_run.font.name = "Calibri"
    sub_run.font.size = Pt(11)
    sub_run.font.color.rgb = RGBColor(85, 85, 85)

    doc.add_paragraph()
    return doc


def save_doc(doc, filename):
    path = OUT / filename
    doc.save(path)
    return path


def literature_summary():
    doc = setup_doc(
        "Compact Literature Review Summary",
        "Guide review pack | AI, ML, XAI and decision support in IVF | Working evidence base",
    )
    doc.add_heading("Purpose", level=1)
    doc.add_paragraph(
        "This document summarizes the current literature-review work for guide discussion. "
        "It is not a final thesis chapter. Detailed extraction remains in the Excel workbook and individual paper notes."
    )
    doc.add_heading("Review Scope", level=1)
    add_table(
        doc,
        ["Item", "Current Status"],
        [
            ["Domain", "Women’s healthcare, focused on IVF and assisted reproductive technology."],
            ["Technical area", "AI, machine learning, explainable AI, clinical decision support and personalized prediction."],
            ["Primary time window", "2021-2025, with a few highly relevant 2026 synthesis/model papers kept as supporting evidence."],
            ["Current reviewed notes", "35 structured paper notes."],
            ["Main source of detail", "Excel literature review matrix and paper-wise documentation pages."],
        ],
        [1.7, 4.6],
    )
    doc.add_heading("Strong Literature Signals", level=1)
    add_bullets(
        doc,
        [
            "Many recent IVF-AI papers focus on prediction of live birth, clinical pregnancy, implantation, miscarriage or ovarian response.",
            "Several studies use tabular clinical data with models such as logistic regression, random forest, XGBoost and LightGBM.",
            "Embryo-image and embryo-selection AI are active areas, but stronger datasets and clinical validation are often required.",
            "Explainability is repeatedly discussed as important for clinical trust, patient communication and ethical AI use.",
            "Decision-support framing is safer than claiming that AI can replace clinical judgment.",
        ],
    )
    doc.add_heading("Representative Paper Groups", level=1)
    add_table(
        doc,
        ["Group", "Examples", "Use in Topic Discovery"],
        [
            ["Live-birth / pregnancy prediction", "Papers 5, 6, 7, 8, 9, 29, 30, 31, 33", "Supports outcome-prediction direction."],
            ["XAI / trustworthy AI", "Papers 1, 14, 25, 26, 27, 33", "Supports explainable model and explanation-output direction."],
            ["CDSS / personalization", "Papers 2, 21, 22, 23", "Supports clinical decision-support and treatment-personalization direction."],
            ["Embryo AI", "Papers 3, 4, 24, 26, 27, 28", "Useful if embryo variables or images are available."],
            ["Review / trend papers", "Papers 12, 13, 15, 32, 34, 35", "Useful for background, gaps and justification."],
        ],
        [1.45, 1.9, 2.95],
    )
    doc.add_heading("Current Interpretation", level=1)
    doc.add_paragraph(
        "The strongest working direction is explainable and personalized IVF outcome prediction with a clinical decision-support framing. "
        "The final title should remain open until clinic data feasibility is confirmed."
    )
    doc.add_page_break()
    doc.add_heading("Paper-Wise Compact Summary", level=1)
    doc.add_paragraph(
        "This section gives a compact guide-facing summary of the current 35 reviewed papers. "
        "It is derived from the working literature matrix; full extraction fields remain in the Excel workbook and paper-wise notes."
    )
    add_compact_paper_table(doc, load_literature_rows())
    return save_doc(doc, "02_compact_literature_review_summary.docx")


def theme_gap_analysis():
    doc = setup_doc(
        "Theme and Gap Analysis",
        "Guide review pack | How the current topic direction emerged from repeated literature signals",
    )
    doc.add_heading("Why Themes Were Created", level=1)
    doc.add_paragraph(
        "Theme classification helps convert individual papers into research directions. "
        "It prevents title selection from depending on a single paper or isolated limitation."
    )
    doc.add_heading("Theme Classification Logic", level=1)
    doc.add_paragraph(
        "The review was organized as: paper-wise extraction, theme grouping, repeated-gap analysis, research opportunity identification, "
        "and then candidate topic development. The final title should emerge from repeated gaps and dataset feasibility, not from a single attractive keyword."
    )
    doc.add_heading("Major Theme Groups", level=1)
    add_table(
        doc,
        ["Major Theme", "Paper Examples", "How It Helps Topic Selection", "Dataset Dependency"],
        [
            [
                "IVF outcome prediction",
                "5, 6, 7, 8, 9, 15, 29, 30, 31, 33",
                "Provides the core predictive analytics direction: clinical pregnancy, live birth, miscarriage or related IVF outcome.",
                "Needs a clear outcome variable; live birth is strongest but may be harder to collect.",
            ],
            [
                "Explainable / trustworthy AI",
                "1, 14, 25, 26, 27, 33",
                "Supports moving beyond black-box prediction toward interpretable, patient-level and clinician-facing explanations.",
                "Needs model outputs that can be explained; clinician review is ideal.",
            ],
            [
                "Clinical decision support",
                "2, 21, 22, 23, 34",
                "Positions the PhD as a usable framework, not only an accuracy comparison study.",
                "Needs careful framing: support clinical counseling or planning, not replace doctors.",
            ],
            [
                "Personalization",
                "1, 2, 12, 21, 23",
                "Supports patient-specific prediction and treatment-context interpretation.",
                "Needs enough patient-level variables and subgroup size.",
            ],
        ],
        [1.35, 1.1, 2.55, 1.35],
    )
    doc.add_heading("Supporting Themes", level=1)
    add_table(
        doc,
        ["Supporting Theme", "Paper Examples", "Use", "Caution"],
        [
            [
                "Embryo and multimodal AI",
                "3, 4, 24, 27, 28",
                "Useful if embryology variables, embryo grades, images or time-lapse data are available.",
                "Do not promise image/deep-learning work without data access.",
            ],
            [
                "Ovarian stimulation / protocol decision support",
                "1, 2, 21, 22, 23",
                "Strong direction if dose, trigger and stimulation-monitoring records are available.",
                "May require more detailed clinical workflow data than basic outcome prediction.",
            ],
            [
                "Indian/context-specific validation",
                "1, 5, 29",
                "Potentially important because many models are not validated in Indian IVF settings.",
                "Should appear in title only if Indian clinic data and validation are feasible.",
            ],
            [
                "Lifestyle and contextual data",
                "Mainly from planned data framework, not yet a strong repeated paper gap",
                "Can enrich personalization if reliably collected.",
                "Should remain conditional until questionnaire/data feasibility is confirmed.",
            ],
        ],
        [1.45, 1.15, 2.25, 1.5],
    )
    doc.add_heading("Repeated Gap Assessment", level=1)
    add_table(
        doc,
        ["Gap", "Frequency", "Evidence Strength", "Actionable in PhD?", "Topic Relevance"],
        [
            [
                "Need external validation",
                "26",
                "Very strong",
                "Conditional",
                "Strong if independent clinic, source or time-period data is available.",
            ],
            [
                "Need clinical decision support",
                "18",
                "Very strong",
                "Yes",
                "Supports CDSS framing and avoids an accuracy-only thesis.",
            ],
            [
                "Need real-world deployment evidence",
                "9",
                "Strong",
                "Partly",
                "Useful for justification; full deployment may be future work.",
            ],
            [
                "Retrospective design",
                "9",
                "Strong",
                "Partly",
                "Can be handled through careful validation and honest limitation wording.",
            ],
            [
                "Trustworthy AI gap",
                "8",
                "Strong",
                "Yes",
                "Supports XAI, clinician review and conservative claims.",
            ],
            [
                "Single-center study",
                "6",
                "Moderate-strong",
                "Conditional",
                "Supports multi-center or temporal validation if feasible.",
            ],
        ],
        [1.4, 0.7, 1.05, 1.0, 2.2],
    )
    doc.add_heading("Strong Gaps Versus Conditional Gaps", level=1)
    add_table(
        doc,
        ["Gap Type", "Gaps", "How To Treat In Proposal"],
        [
            [
                "Strong repeated gaps",
                "External validation, clinical decision support, trustworthy/explainable AI, real-world clinical usefulness, retrospective/single-center limitations.",
                "Use these to justify the main research direction.",
            ],
            [
                "Conditional gaps",
                "Indian validation, lifestyle data, embryo-image/deep-learning work, multi-center validation.",
                "Use only if data access supports them.",
            ],
            [
                "Weak/not-yet-claimable gaps",
                "Any gap supported by only one paper or by our interest alone.",
                "Do not use as novelty claim until stronger evidence is collected.",
            ],
        ],
        [1.35, 2.6, 2.4],
    )
    doc.add_heading("Gaps To Treat Carefully", level=1)
    add_bullets(
        doc,
        [
            "Lifestyle data is promising, but should not be claimed as a repeated core gap unless clinic/questionnaire feasibility is confirmed.",
            "Indian population validation is valuable, but should appear in the final title only if Indian clinic data is available.",
            "Embryo-image deep learning should not be promised unless image or time-lapse data can be accessed ethically and practically.",
        ],
    )
    doc.add_heading("Working Research Opportunity", level=1)
    doc.add_paragraph(
        "The strongest current research opportunity is not simply to build another IVF prediction model. "
        "A more defensible PhD direction is to design an explainable, personalized and clinically usable decision-support framework "
        "for IVF outcome prediction, with the exact data modality and validation strategy finalized after clinic data feasibility is known."
    )
    doc.add_heading("What Should Not Be Claimed Yet", level=1)
    add_bullets(
        doc,
        [
            "Do not claim that AI will improve IVF success rates unless a clinical outcome study proves it.",
            "Do not claim external validation unless an independent source, clinic or time period is used.",
            "Do not include Indian women, lifestyle data or embryo images in the final title unless those data are confirmed.",
            "Do not present model accuracy as the only PhD contribution; explanation, validation and clinical usability matter.",
        ],
    )
    doc.add_heading("Guide Discussion Questions", level=1)
    add_numbered(
        doc,
        [
            "Which theme should be prioritized: outcome prediction, stimulation decision support or broader clinical decision support?",
            "Should the topic remain broad until data access is confirmed, or should it be narrowed now?",
            "Should Indian validation be part of the title, or only a conditional objective?",
            "Which gaps are strong enough for the proposal, and which should remain future work?",
            "What dataset scenario is realistic for the next meeting with doctors or clinics?",
        ],
    )
    return save_doc(doc, "03_theme_and_gap_analysis.docx")


def dataset_feasibility():
    doc = setup_doc(
        "Dataset Feasibility and Data Requirement Plan",
        "Guide review pack | Variables and feasibility questions before final title selection",
    )
    doc.add_heading("Purpose", level=1)
    doc.add_paragraph(
        "The final PhD topic depends heavily on clinic data access. This document identifies the minimum, strong and ideal data scenarios."
    )
    doc.add_heading("Minimum Viable Dataset", level=1)
    add_table(
        doc,
        ["Category", "Minimum Variables"],
        [
            ["Outcome", "Clinical pregnancy or live birth."],
            ["Demographic", "Age, BMI, infertility duration, infertility type/cause."],
            ["Clinical", "AMH, AFC, diagnosis such as PCOS/endometriosis if available."],
            ["Treatment", "IVF/ICSI, fresh/frozen transfer, stimulation protocol, endometrial thickness, embryos transferred."],
            ["Validation", "At least train/test or temporal split; external validation only if independent data exists."],
        ],
        [1.55, 4.8],
    )
    doc.add_heading("Strong Dataset Scenario", level=1)
    add_bullets(
        doc,
        [
            "Clinical variables plus embryology variables such as oocytes retrieved, mature oocytes, fertilization rate, embryo grade, blastocyst grade and transfer day.",
            "Allows the title to include multimodal clinical and embryological data.",
            "Supports stronger personalization and explanation outputs than clinical data alone.",
        ],
    )
    doc.add_heading("Ideal Dataset Scenario", level=1)
    add_bullets(
        doc,
        [
            "Clinical, treatment, embryology and lifestyle variables collected consistently.",
            "More than one clinic or one independent time period for validation.",
            "Clinician review of explanation outputs.",
            "Ethics approval and anonymization process clearly documented.",
        ],
    )
    doc.add_heading("Doctor / Clinic Questions", level=1)
    add_numbered(
        doc,
        [
            "Which IVF variables are routinely recorded in electronic or paper records?",
            "Is live birth available, or only clinical pregnancy?",
            "Are embryology variables available in structured form?",
            "Are lifestyle variables already recorded, or would a questionnaire be needed?",
            "Can data from more than one clinic, doctor, year or time period be accessed?",
            "Can clinicians review whether explanation outputs are meaningful?",
        ],
    )
    doc.add_page_break()
    doc.add_heading("Title Implication", level=1)
    add_table(
        doc,
        ["Data Available", "Safe Topic Direction"],
        [
            ["Clinical data only", "Explainable clinical IVF outcome prediction."],
            ["Clinical + embryology", "Explainable multimodal IVF outcome prediction."],
            ["Clinical + embryology + lifestyle", "Personalized IVF prediction using clinical, embryological and lifestyle data."],
            ["Multi-center data", "External validation in Indian IVF settings can be considered."],
        ],
        [2.0, 4.3],
    )
    return save_doc(doc, "04_dataset_feasibility_and_data_requirements.docx")


def methodology_blueprint():
    doc = setup_doc(
        "Methods, Models and Technical Blueprint",
        "Guide review pack | Tentative implementation plan, subject to data access",
    )
    doc.add_heading("System Idea", level=1)
    doc.add_paragraph(
        "Build an explainable clinical decision-support framework that predicts IVF outcome probability, explains patient-specific factors, "
        "and supports doctor-patient counseling without replacing clinician judgment."
    )
    doc.add_heading("Candidate Data Pipeline", level=1)
    add_numbered(
        doc,
        [
            "Collect anonymized IVF records after permission and ethics approval.",
            "Clean missing values, inconsistent formats and outliers.",
            "Map clinical, treatment-cycle, embryology and optional lifestyle variables.",
            "Train baseline and advanced machine-learning models.",
            "Evaluate discrimination, calibration and subgroup performance.",
            "Generate XAI explanations and test whether clinicians find them useful.",
        ],
    )
    doc.add_heading("Candidate Models", level=1)
    add_table(
        doc,
        ["Model", "Role"],
        [
            ["Logistic Regression", "Baseline and interpretable comparison model."],
            ["Decision Tree", "Simple interpretable model."],
            ["Random Forest", "Non-linear tabular-data baseline."],
            ["XGBoost / LightGBM", "Strong candidate models for structured IVF data."],
            ["SVM", "Comparison model if dataset size and feature set support it."],
            ["Neural network", "Only if data volume or image/time-lapse data justifies it."],
        ],
        [2.1, 4.2],
    )
    doc.add_heading("Explainability Methods", level=1)
    add_bullets(
        doc,
        [
            "SHAP for global and patient-level explanations.",
            "LIME as a possible local explanation comparison.",
            "Permutation importance for model-agnostic feature importance.",
            "Partial dependence or related plots for selected variables if clinically meaningful.",
        ],
    )
    doc.add_heading("Evaluation Metrics", level=1)
    add_table(
        doc,
        ["Area", "Candidate Measures"],
        [
            ["Classification", "AUC, accuracy, sensitivity, specificity, precision, recall, F1."],
            ["Calibration", "Calibration curve and Brier score."],
            ["Clinical usefulness", "Decision curve analysis if feasible."],
            ["Generalization", "External, temporal or subgroup validation depending on data."],
            ["Explainability/usefulness", "Clinician review or structured feedback."],
        ],
        [1.7, 4.6],
    )
    doc.add_heading("Important Boundary", level=1)
    doc.add_paragraph(
        "The current plan should not claim treatment improvement or clinical deployment. "
        "The defensible claim is prediction, explanation, validation and decision-support design."
    )
    return save_doc(doc, "05_methods_models_and_technical_blueprint.docx")


def rq_hypothesis_stats():
    doc = setup_doc(
        "Research Questions, Hypotheses and Statistical Plan",
        "Guide review pack | Draft academic structure for guide discussion",
    )
    doc.add_heading("Current Research Questions", level=1)
    add_numbered(
        doc,
        [
            "Which clinical, embryological and contextual factors are useful for personalized IVF outcome prediction?",
            "Can a multimodal machine-learning model predict IVF outcomes better than a single-data-type model?",
            "How can explainable AI show the main reasons behind each prediction?",
            "Does the model perform consistently across patient groups, clinics or Indian IVF data if such data are available?",
            "How can prediction results be presented to doctors as decision support without replacing doctor judgment?",
        ],
    )
    doc.add_heading("Tentative Hypotheses", level=1)
    add_table(
        doc,
        ["Hypothesis", "Status"],
        [
            ["Clinical and embryological variables together improve prediction compared with clinical variables alone.", "Testable only if embryology variables are available."],
            ["XAI can identify patient-specific positive and negative prediction drivers.", "Testable after model development."],
            ["Model performance differs across age, diagnosis or treatment subgroups.", "Testable if subgroup sizes are adequate."],
            ["Clinicians find structured explanation outputs useful for counseling.", "Testable only if clinician review is feasible."],
        ],
        [3.8, 2.5],
    )
    doc.add_heading("Statistical and ML Evaluation Plan", level=1)
    add_bullets(
        doc,
        [
            "Use descriptive statistics to summarize age, BMI, diagnosis, treatment type and outcomes.",
            "Use appropriate univariate comparison tests depending on variable type and distribution.",
            "Use train/validation/test, cross-validation, bootstrap, temporal validation or external validation depending on dataset size and source.",
            "Report discrimination metrics such as AUC, sensitivity and specificity.",
            "Report calibration because a clinically useful probability must be reliable, not only ranked correctly.",
            "Perform subgroup analysis only when sample sizes are sufficient.",
        ],
    )
    doc.add_heading("Not Final Yet", level=1)
    add_bullets(
        doc,
        [
            "Final dependent variable: live birth is preferred but may not be available.",
            "Final hypotheses: must match actual variables and outcomes.",
            "Final validation plan: depends on whether more than one clinic/source/time period is available.",
        ],
    )
    return save_doc(doc, "06_research_questions_hypotheses_and_stats.docx")


def candidate_topics():
    doc = setup_doc(
        "Candidate PhD Topic Directions",
        "Guide review pack | Topic options for discussion, not final title approval",
    )
    doc.add_heading("Current Position", level=1)
    doc.add_paragraph(
        "The title should not be finalized before clinic data feasibility is confirmed. "
        "The current literature supports a direction, not a final wording."
    )
    doc.add_heading("Candidate Directions", level=1)
    add_table(
        doc,
        ["Candidate Direction", "Strength", "Risk / Dependency"],
        [
            [
                "Explainable and personalized clinical decision-support framework for IVF outcome prediction.",
                "Best overall fit with repeated gaps: XAI, CDSS, personalization and validation.",
                "Needs clinic outcome data and careful scope control.",
            ],
            [
                "Trustworthy AI-based decision support for ovarian stimulation and IVF outcomes.",
                "Strong connection with dose, trigger and protocol decision-support literature.",
                "Requires detailed stimulation and protocol data.",
            ],
            [
                "Integration of clinical, embryological and lifestyle data for explainable IVF success prediction.",
                "Strong personalization angle if lifestyle data can be collected reliably.",
                "Lifestyle data availability and quality are uncertain.",
            ],
            [
                "Explainable ML for IVF live-birth prediction with Indian population validation.",
                "Strong Indian-context contribution if data is available.",
                "Depends heavily on access to Indian clinic data and live-birth outcome.",
            ],
        ],
        [2.2, 2.0, 2.1],
    )
    doc.add_heading("Safest Working Title", level=1)
    doc.add_paragraph(
        "An Explainable and Personalized Clinical Decision Support Framework for IVF Outcome Prediction Using Multimodal Clinical and Embryological Data"
    )
    doc.add_heading("Conditional Title Extensions", level=1)
    add_table(
        doc,
        ["Extension", "Use Only If"],
        [
            ["in Indian Women / Indian IVF Settings", "Indian clinic data and validation are available."],
            ["Using Clinical, Embryological and Lifestyle Data", "Lifestyle variables are collected reliably and ethically."],
            ["with External Validation", "Independent clinic/source/time-period data is available."],
            ["for Live-Birth Prediction", "Live-birth outcome is available with adequate follow-up."],
        ],
        [2.4, 3.9],
    )
    doc.add_heading("Guide Input Needed", level=1)
    add_numbered(
        doc,
        [
            "Which candidate direction is academically strongest for the department?",
            "Which direction is practical given likely clinic access?",
            "Should the first proposal emphasize IVF outcome prediction, stimulation decision support or broader CDSS?",
            "Which title words should be avoided until data access is confirmed?",
        ],
    )
    return save_doc(doc, "07_candidate_phd_topic_directions.docx")


def readme():
    text = """# Guide Review Pack

This folder contains compact material to share with the PhD guide for review.

## Files

1. `01_literature_review_matrix.xlsx` - detailed Excel paper matrix.
2. `02_compact_literature_review_summary.docx` - short review summary.
3. `03_theme_and_gap_analysis.docx` - theme classification and repeated gaps.
4. `04_dataset_feasibility_and_data_requirements.docx` - required variables and clinic questions.
5. `05_methods_models_and_technical_blueprint.docx` - tentative technical plan.
6. `06_research_questions_hypotheses_and_stats.docx` - draft RQs, hypotheses and evaluation plan.
7. `07_candidate_phd_topic_directions.docx` - candidate titles and decision dependencies.

## Suggested Sharing Order

Start with the Excel workbook, compact literature summary, theme-gap document, dataset feasibility document and candidate topic directions.

Use the methods/statistics document as supporting material if the guide asks about implementation feasibility.

## Important Position

The final PhD title is intentionally not fixed yet. The safest current direction is explainable and personalized clinical decision support for IVF outcome prediction. Final wording depends on clinic data feasibility.
"""
    path = OUT / "README.md"
    path.write_text(text, encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    paths = [
        literature_summary(),
        theme_gap_analysis(),
        dataset_feasibility(),
        methodology_blueprint(),
        rq_hypothesis_stats(),
        candidate_topics(),
    ]
    readme()
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
