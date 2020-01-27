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
    myclient = app(__name__)
    yield myclient
