from fastapi import FastAPI
import joblib
import os

# Initialize FastAPI app
app = FastAPI()

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../models/tabular_xgb.joblib")
model = joblib.load(MODEL_PATH)

@app.get("/")
def root():
    return {"message": "Cloudspire API is running 🚀"}

@app.post("/predict")
def predict(data: dict):
    # Example prediction
    prediction = model.predict([list(data.values())])
    return {"prediction": prediction.tolist()}
