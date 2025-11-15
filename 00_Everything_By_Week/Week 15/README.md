# **Week 15 – Advanced NLP, Data Extraction & End-to-End MLOps with MLflow and CI/CD**

## **Overview**

**Week 15** was one of the most intense and transformative weeks of the entire program.
It marked a deep shift from pure NLP learning into the world of **MLOps**, where machine learning models move from experimentation to organized, reproducible, and automated pipelines.

Across **Days 63–70**, I worked through three major themes:

1. **Advanced NLP Techniques** – chunking, extracting structured text, applying ML to text datasets, and using spaCy for industrial NLP.
2. **NLP Project** – building a **Multi-Language Translation App** using Streamlit.
3. **MLOps & CI/CD** – introduction to MLflow, experiment tracking, model versioning, automated pipelines, and continuous integration using GitHub Actions.

This week connected **Data → NLP → Production → Automation**, showing how real-world AI systems are actually built, deployed, and maintained.

---

## **Contents**

---

### **[Day 63 – Chunking in NLP & LLMs](Day63_Chunking_in_NLP_&_LLMs)**

This day introduced **Chunking**, an essential concept in both traditional NLP and modern LLM systems.

**What I learned:**

* Chunking in NLP → extracting meaningful phrases (NP, VP, etc.)
* Chunking in LLMs → splitting long texts into manageable segments to fit model context windows
* Tokenization using GPT-2 & understanding input IDs, attention masks
* Generating text using Transformers
* Creating custom chunking functions for processing large documents
* Working with BERT to chunk long texts based on token lengths

**Key insight:**
Chunking is crucial for both syntactic NLP tasks and efficient LLM processing, especially when dealing with long documents that exceed token limits.

---

### **[Day 64 – How Machine Learning Models are Implemented in NLP](Day64_NLP_ML_Implementation)**

This day demonstrated the full **NLP + ML workflow** using the Restaurant Reviews dataset.

**Pipeline covered:**

* Preprocessing (cleaning, stopwords, stemming)
* Feature extraction: **Bag of Words** & **TF-IDF (unigram + bigram)**
* Training multiple ML models:

  * Naive Bayes
  * Logistic Regression
  * SVM (Linear, RBF)
  * Random Forest, Decision Tree
  * KNN
* Comparing accuracies across representations and dataset expansions

**Results:**

* TF-IDF with dataset expansion delivered **98% accuracy** (SVM RBF & Random Forest).
* Naive Bayes remained a strong baseline (~96%).
* KNN struggled due to sparse vectors.

**Key insight:**
**Data representation quality and dataset size** are the biggest drivers in NLP model performance.

---

### **[Day 65a – Introduction to spaCy](Day65a_NLP_Spacy_Intro)**

spaCy is an industrial-grade NLP library.
This session explored:

* spaCy NLP pipeline
* Tokenization, Lemmatization, POS tagging
* Named Entity Recognition
* Dependency parsing
* Comparing spaCy vs NLTK (speed, accuracy, scalability)

**Key takeaways:**
spaCy is optimized for **production-level NLP**, making it ideal for real-world tasks like information extraction, tagging, and document analysis.

---

### **[Day 65b – Text Summarization using spaCy](Day65b_Spacy_Text_Summarization)**

I implemented an **extractive text summarizer** using:

* Word frequency scoring
* Sentence ranking
* Extracting top-scoring sentences as summary

**Learning outcomes:**

* Difference between extractive and abstractive summarization
* Limitations of frequency-based summaries
* How transformer models (T5, BART) can improve summarization

This showed how simple NLP pipelines can be extended into advanced use cases.

---

### **[Day 66 – XML Scraping & Cleaning](Day66_XML_Scrapping)**

This session focused on extracting usable text from **XML files**, preparing them for NLP pipelines.

**Skills learned:**

* Parsing XML using `ElementTree`
* Cleaning extracted text using BeautifulSoup
* Removing unwanted tags, punctuation, and patterns via regex
* Preparing cleaned text for NLP

**Key insight:**
Most real-world AI systems start with **messy, unstructured data**, and XML parsing is a crucial data engineering step.

---

### **Mini Project – [Multiple Language Translation App](Multiple_Language_Translation)**

Before transitioning to MLOps, I built a fully interactive NLP project using:

* **Streamlit** for UI
* **mtranslate** for translation
* **gTTS** for speech generation
* CSV-based language mapping

**Features delivered:**

* Translate text into **60+ languages**
* Auto language detection
* Text-to-speech output
* Clean, responsive UI with sidebar controls

This project bridged NLP skills with UI development and user experience.

---

## **Transition to MLOps & CI/CD**

After gaining strong NLP foundations, the second half of Week 15 shifted into **MLOps** — the discipline that makes machine learning scalable, maintainable, and deployable in production.

This transition marked a major milestone:
**moving from building models → to maintaining, tracking, and automating them.**

---

### **[Day 67 – MLOps Introduction & MLflow Basics](Day67_MLOps_Introduction_and_MLflow_Basics)**

The journey started by understanding:

* What MLOps is & why it’s essential
* Complete ML lifecycle (data → training → deployment → monitoring)
* MLflow components:

  * **Experiment Tracking**
  * **Model Logging**
  * **UI for run comparison**

Practical exercises included:

* Training Logistic Regression
* Logging parameters, metrics, and models
* Visualizing results in MLflow UI

---

### **[Day 68 – Model Versioning with MLflow](Day68_MLOps_Model_Versioning)**

This day deepened MLOps knowledge through:

* Synthetic dataset training
* Logging multiple models (LR, RF, XGBoost, XGBoost+SMOTE)
* Registering models in the MLflow Model Registry
* Understanding staging, production, and aliasing
* Comparing multiple versions in MLflow UI

**Key insight:**
Model Registry gives enterprise-grade **version control** for ML, similar to Git but for models.

---

### **[Day 69 – MLflow Experiments, Training & Model Registration](Day69_MLOps_Experiment)**

This session demonstrated a complete **end-to-end automated MLflow pipeline** using a single Python script.

The script performed:

* Training two models (Logistic Regression & Random Forest)
* Logging all metrics and parameters
* Saving confusion matrices as artifacts
* Registering models automatically
* Creating new versions when re-run

This showed how real ML systems automate training, logging, and versioning without manual UI work.

---

### **[Day 70 – CI/CD Pipeline using GitHub Actions](Day70_CICD_Pipeline_for_Machine_Learning)**

The week concluded with production-grade **CI/CD automation**.

Using GitHub Actions:

* A YAML workflow was built to trigger on every push
* Dependencies were installed automatically
* `train_model.py` executed end-to-end
* Model training, evaluation, and validation occurred in the cloud
* Optional MLflow logging integrated
* Pipeline status displayed directly in GitHub Actions

**Outcome:**
A fully automated, reproducible ML training workflow — essential for enterprise MLOps.

---

## **Key Takeaways (Week 15)**

### **NLP Advancement**

- Learned chunking, summarization, and production-grade spaCy workflows
- Implemented ML algorithms for text classification
- Built a multi-language translation app

### **Data Engineering**

- Extracted structured text from XML
- Cleaned and prepared real-world document data

### **MLOps & Automation**

- Understood ML lifecycle and experiment tracking
- Logged runs, metrics, parameters, and artifacts using MLflow
- Managed model versions and registry workflows
- Built end-to-end pipelines for automated training
- Implemented CI/CD using GitHub Actions

### **Overall**

Week 15 transformed ML projects from **code experiments → production-ready automated pipelines**, combining:

NLP
Data engineering
MLOps
CI/CD
Model versioning
Translation project

This was the week that connected all previous learning to the real-world AI workflow.

---
