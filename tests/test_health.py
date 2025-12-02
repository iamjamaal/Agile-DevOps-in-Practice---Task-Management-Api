# Create test file

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check_returns_200():
    '''Test that health check endpoint returns 200 status'''
    response = client.get('/health')
    assert response.status_code == 200

def test_health_check_returns_healthy_status():
    '''Test that health check returns healthy status'''
    response = client.get('/health')
    data = response.json()
    assert data['status'] == 'healthy'

def test_health_check_includes_timestamp():
    '''Test that health check includes timestamp'''
    response = client.get('/health')
    data = response.json()
    assert 'timestamp' in data
    assert data['timestamp'] is not None
