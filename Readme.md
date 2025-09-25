# 🚆 RailNova Backend (AI Train Traffic Co-Pilot)

Backend service for **/ RailNova** — an AI-powered assistant that helps railway controllers optimize train schedules, reduce delays, and explain decisions in real time.

---

## ⚙️ Features
- REST API built with Flask
- Accepts train traffic scenarios in JSON
- Returns both optimized schedules and explainable reasoning
- Designed for hackathon prototype integration with a React frontend

---

## 📦 Setup (Backend Developers)
1. Clone this repo:
   ```bash
   git clone <your-repo-url>
   cd RailNova-Backend
   Create virtual environment:

python -m venv venv
venv\Scripts\activate   # (Windows)
# source venv/bin/activate   # (Linux/Mac)


Install dependencies:

pip install -r requirements.txt


Run the Flask app:

python app.py


By default, it runs on:
http://127.0.0.1:5000

🔌 API Endpoints
1. Health Check
GET /


Response:

{ "status": "ok", "message": "RailNova Backend is running 🚆" }

2. Optimize Train Traffic
POST /optimize
Content-Type: application/json


Request Body (example):

{
  "trains": [
    { "train_id": "EXP001", "priority": 1, "status": "delayed_20_mins" },
    { "train_id": "FRG010", "priority": 3, "status": "on_time" }
  ]
}


Response:

{
  "status": "success",
  "data": {
    "schedule": [
      {
        "train_id": "EXP001",
        "priority": 1,
        "initial_delay": 20,
        "final_delay": 10
      },
      {
        "train_id": "FRG010",
        "priority": 3,
        "initial_delay": 0,
        "final_delay": 0
      }
    ],
    "kpis": {
      "total_delay": 10,
      "avg_delay": 5.0,
      "num_trains": 2
    },
    "reasoning": [
      "Reduced EXP001 delay from 20 → 10 (express priority)."
    ]
  }
}

🖥️ Usage (Frontend Developers)

The backend runs locally at http://127.0.0.1:5000

Example React call with axios:

import axios from "axios";

async function runSimulation() {
  try {
    const response = await axios.post("http://127.0.0.1:5000/optimize", {
      trains: [
        { train_id: "EXP001", priority: 1, status: "delayed_20_mins" },
        { train_id: "FRG010", priority: 3, status: "on_time" }
      ]
    });
    console.log(response.data);
    // response.data.data.schedule -> array for Gantt chart
    // response.data.data.kpis -> feed into KPI cards
    // response.data.data.reasoning -> show in RecommendationPanel
  } catch (err) {
    console.error("API call failed:", err);
  }
}


Integrate this data into:

Gantt Chart View → use schedule

KPI Cards → use kpis

Recommendation Panel → use reasoning
