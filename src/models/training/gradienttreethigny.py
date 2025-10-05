import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import joblib
# Exoplanet False Positive Prediction using Logistic Regression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
df = pd.read_csv('src/data/buh.csv')


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

# Encode target: 1 if FALSE POSITIVE, 0 otherwise
df['is_false_positive'] = (df[target] == 'FALSE POSITIVE').astype(int)

X = df[features]
y = df['is_false_positive']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Hyperparameter tuning with GridSearchCV
param_grid = {
	'n_estimators': [100, 200],
	'learning_rate': [0.05, 0.1, 0.2],
	'max_depth': [3, 5, 10],
	'min_samples_split': [2, 5],
	'min_samples_leaf': [1, 2]
}
grid_search = GridSearchCV(GradientBoostingClassifier(random_state=42), param_grid, cv=3, n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

print('Best parameters:', grid_search.best_params_)
model = grid_search.best_estimator_


# Predict and evaluate
y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred, target_names=['Not False Positive', 'False Positive']))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not False Positive', 'False Positive'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

