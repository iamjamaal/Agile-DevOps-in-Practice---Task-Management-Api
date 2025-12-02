import pytest
from fastapi.testclient import TestClient
from src.main import app, task_storage

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_tasks():
    """Clear tasks before each test"""
    task_storage.clear_all()
    yield
    task_storage.clear_all()


class TestCreateTask:
    """Tests for POST /tasks endpoint"""

    def test_create_task_success(self):
        """Test successful task creation"""
        response = client.post(
            '/tasks', json={'title': 'Test task', 'description': 'Test description'}
        )
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == 'Test task'
        assert data['description'] == 'Test description'
        assert data['status'] == 'pending'
        assert 'id' in data
        assert 'created_at' in data

    def test_create_task_without_description(self):
        """Test creating task without description"""
        response = client.post('/tasks', json={'title': 'Task without description'})
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == 'Task without description'
        assert data['description'] is None

    def test_create_task_missing_title(self):
        """Test that missing title returns 422"""
        response = client.post('/tasks', json={'description': 'No title provided'})
        assert response.status_code == 422

    def test_create_task_empty_title(self):
        """Test that empty title returns 422"""
        response = client.post('/tasks', json={'title': '', 'description': 'Empty title'})
        assert response.status_code == 422

    def test_create_task_title_too_long(self):
        """Test that title over 200 chars returns 422"""
        long_title = 'x' * 201
        response = client.post('/tasks', json={'title': long_title})
        assert response.status_code == 422


class TestListTasks:
    """Tests for GET /tasks endpoint"""

    def test_list_tasks_empty(self):
        """Test listing tasks when none exist"""
        response = client.get('/tasks')
        assert response.status_code == 200
        assert response.json() == []

    def test_list_tasks_returns_created_task(self):
        """Test that created task appears in list"""
        # Create a task
        client.post('/tasks', json={'title': 'Task 1'})

        # List tasks
        response = client.get('/tasks')
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]['title'] == 'Task 1'

    def test_list_tasks_multiple(self):
        """Test listing multiple tasks"""
        # Create multiple tasks
        client.post('/tasks', json={'title': 'Task 1'})
        client.post('/tasks', json={'title': 'Task 2'})
        client.post('/tasks', json={'title': 'Task 3'})

        # List tasks
        response = client.get('/tasks')
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3

    def test_list_tasks_ordered_by_date(self):
        """Test that tasks are ordered newest first"""
        # Create tasks in order
        response1 = client.post('/tasks', json={'title': 'First task'})
        response2 = client.post('/tasks', json={'title': 'Second task'})

        # List tasks
        response = client.get('/tasks')
        data = response.json()

        # Newest should be first
        assert data[0]['title'] == 'Second task'
        assert data[1]['title'] == 'First task'
