
from datetime import datetime, timezone
from typing import List, Optional

from src.exceptions import TaskNotFoundException
from src.models.task import Task, TaskUpdate


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

    def update_task(self, task_id: str, task_update: TaskUpdate) -> Task:
        '''Update a task's status or priority'''
        task = self.get_task_by_id(task_id)
        if not task:
            raise TaskNotFoundException(task_id)

        # Update fields if provided
        if task_update.status is not None:
            task.status = task_update.status
        if task_update.priority is not None:
            task.priority = task_update.priority

        # Update timestamp
        task.updated_at = datetime.now(timezone.utc)

        return task

    def delete_task(self, task_id: str) -> bool:
        '''Delete a task by ID'''
        task = self.get_task_by_id(task_id)
        if not task:
            raise TaskNotFoundException(task_id)

        self.tasks.remove(task)
        return True

    def clear_all(self):
        '''Clear all tasks (useful for testing)'''
        self.tasks = []

# Global storage instance
task_storage = TaskStorage()
