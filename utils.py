from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify
import base64
import jwt

private_key = "#~0mPwJ/A8Y(-F~n>,d\]&RapTPAc6i(GYmhGsn8Nff'H3gfq[H3CP_)(2'O$1"


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        jwt = request.headers.get("Authorization")
        print(jwt)
        if decode_auth_token(jwt):
            return f(*args, **kwargs)
        else:
            return jsonify({"error": "Not authorized!"})
    return wrap


def encode_auth_token(user_id):
    try:
        payload = {
            "exp": datetime.utcnow() + timedelta(minutes=30),
            "iat": datetime.utcnow(),
            "sub": str(user_id),
        }
        return jwt.encode(
            payload,
            private_key,
            algorithm="HS256"
        )
    except Exception as e:
        return e


def decode_auth_token(token):
    try:
        payload = jwt.decode(token, private_key, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return "Signature expired!"
    except jwt.InvalidTokenError as e:
        print(e)
        return "Invalid token!"
