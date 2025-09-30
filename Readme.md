# 🚆 RailNova-backend  (Basic Prototype)

This is the **backend service** for the RailNova / Rail-GPT AI Traffic Co-Pilot.  
It is a lightweight prototype built with **Flask + PuLP** to simulate train scheduling, demonstrate optimization, and provide APIs for frontend integration.

---

## 📌 Features
- ✅ Health check endpoint (`/`)  
- ✅ Accepts disruption scenarios (`/optimize`)  
- ✅ Returns both:
  - Baseline schedule (naive solver)  
  - AI-optimized schedule (toy optimization with PuLP)  
- ✅ Generates **KPIs** (e.g., total delay)  
- ✅ Provides **Explainable AI reasoning**  

---

## 🛠️ Tech Stack
- **Python 3.9+**  
- **Flask** – API server  
- **Pandas** – (future data parsing)  
- **PuLP** – Linear programming optimizer  

---

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/Dhriti-5/RailNova-backend.git
cd RailNova-backend
````

### 2. Setup Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Server

```bash
python app.py
```

Backend runs on: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📡 API Endpoints

### 1. Health Check

`GET /`
**Response:**

```json
{"status": "ok"}
```

---

### 2. Optimize Schedule

`POST /optimize`

**Request Example**

```json
{
  "timestamp": "10:00",
  "trains": [
    {"train_id": "Rajdhani_12952", "priority": 1, "status": "delayed_15_mins"},
    {"train_id": "Freight_758", "priority": 3, "status": "on_time"}
  ]
}
```

**Response Example**

```json
{
  "baseline": {
    "schedule": [
      {"train_id": "Rajdhani_12952", "final_delay": 15},
      {"train_id": "Freight_758", "final_delay": 0}
    ],
    "kpis": {"total_delay": 15}
  },
  "ai": {
    "schedule": [
      {"train_id": "Rajdhani_12952", "final_delay": 0.0},
      {"train_id": "Freight_758", "final_delay": 0.0}
    ],
    "kpis": {"total_delay": 0.0},
    "reasoning": ["All trains scheduled with minimal conflict."]
  }
}
```

---

## 🧪 Testing

### With `curl`

```bash
curl -X POST http://127.0.0.1:5000/optimize \
  -H "Content-Type: application/json" \
  -d @data/scenario_1_chaos.json
```

### With PowerShell

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/optimize" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{
    "timestamp": "10:00",
    "trains": [
      {"train_id": "Rajdhani_12952", "priority": 1, "status": "delayed_15_mins"},
      {"train_id": "Freight_758", "priority": 3, "status": "on_time"}
    ]
  }'
```

---

## 📂 Project Structure

```
rail-gpt-backend/
├── app.py              # Flask app & endpoints
├── solvers.py          # Baseline & AI solvers
├── data/               # Dummy data files
│   ├── layout.json
│   ├── timetable.json
│   └── scenario_1_chaos.json
├── requirements.txt    # Dependencies
└── README.md
```

---

## 🔗 Frontend Integration

The backend is designed to be consumed by the **RailNova Frontend Dashboard**.
Frontend will hit:

```
POST http://127.0.0.1:5000/optimize
```

Input: scenario JSON
Output: schedules, KPIs, reasoning

---

