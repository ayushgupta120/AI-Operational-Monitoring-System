import pandas as pd
import numpy as np
import random

# Number of samples
NUM_SAMPLES = 5000

data = []

for _ in range(NUM_SAMPLES):
    
    # Generate realistic sensor values
    temperature = np.random.normal(loc=30, scale=10)  # avg 30°C
    humidity = np.random.uniform(20, 90)
    motion = np.random.choice([0, 1], p=[0.7, 0.3])
    smoke = np.random.choice([0, 1], p=[0.9, 0.1])
    power_usage = np.random.normal(loc=200, scale=50)

    # Clip values to avoid unrealistic numbers
    temperature = max(10, min(temperature, 100))
    power_usage = max(50, min(power_usage, 500))

    # Default values
    incident = "normal"
    severity = "low"

    # 🔥 Rule-based labeling
    if smoke == 1 and temperature > 60:
        incident = "fire"
        severity = "high"

    elif temperature > 45:
        incident = "overheating"
        severity = "medium"

    elif motion == 1 and temperature < 35:
        incident = "intrusion"
        severity = "medium"

    elif power_usage > 350:
        incident = "equipment_failure"
        severity = "high"

    # ✅ Reduced Noise (ONLY CHANGE HERE)
    if random.random() < 0.01:   # changed from 0.05 → 0.01
        incident = "normal"
        severity = "low"

    data.append([
        temperature,
        humidity,
        motion,
        smoke,
        power_usage,
        incident,
        severity
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "temperature",
    "humidity",
    "motion",
    "smoke",
    "power_usage",
    "incident",
    "severity"
])

# Save dataset
df.to_csv("data/operational_data.csv", index=False)

print("Dataset generated successfully!")