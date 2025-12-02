# Create custom exceptions

from fastapi import HTTPException, status

class TaskNotFoundException(HTTPException):
    '''Exception raised when a task is not found'''
    def __init__(self, task_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Task with ID {task_id} not found'
        )

class InvalidTaskStatusException(HTTPException):
    '''Exception raised when an invalid task status is provided'''
    def __init__(self, status: str):
        valid_statuses = ['pending', 'in_progress', 'completed']
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f'Invalid status \"{status}\". Must be one of: {', '.join(valid_statuses)}'
        )

class InvalidPriorityException(HTTPException):
    '''Exception raised when an invalid priority is provided'''
    def __init__(self, priority: str):
        valid_priorities = ['low', 'medium', 'high']
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f'Invalid priority \"{priority}\". Must be one of: {', '.join(valid_priorities)}'
        )
