# Imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy() # ORM
migrate = Migrate() # DB migrations
cors = CORS() # CORS policy
