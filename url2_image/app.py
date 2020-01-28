"""
Main file for the url2_image app
"""
import sys
import os
import pathlib
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# pylint: disable=invalid-name
app = Flask(__name__)

VERSION = "v0.1"


limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["2 per minute", "1 per second"],
)

if os.environ.get("FLASK_DEBUG") is not None:
    limiter.enabled = False

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
    req_format = request.args.get("format")
    sha = ""
    branch = ""
    print(f"Path: {pathlib.Path().absolute()}")
    with open(".git-commit") as f:
        for line in f:
            sha = line

    with open(".git-branch") as f:
        for line in f:
            branch = line
    if req_format == "json":
        response = {}
        response['Version'] = VERSION
        response['Hash'] = sha
        response['Branch'] = branch
        return jsonify(response)
    elif req_format == None:
        return f'Version: {VERSION} - Git Hash: {sha} branch: {branch}'
    else:
        return "Bad Request", 400


if __name__ == "__main__":
    app.run(host='0.0.0.0')
# pylint: enable=invalid-name
