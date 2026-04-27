# Genomic-Clinical-Data-Wrangling
End-to-end Data Analysis pipeline in Python merging clinical outcomes with genomic sequencing results.

# 🧬📊 Genomic & Clinical Data Wrangling Pipeline

This repository contains a Python-based data analysis pipeline that integrates, cleans, and analyzes a simulated dataset merging clinical patient information with genomic sequencing outcomes.

This project demonstrates the ability to translate raw, messy biomedical data into structured, actionable insights suitable for both R&D and strategic business decision-making.

---

### 💼 Business & Scientific Value

* **For Healthcare Consultancies (e.g., Accenture):** Demonstrates ability in **ETL (Extract, Transform, Load)** processes, data cleaning, handling missing values, and generating visual reports on patient population trends. Focuses on operational efficiency in data handling.
* **For Bioinformatics Firms:** Demonstrates domain knowledge in interpretating genomic metrics (like Quality Scores, Coverage) in the context of clinical pathophysiology.

---

### 🛠 Tech Stack & Methodologies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

* **Languages:** Python.
* **Libraries:** Pandas (Data Manipulation), Matplotlib/Seaborn (Visualization).
* **Technologies:** VS Code, Git.
* **Methodologies:** Exploratory Data Analysis (EDA), Data Wrangling, Modelagem de Dados Biomédicos.

---

### 📂 Repository Structure

* `analysis_pipeline.py`: The main Python script containing the ETL and analysis logic.
* `data/`: Directory containing the simulated messy datasets (CSV format).
* `reports/`: Directory containing generated charts and a final PDF summary.

---

### 📊 Project Highlights (How to Run)

> *Note: This is an ongoing project. Currently, it implements the EDA and Cleaning phase.*

**1. Data Cleaning (Pandas)**
The script handles missing clinical dates, normalizes generic mutation nomenclature, and filters out low-quality sequencing runs based on Phred Scores.

**2. Visual Insights (Matplotlib)**
Generating charts to visualize the correlation between specific gene mutations and clinical prognosis.

```markdown
# Example Python code snippet used:
# clinical_df = pd.read_csv('data/clinical_data.csv')
# clean_df = clinical_df.dropna(subset=['diagnosis_date'])

![Quality Chart](quality_report.png)
