from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3


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


def get_database():
    connection = sqlite3.connect("motsireletsi.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    connection = get_database()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            incident_type TEXT NOT NULL,
            description TEXT NOT NULL,
            location TEXT NOT NULL,
            urgency TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


create_database()


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

    connection = get_database()

    cursor = connection.execute(
        """
        INSERT INTO reports
        (incident_type, description, location, urgency)
        VALUES (?, ?, ?, ?)
        """,
        (
            report.incident_type,
            report.description,
            report.location,
            report.urgency
        )
    )

    connection.commit()

    report_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Report received",
        "status": "submitted",
        "report_id": report_id
    }
