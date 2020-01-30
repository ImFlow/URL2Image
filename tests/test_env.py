"""
Tests for the environment variables defaults
"""
import pytest

from url2_image.url2_image_env import JWT_SECRET_KEY, JWT_USER, JWT_PASSWORD, FLASK_DEBUG, USE_LOGIN, JWT_ACCESS_TOKEN_EXPIRES


def test_url2_image_env():
    assert JWT_SECRET_KEY == "Dg6kPHk8P7G9Zu2JtbgnXe"
    assert JWT_USER == "user"
    assert JWT_PASSWORD == "url2image"
    assert FLASK_DEBUG == False
    assert USE_LOGIN == True
    assert JWT_ACCESS_TOKEN_EXPIRES == False