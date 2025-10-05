import numpy as np
import pandas as pd
import os
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from pathlib import Path
import joblib


df = pd.read_csv('src/data/keplar.csv', comment='#')


X = df[['koi_depth', 'koi_duration', 'koi_period', 'koi_prad', 'koi_impact']]
y = df['koi_pdisposition']

X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

log_reg_model = LogisticRegression()
log_reg_model.fit(X=X_train, y=y_train)


y_pred=log_reg_model.predict(X_test)
print(accuracy_score(y_test,y_pred))

labels_sorted = sorted(y_test.unique().tolist())
cnf_matrix = confusion_matrix(y_test, y_pred, labels=labels_sorted)
disp = ConfusionMatrixDisplay(confusion_matrix=cnf_matrix,
                              display_labels=labels_sorted)
disp.plot(cmap='Blues')
plt.title('Logistic Regression - Confusion Matrix')

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

out_dir = Path(__file__).resolve().parent.parent / 'trained_models'
out_dir.mkdir(parents=True, exist_ok=True)

lr_model_path = out_dir / 'logistic_regression_model.joblib'
joblib.dump(log_reg_model, lr_model_path)

classes = getattr(log_reg_model, 'classes_', None)
coef = log_reg_model.coef_
intercept = log_reg_model.intercept_
features = list(X.columns)

print(f"Saved logistic regression model to: {lr_model_path}")

cm_txt_path = out_dir / 'logistic_regression_confusion_matrix.txt'
labels = list(labels_sorted)
with open(cm_txt_path, 'w', encoding='utf-8') as f:
    f.write('label\t' + '\t'.join(str(l) for l in labels) + '\n')
    for i, lab in enumerate(labels):
        row_vals = '\t'.join(str(int(v)) for v in cnf_matrix[i])
        f.write(f"{lab}\t{row_vals}\n")

print(f"Saved logistic regression confusion matrix to: {cm_txt_path}")
