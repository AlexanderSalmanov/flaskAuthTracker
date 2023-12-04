from flask import Blueprint, jsonify, request
from flask_login import current_user

from models.users import AnonymousUser


bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET"])
def index():
    response = {
        "data": "Home Page"
    }
    if current_user.is_authenticated:
        response["user"] = current_user.email
        current_user.increment_visits()
        return jsonify(response), 200
    ip_address = request.remote_addr
    anon_user = AnonymousUser.query.filter_by(ip_address=ip_address).first()
    if not anon_user:
        anon_user = AnonymousUser.create(ip_address=ip_address)
    anon_user.increment_visits()
    response["user"] = anon_user.ip_address
    return jsonify(response), 200

