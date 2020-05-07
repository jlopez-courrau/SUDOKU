"""TODO"""
from flask import Flask
from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  # pylint: disable=import-error

from .config import Config

db = SQLAlchemy()


def create_app():
    """TODO"""
    app = Flask(__name__, static_folder="../static")

    app.config.from_object(Config)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from .routes import routes as main_blueprint

    app.register_blueprint(main_blueprint)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        """Load user by user_id and not by id"""
        return User.query.get(int(user_id))

    return app
