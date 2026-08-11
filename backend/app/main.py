
from fastapi import FastAPI

app = FastAPI(
    title="Mots'ireletsi API",
    description="Rural Community Safety Platform for Lesotho",
    version="0.1.0"
)


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
