from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(50))
    notes = db.relationship('Note',
                            secondary='note_user_link',
                            back_populates='users')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check provided password against this user's stored one."""
        return check_password_hash(self.password, password)
