from flask import Flask, config
from config import config
from extensions import db, migrate
from blueprints.index import index_bp
from blueprints.users import users_bp
from blueprints.search import search_bp
from blueprints.reviews import reviews_bp


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    app.register_blueprint(index_bp)
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(search_bp, url_prefix="/search")
    app.register_blueprint(reviews_bp, url_prefix="/reviews")
    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


app = create_app()
