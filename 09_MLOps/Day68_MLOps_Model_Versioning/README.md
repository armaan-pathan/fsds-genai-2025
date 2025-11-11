# Day 68 – MLOps Model Versioning with MLflow

This notebook is a continuation of my **MLOps learning journey**.  

On this day, I focused on **Model Versioning** — an important part of managing models in production using **MLflow’s Model Registry**.

While Day 67 covered **experiment tracking**, this notebook demonstrates how to:
- **Register models** in MLflow  
- **Track and compare model versions**  
- **Add aliases** for production management  
- Understand the **model lifecycle** from training → versioning → deployment  

---

## Overview

The goal of this practical is to understand **how to handle multiple model versions** efficiently in an MLOps workflow.  
By the end of this notebook, I learned how MLflow automatically:
- Assigns version numbers to registered models  
- Keeps a history of all versions  
- Allows promotion and aliasing for production use  

---

## Workflow Steps

1. **Import Libraries**  
   Imported all necessary modules such as `mlflow`, `sklearn`, and `xgboost`.

2. **Dataset Creation and Training**  
   Created a synthetic dataset using `make_classification()` and trained multiple models:
   - Logistic Regression  
   - Random Forest  
   - XGBoost  
   - XGBoost with SMOTE  

3. **Experiment Tracking**  
   Logged parameters, metrics, and models using **MLflow Tracking API**.

4. **Model Registry Operations**  
   - Registered trained models into MLflow’s Model Registry  
   - Observed **automatic versioning** (Version 1, 2, etc.)  
   - Added **aliases** (like `@appserver`) to represent production-ready models  

5. **MLflow UI Visualization**  
   Explored MLflow’s **Experiments Dashboard**, **Run Comparison View**, and **Model Registry Panel** to analyze performance visually.

---

## MLflow UI Screenshots

1. **Experiments Dashboard** – Displays all created experiments.  
2. **Runs List** – Shows each training run with logged metrics.  
3. **Comparing Runs** – Visual comparison of models using parallel plots.  
4. **Detailed Run Comparison** – Displays accuracy, F1, and recall for all models.  
5. **Models Dashboard** – Central page for managing registered models.  
6. **Creating the Model** – Demonstrates registering the model in MLflow.  
7. **Model Created Successfully** – Confirms model creation in registry.  
8. **Registered Model Details** – Shows model name and metadata.  
9. **After Registering (Version 1)** – Displays the first version of the model.  
10. **After Adding Aliases** – Shows how aliases are assigned.  
11. **Final Production Server** – Final versioned models ready for deployment.

---

## Conclusion

In this notebook, I worked on **model versioning** using MLflow.  
I trained and compared multiple models, registered the best-performing one, and explored how versions are automatically created and managed.  
Adding aliases helped in identifying production-ready models easily.  

This practical showed how model management fits into the overall **MLOps pipeline**, ensuring all models are **organized, reproducible, and deployment-ready**.

---

## Key Learnings

- How to use **MLflow Model Registry** for version tracking.  
- Each registered model automatically receives a **version number**.  
- Learned to assign **aliases** for staging and production models.  
- Explored how MLflow UI helps in **comparing runs and managing models visually**.  
- Understood how versioning streamlines **deployment and maintenance** of ML models.  

---

## Folder Structure

```

Day68_MLOps_Model_Versioning/
│
├── Day68_MLOps_Model_Versioning.ipynb     # Final notebook
├── screenshots/
│   ├── screenshot1.png
│   ├── screenshot2.png
│   ├── screenshot3.png
│   ├── ...
│   └── screenshot11.png
└── README.md

```

---

