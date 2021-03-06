# Imports
from flask import current_app as app
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify
import jwt

# JWT checker function
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

# generate JWT token
def encode_auth_token(user_id):
    try:
        with app.app_context():
            payload = {
                "exp": datetime.utcnow() +
                timedelta(minutes=30),
                "iat": datetime.utcnow(),
                "sub": str(user_id),
            }
            return jwt.encode(
                payload,
                app.config["FLASK_SECRET"],
                algorithm="HS256"
            )
    except Exception as e:
        print(user_id, type(user_id))
        print(e)
        return None

# decode JWT token
def decode_auth_token(token):
    try:
        with app.app_context():
            payload = jwt.decode(
                token, app.config["FLASK_SECRET"], algorithms=["HS256"])
            return payload["sub"], payload["exp"]
    except jwt.ExpiredSignatureError:
        return "Signature expired!"
    except jwt.InvalidTokenError as e:
        print(e)
        return "Invalid token!"
