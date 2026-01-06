import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(path):
    df = pd.read_csv(path)

    # Convert target
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Encode categoricals
    for col in df.select_dtypes(include="object"):
        df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    return X, y
