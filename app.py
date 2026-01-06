import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/random_forest_model.pkl")


st.title("Customer Churn Prediction")

# Input fields
tenure = st.number_input("Tenure (months)", min_value=0, max_value=72)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=500.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=5000.0)

if st.button("Predict"):
    data = pd.DataFrame([[tenure, monthly_charges, total_charges]],
                        columns=['tenure','MonthlyCharges','TotalCharges'])
    prediction = model.predict(data)
    st.write("Customer will churn" if prediction[0] else "Customer will stay")