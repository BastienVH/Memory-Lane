"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "Ikk0(ij~hF&T:Ylx|1sr0F.h9~WthA"
    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    SESSION_COOKIE_SECURE = True
    FILE_UPLOADS = './static/uploads'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True
    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    SESSION_COOKIE_SECURE = False