from pathlib import Path
from flask import Flask
from flask_login import LoginManager
from flask_login.utils import login_user
from . import models


def create_app():
     app = Flask(__name__)
     Path(app.instance_path).mkdir(exist_ok=True)  # ensure instance directory exists
     app.config['SECRET_KEY'] = 'Fromwhereyourekneelingitmustseemlikean18caratrunofbadluckTruthisthegamewasriggedfromthestart'

     models.initialize_database(app)

     from .views import views
     from .auth import auth
     from .template_helpers import configure_helpers

     app.register_blueprint(views, url_prefix='/')
     app.register_blueprint(auth, url_prefix='/')
     configure_helpers(app)

     models.flask_user_control(app)

     return app
