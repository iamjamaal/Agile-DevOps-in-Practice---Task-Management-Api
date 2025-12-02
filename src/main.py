from fastapi import FastAPI

app = FastAPI(
    title = "Task Management API",
    description = "A simple task management system", 
    version = "0.1.0"

)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}