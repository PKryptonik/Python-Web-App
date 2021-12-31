from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, db
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
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('note added', category='success')
        else:
            for message in validation_errors:
                flash(message, category='error' )

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST']) #why is all of this needed?
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})