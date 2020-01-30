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
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from PIL import Image


from url2_image_env import JWT_SECRET_KEY, JWT_USER, JWT_PASSWORD, FLASK_DEBUG, USE_LOGIN, JWT_ACCESS_TOKEN_EXPIRES
from login_util import conditional_decorator

# pylint: disable=invalid-name
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
jwt = JWTManager(app)

VERSION = "v0.1"


limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["2 per minute", "1 per second"],
)

if FLASK_DEBUG:
    limiter.enabled = False


@app.route("/")
@conditional_decorator(jwt_required, USE_LOGIN)
def hello():
    """
    Return "Hello World" as a default for the "/" route
    """
    return "Hello World"


@app.route("/version")
@conditional_decorator(jwt_required, USE_LOGIN)
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
@conditional_decorator(jwt_required, USE_LOGIN)
def get_image():
    """
    Main API endpoint. This takes in an URL and returns an image. 

    Args: 
        url (str): The URL of the target website to be downloaded. 
        width (int): Width of the target image (default=1920)
        height (int): Height of the target image (default=1080)
        format (str): The format of the target image. Either png or jpg (default=png)
        quality (int): JPEG Quality from 0 to 100 (default=60)
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

    req_format = "png"
    if request.args.get('format') is not None: 
        #never trust user input
        wanted_format = request.args.get('format')
        if 'jpg' in wanted_format: 
            req_format = "jpg"

    req_quality = 60
    if request.args.get('quality') is not None:
        req_quality = int(request.args.get('quality'))
    

    if req_format == "jpg": 
        im = Image.open(destination)
        rgb_im = im.convert('RGB')
        destination = "/tmp_images/" + fname + ".jpg"
        rgb_im.save(destination, quality=req_quality, optimize=True, progressive=True)
        with open(destination, "rb") as f:
            return send_file(io.BytesIO(f.read()), attachment_filename="url.jpg", mimetype="image/jpg")

    with open(destination, "rb") as f:
        return send_file(io.BytesIO(f.read()), attachment_filename="url.png", mimetype="image/png")

    return "Image download error", 500


@app.route("/login", methods=['POST'])
def login():
    """
    Login the user using flask_jwt_extented. Accepts json as input and returns an access token. 
    The configuration can be set via environment variables: 

    - JWT_SECRET_KEY: The secret key for JWT

    - JWT_USER: The username of the JWT login. Default: user

    - JWT_PASSWORD: The password for the JWT login. Default: url2image

    - USE_LOGIN: Enables/Disables the requirement for login via JWT. Default: True

    - JWT_ACCESS_TOKEN_EXPIRES: The expiration time (in seconds) of `False` for no expiration of the JWT. Default: False 

    A basic login can be achieved via:: 

        curl -H "Content-Type: application/json" -X POST -d '{"username":"user", "password":"url2image" }' "http://localhost:5000/login"
        {
            "access_token": "TOKEN"
        }

    The authorization is then done in the header::

        curl -H "Authorization: Bearer TOKEN" "http://localhost:5000/getImage?url=google.de"


    Args:

        username: The username to login

        password: The users password

    Returns: 
        The generated access token.
    """
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400

    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != JWT_USER or password != JWT_PASSWORD:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
# pylint: enable=invalid-name
