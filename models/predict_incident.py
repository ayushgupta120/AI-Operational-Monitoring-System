import joblib

# Load models
incident_model = joblib.load("models/incident_model.pkl")
severity_model = joblib.load("models/severity_model.pkl")

def predict(temperature, humidity, motion, smoke, power_usage):
    # Prepare input
    data = [[temperature, humidity, motion, smoke, power_usage]]

    # Predictions
    incident = incident_model.predict(data)[0]
    severity = severity_model.predict(data)[0]

    return incident, severity


# 🔥 Test run (for debugging)
if __name__ == "__main__":
    incident, severity = predict(55, 40, 0, 1, 220)

    print("Predicted Incident:", incident)
    print("Predicted Severity:", severity)