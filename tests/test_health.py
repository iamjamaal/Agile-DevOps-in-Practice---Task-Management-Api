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


def test_health_check_returns_200():
    """Test that health check endpoint returns 200 status"""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_check_returns_healthy_status():
    """Test that health check returns healthy status"""
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "healthy"


def test_health_check_includes_timestamp():
    """Test that health check includes timestamp"""
    response = client.get("/health")
    data = response.json()
    assert "timestamp" in data
    assert data["timestamp"] is not None


def test_health_check_includes_version():
    """Test that health check includes version"""
    response = client.get("/health")
    data = response.json()
    assert "version" in data
    assert data["version"] == "0.2.0"


def test_health_check_includes_task_count():
    """Test that health check includes task count"""
    response = client.get("/health")
    data = response.json()
    assert "tasks_count" in data
    assert isinstance(data["tasks_count"], int)


def test_health_check_task_count_accuracy():
    """Test that task count is accurate"""
    # Initially should be 0
    response = client.get("/health")
    assert response.json()["tasks_count"] == 0

    # Create 3 tasks
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})
    client.post("/tasks", json={"title": "Task 3"})

    # Should now be 3
    response = client.get("/health")
    assert response.json()["tasks_count"] == 3
