from flask import Blueprint, jsonify, request
from extensions import db
from models.user import User
from argon2 import PasswordHasher

from utils import encode_auth_token

import traceback

users_bp = Blueprint("users", __name__)
hasher = PasswordHasher()


@users_bp.route('/register', methods=["POST"])
def register():
    if request.method == "POST":
        data = request.get_json(force=True)
        username = data['username']
        email = data['email']
        password = data['password']

        key = hasher.hash(password)

        user = User(username=username, password=key, email=email)

        try:
            db.session.add(user)
            db.session.commit()

            return jsonify({"message": "User created successfully"})
        except:
            traceback.print_exc()

            return jsonify({"message": "Registration failed."})
    else:
        return "Method not allowed", 405


@users_bp.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json(force=True)
        username = data['username']
        password = data['password']

        try:
            user = User.query.filter_by(username=username).first()
            if hasher.verify(user.password, password):
                token = encode_auth_token(user.id)
                return jsonify({"token": str(token)})
            else:
                return jsonify({"message": "Login failed."})
        except:
            traceback.print_exc()
            return jsonify({"message": "Login failed."})
