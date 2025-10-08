# Day 62 – Word Embedding Techniques in NLP

## Overview
After learning about text preprocessing in previous sessions, this day focuses on how to represent text data in numerical form so that machines can understand and process it.  
This involves learning different **word embedding techniques** such as **Bag of Words (BoW)**, **TF-IDF**, and **Word2Vec**.  

These methods form the foundation of modern NLP systems — helping convert unstructured text into meaningful numeric representations that machine learning and deep learning models can use.

---

## Objectives
- Understand the need for word embeddings in NLP.  
- Learn how to convert text into numerical features using:
  - **Bag of Words (BoW)**
  - **TF-IDF (Term Frequency – Inverse Document Frequency)**
  - **Word2Vec**  
- Compare traditional vectorization methods with neural embeddings.  
- Observe how word relationships and semantics can be captured through embeddings.

---

## Topics Covered
1. **Introduction to Word Embeddings**
   - Why convert text to numbers  
   - Difference between sparse and dense representations  

2. **Bag of Words (BoW)**
   - Vocabulary creation and frequency matrix  
   - Limitations of BoW representation  

3. **TF-IDF (Term Frequency – Inverse Document Frequency)**
   - Importance weighting of words  
   - Formula and practical implementation  

4. **Word2Vec**
   - Concept of neural embeddings  
   - CBOW and Skip-gram models  
   - Generating word vectors and finding similar words using `gensim`  

5. **Comparison Summary**
   - BoW vs TF-IDF vs Word2Vec  

---

## Key Learnings
- **BoW** focuses on word frequency but ignores meaning and order.  
- **TF-IDF** improves BoW by assigning importance scores to unique words.  
- **Word2Vec** captures **semantic and contextual relationships** between words.  
- Word embeddings are essential for advanced NLP tasks like:
  - Sentiment Analysis  
  - Text Classification  
  - Chatbots  
  - Document Similarity  

---

## Libraries Used
- `pandas`  
- `scikit-learn`  
- `gensim`  

---

## Conclusion
Day 62 marks a major step in NLP learning — shifting from **text preprocessing** to **text representation**.  
Understanding word embeddings is essential before moving on to **Deep Learning-based NLP models** like RNN, LSTM, and Transformers in upcoming sessions.

---
