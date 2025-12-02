from fastapi import FastAPI
from datetime import datetime


app = FastAPI(
    title = "Task Management API",
    description = "A simple task management system", 
    version = "0.1.0"

)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() }
