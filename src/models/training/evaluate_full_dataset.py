import joblib
import pandas as pd

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

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


# Shuffle and split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# Predict on the test set only
y_pred = model.predict(X_test)

print('Accuracy on test set:', accuracy_score(y_test, y_pred))
print('Classification Report (test set):')
print(classification_report(y_test, y_pred, target_names=['Not False Positive', 'False Positive']))

# Confusion matrix for test set
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not False Positive', 'False Positive'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix (Test Set)')
plt.show()
