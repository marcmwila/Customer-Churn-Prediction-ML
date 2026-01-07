<<<<<<< HEAD

# Project Structure

customer-churn-ml/
├── data/ # Raw and cleaned dataset
├── notebooks/ # EDA & experimentation
├── src/ # Data processing & modeling code
├── models/ # Saved training models
├── app.py # Streamlit app for predictions
├── requirements.txt # Python dependencies
├── README.md # Project documentation
=======
# Customer-Churn-Prediction-ML
>>>>>>> origin/main

# Customer Churn Prediction (Machine Learning)

**Predict which customers are likely to churn** (leave a service) using real-world data and machine learning models.  
Customer churn prediction is critical for businesses — retaining existing customers is often more cost-effective than acquiring new ones. :contentReference[oaicite:7]{index=7}

---

## Problem Overview

Customer churn refers to customers who stop using a company’s product or service.  
This project uses customer data (e.g., tenure, charges, contract type) to predict churn with machine learning, helping businesses take proactive retention actions. :contentReference[oaicite:8]{index=8}

---

---

##  Tools & Technologies

- **Python** — core programming language  
- **pandas, numpy** — data processing  
- **scikit-learn** — ML modeling (Logistic Regression, Random Forest, etc.)  
- **matplotlib, seaborn** — visualizations  
- **Streamlit** — interactive web app deployment  

---

##  Dataset

Dataset includes customer attributes such as:
- Tenure
- Monthly Charges
- Total Charges
- Contract type
- Payment method  
...and whether they churned or not.  
*(Add data source link if applicable)*

---

##  Approach

1. **Exploratory Data Analysis (EDA)**  
   - Visualize churn distribution by features  
   - Identify patterns and correlations

2. **Preprocessing**
   - Encode categorical variables
   - Scale / normalize numeric features
   - Train-test split

3. **Modeling**
   - Train multiple classification models
   - Evaluate using accuracy, precision, recall, F1-score, ROC-AUC

4. **Deployment**
   - Simple Streamlit app to input new customer data and view churn prediction

---

##  Results

| Model | Accuracy | Precision | Recall | ROC-AUC |
|-------|----------|-----------|--------|---------|
| Logistic Regression | *xx%* | *xx%* | *xx%* | *xx* |
| Random Forest | *xx%* | *xx%* | *xx%* | *xx* |
| (Add others here) | | | | |

> *Typically, Logistic Regression and tree-based models perform well on churn datasets when properly tuned.* :contentReference[oaicite:9]{index=9}

---

##  How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/marcmwila/Customer-Churn-Prediction-ML.git


