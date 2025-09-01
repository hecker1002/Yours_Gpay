
# uSE stremalit to deploy the workign verison of mdode for USers 

import streamlit as st
import pandas as pd
import numpy as np
import mlflow
import os
import datetime

# --- SET UP MLFLOW AND LOAD THE MODEL ---
# The path to your mlruns directory
project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
mlruns_path = os.path.join(project_root_dir, 'mlruns')

# Set the tracking URI to your local mlruns directory
mlflow.set_tracking_uri(f"file:///{mlruns_path}")

# Check if there is a registered model. If not, inform the user.
try:
    client = mlflow.tracking.MlflowClient()
    model_name = "TransactionForecaster"
    # Find the latest version of the model in the registry
    model_version = client.get_latest_versions(model_name, stages=['Production'])[0]
    model_uri = model_version.source
    
    # Load the model from the artifact URI
    model = mlflow.sklearn.load_model(model_uri)
    st.success(f"Model '{model_name}' version {model_version.version} loaded successfully!")
except Exception as e:
    st.error(f"Error loading model from MLflow registry: {e}")
    st.warning("Please ensure you have a model named 'TransactionForecaster' registered in the 'Production' stage.")
    st.stop()


# --- UI LAYOUT ---
st.set_page_config(
    page_title="GPay Transaction Forecaster",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for a clean, modern look
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main-header {
        font-size: 2.5em;
        font-weight: bold;
        color: #1a1a1a;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .sub-header {
        font-size: 1.2em;
        color: #555;
        text-align: center;
        margin-bottom: 2em;
    }
    .widget-label {
        font-weight: bold;
        color: #333;
    }
    .stButton>button {
        color: white;
        background-color: #4a90e2;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-size: 1.1em;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-header">Personalized Financial Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Predict your next transaction using your own spending habits.</p>', unsafe_allow_html=True)

# --- USER INPUT FORM ---
st.markdown("<h3>New Transaction Details</h3>", unsafe_allow_html=True)
with st.form("prediction_form"):
    # Input fields for the user
    merchant_name = st.text_input("Merchant Name", help="e.g., GANESH KUMAR YADAV")
    
    # Placeholder values for demonstration. In a real app, you'd integrate more features.
    acc_no = st.selectbox("Account Number", ["9582", "7922"])
    
    # Time-based features would be preprocessed in the pipeline before prediction
    transaction_date = st.date_input("Transaction Date", datetime.date.today())
    transaction_time = st.time_input("Transaction Time", datetime.datetime.now().time())
    
    submitted = st.form_submit_button("Predict Next Amount")


# --- PREDICTION LOGIC ---
if submitted:
    if not merchant_name:
        st.error("Please enter a Merchant Name.")
    else:
        # Here, you would create a DataFrame with the same features used for training.
        # This is where your feature engineering pipeline becomes critical.
        # For simplicity, we are using a dummy DataFrame with placeholder values.
        # You will need to replace this with your actual preprocessing logic.
        
        # Example of creating a dummy DataFrame with the expected columns
        # You must ensure the column names and data types match your training data.
        input_df = pd.DataFrame({
            'merchants': [merchant_name],
            'Acc No.': [acc_no],
            # Add other relevant features here (e.g., month, year, quarter, moving averages)
            # You would need to re-engineer these features based on the new input
        })
        
        try:
            # Make a prediction using the loaded model
            prediction = model.predict(input_df)[0]
            
            st.success("Prediction Complete!")
            st.markdown(f"**Predicted Next Amount:** ₹{prediction:.2f}")

        except Exception as e:
            st.error(f"Prediction failed. Please check the input data and model compatibility. Error: {e}")
