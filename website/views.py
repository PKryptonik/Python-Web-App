from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required #makes it so you cant access logout unless logged in. flask magic
def home():
    return render_template("home.html")

