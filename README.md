# 💳 GPay Transaction Analyzer: An End-to-End MLOps Project

> Turning raw Google Pay transaction data into actionable insights with a fully reproducible MLOps pipeline.

---

## 🚀 Project Overview
This project demonstrates how **MLOps principles** can transform messy, unstructured financial data into a clean dataset and deploy a machine learning model to power a **personalized financial assistant**.  

The pipeline ingests raw **Google Takeout transaction data**, cleans and validates it, tracks experiments, versions datasets, and deploys a model through an interactive **Streamlit app**.

---

## ✨ Key Features
- **Automated Data Ingestion**: Scrapes and parses transaction data from Google Takeout HTML using Beautiful Soup & regex.  
- **Data Validation & Cleaning**: Handles inconsistent formats, missing values, and impossible dates.  
- **Data Versioning (DVC)**: Tracks both raw and processed datasets for full reproducibility.  
- **Experiment Tracking (MLflow)**: Logs parameters, metrics, and models for every experiment.  
- **CI/CD with GitHub Actions**: Automated checks ensure robust, production-ready code.  
- **Model Deployment (Streamlit)**: Interactive UI to explore predictions in real-time.  

---

## 🧩 The Problem: *Smart Spending Categories*
Most users don’t manually tag transactions, leaving spending history messy and hard to interpret.  
This project addresses that gap by **automatically grouping transactions** into meaningful categories using machine learning.  

📊 Outcome: A **clear breakdown of spending habits** with zero manual effort — a foundation for building a **personalized financial assistant**.

---

## 🔄 MLOps Pipeline Flow
1. **Data Ingestion & Cleaning**  
   - Extracts raw data from Google Takeout `.zip`  
   - Cleans records, normalizes fields, fixes invalid dates  

2. **Data Versioning (DVC)**  
   - Ensures lightweight Git repo while tracking large datasets  
   - Enables “time-travel” through dataset versions  

3. **Model Training & Tracking (MLflow)**  
   - Trains a `RandomForestRegressor` to predict transaction amounts  
   - Tracks hyperparameters (`n_estimators`, `max_depth`) and metrics (`R²`)  

4. **Model Registry**  
   - Best-performing model promoted to **Production** in MLflow Registry  

5. **CI/CD (GitHub Actions)**  
   - Automates testing and pipeline execution on every commit  

6. **Deployment (Streamlit App)**  
   - Loads the **Production model**  
   - Provides a clean UI for real-time predictions and analysis  

---

## 🛠️ Tech Stack
- **Data Ingestion & Cleaning**: Python, Beautiful Soup, Pandas, Regex  
- **MLOps Tools**: MLflow, DVC  
- **Machine Learning**: scikit-learn  
- **Visualization & Deployment**: Matplotlib, Streamlit  
- **Automation**: GitHub Actions  
- **Version Control**: Git & GitHub  

---

## ⚡ Getting Started
Follow these steps to reproduce the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/hecker1002/Yours_Gpay.git
cd gpay-transaction-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Pull versioned data
dvc pull

# 4. Run MLflow tracking server
mlflow ui

# 5. Train the model
python src/components/model_trainer.py

# 6. Launch the Streamlit app
streamlit run app.py
