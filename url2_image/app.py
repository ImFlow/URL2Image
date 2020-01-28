"""
Main file for the url2_image app
"""
from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sys

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

@app.route("/version")
def get_version():
    """
    API endpoint to retrieve version information of the service. 

    """
    format = request.args.get("format")
    print("format foo bar", file=sys.stdout)
    return "format"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
# pylint: enable=invalid-name
