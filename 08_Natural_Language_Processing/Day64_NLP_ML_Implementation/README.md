# Day 64 – How Machine Learning Models are Implemented in NLP

---

## Overview

This notebook demonstrates how **Machine Learning algorithms** can be applied to **Natural Language Processing (NLP)** tasks.
Using a **Restaurant Reviews dataset**, the goal was to build models that predict whether a given customer review is **positive** or **negative**.

Throughout the process, different text representation methods like **Bag of Words** and **TF-IDF** were explored, and multiple ML models were implemented, trained, and compared for performance.

---

## Objectives

* Understand how ML models are used in NLP applications such as **sentiment analysis**.
* Learn the complete **NLP + ML workflow** — from text preprocessing to model evaluation.
* Compare **feature extraction techniques** like Bag of Words and TF-IDF.
* Evaluate different ML algorithms for text classification.
* Observe how dataset expansion and better feature representation affect accuracy and generalization.

---

## Topics Covered

1. **Importing Libraries and Dataset**
2. **Text Cleaning and Preprocessing**

   * Removing special characters, punctuation, and stopwords
   * Stemming and lowercasing
3. **Feature Extraction**

   * Bag of Words (BoW)
   * TF-IDF (with unigrams and bigrams)
4. **Model Training**

   * Naive Bayes, Logistic Regression, SVM (Linear & RBF), Random Forest, Decision Tree, KNN
5. **Evaluation Metrics**

   * Confusion Matrix, Accuracy, Bias & Variance
6. **Dataset Expansion**

   * Improving model generalization through data duplication
7. **Model Comparison and Analysis**

---

## Results

### Performance Summary

* **Bag of Words (BoW, 1000 samples):**

  * Best model – **Naive Bayes (76.5%)**
  * Others between **70–73% accuracy**

* **TF-IDF (1000 samples):**

  * Similar range (**71–76%**) with improved balance.
  * **Naive Bayes** remained strongest.

* **TF-IDF + Expanded Dataset (3000 samples, unigrams + bigrams):**

  * **Random Forest** and **SVM (RBF)** reached **~98.2% accuracy**.
  * **SVM (Linear)** and **Logistic Regression:** ~96–97%.
  * **Naive Bayes:** 96%.
  * **Decision Tree:** 80%.
  * **KNN:** 61%.

---

## Key Learning

* **Representation matters:** TF-IDF captures word importance better than Bag of Words.
* **Data size matters:** Expanding the dataset significantly improved model accuracy and generalization.
* **Top performers:** **Random Forest** and **SVM (RBF)** (~98%) proved highly reliable for sentiment analysis.
* **Strong baselines:** **Naive Bayes** and **Logistic Regression** (~96%) remained fast and efficient.
* **Weak models:** **Decision Tree** overfits easily, and **KNN** struggles with sparse text data.

---

## Conclusion

This day successfully demonstrated how **Machine Learning** can be used to solve **NLP tasks** like sentiment analysis.
By moving from **Bag of Words** to **TF-IDF** and expanding the dataset, model accuracy improved from **76% to 98%**.

Overall, this notebook reinforced that:

* The **quality of data representation** and **quantity of data** are key drivers of ML performance in NLP.
* **SVM (RBF)** and **Random Forest** provide the most robust results.
* **Naive Bayes** and **Logistic Regression** serve as excellent lightweight alternatives for fast, accurate sentiment prediction.


