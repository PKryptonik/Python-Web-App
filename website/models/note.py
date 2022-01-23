from sqlalchemy import func

from .db import db


class Note_user_link(db.Model):  #association
    __tablename__ = 'note_user_link'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id'),
                        nullable=False,
                        index=True)
    note_id = db.Column(db.Integer,
                        db.ForeignKey('note.id'),
                        nullable=False,
                        index=True)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(8000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    users = db.relationship('User',
                            secondary=Note_user_link.__table__,
                            back_populates='notes')


