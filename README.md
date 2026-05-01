# Student Performance Prediction ML Project

An end-to-end Machine Learning project that predicts student performance based on demographic and academic attributes using multiple regression algorithms. This project follows an industry-style ML pipeline structure including data ingestion, preprocessing, model training, evaluation, and deployment-ready artifact generation.

---

## 📌 Project Overview

This project aims to build a robust regression pipeline for predicting student exam performance using machine learning techniques.

The workflow includes:

- Data Ingestion
- Data Transformation
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- Model Serialization
- Exception Handling & Logging

The project is modularized using a production-level folder structure to improve scalability and maintainability. Well-structured ML repositories improve collaboration and maintainability in real-world projects. :contentReference[oaicite:0]{index=0}

---

# 🚀 Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- CatBoost
- XGBoost
- Dill
- Logging
- GridSearchCV

---

# 📂 Project Structure

```bash
mlproject/
│
├── artifacts/                 # Saved model artifacts
│
├── notebook/                  # Jupyter notebooks
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── requirements.txt
├── setup.py
└── README.md
