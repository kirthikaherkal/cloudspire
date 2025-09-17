import pandas as pd
from xgboost import XGBClassifier
import joblib
df = pd.read_csv("data/sim_vitals.csv")
df['diab'] = (df.glucose_fasting >= 126).astype(int)
X = df[["age","sex","heart_rate","spo2","systolic_bp","diastolic_bp","glucose_fasting","temp"]]
y = df['diab']
model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X,y)
joblib.dump(model, "models/tabular_xgb.joblib")
print("Saved model")
