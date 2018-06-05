from flask import render_template, request, redirect, url_for, abort
from . import main

from ..models import User, Pitch, Comment
from flask_login import login_required, current_user
from .. import db, photos


@main.route('/')
def index():
    '''
    Function that renders the index.html and its functions
    '''
    pitches = Pitch.query.all()

    return render_template('index.html', pitches=pitches)
