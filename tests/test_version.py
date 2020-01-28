"""
Test the "/" route of the app
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import

from test_fixture_setup import client


def test_version(client):
    """
    Get the value from the "/" route of the app and compare it to the expected result
    """
    result = client.get("/version")
    assert result.status_code == 200
    assert b'Version' in result.data
    result = client.get("/version?format=json")
    assert result.status_code == 200
    assert b'Version' in result.data
    result = client.get("/version?format=foo")
    assert result.status_code == 400
    assert b'Bad Request' in result.data
