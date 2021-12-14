from flask import (
    Blueprint,
    url_for
)

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"


@views.route('/sign_up')
def signup():
    signup_url = url_for('auth.signup')
    return 'Signup here: {}'.format(signup_url)
