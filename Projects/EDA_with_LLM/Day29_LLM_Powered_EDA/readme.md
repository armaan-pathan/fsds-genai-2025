# Day 29 – LLM Powered EDA Project

This project is an **LLM (Large Language Model) Powered Exploratory Data Analysis (EDA) tool** built using **Gradio, Pandas, Matplotlib, Seaborn, and Ollama’s Mistral-7B model**.  
It allows users to upload a CSV dataset and automatically generates:

1. **Data Summary & Missing Value Report**  
2. **AI-Powered Insights** using a language model  
3. **Data Visualizations** such as histograms and correlation heatmaps  

The tool combines **traditional EDA techniques** with **Generative AI** for deeper dataset understanding.

---

## Features

- **Upload CSV Dataset**: Accepts tabular data files directly.  
- **Data Cleaning**:
  - Numeric columns → missing values filled with **median**.  
  - Categorical columns → missing values filled with **mode**.  
- **Automated EDA**:
  - Data summary statistics (`.describe()` across numeric & categorical).  
  - Missing value detection and reporting.  
- **AI Insights**:
  - Uses **Ollama’s Mistral-7B** model to generate natural language explanations of dataset summary.  
- **Visualizations**:
  - Histograms for all numeric columns.  
  - Correlation heatmap for numerical features.  

---

## Tech Stack

- **Python** (data processing and orchestration)  
- **Pandas** – data handling  
- **Matplotlib & Seaborn** – visualizations  
- **Ollama (Mistral-7B)** – AI-powered analysis  
- **Gradio** – interactive user interface  

---

## How It Works

1. Upload a CSV file via the **Gradio app interface**.  
2. The app processes the data:
   - Cleans missing values.  
   - Generates summary statistics.  
   - Creates visualizations.  
3. The dataset summary is passed to **Mistral-7B LLM** which provides natural language insights.  
4. Results are displayed in the Gradio app:
   - A **report** with summary, missing values, and AI insights.  
   - A **gallery of plots** (histograms + correlation heatmap).  

---

## Key Learnings
- Integrated **traditional statistics** with **LLM insights**.  
- Automated the **EDA workflow** with AI support.  
- Learned how to build a **Gradio-based interactive app**.  
- Understood the role of **Generative AI in augmenting data analysis**.  

---
