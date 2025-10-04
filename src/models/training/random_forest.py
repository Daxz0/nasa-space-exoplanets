import numpy as np
import pandas as pd
import os
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt

dataset_path = r"C:\Users\jchen\Downloads\nasa-space-exoplanets\src\data\keplar.csv"
df = pd.read_csv(dataset_path, comment='#')

# X = df[['koi_depth', 'koi_duration', 'koi_period', 'koi_prad', 'koi_impact', 'koi_model_snr', 'koi_teq', 'koi_dor', 'koi_incl']]

exclude = ['koi_disposition', 'koi_vet_stat', 'koi_vet_date', 'koi_pdisposition', 'koi_disp_prov', 'koi_comment', 'koi_eccen', 'koi_eccen_err1', 'koi_eccen_err2', 'koi_longp', 'koi_longp_err1', 'koi_longp_err2', 'koi_ingress', 'koi_ingress_err1', 'koi_ingress_err2', 'koi_fittype', 'koi_sma_err1', 'koi_sma_err2', 'koi_incl_err1', 'koi_incl_err2', 'koi_teq_err1', 'koi_teq_err2', 'koi_limbdark_mod', 'koi_ldm_coeff4', 'koi_ldm_coeff3', 'koi_parm_prov', 'koi_tce_delivname', 'koi_trans_mod', 'koi_model_dof', 'koi_model_chisq', 'koi_datalink_dvr', 'koi_datalink_dvs', 'koi_sage', 'koi_sage_err1', 'koi_sage_err2', 'koi_sparprov']

X = df[[col for col in df.columns if col.startswith('koi')]]
y = df['koi_pdisposition']

X = X.apply(pd.to_numeric, errors='coerce')
X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=100)

rf_model = RandomForestClassifier(n_estimators=100, random_state=50, max_depth=5, min_samples_split=10, min_samples_leaf=1)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

unique_labels = y_test.unique()
cnf_matrix = confusion_matrix(y_test, y_pred, labels=unique_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cnf_matrix,
                              display_labels=unique_labels)
disp.plot(cmap='Blues')

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
})
print("\nFeature Importance:")
print(feature_importance.sort_values(by='Importance', ascending=False))




plt.show()
