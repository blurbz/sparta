from flask import Blueprint, jsonify, request, current_app as app
import requests
import traceback

search_bp = Blueprint("search", __name__)


def get_books(query):
    try:
        with app.app_context():
            KEY = app.config["GOOGLE_BOOKS_KEY"]
            r = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q={query}&key={KEY}")

            books = r.json()

            return books['items']
    except:
        traceback.print_exc()
        return []


@search_bp.route('/<title>', methods=['GET'])
def search(title):
    if request.method == "GET":
        try:
            books = get_books(title)
            return jsonify({"books": books})
        except:
            return jsonify({"message": "Failed"})
