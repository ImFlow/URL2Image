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
    Main API endpoint
    """
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")
    print("Request ", request)
    d = Xvfb(width=1920, height=1080)
    d.start()
    browser = webdriver.Chrome(chrome_options=chrome_options)
    url = request.args.get('url')
    print("URL:", url)
    browser.get('https://' + url)
    fname = hashlib.md5(url.encode('utf-8')).hexdigest()
    destination = "/tmp_images/" + fname + ".png"
    if browser.save_screenshot(destination):
        print("File saved in the destination filename")
    browser.quit()
    with open(destination, "rb") as f:
        return send_file(io.BytesIO(f.read()), attachment_filename="url.png", mimetype="image/png")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
# pylint: enable=invalid-name
