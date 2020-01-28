"""
Main file for the url2_image app
"""
from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sys
import os

# pylint: disable=invalid-name
app = Flask(__name__)

VERSION = "v0.1"

if os.environ["FLASK_DEBUG"] != 1:
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
    sha = ""
    branch = ""
    with open("/app/git-commit") as f: 
        for line in f:
            sha = line
    
    with open("/app/git-branch") as f: 
        for line in f:
            branch = line
    return f'Version: {VERSION} - Git Hash: {sha} branch: {branch}'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
# pylint: enable=invalid-name
