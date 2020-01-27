"""
Main file for the url2_image app
"""
from flask import Flask

# pylint: disable=invalid-name
app = Flask(__name__)

@app.route("/")
def hello():
    """
    Return "Hello World" as a default for the "/" route
    """
    return "Hello World"

if __name__ == "__main__":
    app.run()
# pylint: enable=invalid-name
