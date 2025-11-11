# Day 67 – MLOps Introduction and MLflow Basics

This notebook marks the **beginning of my MLOps journey**.  
I explored the **concept of MLOps (Machine Learning Operations)** and learned how to use **MLflow**, one of the most popular open-source tools for **experiment tracking and model management**.

The practical focuses on understanding how to make machine learning workflows **reproducible, organized, and production-ready**.

---

## Overview

In this notebook, I:
- Understood **what MLOps is** and why it is essential in ML development.
- Learned about the **MLOps lifecycle** – from data preparation to monitoring.
- Explored **MLflow**, its components, and how it fits into the MLOps pipeline.
- Implemented a simple **Logistic Regression** model.
- Tracked **parameters, metrics, and models** using MLflow.
- Accessed and analyzed results through the **MLflow UI dashboard**.

---

## Key Concepts Covered

| Concept | Description |
|----------|-------------|
| **MLOps** | Combines Machine Learning and DevOps principles to manage ML lifecycles efficiently. |
| **Experiment Tracking** | Logging all training details (parameters, metrics, and models) for reproducibility. |
| **MLflow** | An open-source platform to manage the ML lifecycle — experiment tracking, model packaging, and deployment. |
| **Tracking UI** | A web interface to visualize runs, compare experiments, and access logged artifacts. |

---

## Practical Implementation

### Steps Performed:
1. Imported required Python libraries (`numpy`, `sklearn`, `mlflow`, etc.).
2. Created a **synthetic imbalanced dataset** using `make_classification()`.
3. Split data into training and testing sets.
4. Trained a **Logistic Regression model**.
5. Evaluated the model using classification metrics.
6. Integrated **MLflow** to log:
   - Parameters  
   - Metrics (Accuracy, F1-score, Recall)  
   - Model artifacts
7. Accessed **MLflow UI** at `http://127.0.0.1:5000` for visualization.

---

## MLflow UI Overview

Included screenshots in the notebook demonstrate:
- Experiments dashboard  
- Runs list and details  
- Logged parameters and metrics  
- Visual metric charts for model performance  

These help in understanding how MLflow organizes and tracks experiments.

---

## Key Learnings

- Learned the **basics of MLOps** and why it’s critical for scaling ML workflows.  
- Understood the **role of MLflow** in managing experiments and models.  
- Gained practical experience in **logging, tracking, and visualizing** experiments.  
- Observed how MLflow simplifies **collaboration and reproducibility** for ML teams.  
- Set a strong foundation for upcoming topics like **Model Registry**, **Deployment**, and **Monitoring**.

---


## File Structure

```

Day67_MLOps_Introduction_and_MLflow_Basics/
│
├── Day67_MLOps_Introduction_and_MLflow_Basics.ipynb     # Final notebook for Day 67
├── screenshot1.png                                      # MLflow Experiments Dashboard
├── screenshot2.png                                      # Runs list under experiment
├── screenshot3.png                                      # Run overview and metrics
├── screenshot4.png                                      # Model parameters and logged model
├── screenshot5.png                                      # Metric visualization
└── README.md                                            # Documentation (this file)

```

---

## Conclusion

This notebook successfully demonstrates the **first step of MLOps in action** using MLflow.  
It shows how even a simple machine learning model can be tracked, logged, and managed efficiently — laying the groundwork for building **scalable, production-ready ML pipelines**.


---