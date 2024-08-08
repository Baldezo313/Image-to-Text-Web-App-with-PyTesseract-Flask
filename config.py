import os
from os import environ

class Config(object):
    DEBUG = False
    TESTING = False
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    SECRET_KEY = 'first-coding-job'
    
    UPLOADS = "C:/Users/balde/OneDrive/Bureau/DA_DS/FASTAPI/Image to Text Web App with PyTesseract & Flask/app/static/uploads"
    
    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None
    

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    
class DebugConfig(Config):
    DEBUG =  False