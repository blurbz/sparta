from extensions import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(512), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    registration_time = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialized(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "registration_time": self.registration_time
        }
