"""
Test the "/" route of the app
"""

def test_slash(client):
    """
    Get the value from the "/" route of the app and compare it to the expected result
    """
    result = client.get("/")
    assert b'Hello World' in result.data
