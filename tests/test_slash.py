def test_slash(client):
    rv = client.get("/")
    assert b'Hello World' in rv.data