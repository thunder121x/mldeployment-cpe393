# app/main.py
import pickle
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

# Define column names expected by the model
columns = [
    "area", "bedrooms", "bathrooms", "stories", "mainroad",
    "guestroom", "basement", "hotwaterheating", "airconditioning",
    "parking", "prefarea", "furnishingstatus"
]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "features" not in data:
        return jsonify({"error": "'features' key is required"}), 400

    features = data["features"]

    # Handle single input (1 sample)
    if isinstance(features[0], (int, float, str)):
        features = [features]

    # Validate length
    for i, sample in enumerate(features):
        if len(sample) != 12:
            return jsonify({"error": f"Each sample must contain 12 values. Error at index {i}"}), 400

    try:
        df = pd.DataFrame(features, columns=columns)
        preds = model.predict(df)

        if len(preds) == 1:
            return jsonify({"predicted_price": round(float(preds[0]), 2)})
        else:
            return jsonify({"predicted_prices": [round(float(p), 2) for p in preds]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
