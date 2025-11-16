# **Natural Language Processing (NLP)**

This folder contains all the notebooks and resources for **Days 60–66**, covering the foundational and intermediate concepts of **Natural Language Processing (NLP)**.

NLP is a core component of the Full Stack Data Science & GenAI program, enabling machines to understand, interpret, and generate human language.
These sessions mark the transition from classical ML into the AI and language modeling domain, building skills that connect text preprocessing, feature engineering, deep learning, and modern LLMs.

---

## **Contents (Day 60 – Day 66)**

Below is a summary of the topics covered in this folder:

---

### **Day 60 – Introduction to NLP**

* What NLP is & why it is important
* Applications (chatbots, search engines, sentiment analysis, etc.)
* Tokenization (word, sentence, whitespace, WordPunct)
* N-grams (bigram, trigram)
* Word normalization:

  * Stemming
  * Lemmatization
* Introduction to common NLP libraries (NLTK, spaCy, Gensim)

---

### **Day 61 – Advanced Text Preprocessing**

* Stopword removal
* POS tagging
* Named Entity Recognition (NER)
* WordCloud generation
* Semantic-level preprocessing for downstream NLP tasks

---

### **Day 62 – Word Embedding Techniques**

* Why text must be converted to numerical vectors
* Vectorization methods:

  * Bag of Words (BoW)
  * TF-IDF
  * Word2Vec (CBOW + Skip-gram)
* Differences between sparse & dense embeddings
* Using Gensim to train and load word vectors

---

### **Day 63 – Chunking in NLP & LLMs**

* Understanding chunking in traditional NLP (syntactic chunks)
* Chunking for LLMs (splitting long text for context-window limits)
* GPT-2 tokenization
* Text generation using Transformers
* Custom functions for long-text chunking
* BERT-based chunking approach

---

### **Day 64 – Machine Learning Models in NLP**

* End-to-end sentiment analysis on Restaurant Reviews
* Full NLP + ML pipeline:

  * Cleaning
  * Vectorization (BoW, TF-IDF)
  * Model training (NB, LR, SVM, RF, DT, KNN)
* Accuracy comparison
* Dataset expansion & performance improvement
* Final accuracy achieved: up to **98%** using advanced models

---

### **Day 65a – Introduction to spaCy**

* spaCy NLP workflow
* Tokenization
* POS tagging
* Lemmatization
* NER
* Dependency parsing
* spaCy vs NLTK comparison
* Industrial advantages of spaCy

---

### **Day 65b – Text Summarization using spaCy**

* Extractive summarization
* Word-frequency scoring
* Selecting sentences based on normalized scores
* Limitations of basic summarizers
* Future improvements with transformers (T5, BART, PEGASUS)

---

### **Day 66 – XML Scraping & Cleaning**

* Extracting text from XML files
* Parsing XML using `ElementTree`
* Cleaning and converting structured XML text to plain text
* Removing tags, noise, special characters
* Preparing textual data for NLP pipelines

---

## **What This Folder Represents**

This folder covers the **complete NLP foundation**, including:

* Text preprocessing
* Feature extraction
* ML-based NLP modeling
* spaCy-based advanced NLP
* Working with long text, XML, and document-level processing
* Preparing for deep NLP tasks like LSTMs, Transformers, RAG, and LLM fine-tuning

These concepts build the grounding required for advanced GenAI and Agentic AI development.

---

## **Folder Structure**

```
08_natural_language_processing/
│
├── Day60_Introduction_to_NLP/
├── Day61_Advanced_Text_Preprocessing/
├── Day62_Word_Embeddings/
├── Day63_Chunking_in_NLP_and_LLMs/
├── Day64_ML_Models_in_NLP/
├── Day65a_Intro_to_spaCy/
├── Day65b_Text_Summarization_with_spaCy/
└── Day66_XML_Scraping/
```

Each directory contains:

* Notebook(s)
* Code experiments
* Supporting files (datasets, screenshots, etc.)
* A dedicated README explaining the day's work

---

## **Summary**

The notebooks in this folder build the **entire foundation for NLP**, bridging classical ML and modern LLM-based workflows.
After completing Day 60–66, I gained hands-on experience in transforming raw text → clean text → vectorized text → ML/NLP models → real-world applications.

This prepares the path for upcoming modules like:

* Deep Learning for NLP
* Transformers
* Fine-tuning LLMs
* RAG systems
* GenAI applications
* Agentic AI workflows

---
