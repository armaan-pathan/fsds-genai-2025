# Week 10 – Multiple Regression & Regularization

## Overview

In **Week 10**, I explored advanced regression techniques including **Multiple Linear Regression, Polynomial Regression, and Regularization methods (L1, L2, Elastic Net)**.
Additionally, I studied **feature scaling** and its importance in model training.

---

## Contents

### [Day43 – Multiple Linear Regression](Day43_Multiple_Linear_Regression)

* Theory of **Multiple Linear Regression**.
* Data preprocessing with **dummy variables**.
* Model training and evaluation using **sklearn & statsmodels**.
* Applied **Backward Elimination** to refine features.
* Key insight: Understanding p-values and feature selection.

---

### [Day44 – Regularization Techniques (L1 & L2)](Day44_Regularization_Techniques)

* Concept of **overfitting vs underfitting**.
* Introduction to **Regularization**:

  * **Ridge Regression (L2)** → reduces coefficients without eliminating.
  * **Lasso Regression (L1)** → shrinks some coefficients to zero (feature selection).
  * **Elastic Net** → combination of L1 & L2.
* Implemented Ridge, Lasso, and ElasticNet on **Car MPG dataset**.
* Compared models using **R² and coefficients visualization**.

---

### [Day45 – Feature Scaling in ML](Day45_Feature_Scaling_in_Machine_Learning.ipynb)

* Importance of scaling numerical data.
* Techniques:

  * **Normalization (Min–Max Scaling)** → range \[0,1].
  * **Standardization (Z-score Scaling)** → mean=0, variance=1.
* Compared effects on datasets.
* When to use which scaling method.

---

### [Day46 – Polynomial Regression](Day46a_Polynomial_Regression)

* Extended Linear Regression to **non-linear datasets**.
* Implemented **Polynomial Regression** (degree 2–6).
* Visualized predictions with different degrees.
* Key learning: balance between underfitting (low degree) and overfitting (high degree).

---

### [Day46 – Polynomial Regression Deployment (Streamlit)](Day46b_PR_Deployment_with_Streamlit)

* Saved trained polynomial regression model.
* Built a **Streamlit app** to predict salaries based on experience using polynomial regression.
* Focused on clean frontend + prediction workflow.

---

## Key Takeaways (Week 10)

* Learned **advanced regression techniques** beyond simple linear regression.
* Understood **overfitting & underfitting** and how **regularization** helps combat them.
* Explored the importance of **feature scaling**.
* Built and deployed **Polynomial Regression models** with Streamlit.
