# 🦠 Antibiotic Resistance Analysis Project

## 🎯 Project Goal
The primary objective of this project is to analyze antibiotic resistance patterns within a clinical dataset to identify key drivers of resistance and evaluate the effectiveness of current treatment protocols. 

Key focus areas include:
* **Quantifying Resistance:** Identifying the prevalence of MDR (Multidrug-Resistant) and XDR (Extensively Drug-Resistant) strains.
* **Risk Factor Evaluation:** Using statistical methods like **Relative Risk (RR)** to assess the impact of prior hospitalization and underlying conditions.
* **Data Cleaning:** Handling "dirty" synthetic data, including missing values (`?`, `Missing`) and inconsistent categorical labels.

---

## 📊 Key Findings & Statistics

### 1. Resistance Prevalence
* **68%+** of all bacterial samples were classified as **MDR** or **XDR**.
* This highlights a significant challenge for standard empirical antibiotic therapy.

### 2. Hospitalization vs. Community Resistance
Through statistical analysis of 10,000+ records, we compared the probability of resistance based on patient history:

| Group | MDR Rate |
| :--- | :--- |
| **No Prior Hospitalization** | 73.92% |
| **Prior Hospitalization** | 74.00% |
| **Relative Risk (RR)** | **1.0012** |

**Conclusion:** The **Relative Risk of ~1.0** indicates that in this dataset, prior hospitalization is not a statistically significant risk factor for MDR. This suggests that resistant strains are already deeply embedded in the community.

### 3. Patient Profile
* **70.4%** of MDR cases originated from the community (no recent hospital visit).
* **29.6%** of MDR cases originated from hospitalized patients.
* **Insight:** While individual risk is similar, the sheer volume of resistant infections is driven by the community setting.

---

## 🧬 Pathogen Insights
* **Primary Pathogen:** *E. coli* was identified as the most prevalent bacteria, making it the top priority for monitoring.
* **Last-Resort Antibiotics:** Drugs such as **Imipenem (IPM)** and **Colistin** maintain high efficacy, though the presence of XDR strains remains a threat.
* **Age Distribution:** Resistance levels were found to be age-independent, with a stable average of ~2.15 resistances per sample across all age groups.

---

## 🛠️ Tools Used
* **Python**: Core analysis.
* **Pandas**: Data manipulation and cleaning.
* **Matplotlib & Seaborn**: Data visualization.
* **Jupyter Notebook**: Documentation and interactive environment.

---

## 📂 Project Structure
* `analysis.ipynb`: The main Jupyter Notebook containing the code and visualizations.
* `synthetic_bacteria_dataset.csv`: The raw dataset used for the study.
* `README.md`: Project summary and conclusions.
