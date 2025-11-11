# Day 66 – XML Scraping 

This notebook demonstrates how to **parse XML files** and **clean the extracted text** using Python.
The focus is on converting XML documents into plain text that can later be used for **NLP preprocessing or text analysis**.

---

## Overview

In this session, I learned how to extract raw text from XML files using the **ElementTree** library and then clean the extracted text using **BeautifulSoup** and **regular expressions**.
This process helps remove unwanted tags, special characters, and noise, preparing the data for further **Natural Language Processing (NLP)** tasks such as tokenization, sentiment analysis, or summarization.

---

## Topics Covered

* Reading and parsing XML files using `xml.etree.ElementTree`
* Converting XML tree structure into readable text
* Removing HTML tags and unwanted characters
* Cleaning and denoising text using custom functions
* Preparing XML text for NLP-based analysis

---

## Tech Stack

* **Python**
* **xml.etree.ElementTree** – For XML parsing
* **BeautifulSoup (bs4)** – For HTML/XML text cleaning
* **re (Regular Expressions)** – For removing unwanted patterns
* **nltk** – For tokenization, stopword handling, and lemmatization
* **Jupyter Notebook**

---

## Key Learnings

* Learned how to **read and parse XML files** using ElementTree.
* Understood how to **convert XML elements into plain text**.
* Built custom cleaning functions to remove:

  * HTML tags
  * Square-bracketed text
  * Extra whitespace
* Prepared clean, denoised text for **NLP preprocessing**.
* Understood how text extraction from XML is a critical step before applying any NLP model.

---

## Summary

This session focused on transforming structured XML content into **clean, usable text**.
The process involved parsing XML with **ElementTree**, cleaning it using **BeautifulSoup** and **regex**, and producing a plain text output ready for **NLP applications** such as text classification or summarization.

---
