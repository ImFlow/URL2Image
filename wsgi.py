"""
WSGI config for the running of the app with gunicorn
"""
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/url2_image/')
from url2_image.app import app

if __name__ == '__main__':
    app.run()
