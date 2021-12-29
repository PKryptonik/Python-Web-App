from flask import Blueprint, render_template, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db
from .models import User
import time

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method =='POST':
        validation_errors = {}
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        
        if not username:
            validation_errors['username_error'] = 'A username is required'
        if not password:
            validation_errors['password_error'] = 'A password is required'
        if not len(validation_errors):
            if user:
                if check_password_hash(user.password, password):
                    flash('successfully logged in', category='success')
                    login_user(user, remember=True)
                return redirect(url_for('views.home'))
        else:
            for message in validation_errors.values():
                flash(message, category='error')
            return redirect(request.path)

    return render_template("login.html")

@auth.route('/logout')
@login_required #makes it so you cant access logout unless logged in. flask magic
def logout():
    logout_user()
    flash('logged out', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():


    
    if request.method == 'POST':
        validation_errors = {}
        username = request.form.get('username')
        password1 = request.form.get('password-1')
        password2 = request.form.get('password-2')
        
        user = User.query.filter_by(username=username).first()
        if user:
            validation_errors['username_error'] = 'This Username is already taken'
        if not username:
            validation_errors['username_error'] = 'A username is required'    
        else:
            if len(username) < 4:
                validation_errors['username_error'] = 'Username must be 4 characters or longer'
        if not password1:
            validation_errors['password_error'] = 'A password is required'
        if password1 != password2:
            validation_errors['password_error'] = 'Provided passwords do not match'
        if len(password1) < 4:
            validation_errors['password_error'] = 'Password must be at least 4 characters'
        if not len(validation_errors):
            new_user = User(username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('There were no errors', category='success')
            return redirect(url_for('auth.login'))
        else:
            for message in validation_errors.values():
                flash(message, category='error')
                time.sleep(3)
            return redirect(request.path) #redirect back to the same page

    return render_template("signup.html")
