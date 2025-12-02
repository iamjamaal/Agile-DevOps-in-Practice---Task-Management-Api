import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.services.task_service import task_storage

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_tasks():
    """Clear tasks before each test"""
    task_storage.clear_all()
    yield
    task_storage.clear_all()


class TestUpdateTask:
    """Tests for PATCH /tasks/{task_id} endpoint"""

    def test_update_task_status_success(self):
        """Test successful task status update"""
        # Create a task
        create_response = client.post('/tasks', json={'title': 'Test task'})
        task_id = create_response.json()['id']

        # Update status
        response = client.patch(f'/tasks/{task_id}', json={'status': 'in_progress'})

        assert response.status_code == 200
        data = response.json()
        assert data['id'] == task_id
        assert data['status'] == 'in_progress'
        assert data['updated_at'] is not None

    def test_update_task_to_completed(self):
        """Test updating task to completed status"""
        # Create a task
        create_response = client.post('/tasks', json={'title': 'Test task'})
        task_id = create_response.json()['id']

        # Update to completed
        response = client.patch(f'/tasks/{task_id}', json={'status': 'completed'})

        assert response.status_code == 200
        assert response.json()['status'] == 'completed'

    def test_update_task_priority_success(self):
        """Test successful task priority update"""
        # Create a task
        create_response = client.post('/tasks', json={'title': 'Test task'})
        task_id = create_response.json()['id']

        # Update priority
        response = client.patch(f'/tasks/{task_id}', json={'priority': 'high'})

        assert response.status_code == 200
        data = response.json()
        assert data['priority'] == 'high'
        assert data['updated_at'] is not None

    def test_update_both_status_and_priority(self):
        """Test updating both status and priority"""
        # Create a task
        create_response = client.post('/tasks', json={'title': 'Test task'})
        task_id = create_response.json()['id']

        # Update both
        response = client.patch(
            f'/tasks/{task_id}', json={'status': 'in_progress', 'priority': 'high'}
        )

        assert response.status_code == 200
        data = response.json()
        assert data['status'] == 'in_progress'
        assert data['priority'] == 'high'

    def test_update_nonexistent_task(self):
        """Test updating a task that doesn't exist"""
        response = client.patch('/tasks/nonexistent-id', json={'status': 'completed'})

        assert response.status_code == 404
        assert 'not found' in response.json()['detail'].lower()

    def test_update_with_invalid_status(self):
        """Test updating with invalid status"""
        # Create a task
        create_response = client.post('/tasks', json={'title': 'Test task'})
        task_id = create_response.json()['id']

        # Try invalid status
        response = client.patch(f'/tasks/{task_id}', json={'status': 'invalid_status'})

        assert response.status_code == 422

    def test_update_with_invalid_priority(self):
        """Test updating with invalid priority"""
        # Create a task
        create_response = client.post('/tasks', json={'title': 'Test task'})
        task_id = create_response.json()['id']

        # Try invalid priority
        response = client.patch(f'/tasks/{task_id}', json={'priority': 'urgent'})

        assert response.status_code == 422

    def test_update_with_empty_body(self):
        """Test update with no fields provided"""
        # Create a task
        create_response = client.post('/tasks', json={'title': 'Test task'})
        task_id = create_response.json()['id']

        # Update with empty body
        response = client.patch(f'/tasks/{task_id}', json={})

        assert response.status_code == 200
        # Task should remain unchanged except updated_at
