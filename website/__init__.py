from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
     app = Flask(__name__)
     app.config['SECRET_KEY'] = 'Fromwhereyourekneelingitmustseemlikean18caratrunofbadluckTruthisthegamewasriggedfromthestart'

     from .views import views
     from .auth import auth
     from .template_helpers import configure_helpers

     app.register_blueprint(views, url_prefix='/')
     app.register_blueprint(auth, url_prefix='/')
     configure_helpers(app)

     return app


