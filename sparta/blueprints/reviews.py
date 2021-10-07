from flask import Blueprint, jsonify, request
from sqlalchemy.orm.exc import NoResultFound
from sparta.extensions import db
from sparta.models.review import Review
from sparta.models.user import User

from sparta.utils import decode_auth_token, is_logged_in

reviews_bp = Blueprint("reviews", __name__)


@reviews_bp.route('/<id>/create', methods=['POST'])
@is_logged_in
def create(id):
    if request.method == "POST":
        data = request.get_json(force=True)
        user_id, _ = decode_auth_token(request.headers.get('Authorization'))
        text = data["text"]

        review = Review(user_id=user_id, book_id=id, text=text)

        try:
            db.session.add(review)
            db.session.commit()
            return jsonify({"message": "Success."})
        except Exception as e:
            print(e)
            return jsonify({"message": "Failed."})


@reviews_bp.route('/<id>/all', methods=['GET'])
def get_all(id):
    if request.method == "GET":
        try:
            reviews = Review.query.filter(Review.book_id == id).all()
            print(reviews[0].book_id)
            return jsonify({"reviews": [review.serialized for review in reviews]})
        except NoResultFound as e:
            print(e)
            return jsonify({"reviews": []})
        except Exception as e:
            print(e)
            return jsonify({"message": "Failed."})


@reviews_bp.route('/user/<id>', methods=['GET'])
def get_user_reviews(id):
    if request.method == 'GET':
        try:
            user = User.query.filter(User.id == id).one()
            reviews = user.reviews

            return jsonify({"reviews": [review.serialized for review in reviews]})
        except Exception as e:
            print(e)
            return jsonify({"message": "Failed"})


@reviews_bp.route('/is_reviewed/<book_id>/<user_id>', methods=["GET"])
@is_logged_in
def get_is_reviewed(book_id, user_id):
    if request.method == "GET":
        try:
            user = User.query.filter(User.id == user_id).one()
            review = Review.query.filter(
                Review.user_id == user.id, Review.book_id == book_id).one()

            return jsonify({"available": True})
        except NoResultFound as e:
            print(e)
            return jsonify({"available": False})
        except Exception as e:
            print(e)
            return jsonify({"message": "Failed."})
