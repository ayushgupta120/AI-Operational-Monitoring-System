from fastapi import FastAPI
import numpy as np
from schemas import SensorData
from model_loader import incident_model, severity_model
from decision_logic import get_action

app = FastAPI(title="Operational AI API")

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.post("/predict")
def predict(data: SensorData):
    
    input_data = np.array([[
        data.temperature,
        data.humidity,
        data.motion,
        data.smoke,
        data.power_usage
    ]])

    incident = incident_model.predict(input_data)[0]
    severity = severity_model.predict(input_data)[0]

    action = get_action(incident)

    return {
        "incident": incident,
        "severity": severity,
        "recommended_action": action
    }