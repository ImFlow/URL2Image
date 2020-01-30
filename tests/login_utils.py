"""
Helper function to log in during testing
"""
from test_fixture_setup import client
import json


def log_me_in(client):
    payload = {
        'username': 'user',
        'password': 'url2image'
    }
    header = {
        "Content-Type": "application/json",
    }
    result = client.post("/login", data=json.dumps(payload), headers=header)
    access_token = json.loads(result.data)["access_token"]

    return_header = {
        "Authorization": f"Bearer {access_token}"
    }

    return return_header
