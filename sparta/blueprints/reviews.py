from flask import Blueprint, jsonify, request
from sparta.extensions import db
from sparta.models.review import Review

from sparta.utils import decode_auth_token, is_logged_in

import traceback

reviews_bp = Blueprint("reviews", __name__)


@reviews_bp.route('/<isbn>/create', methods=['POST'])
@is_logged_in
def create(isbn):
    if request.method == "POST":
        data = request.get_json(force=True)
        user_id = decode_auth_token(request.headers.get('Authorization'))
        text = data["text"]

        review = Review(user_id=user_id, book_isbn=isbn, text=text)

        try:
            db.session.add(review)
            db.session.commit()
            return jsonify({"message": "Success."})
        except:
            traceback.print_exc()
            return jsonify({"message": "Failed."})


@reviews_bp.route('/<isbn>/all', methods=['GET'])
def all(isbn):
    if request.method == "GET":
        try:
            reviews = Review.query.filter_by(book_isbn=isbn).all()
            return jsonify({"reviews": [review.serialized for review in reviews]})
        except:
            traceback.print_exc()
            return jsonify({"message": "Failed."})
