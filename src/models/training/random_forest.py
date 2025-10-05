import numpy as np
import pandas as pd
import os
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from pathlib import Path
import joblib

df = pd.read_csv('src/data/keplar.csv', comment='#')

X = df[['koi_prad','koi_dor','koi_period','koi_duration','koi_depth']]


# exclude = ['koi_disposition', 'koi_pdisposition', 'koi_model_snr', 'koi_fpflag_nt', 'koi_fpflag_ss', 'koi_fpflag_co', 'koi_fpflag_ec', 'koi_score']
# X = df[[col for col in df.columns if col.startswith('koi') and col not in exclude]]

y = df['koi_pdisposition']
X = X.apply(pd.to_numeric, errors='coerce')
X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=48, max_depth=25, min_samples_split=15, min_samples_leaf=1, max_features='sqrt')
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

labels_sorted = sorted(y_test.unique().tolist())
cnf_matrix = confusion_matrix(y_test, y_pred, labels=labels_sorted)
disp = ConfusionMatrixDisplay(confusion_matrix=cnf_matrix,
                              display_labels=labels_sorted)
disp.plot(cmap='Blues')
plt.title('Random Forest - Confusion Matrix')

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
})
print("\nFeature Importance:")
print(feature_importance.sort_values(by='Importance', ascending=False))



out_dir = Path(__file__).resolve().parent.parent / 'trained_models'
out_dir.mkdir(parents=True, exist_ok=True)

model_path = out_dir / 'random_forest_model.joblib'
joblib.dump(rf_model, model_path)

fi_sorted = feature_importance.sort_values(by='Importance', ascending=False)

cm_txt_path = out_dir / 'random_forest_confusion_matrix.txt'
labels = list(labels_sorted)
with open(cm_txt_path, 'w', encoding='utf-8') as f:
    f.write('label\t' + '\t'.join(str(l) for l in labels) + '\n')
    for i, lab in enumerate(labels):
        row_vals = '\t'.join(str(int(v)) for v in cnf_matrix[i])
        f.write(f"{lab}\t{row_vals}\n")

print(f"\nSaved model to: {model_path}")
print(f"Saved confusion matrix to: {cm_txt_path}")

plt.show()
