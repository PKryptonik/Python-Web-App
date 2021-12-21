from flask import Blueprint, render_template, request, flash
import time

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
        username = request.form.get('username')
        password1 = request.form.get('password-1')
        password2 = request.form.get('password-2')

        if  len(username) < 2:
            flash('Username must be at least 2 characters long.', category='error')
        elif len(password1) < 4:
            flash('password must be at least 4 characters long.', category='error')
        elif password1 != password2:
            flash('Passwords must match in order to proceed.', category='error')
        else:
            flash('You are all signed up!', category='success')
            #time.sleep(3)
            #@auth.route('/login') 
         
    return render_template("signup.html")