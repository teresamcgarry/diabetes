#!/usr/bin/env python3
# Fast RandomForest with SMOTE oversampling and class_weight='balanced'

import sys
import subprocess
import os
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Ensure imbalanced-learn (SMOTE) is available
try:
    from imblearn.over_sampling import SMOTE
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "imbalanced-learn"])
    from imblearn.over_sampling import SMOTE

RANDOM_STATE = 42
DATA_PATH = "diabetes.csv"

if not os.path.exists(DATA_PATH):
    print(f"Data file {DATA_PATH} not found in {os.getcwd()}")
    sys.exit(1)

print("Loading data...")
df = pd.read_csv(DATA_PATH)

# Prepare features and target
X = df.select_dtypes(include=["number"]).copy()
if "Diabetes_012" not in X.columns:
    raise SystemExit("Target column 'Diabetes_012' not present in data")

X = X.drop(columns=["Diabetes_012"])
y = df["Diabetes_012"].astype(int)

print("Class distribution (original):", Counter(y))

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE
)

print("Class distribution (train before SMOTE):", Counter(y_train))

# SMOTE with capped target size
train_counts = Counter(y_train)
major_label, major_count = train_counts.most_common(1)[0]

TARGET = 30000  # fast + balanced
sampling_strategy = {lbl: TARGET for lbl in train_counts if lbl != major_label}

print("SMOTE sampling_strategy:", sampling_strategy)
smote = SMOTE(sampling_strategy=sampling_strategy, random_state=RANDOM_STATE)
X_res, y_res = smote.fit_resample(X_train, y_train)

print("Class distribution (train after SMOTE):", Counter(y_res))

# Optional: cap total rows for speed
MAX_TRAIN_ROWS = 150000
if X_res.shape[0] > MAX_TRAIN_ROWS:
    print(f"Sampling down to {MAX_TRAIN_ROWS} rows for fast training...")
    rs = np.random.RandomState(RANDOM_STATE)
    idx = rs.choice(X_res.shape[0], size=MAX_TRAIN_ROWS, replace=False)
    X_res = X_res.iloc[idx].reset_index(drop=True)
    y_res = pd.Series(y_res).iloc[idx].reset_index(drop=True)

# Fast RandomForest
rf = RandomForestClassifier(
    n_estimators=80,
    max_depth=8,
    class_weight='balanced',
    random_state=RANDOM_STATE,
    n_jobs=-1
)

print("Training RandomForest (fast settings)...")
rf.fit(X_res, y_res)

# Predict
y_pred = rf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {acc:.4f}")
print("\nClassification report:\n", classification_report(y_test, y_pred, digits=4))
print("\nConfusion matrix:\n", confusion_matrix(y_test, y_pred))

# Feature importances
fi = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
fi.to_csv("rf_smote_feature_importances.csv", header=["importance"])
print("\nSaved feature importances to rf_smote_feature_importances.csv")

# Plot
plt.figure(figsize=(8,6))
fi.head(15).sort_values().plot(kind='barh')
plt.title('Top 15 RandomForest feature importances (SMOTE + class_weight)')
plt.tight_layout()
plt.savefig("rf_smote_feature_importances.png", dpi=150)
print("Saved feature importances plot to rf_smote_feature_importances.png")

print("\nDone.")