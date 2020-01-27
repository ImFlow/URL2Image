"""
Setup fixtures for the tests of the url2_image app.
Since we are not using any DBs the setup is rather simple and (maybe) can omitted
"""

import pytest

from url2_image.app import app

@pytest.fixture
def client():
    """
    Return a configured client for testing
    """

    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()
