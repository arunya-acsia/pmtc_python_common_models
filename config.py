"""
cofiguration informations
"""
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Configuration class
    """
    SECRET_KEY = 'This-is-a-secret-key'
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    CONFIG_NAME = "dev"
    DEBUG = True
    BASIC_URL = ""

    DB_NAME = '' #DB name
    DB_HOST_NAME = '' # DB host IP
    DB_USER = '' # DB username
    DB_PASSWORD = '' # DB password
    DB_PORT = 5432 # DB post number

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres://{username}:{password}@{host}:{port}/{db_name}' \
        .format(username=DB_USER, password=DB_PASSWORD, host=DB_HOST_NAME, port=DB_PORT, db_name=DB_NAME)
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "You can't see California without Marlon Widgeto's eyes"
    )


class TestingConfig(Config):
    CONFIG_NAME = "qa"
    DEBUG = False
    DB_NAME = ''
    DB_HOST_NAME = ''
    DB_USER = ''
    DB_PASSWORD = ''
    DB_PORT = 5432
    BASIC_URL = ""

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres://{username}:{password}@{host}:{port}/{db_name}'\
        .format(username=DB_USER, password=DB_PASSWORD, host=DB_HOST_NAME, port=DB_PORT, db_name=DB_NAME)
    SECRET_KEY = os.getenv("TEST_SECRET_KEY", "Thanos did nothing wrong")
