from fastapi import FastAPI, Request
from datetime import datetime
import json
import re

app = FastAPI()

@app.post("/parse-job")
async def parse_job(request: Request):
    body = await request.json()

    content = body.get("content", {})
    raw = content["parts"][0]["text"]

    raw = raw.replace("```json", "").replace("```", "").strip()

    match = re.search(r"\{[\s\S]*\}", raw)
    if match:
        raw = match.group(0)

    data = json.loads(raw)

    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "job_title": data.get("job_title", ""),
        "company": data.get("company", ""),
        "location": data.get("location", ""),
        "job_link": data.get("job_link", ""),
        "experience_required": data.get("experience_required", ""),
        "skills_found": ", ".join(data.get("skills_found", [])),
        "matched_skills": ", ".join(data.get("matched_skills", [])),
        "missing_skills": ", ".join(data.get("missing_skills", [])),
        "relevance_score": data.get("relevance_score", ""),
        "apply_decision": data.get("apply_decision", ""),
        "reason": data.get("reason", ""),
        "status": "Not Applied"
    }