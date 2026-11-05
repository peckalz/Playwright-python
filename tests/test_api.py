import requests
import pytest
from playwright.sync_api import expect


def test_request_first_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200

    user = response.json()

    assert "city" in user["address"]
    assert "address" in user
    assert user["id"] == 1
    assert isinstance(user["id"], int)
    assert isinstance(user, dict)
    assert isinstance(user["name"], str)
    assert isinstance(user["email"], str)
    assert isinstance(user["address"], dict)
    assert isinstance(user["address"]["city"], str)


def test_request_nonexistent_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")

    assert response.status_code == 404
    assert response.text == "{}"


def test_create_user():
    payload = {
        "name": "John",
        "email": "john@email.com"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/users", json = payload)

    assert response.status_code == 201
    user = response.json()
    assert user["name"]  == payload["name"]
    assert user["email"]  == payload["email"]
    assert "id" in user


def test_update_user_put():
    payload = {
        "name": "Ben",
        "email": "ben123@mail.com",
        "username": "ben123"
    }

    response = requests.put("https://jsonplaceholder.typicode.com/users/1", json = payload)

    user = response.json()
    assert response.status_code == 200
    assert user["name"] == payload["name"]
    assert user["email"] == payload["email"]


def test_update_user_patch():
    payload = {
        "email": "ben321@mail.com"
    }
    response = requests.patch("https://jsonplaceholder.typicode.com/users/1", json = payload)

    user = response.json()
    assert response.status_code == 200
    assert user["email"] == payload["email"]


def test_user_delete():
    response = requests.delete("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200
    assert response.text == "{}"