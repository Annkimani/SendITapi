import os

class Config():
    """The Parent Class to set our environments and docstring for Config"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = os.getenv('SECRET_KEY')

class Development(Config):
    """The Development environment"""
    DEBUG = True
    TESTING = True

class Production(Config):
    """The Production environment"""
    DEBUG = False
    TESTING = False

class Testing(Config):
    """The Testing environment"""
    DEBUG = True
    TESTING = True

app_config = {
    "development": Development,
    "production": Production,
    "testing": Testing
    }