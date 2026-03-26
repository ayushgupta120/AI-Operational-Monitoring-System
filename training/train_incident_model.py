import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load dataset
df = pd.read_csv("data/operational_data.csv")

# Features
X = df[["temperature", "humidity", "motion", "smoke", "power_usage"]]

# Targets
y_incident = df["incident"]
y_severity = df["severity"]

# Split data
X_train, X_test, y_train_inc, y_test_inc = train_test_split(
    X, y_incident, test_size=0.2, random_state=42
)

_, _, y_train_sev, y_test_sev = train_test_split(
    X, y_severity, test_size=0.2, random_state=42
)

# Train Incident Model
incident_model = RandomForestClassifier(n_estimators=100)
incident_model.fit(X_train, y_train_inc)

# Train Severity Model (NEW 🔥)
severity_model = RandomForestClassifier(n_estimators=100)
severity_model.fit(X_train, y_train_sev)

# Evaluate
print("Incident Model Report:")
print(classification_report(y_test_inc, incident_model.predict(X_test)))

print("\nSeverity Model Report:")
print(classification_report(y_test_sev, severity_model.predict(X_test)))

# Save models
joblib.dump(incident_model, "models/incident_model.pkl")
joblib.dump(severity_model, "models/severity_model.pkl")

print("Models saved successfully!")