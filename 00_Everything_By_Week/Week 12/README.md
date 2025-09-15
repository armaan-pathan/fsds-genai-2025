# Week 12 – Classification, Logistic Regression, PCA, KNN & SVM

## Overview

In **Week 12**, I shifted from Regression into **Classification algorithms** and dimensionality reduction techniques.  
This week’s focus was on building classification models, evaluating them with proper metrics, testing on unseen data, and exploring how preprocessing like PCA and scaling impacts performance.

---

## Contents

### [Day49 – Introduction to Classification & Logistic Regression](Day49_Intro_to_Classification_&_Logistic_Regression)

* Introduction to **Classification** and how it differs from Regression.  
* Detailed theory of **Logistic Regression**.  
* Covered steps to build a classification model.  
* Explained why Logistic Regression is a classification algorithm.  
* Introduced **Confusion Matrix** with metrics: Accuracy, Precision, Recall, F1-score.  
* Practical experiments with Logistic Regression using different preprocessing methods (scaling, normalization).  

---

### [Day50a – Logistic Regression on Unseen Data](Day50a_Logistic_Regression_on_Unseen_Data)

* Extended Logistic Regression to **future/unseen data**.  
* Trained the model on one dataset and predicted results on another unseen dataset.  
* Emphasized the importance of **generalization** in ML models.  
* Compared results between training and unseen datasets.  

---

### [Day50b – Logistic Regression Deployment with Streamlit](Day50b_LR_Deployment_with_Streamlit)

* Saved the trained Logistic Regression model and scaler.  
* Built a simple **Streamlit web app** for predictions.  
* End-users can input **Age** and **Estimated Salary** to predict whether a purchase will be made.  
* Demonstrated deployment as an interactive way to test ML models.  

---

### [Day51 – Principal Component Analysis (PCA)](Day51_PCA_in_Machine_Learning.ipynb)

* Studied **PCA**, a popular dimensionality reduction technique.  
* Theory: bias-variance tradeoff, explained variance ratio, and optimal number of components.  
* Applied PCA with Logistic Regression on the dataset.  
* Found that **12 components preserved \~90% of variance** with maximum accuracy of **0.8227**.  
* Plotted explained variance to visualize feature reduction.  

---

### [Day52 – K-Nearest Neighbors (KNN) Classification](Day52_K-Nearest_Neighbors_(KNN)_Classification)

* Introduced **KNN Classification**: a distance-based supervised learning algorithm.  
* Explained how KNN works (distance calculation, majority voting).  
* Highlighted importance of **feature scaling** in distance-based models.  
* Experiments with `k=3,4,5` (scaled data) → Accuracy = **0.93**.  
* Without scaling (k=3) → Accuracy dropped to **0.78**.  
* Compared confusion matrices across experiments.  

---

### [Day53 – Support Vector Machine (SVM) Classifier](Day53_Support_Vector_Machine(SVM)_Classification)

* Introduced **Support Vector Machine (SVM)**, a powerful classification algorithm that finds the optimal hyperplane to separate classes.  
* Covered the concepts of **support vectors, margin, and kernel trick**.  
* Implemented SVM classifier with different kernel functions (`linear`, `rbf`).  
* Compared model performance with and without scaling, showing that **SVM is highly sensitive to feature scaling**.  
* Evaluated results using confusion matrices and additional metrics like **ROC curve and AUC score**.  
* Extended the experiment to **future prediction tasks**, applying the trained model on unseen data.  

---

## Key Takeaways (Week 12)

* **Classification vs Regression** → classification predicts categories, regression predicts continuous values.  
* Logistic Regression is a **classification algorithm**, not a regression one.  
* **Evaluation metrics** (Confusion Matrix, Precision, Recall, F1-score) provide deeper insights than accuracy alone.  
* Models must **generalize to unseen data**.  
* **Deployment with Streamlit** shows practical application of ML models.  
* **PCA reduces dimensionality** while retaining most variance, improving efficiency.  
* **KNN is distance-based** and highly dependent on scaling and the choice of `k`.  
* **SVM is powerful and works well in high dimensions**, but requires proper scaling and kernel selection.  

---

This week gave a strong foundation in **Classification techniques (Logistic Regression, KNN, SVM), PCA, and deployment**, combining theory, implementation, evaluation, and practical applications.
