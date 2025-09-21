# Clustering

## Overview

The **Clustering** section focuses on **unsupervised learning**, where data is grouped based on similarity without predefined labels.
I explored the most widely used clustering techniques: **K-Means**, **Hierarchical (Agglomerative)**, and **DBSCAN**.
These methods help uncover hidden patterns in datasets, such as customer segmentation.

---

## Contents

### [Day 58 – Clustering](Day58_Clustering)

* Introduction to **Clustering** and difference from supervised learning.
* Detailed explanation of the **K-Means algorithm** (centroids, WCSS, iterations).
* Applied the **Elbow Method** to find the optimal number of clusters (`k=5`).
* Implemented K-Means on the **Mall Customers dataset** (Annual Income vs Spending Score).
* Visualized 5 distinct clusters with centroids marked.
* Interpreted each cluster as a unique customer group (e.g., high income–high spending, low income–low spending).

---

### [Day 59 – Hierarchical and Density-Based Clustering](Day59_Hierarchical_and_Density-Based_Clustering)

* Studied **Hierarchical Clustering**:

  * **Agglomerative approach** (bottom-up merging).
  * Linkage methods (single, complete, average, Ward’s).
* Built and interpreted a **dendrogram** to visualize cluster formation and decide optimal clusters.
* Implemented **Agglomerative Clustering** and plotted customer groups.
* Explored **DBSCAN (Density-Based Clustering)**:

  * Formed clusters based on density.
  * Identified **outliers/noise points** automatically.
  * Compared DBSCAN with K-Means and Hierarchical methods.
* Observed how DBSCAN detects irregular cluster shapes and noise better than other methods.

---

## Key Takeaways

* **Clustering** is unsupervised and groups data without labels.
* **K-Means**: Simple, fast, and effective for spherical clusters, but requires predefined `k` and is sensitive to outliers.
* **Hierarchical (Agglomerative)**: Builds a tree of clusters using a bottom-up approach and visualizes it with a **dendrogram**.
* **DBSCAN**: Density-based, finds arbitrary-shaped clusters, and detects noise points automatically.
* Together, these methods cover the most practical approaches to clustering for real-world datasets like customer segmentation.

---

**Conclusion:**
The Clustering section gave me hands-on experience with **K-Means, Hierarchical, and DBSCAN**, making it clear how unsupervised learning can reveal hidden groups and patterns in data.

---
