"""Flask config"""
from os import environ, path, getenv
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = getenv("SECRET_KEY")
    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    SESSION_COOKIE_SECURE = True
    UPLOAD_FOLDER = './static/uploads'
    UPLOAD_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.mov']

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