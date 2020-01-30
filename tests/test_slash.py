"""
Test the "/" route of the app
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import

from test_fixture_setup import client
from login_utils import log_me_in


def test_main(client):
    """
    Get the value from the "/" route of the app and compare it to the expected result
    """
    header = log_me_in(client)
    result = client.get("/", headers=header)
    assert result.status_code == 200
    assert b'Hello World' in result.data


def test_main_no_credentials(client):
    """
    Get the value from the "/" route of the app and compare it to the expected result
    """
    header = log_me_in(client)
    result = client.get("/")
    assert result.status_code == 401
    assert b'Missing Authorization Header' in result.data
