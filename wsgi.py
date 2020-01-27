"""
WSGI config for the running of the app with gunicorn
"""
from url2_image.app import app

if __name__ == '__main__':
    app.run()
