from pathlib import Path

from flask import Flask

from . import models


def create_app():
    app = Flask(__name__)
    Path(app.instance_path).mkdir(
        exist_ok=True)  # ensure instance directory exists
    app.config[
        'SECRET_KEY'] = 'Fromwhereyourekneelingitmustseemlikean18caratrunofbadluckTruthisthegamewasriggedfromthestart'

    models.initialize_database(app)

    from .views.core import core
    from .views.auth import auth
    from .views.notes import notes
    from website.lib.template_helpers import configure_helpers

    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(notes, url_prefix='/notes')
    configure_helpers(app)

    models.flask_user_control(app)

    return app
