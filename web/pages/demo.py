import joblib
import numpy as np
import pandas as pd

# model = joblib.load('src/models/trained_models/random_forest_model.joblib')

feature_names = [
    'koi_period',
    'koi_duration',
    'koi_depth',
    'koi_prad',
    'koi_model_snr'
]

print("Enter the following features for prediction:")
user_input = []
for feature in feature_names:
    value = float(input(f"{feature}: "))
    user_input.append(value)

X_new = pd.DataFrame([user_input], columns=feature_names)
pred = model.predict(X_new)[0]

proba = model.predict_proba(X_new)[0]

confidence_intervals = {
    'Class 0 (True Positive)': f"{proba[0] * 100:.2f}%",
    'Class 1 (False Positive)': f"{proba[1] * 100:.2f}%"
}

if pred == 1:
    print(f"False Positive ({confidence_intervals['Class 1 (False Positive)']})")
else:
    print(f"True Positive ({confidence_intervals['Class 0 (True Positive)']})")
