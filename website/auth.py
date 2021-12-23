from flask import Blueprint, render_template, request, flash
import time
from flask.helpers import url_for
from werkzeug.utils import redirect

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if request.method == 'POST':
        validation_errors = {}

        username = request.form.get('username')
        password1 = request.form.get('password-1')
        password2 = request.form.get('password-2')

        if not username:
            validation_errors['username'] = 'A username is required'
        else:
            if len(username) <4:
                validation_errors['username'] = 'Username must be 4 characters or longer'

        if not password1:
            validation_errors['password'] = 'A password is required'

        if password1 != password2:
            validation_errors['password'] = 'Provided passwords do not match'
        if len(password1) < 4:
            validation_errors['password'] = 'Password must be at least 4 characters'

        if not len(validation_errors):
            flash('There were no errors', category='success')
            return redirect(url_for('auth.login'))
        else:
            for message in validation_errors.values():
                flash(message, category='error')
                time.sleep(3)
                return redirect(request.path) #redirect back to the same page

    return render_template("signup.html")