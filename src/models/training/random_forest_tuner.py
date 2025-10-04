from sklearn.model_selection import GridSearchCV
import numpy as np
import pandas as pd
import os
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from tqdm import tqdm


dataset_path = r"C:\Users\jchen\Downloads\nasa-space-exoplanets\src\data\keplar.csv"
df = pd.read_csv(dataset_path, comment='#')

X = df[['koi_depth', 'koi_duration', 'koi_period', 'koi_prad', 'koi_impact', 'koi_model_snr', 'koi_teq']]
y = df['koi_pdisposition']
X = X.fillna(X.mean())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)



param_grid = {
    'n_estimators': [100, 300, 500],
    'max_depth': [None, 5, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2']
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=50),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

class TQDMCallback:
    def __init__(self, total):
        self.pbar = tqdm(total=total)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.pbar.close()

    def __call__(self, *args, **kwargs):
        self.pbar.update(1)

total_iterations = (
    len(param_grid['n_estimators']) *
    len(param_grid['max_depth']) *
    len(param_grid['min_samples_split']) *
    len(param_grid['min_samples_leaf']) *
    len(param_grid['max_features'])
)

with TQDMCallback(total=total_iterations) as callback:
    grid_search.fit(X_train, y_train)

print("Best params:", grid_search.best_params_)
print("Best CV accuracy:", grid_search.best_score_)
