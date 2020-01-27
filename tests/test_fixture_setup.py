import pytest

import pathlib

from URL2Image.app import app

@pytest.fixture
def client():
    client = app(__name__)
    yield client