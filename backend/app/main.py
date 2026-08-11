from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Mots'ireletsi API",
    description="Rural Community Safety Platform for Lesotho",
    version="0.1.0"
)


class IncidentReport(BaseModel):
    incident_type: str
    description: str
    location: str
    urgency: str


@app.get("/")
def root():
    return {
        "message": "Welcome to Mots'ireletsi",
        "status": "API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/reports")
def create_report(report: IncidentReport):
    return {
        "message": "Report received",
        "status": "submitted",
        "report": report
    }
