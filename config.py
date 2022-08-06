import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
            
            
class DockerConfig(ProductionConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DOCKER_DATABASE_URL')
    
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'docker': DockerConfig,
}