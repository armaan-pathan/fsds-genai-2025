# Day 70 – CI/CD Pipeline for Machine Learning using GitHub Actions

This project demonstrates how to build and automate a **Continuous Integration and Continuous Deployment (CI/CD)** pipeline for a **machine learning model** using **GitHub Actions**.
The goal is to ensure that every change in the codebase automatically triggers model training, testing, and validation — making the workflow **reliable, repeatable, and production-ready**.

---

## Project Overview

In traditional ML workflows, code changes often require manual retraining and evaluation.
With CI/CD, these tasks are automated so that each update in your repository:

* Triggers the pipeline automatically
* Validates dependencies and runs tests
* Trains and evaluates the model
* Ensures consistent, error-free results before merging to production

This project uses **GitHub Actions** to implement an **automated ML workflow** that continuously monitors and retrains models as needed.

---

## Features

* **Automated pipeline** using GitHub Actions
* **Model training and evaluation** using Python (scikit-learn)
* **Integration with MLflow** for experiment tracking (optional)
* **Automatic validation** on each push or pull request
* **Reproducible and version-controlled** ML experiments

---

 Project Structure

```
├── Day70_CICD_Pipeline_for_ML.ipynb        # Notebook explaining your entire CI/CD project
│
├── cicd_pipeline-main/                     # Main working CI/CD project
│   ├── data/
│   │   └── iris.csv                        # Dataset used for training
│   ├── train_model.py                      # Model training and evaluation script
│   ├── requirements.txt                    # Python dependencies
│   └── .github/
│       └── workflows/
│           └── mlops_cicd.yml              # GitHub Actions workflow file
│
├── screenshots/
│   ├── screenshot1.png
│   ├── screenshot2.png
│   ├── screenshot3.png
│   └── screenshot6.png
│
└── README.md                              # Documentation
```

---

## How It Works

1. **Push or Pull Request:**
   When you push code to GitHub, it automatically triggers the CI/CD workflow.
2. **Install Dependencies:**
   The pipeline installs all required packages listed in `requirements.txt`.
3. **Run Training Script:**
   Executes `train_model.py`, which trains and evaluates an ML model (e.g., Logistic Regression on the Iris dataset).
4. **Validation & Logging:**
   Metrics are printed in the Actions log and optionally logged to MLflow.
5. **Pipeline Completion:**
   If successful, the workflow shows a  green status in GitHub Actions.

---

## Tech Stack

* **Python**
* **scikit-learn**
* **GitHub Actions (CI/CD)**
* **MLflow (optional for tracking)**
* **YAML (for workflow configuration)**

---

## Conclusion

This project integrates **CI/CD automation** into the machine learning workflow using **GitHub Actions**, ensuring that every code change is automatically tested and validated.
It bridges the gap between **ML model development** and **deployment readiness**, making the entire process **more efficient, reproducible, and scalable**.

---

## Key Learnings

* Understood how **CI/CD pipelines** enhance the MLOps workflow
* Learned to configure a **GitHub Actions** workflow for automation
* Implemented **automated model training and testing** pipelines
* Observed how automation ensures **model stability and reliability**
* Gained practical exposure to **continuous integration in ML projects**

---
