import numpy as np
import pandas as pd
import os
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt


dataset_path = r"C:\Users\jchen\Downloads\nasa-space-exoplanets\src\data\keplar.csv"
df = pd.read_csv(dataset_path, comment='#')

X = df[['koi_depth', 'koi_duration', 'koi_period', 'koi_prad', 'koi_impact']]
y = df['koi_pdisposition']

X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=50)

log_reg_model = LogisticRegression()
log_reg_model.fit(X=X_train, y=y_train)


y_pred=log_reg_model.predict(X_test)
print(accuracy_score(y_test,y_pred))

unique_labels = y_test.unique()
cnf_matrix = confusion_matrix(y_test, y_pred, labels=unique_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cnf_matrix,
                              display_labels=unique_labels)
disp.plot(cmap='Blues')

plt.show()

# cv_scores = cross_val_score(log_reg_model, X, y, cv=5, scoring='accuracy')
# print("Cross-Validation Accuracy Scores:", cv_scores)
# print("Mean CV Accuracy:", cv_scores.mean())

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': log_reg_model.coef_[0]
})
print("\nFeature Importance:")
print(feature_importance.sort_values(by='Importance', ascending=False))
