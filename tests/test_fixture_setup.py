"""
Setup fixtures for the tests of the url2_image app.
Since we are not using any DBs the setup is rather simple and (maybe) can omitted
"""
import pytest
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../url2_image/')


@pytest.fixture
def client():
    """
    Return a configured client for testing
    """

    from url2_image.app import app, limiter

    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    limiter.enabled = False
    yield testing_client
    ctx.pop()
