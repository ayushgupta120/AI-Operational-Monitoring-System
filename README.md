AI Operational Monitoring System

A full-stack AI-powered monitoring system that analyzes real-time sensor data, detects incidents, predicts severity, and provides automated decision-making through an interactive dashboard.

🎯 Objective

To build a scalable AI system that:

Monitors operational sensor data
Detects incidents using Machine Learning
Predicts severity levels
Recommends actions automatically
Visualizes real-time analytics
🏗️ System Architecture
Streamlit Dashboard (Frontend)
        ↓
FastAPI Backend (API Layer)
        ↓
Machine Learning Models (Random Forest)
        ↓
Decision Engine (Rule-Based Logic)
        ↓
Logging + Analytics (CSV + Visualization)
⚙️ Features
🔹 Real-Time Monitoring
Interactive dashboard using Streamlit
User-controlled sensor inputs:
Temperature
Humidity
Motion
Smoke
Power usage
🔹 Incident Detection (ML Model)
Built using Random Forest (scikit-learn)
Detects:
Normal
Fire
Overheating
Intrusion
Equipment Failure
🔹 Severity Prediction
Classifies incidents into:
Low
Medium
High
🔹 Decision Engine
Rule-based automated actions:
Fire → Evacuate immediately
Overheating → Inspect cooling system
Intrusion → Alert security
Equipment failure → Schedule maintenance
🔹 FastAPI Backend
REST API endpoint:
/predict
Handles:
Input validation (Pydantic)
Model inference
Decision logic
🔹 Logging System
Stores:
Sensor values
Predicted incident
Severity
Recommended action
Saved in:
logs/system_logs.csv
🔹 Data Visualization
Incident distribution (bar chart)
Severity distribution (pie chart)
Temperature trend (line chart)
🧠 Technologies Used
Python
FastAPI
Streamlit
scikit-learn
Pandas
Matplotlib
Joblib
📂 Project Structure
AI-Operational-Monitoring-System/
│
├── backend/
│   ├── main.py
│   ├── model_loader.py
│   ├── schemas.py
│   └── decision_logic.py
│
├── dashboard/
│   └── app.py
│
├── models/
│   ├── incident_model.pkl
│   └── severity_model.pkl
│
├── decision_engine/
│   └── decision.py
│
├── logs/
│   └── system_logs.csv
│
├── requirements.txt
└── README.md
🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/AI-Operational-Monitoring-System.git
cd AI-Operational-Monitoring-System
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Backend (FastAPI)
cd backend
python -m uvicorn main:app --reload

👉 API will run at:

http://127.0.0.1:8000/docs
5️⃣ Run Frontend (Streamlit)
cd dashboard
python -m streamlit run app.py

👉 Dashboard will open at:

http://localhost:8501
🔗 API Endpoint
POST /predict
Input:
{
  "temperature": 80,
  "humidity": 60,
  "motion": 1,
  "smoke": 1,
  "power_usage": 300
}
Output:
{
  "incident": "fire",
  "severity": "high",
  "recommended_action": "Evacuate immediately"
}
🎯 Key Highlights
Full-stack AI system (Frontend + Backend + ML)
Real-time data processing
API-based architecture (FastAPI)
Automated decision-making system
Interactive analytics dashboard
🧠 Future Improvements
🔔 Alert system (Email/Sound notifications)
🔐 Authentication system
🗄️ Database integration (MongoDB)
☁️ Cloud deployment (AWS/Render)
🤖 Explainable AI (SHAP integration)
👨‍💻 Author

Ayush Gupta
MCA Final Year Student
