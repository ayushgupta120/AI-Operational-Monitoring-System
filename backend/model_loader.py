import joblib

def load_model():
    model = joblib.load("../models/incident_model.pkl")
    severity_model = joblib.load("../models/severity_model.pkl")
    return model, severity_model

incident_model, severity_model = load_model()