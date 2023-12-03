from flask import Blueprint, request, jsonify
from flask_login import logout_user, current_user

from models.users import User
from helpers import login_and_increment_visits
from main import constants


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/signup", methods=["POST"])
def signup():
    """Register a new user.
    Request body structure:
        {
            "email": "string",
            "password" "string"
        }
    If the user with the given email already exists -> response:
        {
            "error": "User already exists"
        }
    If the user was successfully created -> response:
        {
            "success": "User created"
        }
    """
    data = request.get_json()
    user_data = dict(email=data["email"], password=data["password"])
    existing_user = User.query.filter_by(email=user_data["email"]).first()
    if existing_user:
        return (
            jsonify({"error": constants.USER_ALREADY_EXISTS}),
            400,
        )  # Do not explicitly pass error reason to avoid leaking sensitive information
    user = User.create(**user_data)
    login_and_increment_visits(user)
    return jsonify({"success": constants.USER_CREATED}), 201


@bp.route("/login", methods=["POST"])
def login():
    """Log in a user.
    Request body structure:
        {
            "email": "string",
            "password" "string"
        }
    If the user does not exist -> response:
        {
            "error": "User does not exist"
        }
    If the user exists but the password is incorrect -> response:
        {
            "error": "Invalid credentials"
        }
    If the user was successfully logged in -> response:
        {
            "success": "User logged in"
        }
    """
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        return jsonify({"error": constants.USER_DOES_NOT_EXIST}), 400
    if user.password != data["password"]:
        return jsonify({"error": constants.INVALID_CREDENTIALS_PROVIDED}), 400
    login_and_increment_visits(user)
    return jsonify({"success": constants.USER_LOGGED_IN}), 200


@bp.route("/logout", methods=["POST"])
def logout():
    """Log out the current user.
    If the user was logged in -> response:
        {
            "success": "User logged out"
        }
    If the user was not logged in -> response:
        {
            "error": "User was not logged in"
        }
    """
    if current_user.is_authenticated:
        logout_user()
        return jsonify({"success": constants.USER_LOGGED_OUT}), 200
    return jsonify({"error": constants.USER_WAS_NOT_LOGGED_IN}), 400
