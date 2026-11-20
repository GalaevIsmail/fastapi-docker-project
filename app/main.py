from fastapi import FastAPI
from redis import Redis
from sqlalchemy import text

from app.database import engine

app = FastAPI(
    title="Docker FastAPI Project",
    description="FastAPI application with PostgreSQL and Redis",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "FastAPI Docker Project is running!",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/db-check")
def database_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {"database": "connected"}