from flask import Blueprint, jsonify, request
from sparta.extensions import db
from sparta.models.user import User
from argon2 import PasswordHasher

from sparta.utils import decode_auth_token, encode_auth_token

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

            token = encode_auth_token(str(user.id))
            print(token)
            _, expires_at = decode_auth_token(token)
            print(expires_at)
            return jsonify({"message": "User created successfully", "token": token, "userInfo": {'email': user.email}, "expiresAt": expires_at})
        except Exception as e:
            print(e)
            return jsonify({"message": "Registration failed."}), 401
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
                token, _ = encode_auth_token(str(user.id))
                _, expires_at = decode_auth_token(token)
                return jsonify({"message": "Login successful.", "token": token, "userInfo": {'email': user.email}, "expiresAt": expires_at}), 200
            else:
                return jsonify({"message": "Login failed."}), 401
        except Exception as e:
            print(e)
            return jsonify({"message": "Login failed."}), 401
