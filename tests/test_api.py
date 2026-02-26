import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
import database

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_tudo(client):
    rv = client.get('/api/tudo')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert 'escaleta' in json_data

def test_listar_modulo(client):
    rv = client.get('/api/jornalismo')
    assert rv.status_code == 200
    assert isinstance(rv.get_json(), list)
