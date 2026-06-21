# Gemini AI Log Analytics & Anomaly Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb&logoColor=white) ![Gemini](https://img.shields.io/badge/Google%20Gemini-AI%20API-4285F4?logo=google&logoColor=white) ![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> An AI-powered log analytics platform that ingests, parses, and analyzes application logs using Google Gemini AI — with real-time anomaly detection, interactive dashboards, and a natural language chat interface for log querying.

---

## Overview

This project combines a FastAPI-based backend for log ingestion and processing with a Streamlit frontend for visualization and AI-assisted exploration. Logs are stored in MongoDB, analyzed through a custom metrics engine, and surfaced through an interactive dashboard. The Gemini AI integration enables conversational querying — users can ask natural language questions about their logs and get intelligent, context-aware answers.

---

## Repository Structure

```
Gemini-AI-Log-Analytics/
│
├── .devcontainer/
│   └── devcontainer.json              # Dev container config for VS Code / GitHub Codespaces
│
├── .streamlit/
│   └── config.toml                    # Streamlit theme and server configuration
│
├── app/                               # Streamlit frontend
│   ├── components/
│   │   ├── cards.py                   # KPI metric card components
│   │   ├── charts.py                  # Chart rendering components (Plotly/Altair)
│   │   └── tables.py                  # Data table display components
│   ├── pages/
│   │   ├── dashboard.py               # Main analytics dashboard page
│   │   ├── ai_chat.py                 # Gemini AI conversational log query page
│   │   └── upload_logs.py             # Log file upload and ingestion UI
│   ├── services/
│   │   ├── gemini_client.py           # Google Gemini API integration
│   │   └── mongo_client.py            # MongoDB connection for frontend
│   ├── app.py                         # Streamlit app entry point
│   └── __init__.py
│
├── backend/                           # FastAPI backend
│   ├── log_ingestor.py                # Log ingestion pipeline
│   ├── log_parser.py                  # Log parsing and structuring logic
│   ├── metrics_engine.py              # Anomaly detection and metrics computation
│   ├── mongo_client.py                # MongoDB connection for backend
│   ├── main.py                        # FastAPI app entry point
│   └── __init__.py
│
└── requirements.txt                   # Python dependencies
```

---

## Architecture

```
┌─────────────────────┐       ┌──────────────────────┐
│   Streamlit Frontend │◄─────►│   FastAPI Backend     │
│                     │       │                      │
│  • Dashboard        │       │  • Log Ingestor      │
│  • AI Chat          │       │  • Log Parser        │
│  • Upload Logs      │       │  • Metrics Engine    │
└────────┬────────────┘       └──────────┬───────────┘
         │                               │
         ▼                               ▼
┌─────────────────┐             ┌─────────────────────┐
│  Google Gemini  │             │      MongoDB         │
│     AI API      │             │  (Log Storage &      │
│  (NL Querying)  │             │   Aggregations)      │
└─────────────────┘             └─────────────────────┘
```

---

## Features

### Backend
- **Log Ingestion** — Accepts raw log files via API, supports multiple formats (Apache, JSON, custom)
- **Log Parsing** — Extracts structured fields: timestamp, level, service, message, IP, status code
- **Metrics Engine** — Computes error rates, request frequency, latency spikes, and anomaly scores
- **Anomaly Detection** — Flags unusual patterns using statistical thresholds and frequency analysis

### Frontend (Streamlit)
- **Dashboard Page** — Real-time KPI cards, error trend charts, log level distribution, service-wise breakdown
- **AI Chat Page** — Natural language interface powered by Gemini AI; ask questions like *"Which service had the most errors yesterday?"*
- **Upload Logs Page** — Drag-and-drop log file upload with instant parsing preview

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit, Plotly |
| Backend | FastAPI, Python |
| AI Integration | Google Gemini API (`gemini-1.5-flash`) |
| Database | MongoDB (Atlas or local) |
| Dev Environment | VS Code Dev Containers / GitHub Codespaces |
| Data Processing | Pandas, NumPy |

---

## Getting Started

### Option 1 — Dev Container (Recommended)

Open in **VS Code** with the Dev Containers extension, or launch directly in **GitHub Codespaces**. Everything is pre-configured via `.devcontainer/devcontainer.json`.

### Option 2 — Local Setup

#### 1. Clone the repository
```bash
git clone https://github.com/adithya7781/Gemini-AI-Log-Analytics.git
cd Gemini-AI-Log-Analytics
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Set environment variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_google_gemini_api_key
MONGO_URI=mongodb://localhost:27017/log_analytics
```

#### 4. Start the backend
```bash
cd backend
uvicorn main:app --reload --port 8000
```

#### 5. Start the Streamlit frontend
```bash
cd app
streamlit run app.py
```

Visit `http://localhost:8501` to access the dashboard.

---

## API Endpoints (FastAPI)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/ingest` | Upload and ingest a log file |
| `GET` | `/metrics` | Retrieve computed metrics and anomaly scores |
| `GET` | `/logs` | Query stored logs with filters |
| `GET` | `/health` | Backend health check |

---

## Example AI Chat Queries

> "What was the peak error rate in the last 24 hours?"

> "Which endpoints returned the most 500 errors this week?"

> "Summarize anomalies detected between 2 AM and 4 AM."

> "How does today's traffic compare to yesterday?"

---

## Key Highlights

- End-to-end pipeline from raw log ingestion → parsing → storage → AI-assisted analysis
- Modular component design: frontend, backend, and AI layer are fully decoupled
- Dev container support makes the project instantly reproducible with zero local setup
- Gemini AI integration enables non-technical users to query complex log data conversationally

---

## Author

**Ketharaju Vishal Adithya**  
B.Tech Data Science, Vignana Bharathi Institute of Technology (VBIT), Hyderabad  
[GitHub](https://github.com/adithya7781)

---

## License

This project is for educational and portfolio demonstration purposes.
