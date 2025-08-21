# Day 28 – Exploratory Data Analysis on Heart Disease Dataset

This project focuses on **EDA for a healthcare dataset** aimed at predicting **heart disease risk**.  
The analysis explored patient records, identified key health indicators, and visualized differences between healthy and diseased groups.

---

## Objectives
- Understand the dataset’s medical features (age, cholesterol, blood pressure, etc.).  
- Perform cleaning and preparation for analysis.  
- Identify patterns and correlations between health attributes.  
- Compare distributions across patients with and without heart disease.  
- Generate insights useful for future **predictive modeling**.

---

## Key Steps & Analysis
1. **Data Loading & Inspection**
   - Imported dataset into Pandas.
   - Examined structure with `.head()`, `.info()`, `.describe()`.

2. **Data Cleaning**
   - Handled missing or inconsistent entries.  
   - Converted categorical values where necessary.

3. **Univariate Analysis**
   - Distribution of **age**, **cholesterol**, and **blood pressure**.  
   - Count of patients with and without heart disease.

4. **Bivariate Analysis**
   - Cross-comparison of attributes (e.g., cholesterol vs disease presence).  
   - Gender-based analysis of heart disease occurrence.  

5. **Visualizations**
   - **Histograms** – Age & cholesterol distributions.  
   - **Boxplots** – Outlier detection in medical features.  
   - **Heatmaps** – Correlation between numerical variables.  

---

## Dataset
- Source: UCI Heart Disease Dataset.
- Medical attributes of patients used for heart disease prediction.
- Key columns:
  - `age`: Age of the patient
  - `sex`: Gender (1 = male, 0 = female)
  - `cp`: Chest pain type
  - `trestbps`: Resting blood pressure
  - `chol`: Serum cholesterol level
  - `target`: 1 = Heart disease present, 0 = Not present

---

## Key Insights
- Higher cholesterol and older age groups show **greater association with heart disease**.  
- Blood pressure is another significant factor.  
- Gender differences were observed in disease distribution.  
- Several features show moderate-to-strong correlation, which can be leveraged in **ML models**.  

---

## Tools & Libraries
- **Pandas** – Data manipulation  
- **NumPy** – Numerical computations  
- **Matplotlib & Seaborn** – Visualization  
- **SciPy** – Statistical insights  

---

## Learning Outcome
Through this project, I learned how to:  
- Apply EDA in a **healthcare context**.  
- Use visualizations to highlight risk factors.  
- Build insights that can directly support **predictive modeling** for heart disease detection.  
