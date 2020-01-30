import os

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY",default="Dg6kPHk8P7G9Zu2JtbgnXe")
JWT_USER = os.getenv("JWT_USER", default="user")
JWT_PASSWORD = os.getenv("JWT_PASSWORD", default="url2image")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", default=False)