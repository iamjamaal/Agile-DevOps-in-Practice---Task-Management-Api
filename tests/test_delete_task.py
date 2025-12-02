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


class TestDeleteTask:
    """Tests for DELETE /tasks/{task_id} endpoint"""

    def test_delete_task_success(self):
        """Test successful task deletion"""
        # Create a task
        create_response = client.post("/tasks", json={"title": "Task to delete"})
        task_id = create_response.json()["id"]

        # Delete the task
        response = client.delete(f"/tasks/{task_id}")

        assert response.status_code == 204
        assert response.content == b""

    def test_deleted_task_not_in_list(self):
        """Test that deleted task doesn't appear in list"""
        # Create a task
        create_response = client.post("/tasks", json={"title": "Task to delete"})
        task_id = create_response.json()["id"]

        # Delete the task
        client.delete(f"/tasks/{task_id}")

        # List tasks
        list_response = client.get("/tasks")
        tasks = list_response.json()

        # Verify task is not in list
        task_ids = [task["id"] for task in tasks]
        assert task_id not in task_ids

    def test_get_deleted_task_returns_404(self):
        """Test that getting a deleted task returns 404"""
        # Create a task
        create_response = client.post("/tasks", json={"title": "Task to delete"})
        task_id = create_response.json()["id"]

        # Delete the task
        client.delete(f"/tasks/{task_id}")

        # Try to get the deleted task
        get_response = client.get(f"/tasks/{task_id}")

        assert get_response.status_code == 404

    def test_delete_nonexistent_task(self):
        """Test deleting a task that doesn't exist"""
        response = client.delete("/tasks/nonexistent-id")

        assert response.status_code == 404
        assert "not found" in response.json()["detail"].lower()

    def test_delete_multiple_tasks(self):
        """Test deleting multiple tasks"""
        # Create multiple tasks
        task1 = client.post("/tasks", json={"title": "Task 1"}).json()
        task2 = client.post("/tasks", json={"title": "Task 2"}).json()
        task3 = client.post("/tasks", json={"title": "Task 3"}).json()

        # Delete task 2
        client.delete(f"/tasks/{task2['id']}")

        # Verify task 1 and 3 still exist
        tasks = client.get("/tasks").json()
        task_ids = [task["id"] for task in tasks]

        assert task1["id"] in task_ids
        assert task2["id"] not in task_ids
        assert task3["id"] in task_ids
        assert len(tasks) == 2

    def test_cannot_update_deleted_task(self):
        """Test that updating a deleted task returns 404"""
        # Create a task
        create_response = client.post("/tasks", json={"title": "Task to delete"})
        task_id = create_response.json()["id"]

        # Delete the task
        client.delete(f"/tasks/{task_id}")

        # Try to update the deleted task
        update_response = client.patch(
            f"/tasks/{task_id}", json={"status": "completed"}
        )

        assert update_response.status_code == 404