# Day 27 – Exploratory Data Analysis on Movie Ratings

This project applies **Exploratory Data Analysis (EDA)** techniques to a **Movie Ratings dataset**.  
The goal was to uncover trends, patterns, and user behavior through data exploration and visualization.

---

## Objectives
- Understand the structure of the movie ratings dataset.  
- Explore the distribution of ratings across movies and users.  
- Identify the most popular movies and genres.  
- Analyze user preferences and rating behavior.  
- Visualize insights using plots for better interpretation.

---

## Key Steps & Analysis
1. **Data Loading & Inspection**
   - Loaded dataset into Pandas.
   - Used `.head()`, `.info()`, `.describe()` to understand data structure.

2. **Data Cleaning**
   - Checked for missing values or duplicates.
   - Verified consistency of ratings.

3. **Univariate Analysis**
   - Distribution of ratings (1–5 scale).
   - Count of ratings per movie.

4. **Bivariate Analysis**
   - Relationship between users and number of ratings given.
   - Popularity of certain movies across different groups.

5. **Visualizations**
   - **Histograms** – Distribution of ratings.  
   - **Bar Charts** – Most rated movies, popular genres.  
   - **Heatmaps** – Correlation between features.  

---

## Key Insights
- Most ratings fall within a **middle range** (3–4 stars).  
- Some movies receive significantly more ratings, showing **popularity bias**.  
- User activity follows a long-tail distribution: a small set of users rate very frequently.  

---

## Tools & Libraries
- **Pandas** – Data handling  
- **Matplotlib & Seaborn** – Visualization  
- **NumPy** – Numerical operations  

---

## Learning Outcome
By working on this project, I learned how to:  
- Perform EDA on real-world entertainment data.  
- Clean and explore datasets to uncover meaningful insights.  
- Present findings visually to support decision-making in areas like movie recommendations.  
