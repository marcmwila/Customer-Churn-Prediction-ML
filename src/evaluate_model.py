import joblib
from sklearn.metrics import roc_auc_score
from data_preprocessing import load_and_preprocess
from sklearn.model_selection import train_test_split

X, y = load_and_preprocess("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = joblib.load("models/random_forest_model.pkl")
y_prob = model.predict_proba(X_test)[:,1]

print("ROC-AUC:", roc_auc_score(y_test, y_prob))
