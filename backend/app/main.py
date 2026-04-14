from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI(title="DevOps Lernplattform API", version="1.0.0")

COURSES = [
    {"id": "linux-basics", "title": "Linux Basics", "modules": 2},
    {"id": "docker-basics", "title": "Docker Basics", "modules": 2},
]
LAB_RUNS = {}
GRADES = {}


class StartLabResponse(BaseModel):
    runId: str
    status: str


class TerminalSessionResponse(BaseModel):
    wsUrl: str
    token: str
    expiresAt: str


@app.get("/healthz")
def healthz():
    return {"ok": True, "service": "backend"}


@app.get("/api/me")
def me():
    return {"id": "demo-user", "email": "learner@example.com", "roles": ["learner"]}


@app.get("/api/courses")
def list_courses():
    return {"items": COURSES, "total": len(COURSES)}


@app.post("/api/labs/{lab_id}/runs", response_model=StartLabResponse)
def start_lab(lab_id: str):
    run_id = str(uuid4())
    LAB_RUNS[run_id] = {
        "id": run_id,
        "labId": lab_id,
        "status": "running",
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }
    return {"runId": run_id, "status": "running"}


@app.get("/api/lab-runs/{run_id}")
def get_lab_run(run_id: str):
    if run_id not in LAB_RUNS:
        raise HTTPException(404, "run not found")
    return LAB_RUNS[run_id]


@app.post("/api/lab-runs/{run_id}/grade")
def trigger_grade(run_id: str):
    if run_id not in LAB_RUNS:
        raise HTTPException(404, "run not found")
    GRADES[run_id] = {
        "runId": run_id,
        "status": "passed",
        "score": 100,
        "checks": [
            {"id": "svc", "passed": True, "message": "service active"},
            {"id": "perm", "passed": True, "message": "permissions correct"},
        ],
    }
    return GRADES[run_id]


@app.get("/api/lab-runs/{run_id}/grade")
def get_grade(run_id: str):
    if run_id not in GRADES:
        raise HTTPException(404, "grade not found")
    return GRADES[run_id]


@app.post("/api/lab-runs/{run_id}/terminal-sessions", response_model=TerminalSessionResponse)
def create_terminal_session(run_id: str):
    if run_id not in LAB_RUNS:
        raise HTTPException(404, "run not found")
    token = str(uuid4())
    expires = datetime.now(timezone.utc) + timedelta(minutes=20)
    LAB_RUNS[run_id]["terminalToken"] = token
    return {
        "wsUrl": "ws://localhost:8090/ws/terminal",
        "token": token,
        "expiresAt": expires.isoformat(),
    }
