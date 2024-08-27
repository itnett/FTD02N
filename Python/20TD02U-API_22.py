python
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    rv = client.get('/users')
    assert rv.status_code == 200
    assert b'John Doe' in rv.data