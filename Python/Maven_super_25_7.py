python
import pytest
from flask import Flask, jsonify, request
from my_api import app  # Anta at Flask-appen er i en fil kalt my_api.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_book(client):
    new_book = {"title": "Ny Bok", "author": "Forfatter"}
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    assert response.json == new_book

def test_delete_book(client):
    response = client.delete('/books/0')
    assert response.status_code == 200 or response.status_code == 404