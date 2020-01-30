"""
Test the "/" route of the app
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import

from test_fixture_setup import client
from login_utils import log_me_in

def test_version(client):
    """
    Get the value from the "/" route of the app and compare it to the expected result
    """
    header = log_me_in(client)
    result = client.get("/version", headers=header)
    assert result.status_code == 200
    assert b'Version' in result.data

def test_version_json(client):
    header = log_me_in(client)
    result = client.get("/version?format=json", headers=header)
    assert result.status_code == 200
    assert b'Version' in result.data

def test_version_wrong_format(client):
    header = log_me_in(client)
    result = client.get("/version?format=foo", headers=header)
    assert result.status_code == 400
    assert b'Bad Request' in result.data

def test_version_no_credentials(client):
    result = client.get("/version")
    assert result.status_code == 401
    assert b'Missing Authorization Header' in result.data
