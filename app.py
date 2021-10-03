from flask import Flask
from sparta.config import config_map
from sparta.extensions import db, migrate
from sparta.blueprints.index import index_bp
from sparta.blueprints.users import users_bp
from sparta.blueprints.search import search_bp
from sparta.blueprints.reviews import reviews_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_map.get(app.config["ENV"]))
    app.register_blueprint(index_bp)
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(search_bp, url_prefix="/search")
    app.register_blueprint(reviews_bp, url_prefix="/reviews")
    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
