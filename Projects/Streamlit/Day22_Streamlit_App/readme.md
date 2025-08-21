# Day 22 – Streamlit App

This folder contains my first projects using **Streamlit**, a Python library for building interactive web applications quickly and easily.  

On this day, I explored the basics of Streamlit and created **two small apps**:  
1. A **Square Calculator App**.  
2. A **User Profile & Data Display App**.  

---

## Contents

### **App 1 – Square Calculator**
- Title: *First Streamlit App*  
- Features:
  - Displays a welcome message.
  - Includes a **slider widget** for selecting a number between 0 and 100.
  - Calculates and displays the **square of the selected number**.  
- Example: If the slider is set to 50, the app outputs:  
  *The square of 50 is 2500.*

---

### **App 2 – User Profile & Interactive Features**
- Title: *Streamlit App*  
- Features:
  - Sidebar with input widgets:
    - **Text Input** → User enters their name.  
    - **Slider** → User selects their age.  
    - **Select Box** → User picks their favorite color.  
  - Main page displays a personalized welcome message using the inputs.  
  - Generates and shows a **random dataset (10×5 DataFrame)**.
  - Includes interactivity:
    - **Checkbox** → Toggle display of raw dataset.  
    - **Button** → Display “Hello there!” when clicked, otherwise shows “Goodbye”.

---

## Key Learnings
- Basics of **Streamlit components**:
  - `st.title()`, `st.header()`, `st.subheader()` for text formatting.
  - `st.slider()`, `st.text_input()`, `st.selectbox()` for user inputs.
  - `st.write()` and `st.dataframe()` for displaying text and data.
  - `st.checkbox()` and `st.button()` for interactivity.
- Difference between **main content area** and **sidebar** in Streamlit apps.
- How to combine UI elements with Python logic to build interactive dashboards.

---

## Libraries Used
- **streamlit** → UI and interactivity  
- **pandas** → Data handling  
- **numpy** → Random number generation for datasets  

---

## Learning Outcome
By building these apps, I learned:  
- How to create **interactive web apps with Streamlit** in just a few lines of Python.  
- How to use sliders, text input, checkboxes, and buttons effectively.  
- How to connect user input with backend logic to generate dynamic outputs.  

---

## Running the Apps
To run any app locally:
```bash
streamlit run intro.py
