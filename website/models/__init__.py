from pathlib import Path

from flask import Flask
from flask_login import LoginManager

from .db import db
from .initialize import initialize_starting_data
from .user import User


def flask_user_control(
    app: Flask
):  # unsure of the "(app: Flask)" portions use, does this let this function be used during the initialization of the app?
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


def initialize_database(app: Flask):
    """Initialize the application database. It is contained in the Flask instance directory"""
    DB_NAME = 'web_app.sqlite'
    db_path = Path(app.instance_path) / 'db'
    db_path.mkdir(exist_ok=True)
    db_path_full = db_path / DB_NAME

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path_full}'
    db.init_app(app)
    db.create_all(app=app)

    initialize_starting_data(app)

