"""
Test the "/getImage" route of the app
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import

from test_fixture_setup import client
from login_utils import log_me_in

def test_get_image_no_credentials(client):
    """
    Get the value from the "/get_image" route of the app and compare it to the expected result
    """
    result = client.get("/getImage")
    assert result.status_code == 401
    assert b'Missing Authorization Header' in result.data

def test_get_image_no_credentials(client):
    """
    Get the value from the "/get_image" route of the app and compare it to the expected result
    """
    header = log_me_in(client)
    result = client.get("/getImage", headers=header)
    assert result.status_code == 400
    assert b'Bad Request' in result.data

def test_get_image(client):
    header = log_me_in(client)
    result = client.get("/getImage?url=google.de", headers=header)
    assert result.status_code == 200
    assert "image" in result.headers.get('Content-Type')

def test_get_image_width(client):
    header = log_me_in(client)
    result = client.get("/getImage?url=google.de&width=1000", headers=header)
    assert result.status_code == 200
    assert "image" in result.headers.get('Content-Type')

def test_get_image_height(client):
    header = log_me_in(client)
    result = client.get("/getImage?url=google.de&height=1000", headers=header)
    assert result.status_code == 200
    assert "image" in result.headers.get('Content-Type')

def test_get_image_width_height(client):
    header = log_me_in(client)
    result = client.get("/getImage?url=google.de&width=1000&height=1000", headers=header)
    assert result.status_code == 200
    assert "image" in result.headers.get('Content-Type')
