# Day 63 – Chunking in NLP & LLMs

## Overview  
This notebook explores the concept of **Chunking** in the context of both **traditional Natural Language Processing (NLP)** and **Large Language Models (LLMs)**.  
It provides theoretical understanding along with practical implementations using **Hugging Face Transformers**.  

---

## Objectives  
- Understand the meaning and purpose of **chunking** in NLP.  
- Learn the difference between **syntactic chunking** and **context-based chunking**.  
- Implement **tokenization**, **text generation**, and **text chunking** using pre-trained transformer models.  
- Explore how chunking helps manage large text inputs efficiently in **LLMs**.

---

## Topics Covered  

### 1. Introduction to Chunking  
- What is chunking in NLP and LLMs?  
- Importance of chunking in text processing and model performance.

### 2. Environment Setup  
- Checking GPU availability (`nvidia-smi`).  
- Installing and importing required libraries like `transformers`.

### 3. Understanding Transformer Models  
- Overview of popular transformer architectures such as **BERT**, **GPT**, **T5**, **RoBERTa**, **XLNet**, and others.  
- Explanation of how transformers revolutionized NLP.

### 4. Tokenization  
- Converting text into tokens using GPT-2 tokenizer.  
- Understanding **input IDs** and **attention masks**.  
- Explanation of how tokenization prepares text for model processing.

### 5. Text Generation with GPT-2  
- Generating text based on a prompt using **AutoModelForCausalLM**.  
- Understanding the `generate()` and `decode()` functions in text generation.

### 6. Text Chunking Implementation  
- Writing a custom function to **split long text** into smaller chunks.  
- Generating responses for each chunk using the GPT-2 model.  
- Understanding how chunking helps models overcome **context window limitations**.

### 7. Chunking Example using BERT  
- Using **BERT tokenizer** to split long text into token chunks.  
- Explanation of chunk size and its importance in text processing.

### 8. Using Transformer Pipelines  
- Performing **sentiment analysis** using Hugging Face’s ready-to-use pipelines.  
- Understanding pre-trained pipeline outputs.

---

## Conclusion  
This notebook provided a detailed understanding of **Chunking** and its two main perspectives:  
1. **Chunking in Traditional NLP** – syntactic parsing to identify phrases.  
2. **Chunking in LLMs** – context and efficiency strategy for managing long documents.  

It demonstrated how chunking is essential for both **linguistic structure analysis** and **efficient model processing** in modern NLP applications.

---

##  Key Learning  
- Dual role of chunking in NLP and LLMs.  
- How chunking improves efficiency and preserves context.  
- Practical implementation of tokenization, generation, and chunking using Transformer models.

---
