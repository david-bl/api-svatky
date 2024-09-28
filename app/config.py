import os

from dotenv import load_dotenv


# Load .env file
load_dotenv()


# Base dir of project
basedir = os.path.abspath(os.path.dirname(__file__))

# Config envrioment (prod/dev/test)
config_env = os.getenv('FLASK_ENV', 'dev')

# Secret key
SECRET_KEY = os.environ.get('SECRET_KEY', None)
if SECRET_KEY is None and config_env == 'prod':
    raise ValueError("No SECRET_KEY set for Flask application")


class Config:
    '''Base configuration'''
    SECRET_KEY = SECRET_KEY
    DBFILE = 'db.sqlite'
    TESTING = False
    DEBUG = False


class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    DEBUG = True


config_ = {
    'test': TestConfig,
    'prod': Config,
    'dev': DevelopmentConfig
}.get(config_env, DevelopmentConfig)
