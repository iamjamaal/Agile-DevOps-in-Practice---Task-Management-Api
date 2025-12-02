
import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.services.task_service import task_storage

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_tasks():
    '''Clear tasks before each test'''
    task_storage.clear_all()
    yield
    task_storage.clear_all()

class TestTaskPriority:
    '''Tests for task priority functionality'''

    def test_create_task_with_default_priority(self):
        '''Test that tasks default to medium priority'''
        response = client.post('/tasks', json={'title': 'Default priority task'})

        assert response.status_code == 201
        data = response.json()
        assert data['priority'] == 'medium'

    def test_create_task_with_low_priority(self):
        '''Test creating task with low priority'''
        response = client.post('/tasks', json={
            'title': 'Low priority task',
            'priority': 'low'
        })

        assert response.status_code == 201
        assert response.json()['priority'] == 'low'

    def test_create_task_with_high_priority(self):
        '''Test creating task with high priority'''
        response = client.post('/tasks', json={
            'title': 'High priority task',
            'priority': 'high'
        })

        assert response.status_code == 201
        assert response.json()['priority'] == 'high'

    def test_create_task_with_invalid_priority(self):
        '''Test that invalid priority returns 422'''
        response = client.post('/tasks', json={
            'title': 'Invalid priority task',
            'priority': 'urgent'
        })

        assert response.status_code == 422

    def test_update_task_priority(self):
        '''Test updating task priority'''
        # Create task with default priority
        create_response = client.post('/tasks', json={'title': 'Test task'})
        task_id = create_response.json()['id']

        # Update priority to high
        update_response = client.patch(
            f'/tasks/{task_id}',
            json={'priority': 'high'}
        )

        assert update_response.status_code == 200
        assert update_response.json()['priority'] == 'high'

    def test_update_priority_from_high_to_low(self):
        '''Test changing priority from high to low'''
        # Create high priority task
        create_response = client.post('/tasks', json={
            'title': 'High priority task',
            'priority': 'high'
        })
        task_id = create_response.json()['id']

        # Update to low priority
        update_response = client.patch(
            f'/tasks/{task_id}',
            json={'priority': 'low'}
        )

        assert update_response.status_code == 200
        assert update_response.json()['priority'] == 'low'

    def test_priority_persists_across_status_update(self):
        '''Test that priority is maintained when updating status'''
        # Create high priority task
        create_response = client.post('/tasks', json={
            'title': 'Test task',
            'priority': 'high'
        })
        task_id = create_response.json()['id']

        # Update status only
        update_response = client.patch(
            f'/tasks/{task_id}',
            json={'status': 'completed'}
        )

        # Priority should still be high
        assert update_response.json()['priority'] == 'high'

    def test_all_priority_levels(self):
        '''Test all three priority levels'''
        priorities = ['low', 'medium', 'high']

        for priority in priorities:
            response = client.post('/tasks', json={
                'title': f'{priority.capitalize()} priority task',
                'priority': priority
            })

            assert response.status_code == 201
            assert response.json()['priority'] == priority
