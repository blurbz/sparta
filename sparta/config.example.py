from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_SECRET = SECRET_KEY
    GOOGLE_BOOKS_KEY = environ.get("GOOGLE_BOOKS_KEY")


class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = ""
    GOOGLE_BOOKS_KEY = ""
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "app.db")


class ProdConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    SECRET_KEY = ""
    GOOGLE_BOOKS_KEY = ""
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "app.db")


config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig,
}
