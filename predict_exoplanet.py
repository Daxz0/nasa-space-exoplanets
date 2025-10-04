import joblib
import numpy as np

# Load the trained model
model = joblib.load('trained_exoplanet_model.joblib')

# Feature names in order
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

X_new = np.array(user_input).reshape(1, -1)
pred = model.predict(X_new)[0]

if pred == 1:
    print("Prediction: FALSE POSITIVE")
else:
    print("Prediction: NOT FALSE POSITIVE")
