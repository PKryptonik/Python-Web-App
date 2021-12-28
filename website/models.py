from pathlib import Path

from enum import unique
from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


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


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(8000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #"one to many" parent to many children


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(50))
    notes = db.relationship('Note')
