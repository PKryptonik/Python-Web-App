from typing import Optional, Sequence, List
from flask import session
from flask_login import current_user
from .flashed_messages import (
    get_flashed_messages,
    peek_flashed_messages
)


def get_category_class(category):
    category_map = {'error': 'alert-danger', 'success': 'alert-success'}
    return category_map.get(category, 'alert-info')


def configure_helpers(app):
    @app.context_processor
    def utility_processor():
        return dict(get_category_class=get_category_class,
                    peek_flashed_messages=peek_flashed_messages,
                    get_flashed_messages=get_flashed_messages,
                    user=current_user)
