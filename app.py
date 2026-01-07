import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Customer Churn Predictor")

st.title("📊 Customer Churn Prediction")

from pathlib import Path
import pickle

MODEL_PATH = Path(__file__).parent / "models" / "random_forest_model.pkl"
model = pickle.load(open(MODEL_PATH, "rb"))



tenure = st.number_input("Tenure", min_value=0)
monthly = st.number_input("Monthly Charges", min_value=0.0)
total = st.number_input("Total Charges", min_value=0.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

if st.button("Predict Churn"):
    input_df = pd.DataFrame([{
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "Contract": contract,
        "PaymentMethod": payment,
        "InternetService": internet
    }])

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Customer likely to churn (probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer likely to stay (probability: {1-prob:.2f})")
