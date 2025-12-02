# Create in-memory storage
from typing import List, Optional
from src.models.task import Task

class TaskStorage:
    '''In-memory task storage'''
    
    def __init__(self):
        self.tasks: List[Task] = []
    
    def add_task(self, task: Task) -> Task:
        '''Add a new task to storage'''
        self.tasks.append(task)
        return task
    
    def get_all_tasks(self) -> List[Task]:
        '''Get all tasks, sorted by creation date (newest first)'''
        return sorted(self.tasks, key=lambda t: t.created_at, reverse=True)
    
    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        '''Get a specific task by ID'''
        return next((task for task in self.tasks if task.id == task_id), None)
    
    def clear_all(self):
        '''Clear all tasks (useful for testing)'''
        self.tasks = []


# Global storage instance
task_storage = TaskStorage()