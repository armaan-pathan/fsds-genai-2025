# Classification in Machine Learning

## Overview

The **Classification** folder contains all notebooks and projects related to **classification algorithms in Machine Learning**.
Unlike regression (which predicts continuous values), classification is about predicting **categories or classes** (e.g., Yes/No, Spam/Not Spam, Purchase/Not Purchase).

This section begins with the foundation of classification, covers **Logistic Regression**, extends it to unseen data, and demonstrates **deployment using Streamlit**.

---

## Contents
[Day42 – Simple Linear Regression with Streamlit App](Day42_SLR_Deployment_with_Streamlit)
### [Day49 – Introduction to Classification & Logistic Regression](Day49_Intro_to_Classification_&_Logistic_Regression)

* Theory of **Classification** and its importance.
* Difference between **Classification and Regression**.
* Logistic Regression explained in detail (Sigmoid, probabilities, why it’s classification not regression).
* **Confusion Matrix** explained with COVID doctor–patient example.
* Performance metrics: Accuracy, Precision, Recall, F1-score.
* **Bias–Variance** concept with train/test accuracies.
* Multiple experiments: without scaling, StandardScaler, Normalizer, and different random states.
* **Best Accuracy achieved: 0.92** (StandardScaler, random\_state=0, test\_size=0.20).

---

### [Day50 – Logistic Regression with Unseen Data](Day50a_Logistic_Regression_on_Unseen_Data)

* Extended Logistic Regression to predict on **unseen/future data**.
* Workflow: Train → Save → Load unseen dataset → Preprocess → Predict.
* Emphasized **preprocessing consistency** between training and new data.
* Predictions generated for unseen dataset → showing how models generalize in real-world scenarios.
* Acts as a bridge towards **deployment**.

---

### [Day50 – Logistic Regression Deployment with Streamlit](Day50b_LR_Deployment_with_Streamlit)

* Built a **Streamlit web app** for Logistic Regression.
* User enters **Age** and **Estimated Salary** to predict:

  * Will Purchase
  * Will Not Purchase
* Inputs placed in sidebar, clean UI with footer branding.
* App demonstrates how ML models move from **Jupyter notebooks → real-world interactive apps**.

---

## Key Takeaways from Classification (so far)

* Classification is about predicting **categories** instead of numbers.
* Logistic Regression, despite its name, is a **classification algorithm**.
* Preprocessing (scaling/normalization) impacts accuracy.
* Confusion matrix & metrics (Precision, Recall, F1-score) give deeper insights than accuracy alone.
* Models must generalize well → tested with **unseen data**.
* Deployment with **Streamlit** shows how end-users can interact with ML models.

---

## Next Steps

Upcoming notebooks in this folder will cover more **classification algorithms** such as:

* K-Nearest Neighbors (KNN)
* Support Vector Machines (SVM)
* Decision Trees
* Random Forest
* Naive Bayes

---

👉 This README introduces beginners to **classification workflows** and makes it easy to navigate through Day49 & Day50 notebooks/projects.

---

Do you want me to also include a **mini comparison table** of the experiments from Day49 (like we put in its own README) here inside the Classification README, or should we keep it high-level only?
