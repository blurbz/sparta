from sparta.extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    registration_time = db.Column(db.DateTime, default=datetime.utcnow)

    reviews = db.relationship("Review", backref=db.backref(
        "user", lazy="joined"), lazy="select")

    @property
    def serialized(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "registration_time": self.registration_time
        }
