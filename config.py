import os


class Config:
    """
    General parent configurations
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    SIMPLEMDE_JS_IIFE = True
    SIMPLE_USE_CDN = True

    @staticmethod
    def init_app(app):
        app


class ProdConfig(Config):
    """
    Child configurations with the Config passed in as a class.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    """
    Child configurations with the Config passed in as a class.
    To test out database relationship.
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jared:12345@localhost/pitch2'


class DevConfig(Config):
    """
    Child configurations with the Config passed in as a class.
    """
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jared:12345@localhost/pitch2'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
