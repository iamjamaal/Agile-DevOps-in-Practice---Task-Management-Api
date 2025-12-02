# Create Task model
from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    """Schema for creating a new task"""

    title: str = Field(..., min_length=1, max_length=200, description='Task title')
    description: Optional[str] = Field(None, max_length=1000, description='Task description')


class Task(BaseModel):
    """Complete task model"""

    id: str = Field(default_factory=lambda: str(uuid4()), description='Unique task ID')
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: str = Field(default='pending', description='Task status')
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            'example': {
                'id': '123e4567-e89b-12d3-a456-426614174000',
                'title': 'Complete project documentation',
                'description': 'Write comprehensive README and API docs',
                'status': 'pending',
                'created_at': '2024-12-02T10:30:00',
            }
        }
