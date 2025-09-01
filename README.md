GPay Transaction Analyzer: An End-to-End MLOps Project
Project Overview
This project is an end-to-end MLOps pipeline designed to turn raw, unstructured financial data into a clean, actionable dataset and then deploy a machine learning model to solve a real-world problem. The core idea is to build a personalized financial assistant that learns a user's spending habits.

Key Features
Automated Data Ingestion: A robust pipeline that scrapes transaction data from local Google Takeout HTML files.

Data Validation: A dedicated component that validates and cleans data, handling inconsistent formats and impossible dates.

MLflow Experimentation: Systematic tracking of model runs, parameters, and metrics to ensure the best model is always chosen.

Data Versioning (DVC): Git-based version control for large datasets, ensuring the entire project is fully reproducible.

Continuous Integration (CI): An automated GitHub Actions pipeline that validates the project's code on every commit.

Interactive Web Application: A simple Streamlit app that serves the model and provides an intuitive UI for real-time predictions.

The Problem: "Smart Spending Categories"
The core machine learning problem addressed in this project is to automatically categorize a user's spending. Most people don't manually tag their transactions. This project uses an unsupervised learning approach to group similar merchants and transactions, providing users with a clear, automatic breakdown of their spending habits without any manual input. This is a crucial first step in building a personalized financial assistant.

MLOps Pipeline Flow
The project follows a structured MLOps pipeline to ensure a reproducible and professional workflow.

Data Ingestion & Cleaning: A Python script uses Beautiful Soup and regex to extract raw transaction details from a Google Takeout ZIP file. The data is then cleaned, and impossible dates are handled.

Data Versioning (DVC): The raw and processed datasets are versioned using DVC, making the entire pipeline reproducible. Every change to the data is tracked. This keeps our Git repository lightweight while allowing us to time-travel through our data history.

Model Training & Experiment Tracking (MLflow): A RandomForestRegressor is trained to predict transaction amounts. MLflow tracks every experiment, logging hyperparameters (n_estimators, max_depth) and metrics (r2_score).

Model Registry: The best-performing model from the experiments is registered in the MLflow Model Registry and promoted to the Production stage for easy deployment.

CI/CD (GitHub Actions): A ci.yml file configures a GitHub Actions workflow that automatically runs the entire training pipeline on every code push, ensuring code and model integrity.

Model Deployment (Streamlit): A Streamlit app loads the "Production" model from the MLflow Registry and provides an intuitive UI for real-time predictions and analysis.

Technologies Used
Data Ingestion & Cleaning: Python, Beautiful Soup, Pandas, regex

MLOps Frameworks: MLflow, DVC

ML Libraries: scikit-learn

Visualization: Matplotlib, Streamlit

Automation: GitHub Actions

Version Control: Git

How to Reproduce this Project
Clone the repository: git clone <your-repo-url>

Install dependencies: pip install -r requirements.txt

Set up DVC: dvc pull to retrieve the data artifacts.

Run the MLflow tracking server: mlflow ui

Run the training pipeline: python src/components/model_trainer.py

Launch the Streamlit app: streamlit run app.py