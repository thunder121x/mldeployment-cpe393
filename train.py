# train.py
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Load data
df = pd.read_csv("Housing.csv")

X = df.drop("price", axis=1)
y = df["price"]

# Identify categorical and numerical columns
categorical = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"]
numerical = [col for col in X.columns if col not in categorical]

# Preprocessing
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(drop="first"), categorical)
], remainder="passthrough")

# Pipeline
model = Pipeline([
    ("pre", preprocessor),
    ("reg", RandomForestRegressor(n_estimators=100, random_state=42))
])

model.fit(X, y)

# Save model
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)
