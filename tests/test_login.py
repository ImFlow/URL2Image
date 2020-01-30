"""
Tests for the login route
"""

from test_fixture_setup import client
import json


def test_login_no_args(client):
    result = client.post("/login")
    assert result.status_code == 400
    assert "Missing JSON in request" in json.loads(result.data)["msg"]


def test_login_no_user(client):
    payload = {
        'password': 'url2image'
    }
    header = {
        "Content-Type": "application/json",
    }
    result = client.post("/login", data=json.dumps(payload), headers=header)
    assert result.status_code == 400
    assert "Missing username parameter" in json.loads(result.data)["msg"]


def test_login_no_password(client):
    payload = {
        'username': 'user',
    }
    header = {
        "Content-Type": "application/json",
    }
    result = client.post("/login", data=json.dumps(payload), headers=header)
    assert result.status_code == 400
    assert "Missing password parameter" in json.loads(result.data)["msg"]


def test_login_wrong_user(client):
    payload = {
        'username': 'foo',
        'password': 'url2image'
    }
    header = {
        "Content-Type": "application/json",
    }
    result = client.post("/login", data=json.dumps(payload), headers=header)
    assert result.status_code == 401
    assert "Bad username or password" in json.loads(result.data)["msg"]


def test_login_wrong_password(client):
    payload = {
        'username': 'user',
        'password': 'foo'
    }
    header = {
        "Content-Type": "application/json",
    }
    result = client.post("/login", data=json.dumps(payload), headers=header)
    assert result.status_code == 401
    assert "Bad username or password" in json.loads(result.data)["msg"]


def test_login_success(client):
    payload = {
        'username': 'user',
        'password': 'url2image'
    }
    header = {
        "Content-Type": "application/json",
    }
    result = client.post("/login", data=json.dumps(payload), headers=header)
    assert result.status_code == 200
    assert "access_token" in json.loads(result.data)
