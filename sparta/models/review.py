from sparta.extensions import db
from datetime import datetime


class Review(db.Model):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialized(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "user": self.user.serialized,
            "text": self.text,
            "created_on": self.created_on
        }
