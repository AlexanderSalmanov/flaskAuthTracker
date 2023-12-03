from flask import Blueprint, jsonify, request
from flask_login import current_user

from models.users import AnonymousUser, User
from schemas.user import user_schema
from schemas.anonymous_user import anon_user_schema


bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/authenticated-list", methods=["GET"])
def authenticated_list():
    """List all authenticated users.
    Response structure:
        [
            {
                "id": 1,
                "email": "mail@mail.com",
                "num_visits": 2
            },
            {
                "id": 2,
                "email": "mail2@mail.com",
                "num_visits": 1
            }
        ]
    """
    users = User.query.all()
    return jsonify(user_schema.dump(users, many=True)), 200


@bp.route("/anonymous-list", methods=["GET"])
def anonymous_list():
    """List all anonymous users.
    Response structure:
        [
            {
                "id": 1,
                "ip_address": "122.2.2.2",
                "num_visits": 2
            },
            {
                "id": 2,
                "ip_address": "123.3.3.3",
                "num_visits": 1
            },
            ...
        ]
    """
    users = AnonymousUser.query.all()
    return jsonify(anon_user_schema.dump(users, many=True)), 200


@bp.route("/current-user", methods=["GET"])
def current_user_details():
    """Get the details of the current user.
    Response is either a User or AnonymousUser object.
    If the user is authenticated, the response looks like this:
        {
            "id": 1,
            "email": "some@mail.com",
            "num_visits": 2
        }
    If the user is anonymous, the response looks like this:
        {
            "id": 1,
            "ip_address": "127.0.2.2.1"
        }
    """
    if current_user.is_authenticated:
        return jsonify(user_schema.dump(current_user)), 200
    curr_anon_user = AnonymousUser.query.filter_by(
        ip_address=request.remote_addr
    ).first()
    return jsonify(anon_user_schema.dump(curr_anon_user)), 200
