from pathlib import Path
from enum import unique
from flask import Flask
from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


def initialize_database(app: Flask):
    """Initialize the application database. It is contained in the Flask instance directory"""
    DB_NAME = 'web_app.sqlite'
    db_path = Path(app.instance_path) / 'db'
    db_path.mkdir(exist_ok=True)
    db_path_full = db_path / DB_NAME

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path_full}'
    db.init_app(app)
    db.create_all(app=app)



class Note_user_link(db.Model): #association
    __tablename__ = 'note_user_link'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False, index=True)



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(8000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    users = db.relationship('User', secondary=Note_user_link.__table__, back_populates='notes')



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(50))
    notes = db.relationship('Note', secondary=Note_user_link.__table__, back_populates='users')

    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check provided password against this user's stored one."""
        return check_password_hash(self.password, password)


def flask_user_control(app: Flask): #unsure of the "(app: Flask)" portions use, does this let this function be used during the initialization of the app?
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
     
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


def initialize_database(app: Flask):
    """Initialize the application database. It is contained in the Flask instance directory"""
    DB_NAME = 'web_app.sqlite'
    db_path = Path(app.instance_path) / 'db'
    db_path.mkdir(exist_ok=True)
    db_path_full = db_path / DB_NAME

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path_full}'
    db.init_app(app)
    db.create_all(app=app)

    with app.app_context():
        if db.session.query(User).count() == 0:
            user = User(username='test')
            user.set_password('test')

            note = Note(data='Yay, this is a test note from the system!')
            user.notes.append(note)

            db.session.add(user)
            db.session.commit()
