import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the root route returns success"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Enterprise CI/CD Pipeline!" in response.data

def test_health_check(client):
    """Test the health route returns healthy status"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data