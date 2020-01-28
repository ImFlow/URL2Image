"""
Main file for the url2_image app
"""
import os
import io
import pathlib
import hashlib
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from xvfbwrapper import Xvfb
from flask import Flask, request, jsonify, send_file
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

    Example: 
        The Api endpoint can be queried as follows:: 

            $ curl "localhost:5000/version"
            $ curl "localhost:5000/version?format=json"

    Args: 
        format (str): (Optional) when format=json a json object is returned
    Returns: 
        Version information of the service either as plaintext or json. Information contains version number, git hash (one commit behind) and git branch.
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
    return "Bad Request", 400


@app.route("/getImage")
def get_image():
    """
    Main API endpoint. This takes in an URL and returns an image. 

    Args: 
        url (str): The URL of the target website to be downloaded. 
        width (int): Width of the target image (default=1920)
        height (int): Height of the target image (default=1080)
    Returns: 
        A bytestream containing the downloaded website as image
    """
    req_url = request.args.get('url')
    if req_url is None:
        return "Bad Request", 400

    req_width = 1920
    if request.args.get('width') is not None:
        req_width = int(request.args.get('width'))

    req_height = 1080
    if request.args.get('height') is not None:
        req_height = int(request.args.get('height'))

    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={req_width},{req_height}")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")

    d = Xvfb(width=req_width, height=req_height)
    d.start()
    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get('https://' + req_url)
    fname = hashlib.md5(req_url.encode('utf-8')).hexdigest()
    destination = "/tmp_images/" + fname + ".png"

    if browser.save_screenshot(destination):
        print("File saved in the destination filename")
    browser.quit()

    with open(destination, "rb") as f:
        return send_file(io.BytesIO(f.read()), attachment_filename="url.png", mimetype="image/png")

    return "Image download error", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0')
# pylint: enable=invalid-name
