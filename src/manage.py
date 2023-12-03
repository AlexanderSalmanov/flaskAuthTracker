import sys

sys.path.append("/code/src")  # noqa

import logging
from flask import Flask
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

from main.blueprints.home import bp as home_bp
from main.blueprints.auth import bp as auth_bp
from main.blueprints.users import bp as users_bp
from models.users import User, AnonymousUser
from settings import config

from extensions import db, login_manager


logging.basicConfig(level=logging.DEBUG)


SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.yaml"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "FlaskAuth OpenAPI"},
)


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
    )
    app.config.from_object(config)
    app.register_blueprint(swaggerui_blueprint)

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    db.init_app(app)
    return app, db


app, db = create_app()
login_manager.init_app(app)
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
