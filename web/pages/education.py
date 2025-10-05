import numpy as np
import pandas as pd
import joblib
import streamlit as st
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


@st.cache_data(show_spinner=False)
def _load_data():
	repo_root = Path(__file__).resolve().parents[2]
	csv_path = repo_root / 'src' / 'data' / 'keplar.csv'
	if csv_path.exists():
		df = pd.read_csv(csv_path, comment='#')
		return df, str(csv_path)
	return None, None

@st.cache_resource(show_spinner=False)
def _get_model():
	repo_root = Path(__file__).resolve().parents[2]
	joblib_path = repo_root / 'src' / 'models' / 'trained_models' / 'random_forest_model.joblib'

	if joblib_path.exists():
		try:
			m = joblib.load(joblib_path)
			st.info(f"Loaded pretrained model: {joblib_path}")
			return m
		except Exception as e:
			st.warning(f"Could not load pretrained model ({joblib_path}): {e}")

	df, csv_path = _load_data()
	if df is not None:
		candidate_feats = [
			'koi_prad','koi_dicco_msky','koi_dikco_msky','koi_dor',
			'koi_prad_err2','koi_period','koi_duration','koi_depth'
		]
		features = [c for c in candidate_feats if c in df.columns]
		if not features:
			st.error("No expected feature columns found in CSV; cannot train model.")
			return RandomForestClassifier(n_estimators=50, random_state=48)

		X = df[features].apply(pd.to_numeric, errors='coerce')
		X = X.fillna(X.mean(numeric_only=True))
		if 'koi_pdisposition' not in df.columns:
			st.error("Target column 'koi_pdisposition' not found; cannot train model.")
			return RandomForestClassifier(n_estimators=50, random_state=48)
		y = df['koi_pdisposition']

		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
		m = RandomForestClassifier(
			n_estimators=80, max_depth=25, min_samples_split=15,
			min_samples_leaf=1, max_features='sqrt', random_state=48
		)
		m.fit(X_train, y_train)
		st.success(f"Trained model from local CSV: {csv_path}")
		return m

	st.warning("No model file or dataset found; using untrained RandomForest for UI only.")
	return RandomForestClassifier(n_estimators=50, random_state=48)


model = _get_model()
