import trace
from flask import Blueprint, jsonify, request
import requests
import traceback

search_bp = Blueprint("search", __name__)

KEY = "AIzaSyAgIrCcfsBrr_dxVHYUlPyGIrOc3pZlAeE"


def get_books(query):
    try:
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
