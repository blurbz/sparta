from sparta.extensions import db, migrate
from datetime import datetime


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_isbn = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialized(self):
        return {
            "id": self.id,
            "book_isbn": self.book_isbn,
            "user_id": self.user_id,
            "text": self.text,
            "created_on": self.created_on
        }
