# Diabetes Data Analysis Dashboard

---

## Introduction
An end‑to‑end data analytics project on the Pima Indians Diabetes Dataset, focusing on data cleaning, exploratory data analysis (EDA), and insight generation, with a simple Streamlit dashboard for interactive exploration.

---​

## 1. Project Overview
This project answers a central question:

How do health indicators such as glucose, blood pressure, BMI, age, and others relate to diabetes risk?

**Key goals:**

- Clean and analyze the diabetes dataset to identify patterns and risk factors.
- Visualize relationships between health metrics and diabetes outcome to support data‑driven decisions.
- Provide an interactive web dashboard where users can explore indicators and see the predicted risk for a given patient profile.

---​

## 2. Tech Stack
**Language:** Python

**Analytics & Data Handling:** Pandas, NumPy.
​
**Visualization:** Matplotlib, Seaborn, Streamlit charts.​

**Modeling (lightweight):** scikit‑learn (train_test_split, StandardScaler, SVM) – used to generate a simple risk score.​

**Dataset:** Pima Indians Diabetes Dataset.​

---

## 3. Dataset & Business Understanding
Each record represents one patient, with: pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, age, and outcome (0/1).​

From an analytics viewpoint, the dataset is used to:
- Profile diabetic vs non‑diabetic patients.
- Understand which variables differ most across the two groups.
- Support early risk assessment discussions in a healthcare setting.

---

## 4. Analytics Workflow

**Data Loading & Quality Checks**

- Load diabetes.csv into a DataFrame and inspect row/column counts, data types, and basic statistics.
​- Identify suspicious zeros or outliers in medical fields (e.g., glucose, blood pressure).

**Data Cleaning & Feature Preparation**

- Replace invalid zeros in clinical columns with more reasonable values (medians/means) where appropriate.
- Create derived fields (e.g., BMI categories, age groups) to simplify analysis.

**Exploratory Data Analysis (EDA)**

- Distribution plots for glucose, BMI, age, etc. to understand typical ranges.
- Grouped analysis: compare averages of key metrics for diabetic vs non‑diabetic patients.
- Correlation matrix and heatmap to see which features are most associated with the outcome.

**Model‑Based Risk Scoring**

- Standardize numeric features with StandardScaler and split into train/test sets.​
- Train a simple SVM classifier to generate a diabetes risk prediction (around 77% accuracy on test data).
- Use the model primarily as a scoring function to complement the descriptive analytics.

---

## 5. Streamlit Analytics Dashboard
The **Streamlit app** acts as a mini analytics tool rather than just a ML demo:​

**Input Panel:**

Users enter values for pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, and age.
​
**Summary Metrics:**

Display key stats (e.g., entered BMI category, how the patient’s glucose compares to dataset average).

**Risk Result:**

Show whether the profile is classified as at risk for diabetes, along with a brief explanation referencing the most influential indicators.

---
​
## 6. Key Insights 

- Patients with higher glucose and BMI levels show a significantly higher proportion of positive diabetes outcomes.
- Older age groups (e.g., 40+) have a higher diabetes rate compared with younger groups.
- Some clinical measurements contain many zeros, highlighting potential data quality issues that must be handled before modeling.

