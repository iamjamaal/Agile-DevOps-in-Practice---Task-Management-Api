
from datetime import datetime, timezone
from typing import Literal, Optional
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    '''Schema for creating a new task'''
    title: str = Field(..., min_length=1, max_length=200, description='Task title')
    description: Optional[str] = Field(None, max_length=1000, description='Task description')
    priority: Literal['low', 'medium', 'high'] = Field(default='medium', description='Task priority')

class TaskUpdate(BaseModel):
    '''Schema for updating a task'''
    status: Optional[Literal['pending', 'in_progress', 'completed']] = Field(None, description='Task status')
    priority: Optional[Literal['low', 'medium', 'high']] = Field(None, description='Task priority')

class Task(BaseModel):
    '''Complete task model'''
    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': '123e4567-e89b-12d3-a456-426614174000',
                'title': 'Complete project documentation',
                'description': 'Write comprehensive README and API docs',
                'status': 'pending',
                'priority': 'high',
                'created_at': '2024-12-02T10:30:00',
                'updated_at': None
            }
        }
    )

    id: str = Field(default_factory=lambda: str(uuid4()), description='Unique task ID')
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Literal['pending', 'in_progress', 'completed'] = Field(default='pending', description='Task status')
    priority: Literal['low', 'medium', 'high'] = Field(default='medium', description='Task priority')
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = Field(default=None)
