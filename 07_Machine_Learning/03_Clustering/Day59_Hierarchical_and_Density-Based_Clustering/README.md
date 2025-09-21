# Day 59 – Hierarchical and Density-Based Clustering

## Overview

On **Day 59**, I continued learning **Clustering techniques**, moving beyond K-Means to more advanced methods.
The focus was on **Hierarchical (Agglomerative) Clustering** and **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**.
These algorithms allow clustering without pre-defining the number of clusters and can handle more complex patterns, such as irregular shapes and noisy data.

---

## Contents

### 1. Theory

* **Hierarchical Clustering**

  * Explained the difference between **Agglomerative (bottom-up)** and **Divisive (top-down)** approaches.
  * Detailed steps of **Agglomerative Clustering**: starting with individual points, merging closest clusters until one cluster remains.
  * Introduced **linkage methods** (single, complete, average, Ward’s).

* **Dendrogram**

  * Tree-like diagram showing the merging of clusters.
  * X-axis = data points, Y-axis = distance/dissimilarity at which clusters merge.
  * Cutting the dendrogram at a chosen height gives the number of clusters.

* **DBSCAN (Density-Based Clustering)**

  * Groups dense regions into clusters while marking sparse points as noise.
  * Key parameters: `eps` (neighborhood radius), `min_samples` (minimum points for a cluster).
  * Advantages: finds clusters of arbitrary shape, automatically detects outliers, does not require specifying `k`.
  * Limitations: results depend heavily on parameter selection.

* **Comparison with K-Means**

  * K-Means requires `k`, assumes spherical clusters, and is sensitive to outliers.
  * Hierarchical clustering builds a hierarchy and works without predefining `k`.
  * DBSCAN handles arbitrary shapes and noise, making it more flexible in real-world data.

---

### 2. Code Implementation

* Built a **dendrogram** to visualize merging of data points.
* Applied **Agglomerative Clustering** with `n_clusters=5` and plotted the resulting clusters.
* Implemented **DBSCAN** with tuned parameters (`eps`, `min_samples`) and plotted clusters with noise points marked in black.
* Compared clustering behaviors:

  * Agglomerative created structured clusters similar to K-Means.
  * DBSCAN revealed noise points and formed clusters based on density.

---

## Results & Observations

* The **dendrogram** showed clear merging of data points and helped identify a good cut for forming 5 clusters.
* **Agglomerative Clustering** grouped customers into distinct segments similar to K-Means but without predefining `k`.
* **DBSCAN** successfully identified clusters of arbitrary shape and marked scattered points as noise.
* Key insight: DBSCAN is more robust in detecting outliers compared to hierarchical and centroid-based methods.

---

## Key Takeaways

* **Hierarchical Clustering** builds a tree of clusters step by step, with **Agglomerative (bottom-up)** being the most common approach.
* A **dendrogram** is an essential tool to visualize merges and decide the number of clusters.
* **DBSCAN** groups dense areas and identifies **noise/outliers** automatically, making it powerful for irregular datasets.
* Compared to K-Means:

  * Hierarchical clustering doesn’t need `k` in advance.
  * DBSCAN works well with arbitrary shapes and noise.
* Together, hierarchical clustering and DBSCAN extend clustering beyond K-Means, making analysis more flexible and robust for real-world data.

---

**Conclusion:**
This day provided deeper insights into clustering by introducing **hierarchical methods** and **density-based clustering**.
These algorithms allow more flexibility in identifying hidden patterns and are especially useful when data is noisy or doesn’t fit the assumptions of K-Means.

---
