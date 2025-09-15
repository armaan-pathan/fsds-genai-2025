# Classification in Machine Learning

## Overview

The **Classification** folder contains all notebooks and projects related to **classification algorithms in Machine Learning**.
Unlike regression (which predicts continuous values), classification is about predicting **categories or classes** (e.g., Yes/No, Spam/Not Spam, Purchase/Not Purchase).

This section begins with the foundation of classification, covers **Logistic Regression**, extends it to unseen data, and demonstrates **deployment using Streamlit**.

---

## Contents

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

### [Day52 – K-Nearest Neighbors (KNN) Classification](Day52_K-Nearest_Neighbors_(KNN)_Classification)

* Introduction to **KNN Classification**, a distance-based supervised learning algorithm.
* Explained how KNN works step by step: choosing `k`, calculating distances, finding nearest neighbors, and majority voting.
* Discussed the **importance of feature scaling** for KNN since it relies on distance.
* Experiments performed with different values of `k` (3, 4, 5) using scaled data → **accuracy = 0.93**.
* Compared with **no scaling (k=3)** → accuracy dropped to **0.78**, showing why preprocessing is crucial.
* Confusion matrices analyzed to understand misclassifications.
* Key learning: KNN is simple, effective, but highly dependent on **k-value choice** and **scaling**.

---

## Key Takeaways from Classification (so far)

* Classification is about predicting **categories** instead of numbers.
* Logistic Regression, despite its name, is a **classification algorithm**.
* Preprocessing (scaling/normalization) impacts accuracy.
* Confusion matrix & metrics (Precision, Recall, F1-score) give deeper insights than accuracy alone.
* Models must generalize well → tested with **unseen data**.
* Deployment with **Streamlit** shows how end-users can interact with ML models.
* K-Nearest Neighbors (KNN) is a simple distance-based algorithm where predictions depend on the majority class of neighbors.
* The choice of k-value impacts performance (small k → overfitting, large k → underfitting).
* Feature scaling is critical for KNN: accuracy improved from 0.78 (unscaled) to 0.93 (scaled).

---

## Next Steps

Upcoming notebooks in this folder will cover more **classification algorithms** such as:

* Support Vector Machines (SVM)
* Decision Trees
* Random Forest
* Naive Bayes
