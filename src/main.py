from fastapi import FastAPI, status
from datetime import datetime, timezone
from typing import List
from src.models.task import Task, TaskCreate
from src.services.task_service import TaskStorage

app = FastAPI(
    title='Task Management API', description='A simple task management system', version='0.1.0'
)

# Initialize task storage
task_storage = TaskStorage()


@app.get('/')
def read_root():
    return {'message': 'Welcome to the Task Management API'}


@app.get('/health')
def health_check():
    return {'status': 'healthy', 'timestamp': datetime.now(timezone.utc).isoformat()}


@app.post('/tasks', response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    """Create a new task."""
    task = Task(title=task_data.title, description=task_data.description)
    created_task = task_storage.add_task(task)
    return created_task


@app.get('/tasks', response_model=List[Task])
def get_tasks():
    """Retrieve all tasks."""
    return task_storage.get_all_tasks()
