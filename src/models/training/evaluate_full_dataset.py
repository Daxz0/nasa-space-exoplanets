import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# Load the trained model
model = joblib.load('trained_exoplanet_model.joblib')

# Load the dataset
csv_path = 'src/data/buh.csv'
df = pd.read_csv(csv_path)

features = [
    'koi_period',
    'koi_duration',
    'koi_depth',
    'koi_prad',
    'koi_model_snr'
]
target = 'koi_disposition'

# Drop rows with missing values in selected columns
df = df.dropna(subset=features + [target])

df['is_false_positive'] = (df[target] == 'FALSE POSITIVE').astype(int)
X = df[features]
y = df['is_false_positive']

# Predict on the entire dataset
y_pred = model.predict(X)

print('Overall Accuracy on all data:', accuracy_score(y, y_pred))
print('Classification Report (all data):')
print(classification_report(y, y_pred, target_names=['Not False Positive', 'False Positive']))
