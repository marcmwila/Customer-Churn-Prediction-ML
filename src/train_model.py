from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import joblib
import os
from data_preprocessing import load_and_preprocess

X, y = load_and_preprocess("data/churn.csv")


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "models/random_forest_model.pkl")

print(classification_report(y_test, model.predict(X_test)))
