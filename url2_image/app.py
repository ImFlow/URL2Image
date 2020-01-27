"""
Main file for the url2_image app
"""
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# pylint: disable=invalid-name
app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["2 per minute", "1 per second"],
)


@app.route("/")
def hello():
    """
    Return "Hello World" as a default for the "/" route
    """
    return "Hello World"


if __name__ == "__main__":
    app.run()
# pylint: enable=invalid-name
