"""
Test the "/" route of the app
"""
import pytest

from test_fixture_setup import client


def test_main(client):
    """
    Get the value from the "/" route of the app and compare it to the expected result
    """
    result = client.get("/")
    assert b'Hello World' in result.data
