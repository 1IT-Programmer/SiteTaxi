# config.py
import os

class Config(object):
    SECRET_KEY = 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), "transport.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
