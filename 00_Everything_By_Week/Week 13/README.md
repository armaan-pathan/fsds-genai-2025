# **Week 13 – Naive Bayes, Decision Trees, Ensemble Learning & Model Evaluation (CV + ROC/AUC)**

## **Overview**

**Week 13** focused on strengthening classification fundamentals while advancing into more powerful modeling techniques.
This week covered:

* **Probabilistic classifiers (Naive Bayes)**
* **Tree-based models (Decision Trees)**
* **Ensemble methods (Bagging, Boosting, Voting, Stacking)**
* **Advanced evaluation techniques (Cross-Validation & ROC/AUC)**

Across these four days, I learned how different algorithms behave with preprocessing, how model ensembles improve performance, and how to evaluate models beyond simple accuracy.

---

## **Contents**

### **[Day 54 – Naive Bayes Classifier](Day54_Naive_Bayes_Classification)**

* Covered the theory behind **Bayes’ Theorem**, conditional probability, and independence assumptions.
* Studied variants of Naive Bayes:

  * **GaussianNB** — for continuous features
  * **MultinomialNB** — for count-based features
  * **BernoulliNB** — for binary features
* Tested all three variants under different preprocessing setups:

  * No scaling
  * **StandardScaler**
  * **Normalizer**
* Key observations:

  * GaussianNB benefits from scaling
  * MultinomialNB breaks with StandardScaler (negative values)
  * Normalizer can degrade performance
* Evaluated using accuracy, confusion matrix, and classification report.

---

### **[Day 55 – Decision Tree Classifier](Day55_Decision_Tree_Classification)**

* Learned how Decision Trees split data using:

  * **Entropy & Information Gain**
  * **Gini Index & Gini Impurity**
* Implemented pruning techniques:

  * `max_depth`
  * `min_samples_split`
  * `min_samples_leaf`
* Compared models with different depths (3 vs 10), showing overfitting in deeper trees.
* Highlight: Decision Trees are **scale-invariant** → scaling does not impact accuracy.
* Gained understanding of the interpretability & explainability benefits of tree-based models.

---

### **[Day 56 – Ensemble Learning](Day56_Ensemble_Learning)**

* Explored why combining weak learners produces stronger, more stable models.
* Studied major ensemble categories:

  * **Bagging** → Random Forest
  * **Boosting** → AdaBoost, XGBoost, LightGBM
  * **Voting Classifier** (hard & soft)
  * **Stacking Classifier** with a meta-learner
* Implemented all four ensemble types and compared performance using:

  * Accuracy
  * Confusion Matrix
  * Classification Report
* Observations:

  * **AdaBoost achieved the highest accuracy (0.94)**
  * Random Forest & Stacking also performed strongly
  * Voting classifier under-performed relative to other ensembles

---

### **[Day 57 – Cross-Validation & ROC/AUC](Day57_Cross_Validation_and_ROC_AUC)**

* Studied why a single train/test split is not reliable.
* Implemented:

  * **k-Fold Cross-Validation**
  * **Stratified k-Fold** (important for class imbalance)
* Evaluated Logistic Regression with both accuracy and ROC-AUC across folds.
* Plotted the **ROC Curve** and calculated **AUC** (>0.90 = excellent).
* Analyzed confusion matrix to understand misclassifications.

---

## **Key Takeaways (Week 13)**

### **Naive Bayes**

- Best for probabilistic modeling and high-dimensional data (e.g., text)
- MultinomialNB requires **non-negative** count features
- Scaling can break or improve different variants

### **Decision Trees**

- Highly interpretable
- No need for scaling
- Pruning is essential to prevent overfitting

### **Ensemble Learning**

- Combines multiple weak learners → strong, robust models
- Boosting focuses on mistakes → often best accuracy
- Stacking leverages strengths of multiple algorithms
- Ensembles frequently outperform single models

### **Cross-Validation & ROC/AUC**

- CV gives reliable performance estimates
- ROC curve shows classifier performance across thresholds
- AUC > 0.9 means excellent separation ability
- Evaluation must go beyond accuracy

---

## **Summary**

Week 13 provided a solid progression from classical classification models to more advanced ensemble techniques and evaluation strategies.
This week built the foundation for working with stronger, scalable, and production-ready models — while emphasizing the importance of robust evaluation.

---
