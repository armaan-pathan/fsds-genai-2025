# Multiple Language Translation App

This project is a **Multi-Language Translation System** built using **Streamlit**, allowing users to **translate text into multiple languages** and optionally **listen to the translated audio** using **Google Text-to-Speech (gTTS)**.

It supports **over 60 languages**, making it a simple and interactive tool for real-time translation and pronunciation.

---

## Features

* **Multi-language Translation:** Instantly translate text into 60+ supported languages.
* **Text-to-Speech Support:** Play or download audio of the translated text (for supported languages).
* **Interactive Streamlit UI:** Clean, responsive, and visually appealing user interface.
* **Auto Detection:** Automatically detects input language when source is set to *Auto-Detect*.

---

## Installation & Setup

### 1️. Clone the Repository

```bash
git clone https://github.com/armaan-pathan/fsds-genai-2025.git
cd multiple-language-translation
```

### 2️. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️. Run the Streamlit App

```bash
streamlit run app.py
```

---

## Input Example

Enter text in the main input box, select a **target language** from the sidebar, and click **Translate**.

Example Input:

```text
Hello, how are you?
```

**Select Target Language:** French 🇫🇷
**Output:** Bonjour, comment allez-vous ?

You can also play or download the translated audio if speech synthesis is supported.

---

## Screenshots

### Home Interface

![App Home](screenshots/output1.png)

### Translation Output

![Translation Output](screenshots/output2.png)

---

## Tech Stack

* **Python**
* **Streamlit** – for the interactive user interface
* **mtranslate** – for language translation
* **gTTS (Google Text-to-Speech)** – for generating audio output
* **Pandas** – for managing language data from CSV
* **HTML/CSS** – for the soft light UI theme customization

---

## Future Improvements

* Add **Dark/Light theme toggle**.
* Support **batch translation** for multiple sentences or files.
* Integrate **Hugging Face translation models** for improved accuracy.
* Include **language detection visualization** with confidence scores.
* Deploy the app on **Streamlit Cloud or Hugging Face Spaces**.

---

## Acknowledgments

* [mtranslate](https://pypi.org/project/mtranslate/) for translation functionality
* [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) for speech synthesis
* [Streamlit](https://streamlit.io/) for the interactive frontend

---

## Project Structure

```
multiple-language-translation/
│
├── screenshots/                         # App screenshots for README
│
├── README.md                            # Project documentation
├── app.py                               # Streamlit app script
├── language.csv                         # Language names and ISO codes
├── requirements.txt                     # Python dependencies
├── translator_demo.ipynb                # Optional notebook for testing
```

---
