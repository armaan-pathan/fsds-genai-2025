# Regression in Machine Learning

This folder contains my learning journey of **Regression techniques** in Machine Learning, starting from **Simple Linear Regression** to more advanced methods like **Multiple Linear Regression** and **Regularization (Ridge, Lasso, Elastic Net)**.  
Each sub-folder documents one day’s work with **theory, code, and results**.  

---

## Contents

### [Day41 – Simple Linear Regression](Day41_Simple_Linear_Regression)
- Learned the concept of **Simple Linear Regression (SLR)**.  
- Implemented a regression model to study the relationship between two variables.  
- Evaluated the model using statistical methods (`scipy.stats`, R², p-value, etc.).  
- Documented the workflow in **Spyder** for coding and **Jupyter Notebook** for explanation.  

---

### [Day42 – Simple Linear Regression with Streamlit App](Day42_SLR_Deployment_with_Streamlit)
- Deployed the **SLR model from Day41** using **Streamlit**.  
- Built a simple frontend where users can input values and get predictions.  
- Exported trained model, integrated it into `app.py`, and created an interactive prediction tool.  
- Includes a PDF screenshot of the app output.  

---

### [Day43 – Multiple Linear Regression](Day43_Multiple_Linear_Regression)
- Extended SLR to **Multiple Linear Regression (MLR)** with multiple independent variables.  
- Data preprocessing with **get_dummies (encoding)**.  
- Applied regression using both **sklearn** and **statsmodels (OLS)**.  
- Learned about **p-values** and performed **backward elimination** to refine the model.  
- Compared predicted vs actual values and analyzed **model parameters vs performance**.  

---

### [Day44 – Regularization Techniques](Day44_Regularization_Techniques)
- Learned about **Overfitting vs Underfitting** and the **Bias–Variance Tradeoff**.  
- Explored **regularization techniques** to prevent overfitting:
  - **Ridge Regression (L2)** – shrinks coefficients.  
  - **Lasso Regression (L1)** – feature elimination by shrinking some coefficients to zero.  
  - **Elastic Net (L1 + L2)** – combines advantages of Ridge and Lasso.  
- Implemented all models on the **Car MPG dataset**.  
- Compared model performance using **R² Score, MSE** and visualized coefficient differences.  

---

## Key Learnings Across Regression
- Regression helps understand relationships between features and target variables.  
- **SLR → MLR → Regularization** shows the natural progression from simple models to robust, real-world applicable models.  
- Learned to use:
  - **sklearn** for implementation,  
  - **statsmodels** for detailed statistics,  
  - **Streamlit** for deployment.  
- Regularization improves model generalization and prevents overfitting.  

---

## Upcoming Work
- Polynomial Regression  
- Advanced regression use-cases  
- Transition into **Classification algorithms**  

