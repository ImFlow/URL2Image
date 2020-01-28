"""
Test the "/" route of the app
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-import

from test_fixture_setup import client


def test_get_image(client):
    """
    Get the value from the "/get_image" route of the app and compare it to the expected result
    """
    result = client.get("/getImage")
    assert result.status_code == 400
    assert b'Bad Request' in result.data
    result = client.get("/getImage?url=google.de")
    assert result.status_code == 200
    assert "image" in result.Headers.get("Content-Type")
