import requests
# import sys
import os
import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from decision_engine.decision import get_action
# from models.predict_incident import predict

st.set_page_config(page_title="AI Monitoring System", layout="centered")

st.title("🚀 AI Operational Monitoring System")
st.markdown("### Live Sensor Monitoring")

# =========================
# INPUTS
# =========================
temperature = st.slider("Temperature (°C)", 0, 100, 30)
humidity = st.slider("Humidity (%)", 0, 100, 50)
motion = st.selectbox("Motion Detected", [0, 1])
smoke = st.selectbox("Smoke Detected", [0, 1])
power_usage = st.slider("Power Usage", 0, 500, 200)

run = st.checkbox("Enable Real-Time Monitoring")

placeholder = st.empty()

# =========================
# CREATE LOG FILE IF NOT EXISTS
# =========================
log_file = "logs/system_logs.csv"

if not os.path.exists("logs"):
    os.makedirs("logs")

if not os.path.exists(log_file):
    df_init = pd.DataFrame(columns=[
        "temperature", "humidity", "motion", "smoke",
        "power_usage", "incident", "severity", "action"
    ])
    df_init.to_csv(log_file, index=False)

# =========================
# REAL-TIME LOOP
# =========================
if run:
    for _ in range(1000):

        # 🔥 Prediction
        # incident, severity = predict(
        #     temperature, humidity, motion, smoke, power_usage
        # )

        # # 🔥 Decision
        # action = get_action(incident, severity)
        
        url = "http://127.0.0.1:8000/predict"
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "motion": motion,
            "smoke": smoke,
            "power_usage": power_usage
        }
        
        try:
            response = requests.post(url, json=data)
            result = response.json()
            incident = result["incident"]
            severity = result["severity"]
            action = result["recommended_action"]

        except:
            incident = "API Error"
            severity = "low"
            action = "Check backend server"

        # =========================
        # ✅ LOGGING (FIXED)
        # =========================
        log_data = {
            "temperature": temperature,
            "humidity": humidity,
            "motion": motion,
            "smoke": smoke,
            "power_usage": power_usage,
            "incident": incident,
            "severity": severity,
            "action": action
        }

        df = pd.DataFrame([log_data])
        df.to_csv(log_file, mode='a', header=False, index=False)

        # =========================
        # DISPLAY OUTPUT
        # =========================
        with placeholder.container():
            st.markdown("---")
            st.subheader("📊 Live Results")

            if severity == "high":
                st.error(f"🔥 Incident: {incident}")
            elif severity == "medium":
                st.warning(f"⚠️ Incident: {incident}")
            else:
                st.success(f"✅ Incident: {incident}")

            st.info(f"Recommended Action: {action}")

        time.sleep(2)

# =========================
# 📊 GRAPH SECTION
# =========================
st.markdown("---")
st.subheader("📊 System Analytics")

if os.path.exists(log_file):
    logs = pd.read_csv(log_file)

    if not logs.empty:

        # -------------------------
        # 1️⃣ Incident Graph
        # -------------------------
        st.write("### Incident Distribution")

        incident_counts = logs["incident"].value_counts()

        fig1, ax1 = plt.subplots()
        incident_counts.plot(kind='bar', ax=ax1)
        ax1.set_title("Incident Frequency")
        ax1.set_xlabel("Incident Type")
        ax1.set_ylabel("Count")

        st.pyplot(fig1)

        # -------------------------
        # 2️⃣ Severity Graph
        # -------------------------
        st.write("### Severity Distribution")

        severity_counts = logs["severity"].value_counts()

        fig2, ax2 = plt.subplots()
        severity_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
        ax2.set_title("Severity Levels")

        st.pyplot(fig2)


        st.write("### Temperature Trend")

        fig3, ax3 = plt.subplots()
        logs["temperature"].tail(20).plot(ax=ax3)
        ax3.set_title("Recent Temperature Readings")
        ax3.set_xlabel("Time")
        ax3.set_ylabel("Temperature")

        st.pyplot(fig3)

    else:
        st.warning("No data yet. Run system to generate logs.")

else:
    st.warning("Log file not found.")