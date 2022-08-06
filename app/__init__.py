from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
        
    from .api import api
    app.register_blueprint(api, url_prefix='/api/v1')
    

    return app