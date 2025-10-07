# Day 60 – Introduction to NLP

## Overview
After completing the **Machine Learning** segment, this day marks the beginning of the **Artificial Intelligence (AI)** module — starting with **Natural Language Processing (NLP)**.  
In this notebook, I explore how machines understand and process human language, covering essential NLP preprocessing concepts such as **tokenization**, **stemming**, and **lemmatization**.

---

## Objectives
- Understand the concept and importance of **Artificial Intelligence (AI)**.
- Learn the basics of **Natural Language Processing (NLP)** and its applications.
- Explore how **NLP** helps machines interpret human language.
- Perform **text tokenization**, **stemming**, and **lemmatization** using `NLTK`.
- Understand the difference between stemming and lemmatization.
- Build a foundation for upcoming advanced NLP tasks.

---

## Topics Covered
1. **Introduction to Artificial Intelligence**
   - AI vs ML Overview  
   - Types of Unstructured Data (Text, Image, Audio, etc.)

2. **Introduction to NLP**
   - What is NLP  
   - How NLP works  
   - Applications of NLP  
   - Components: **NLU** (Understanding) & **NLG** (Generation)  
   - Popular NLP Libraries: `NLTK`, `spaCy`, `Gensim`, `Stanford NLP`

3. **Text Preprocessing Techniques**
   - **Hierarchy of Text in NLP** (Words → Sentences → Paragraphs → Documents → Articles)
   - **Tokenization** (Word, Sentence, Paragraph, Whitespace, WordPunct)
   - **N-grams** (Bigram, Trigram, N-gram)

4. **Word Normalization Techniques**
   - **Stemming** (Porter, Lancaster, Snowball Stemmer)
   - **Lemmatization** (Using WordNet Lemmatizer)

---

## Key Takeaways
- NLP is a branch of AI that enables machines to **read, understand, and derive meaning from text**.  
- **Tokenization** splits raw text into manageable units for processing.  
- **Stemming** trims words to their root by removing suffixes, while **Lemmatization** provides a dictionary-based base form.  
- Text preprocessing is a **crucial foundation** for all NLP and deep learning tasks.  
- Libraries like **NLTK**, **spaCy**, and **Gensim** are essential for NLP pipelines.

---

## Libraries Used
```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, BlanklineTokenizer, WhitespaceTokenizer, WordPunctTokenizer
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
````

---

## Next Steps

In the upcoming days, I’ll move deeper into NLP by learning:

* Text Cleaning & Stopword Removal
* Bag of Words and TF-IDF
* Text Classification Models
* Introduction to RNNs and LLMs

---

Would you like me to also include a **“UI Preview / Output”** section (like your Flask project READMEs) showing screenshots of tokenization or outputs for GitHub visuals?
```
