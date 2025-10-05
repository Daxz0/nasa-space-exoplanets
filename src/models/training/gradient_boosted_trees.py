import os
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score


def get_project_paths():
	training_dir = os.path.dirname(os.path.abspath(__file__))
	src_dir = os.path.dirname(os.path.dirname(training_dir))
	project_root = os.path.dirname(src_dir)
	data_path = os.path.join(project_root, 'src', 'data', 'keplar.csv')
	models_dir = os.path.join(project_root, 'src', 'models', 'trained_models')
	os.makedirs(models_dir, exist_ok=True)
	model_path = os.path.join(models_dir, 'gradient_boosted_trees_model.joblib')
	return data_path, model_path


def load_data(dataset_path: str):
	df = pd.read_csv(dataset_path, comment='#')

	feature_cols = [
		'koi_period',
		'koi_duration',
		'koi_depth',
		'koi_prad',
		'koi_model_snr',
	]

	X = df[feature_cols]
	y = df['koi_pdisposition']

	X = X.apply(pd.to_numeric, errors='coerce')
	X = X.fillna(X.mean(numeric_only=True))
	return X, y, feature_cols


def train_and_evaluate(X, y):
	X_train, X_test, y_train, y_test = train_test_split(
		X, y, test_size=0.2, random_state=42, stratify=y if hasattr(y, 'nunique') and y.nunique() > 1 else None
	)

	gbt = GradientBoostingClassifier(
		random_state=48,
		n_estimators=300,
		learning_rate=0.05,
		max_depth=3,
		subsample=0.9,
		max_features=None,
	)

	gbt.fit(X_train, y_train)

	y_pred = gbt.predict(X_test)
	acc = accuracy_score(y_test, y_pred)
	print(f"Accuracy: {acc:.4f}")
	print("\nClassification report:\n", classification_report(y_test, y_pred))

	unique_labels = y_test.unique()
	cnf_matrix = confusion_matrix(y_test, y_pred, labels=unique_labels)
	disp = ConfusionMatrixDisplay(confusion_matrix=cnf_matrix, display_labels=unique_labels)
	disp.plot(cmap='Blues')
	plt.title('Gradient Boosted Trees - Confusion Matrix')

	return gbt, acc, (unique_labels, cnf_matrix)


def show_feature_importance(model, feature_names):
	if hasattr(model, 'feature_importances_'):
		importances = model.feature_importances_
		fi = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
		fi_sorted = fi.sort_values(by='Importance', ascending=False)
		print("\nFeature Importance:")
		print(fi_sorted)

def main():
	dataset_path, model_path = get_project_paths()

	X, y, feature_names = load_data(dataset_path)
	model, acc, (unique_labels, cnf_matrix) = train_and_evaluate(X, y)
	show_feature_importance(model, feature_names)

	joblib.dump(model, model_path)
	print(f"\nSaved Gradient Boosted Trees model to: {model_path}")

	# Save confusion matrix as raw text (TSV)
	models_dir = os.path.dirname(model_path)
	cm_txt_path = os.path.join(models_dir, 'gradient_boosted_trees_confusion_matrix.txt')
	labels = list(unique_labels)
	with open(cm_txt_path, 'w', encoding='utf-8') as f:
		f.write('label\t' + '\t'.join(str(l) for l in labels) + '\n')
		for i, lab in enumerate(labels):
			row_vals = '\t'.join(str(int(v)) for v in cnf_matrix[i])
			f.write(f"{lab}\t{row_vals}\n")
	print(f"Saved Gradient Boosted Trees confusion matrix to: {cm_txt_path}")

	plt.show()


if __name__ == "__main__":
	main()
