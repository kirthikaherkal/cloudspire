import numpy as np, pandas as pd
rows=[]
for i in range(200):
    rows.append({
      "patient_id": f"SIM{i:03d}",
      "age": int(np.random.normal(45,12)),
      "sex": np.random.choice([0,1]),
      "heart_rate": int(np.random.normal(78,12)),
      "spo2": int(np.clip(np.random.normal(97,2),85,100)),
      "systolic_bp": int(np.random.normal(125,15)),
      "diastolic_bp": int(np.random.normal(80,10)),
      "glucose_fasting": int(np.random.normal(110,30)),
      "temp": round(np.random.normal(36.7,0.5),1)
    })
pd.DataFrame(rows).to_csv("data/sim_vitals.csv", index=False)
