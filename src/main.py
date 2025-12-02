
from datetime import datetime, timezone

from fastapi import FastAPI, status

from src.exceptions import TaskNotFoundException
from src.logging_config import logger
from src.middleware import RequestLoggingMiddleware
from src.models.task import Task, TaskCreate, TaskUpdate
from src.services.task_service import task_storage

app = FastAPI(
    title='Task Management API',
    description='A simple task management system with monitoring and logging',
    version='0.2.0'
)

# Add logging middleware
app.add_middleware(RequestLoggingMiddleware)

@app.get('/')
def read_root():
    '''Root endpoint'''
    return {'message': 'Welcome to Task Management API', 'version': '0.2.0'}

@app.get('/health')
def health_check():
    '''Health check endpoint with system information'''
    task_count = len(task_storage.get_all_tasks())
    return {
        'status': 'healthy',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'version': '0.2.0',
        'tasks_count': task_count
    }

@app.post('/tasks', response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    '''Create a new task'''
    logger.info(f'Creating new task: {task_data.title}')

    task = Task(
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority
    )
    created_task = task_storage.add_task(task)

    logger.info(f'Task created successfully: {created_task.id}')
    return created_task

@app.get('/tasks', response_model=list[Task])
def get_tasks():
    '''Get all tasks'''
    tasks = task_storage.get_all_tasks()
    logger.info(f'Retrieved {len(tasks)} tasks')
    return tasks

@app.get('/tasks/{task_id}', response_model=Task)
def get_task(task_id: str):
    '''Get a specific task by ID'''
    logger.info(f'Retrieving task: {task_id}')

    task = task_storage.get_task_by_id(task_id)
    if not task:
        logger.warning(f'Task not found: {task_id}')
        raise TaskNotFoundException(task_id)

    return task

@app.patch('/tasks/{task_id}', response_model=Task)
def update_task(task_id: str, task_update: TaskUpdate):
    '''Update a task's status or priority'''
    logger.info(f'Updating task: {task_id}')

    try:
        updated_task = task_storage.update_task(task_id, task_update)
        logger.info(f'Task updated successfully: {task_id}')
        return updated_task
    except TaskNotFoundException as e:
        logger.warning(f'Update failed - task not found: {task_id}')
        raise e

@app.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    '''Delete a task'''
    logger.info(f'Deleting task: {task_id}')

    try:
        task_storage.delete_task(task_id)
        logger.info(f'Task deleted successfully: {task_id}')
        return None
    except TaskNotFoundException as e:
        logger.warning(f'Delete failed - task not found: {task_id}')
        raise e
