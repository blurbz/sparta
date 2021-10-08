# Imports
from flask import Flask, Blueprint
from sparta.config import config_map
from sparta.extensions import db, migrate, cors
from sparta.blueprints.index import index_bp
from sparta.blueprints.users import users_bp
from sparta.blueprints.search import search_bp
from sparta.blueprints.reviews import reviews_bp

# App factory
def create_app():
    app = Flask(__name__)
    app.config.from_object(config_map.get(app.config["ENV"]))

    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(index_bp)
    api.register_blueprint(users_bp, url_prefix="/users")
    api.register_blueprint(search_bp, url_prefix="/search")
    api.register_blueprint(reviews_bp, url_prefix="/reviews")

    app.register_blueprint(api)
    register_extensions(app)

    return app

# Extension initialisation
def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
