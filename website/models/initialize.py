from flask import Flask

from .db import db
from .user import User
from .note import Note


def initialize_starting_data(app: Flask):
    with app.app_context():
        if db.session.query(User).count() == 0:
            user = User(username='test')
            user.set_password('test')

            note = Note(data='Yay, this is a test note from the system!')
            user.notes.append(note)

            db.session.add(user)
            db.session.commit()
