# **Week 14 – Clustering, Project Deployment & Introduction to NLP**

## **Overview**

**Week 14** marked an important transition from **Unsupervised Learning** to **Natural Language Processing (NLP)**.
The week began by strengthening unsupervised learning skills with clustering algorithms, followed by developing a practical ML deployment project, and finally entering the world of textual data processing.

Across Days **58–62**, the focus evolved from:

* Understanding structure in unlabeled data (Clustering)
* Applying ML concepts in a real-world **Flask-based project**
* Moving into NLP with text preprocessing and representation techniques

The week created a bridge between classical machine learning and the AI/NLP domain.

---

## **Contents**

---

### **[Day 58 – Clustering with K-Means](Day58_Clustering)**

The week started with **Unsupervised Learning** through **K-Means**, one of the most widely used clustering algorithms.

**Key concepts covered:**

* What clustering is and how it differs from supervised learning
* How K-Means works:

  * Initializing centroids
  * Assigning points to nearest centroids
  * Updating centroids iteratively
* **Within-Cluster Sum of Squares (WCSS)** and optimization
* Selecting the optimal number of clusters using the **Elbow Method**

**Implementation & Insights:**

* Applied K-Means to the **Mall Customers Dataset**
* Identified optimal `k = 5` using the Elbow Method
* Visualized 5 well-separated clusters representing different customer segments
* Interpreted clusters based on income & spending score patterns

This session set the stage for exploring more flexible clustering techniques.

---

### **[Day 59 – Hierarchical & Density-Based Clustering](Day59_Hierarchical_and_Density-Based_Clustering)**

Building on K-Means, Day 59 introduced more advanced clustering algorithms.

**Hierarchical Clustering:**

* Difference between **Agglomerative (bottom-up)** and **Divisive (top-down)**
* Linkage methods: single, complete, average, Ward’s
* Constructing and interpreting **dendrograms**

**DBSCAN (Density-Based Spatial Clustering):**

* Grouping data based on density without specifying number of clusters
* Parameters: `eps`, `min_samples`
* Ability to detect noise and clusters of **irregular shapes**

**Observations:**

* Hierarchical clustering provides a **full cluster hierarchy** without predefining `k`
* DBSCAN effectively identifies noise and clusters not captured by K-Means
* DBSCAN is robust to outliers and captures complex shapes in data

This day completed the clustering module with methods suitable for real-world noisy datasets.

---

### **[Project: Student Mark Predictor](Student_Mark_Predictor)**

Mid-week, I worked on a **complete end-to-end machine learning project** combining model building and deployment.

**Project Highlights:**

* Built a **Linear Regression model** to predict marks based on study hours
* Saved the model using **Joblib**
* Integrated it into a **Flask web application**
* Designed an attractive UI with gradients, validations, and responsive layout
* Implemented input validation (1–24 hours) with meaningful user feedback

**Key Skills Practiced:**

* Model packaging
* Backend integration with Flask
* Designing user-friendly interfaces
* Deploying predictive models in real-world settings

The project served as a practical checkpoint before transitioning to NLP.

---

### **[Day 60 – Introduction to NLP](Day60 Intro to NLP and Text Preprocessing)**

After completing the ML module, I officially entered the **AI/NLP** domain.

**Topics Covered:**

* What NLP is and how it helps machines understand language
* Applications of NLP (chatbots, sentiment analysis, search engines, etc.)
* Components of NLP:

  * **NLU – Natural Language Understanding**
  * **NLG – Natural Language Generation**
* Text preprocessing fundamentals:

  * **Tokenization** (word, sentence, whitespace, WordPunct)
  * **N-grams** (bigram, trigram)
* Word normalization techniques:

  * **Stemming**
  * **Lemmatization**

This day built the core foundation for processing raw textual data.

---

### **[Day 61 – Advanced Text Preprocessing](Day61_Advanced_Text_Preprocessing_in_NLP)**

Day 61 strengthened the preprocessing depth by adding semantic-level text analysis.

**Skills Learned:**

* **Stopword Removal** using NLTK
* **POS Tagging** – identifying grammatical roles (NOUN, VERB, ADJ, etc.)
* **Named Entity Recognition (NER)** to extract real-world entities
* **WordCloud Visualization** to analyze dominant words

**Why this matters:**

* Stopword removal helps focus on important terms
* POS tagging and NER bring linguistic understanding essential for advanced NLP tasks
* WordCloud provides a quick summary of text themes

This session prepared me for feature extraction techniques coming next.

---

### **[Day 62 – Word Embedding Techniques](Day62_Word_Embedding_Techniques_in_NLP)**

The week concluded with converting text into meaningful **numerical representations**.

**Covered Embedding Techniques:**

* **Bag of Words (BoW)** – frequency-based representation
* **TF-IDF** – importance-weighted representation
* **Word2Vec** (CBOW & Skip-Gram) – neural network-based dense embeddings

**Key Learnings:**

* BoW is simple but ignores order & meaning
* TF-IDF highlights important words over common ones
* Word2Vec captures **semantic relationships** (e.g., king – man + woman ≈ queen)
* Word embeddings form the backbone of modern NLP models like RNNs, LSTMs, and Transformers

This day marked the completion of NLP fundamentals and prepared for deep NLP modeling ahead.

---

## **Key Takeaways (Week 14)**

### **Clustering**

- K-Means helps find structured segments
- Hierarchical clustering builds complete cluster trees
- DBSCAN handles irregular shapes and identifies noise

### **Practical ML Deployment**

- Built and deployed an ML model using Flask
- Learned UI design, validation, and backend integration

### **NLP Foundations**

- Understood how text is processed and normalized
- Learned significant preprocessing steps: tokenization, stemming, lemmatization
- Advanced cleaning: POS tagging, NER, word clouds
- Explored vectorization: BoW, TF-IDF, Word2Vec

---

## **Summary**

Week 14 served as a transition point:

* From **unsupervised learning → practical deployment → NLP**
* From structured numerical data → **unstructured text data**
* From classical ML techniques → foundations of **AI and language modeling**

This week built both theoretical understanding and practical skills that will carry forward into **Deep Learning, GenAI, and Agentic AI** modules in the coming weeks.

---
