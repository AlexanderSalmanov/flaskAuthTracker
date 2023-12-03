from flask import Blueprint, jsonify


bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET"])
def index():
    return jsonify({"data": "Home Page"})
