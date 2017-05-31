import os


class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    DEBUG = os.environ.get('DEBUG', True)
    DB_NAME = os.environ.get('DB_NAME', 'weebly')
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASS = os.environ.get('DB_PASS', 'postgres')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
            DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)

