# Day 58 – Clustering with K-Means

## Overview

On **Day 58**, I began exploring **Unsupervised Learning**, starting with **Clustering techniques**.
Unlike classification and regression, clustering does not use predefined labels. Instead, it groups data points based on similarity.
The main focus of this notebook was the **K-Means algorithm**, one of the most widely used clustering methods.

---

## Contents

### 1. Theory

* Introduction to **Clustering** and how it differs from supervised learning.
* Detailed explanation of the **K-Means algorithm**:

  * How centroids are chosen and updated.
  * Objective of minimizing **Within-Cluster Sum of Squares (WCSS)**.
* **Elbow Method** to determine the optimal number of clusters.
* Real-world use cases such as **customer segmentation**, **market research**, and **recommendation systems**.

---

### 2. Code Implementation

* Used the **Mall Customers dataset** with features: **Annual Income** and **Spending Score**.
* Applied the **Elbow Method** → identified `k=5` as the best number of clusters.
* Trained a **K-Means model** to segment customers.
* Visualized clusters with different colors and centroids marked.
* Interpreted each cluster as a unique customer group with distinct spending and income behavior.

---

## Results & Observations

* The **Elbow Method curve** showed a clear bend at `k=5`, confirming 5 clusters as optimal.
* Cluster visualization revealed five distinct customer groups:

  * Low income, low spending.
  * High income, high spending.
  * Medium income, medium spending.
  * Low income, high spending.
  * High income, low spending.
* These insights can directly guide **business strategies and marketing decisions**.

---

## Key Takeaways

* **Clustering** groups similar data points without using labels.
* **K-Means** is simple, efficient, and widely applied for segmentation tasks.
* The **Elbow Method** helps determine the right number of clusters.
* Visualization makes it easier to interpret clusters in real-world contexts.
* Practical applications include **customer segmentation**, **image compression**, and **pattern discovery**.

---

**Conclusion:**
This day provided a solid introduction to **Unsupervised Learning** through clustering.
By applying K-Means to customer data, I learned how businesses can segment customers and design targeted strategies.

---
