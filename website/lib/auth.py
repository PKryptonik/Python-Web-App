from flask import Flask
from flask_login import LoginManager

from ..models.user import User


def configure_flask_auth(
    app: Flask
):  # unsure of the "(app: Flask)" portions use, does this let this function be used during the initialization of the app?
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
