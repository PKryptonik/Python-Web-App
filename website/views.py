from flask import Blueprint, render_template, request, jsonify, session
from flask_login import login_required, current_user
from .models import Note, Note_user_link, User, db
from .flashed_messages import flash
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required #makes it so you cant access logout unless logged in. flask magic
def home():
    if request.method == 'POST':
        validation_errors = {}
        note = request.form.get('note')

        if len(note) < 1:
            validation_errors['note_error'] = 'Note cannot be blank'
        if not len(validation_errors):
            new_note = Note(data=note)
            current_user.notes.append(new_note)
            db.session.add(new_note)
            db.session.commit()
            flash('note added', category='success')
        else:
            for message in validation_errors:
                flash(message, category='error' )

    return render_template("home.html")


@views.route('/notifications', methods=['GET'])
@login_required
def notifications():
    return render_template('notifications.html')


@views.route('/delete-note', methods=['POST']) 
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note in current_user.notes:
            current_user.notes.remove(note)
            db.session.flush()
            if not len(note.users):
                db.session.delete(note)
        db.session.commit()
        return jsonify(result=True)
    else:
        return jsonify(result=False)


@views.route('/share-note', methods=['POST'])
def share_note():
    body = request.json

    flash('A user has shared a note with you! Click here to view', category='notification')

    current_user
    target_user = db.session.query(User).filter_by(username=body['username']).scalar()
    if not target_user:
        return jsonify(result=False, message=f"User {body['username']} does not exist")

    note = db.session.query(Note).get(body['noteId'])
    if not note:
        return jsonify(result=False, message='Invalid note id')

    note_copy = Note()
    attrs = ['data']
    for attr in attrs:
        setattr(note_copy, attr, getattr(note, attr))

    target_user.notes.append(note_copy)
    db.session.add(note_copy)
    db.session.commit()

    return jsonify(result=True)

@views.route('/edit-note', methods=['POST'])
@login_required
def edit_note():
    editedNote = json.loads(request.data)
    noteId = editedNote['noteId']
    newNoteData = editedNote['data']
    note = Note.query.get(noteId)
    if note:
        if note in current_user.notes:
            note.data = newNoteData
            db.session.commit()
        return jsonify(result=True)


@views.route('/collab-note', methods=['POST'])
def collab_note():
    body = request.json
    flash('A user has collaborated a note with you! Click here to view', category='notification')

    current_user
    target_user = db.session.query(User).filter_by(username=body['username']).scalar()
    if not target_user:
        return jsonify(result=False, message=f"User {body['username']} does not exist")

    note = db.session.query(Note).get(body['noteId'])
    if not note:
        return jsonify(result=False, message='Invalid note id')
    
    note = note.id
    target_user = target_user.id

    note_collab = Note_user_link(user_id=target_user, note_id=note)
    db.session.add(note_collab)
    db.session.commit()

    return jsonify(result=True)
