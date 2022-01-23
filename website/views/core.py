from flask import Blueprint, render_template
from flask.helpers import url_for
from flask_login import login_required
from werkzeug.utils import redirect


core = Blueprint('core', __name__)


@core.route('/')
def root_view():
    return redirect(url_for('notes.list'))


@core.route('/notifications')
@login_required
def notifications():
    return render_template('notifications.html')
