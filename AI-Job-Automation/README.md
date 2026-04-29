#  AI Job Automation System

An end-to-end AI-powered workflow that automatically processes job alerts and organizes them intelligently.

##  Features
- Reads job emails from Gmail
- Extracts job details using AI (Gemini)
- Processes data using FastAPI (Python)
- Scores job relevance
- Stores structured data in Google Sheets

##  Tech Stack
- n8n
- Google Gemini
- FastAPI
- Python
- Gmail API
- Google Sheets

##  Workflow
Gmail → AI Extraction → Python API → Google Sheets

##  Setup

### 1. Run FastAPI
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
