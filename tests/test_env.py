import pytest

from url2_image.env import JWT_SECRET_KEY,JWT_USER,JWT_PASSWORD,FLASK_DEBUG

def test_env():
    assert JWT_SECRET_KEY == "Dg6kPHk8P7G9Zu2JtbgnXe"
    assert JWT_USER == "user"
    assert JWT_PASSWORD == "url2image"
    assert FLASK_DEBUG == False