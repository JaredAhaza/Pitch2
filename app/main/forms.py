from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    body = TextAreaField('Enter your comment here', validators=[Required()])
    author = StringField('Author', validators=[Required()])
    category = RadioField('Pick Category',choices=[('business', 'business'),('wired', 'wired')],validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')


class Vote(FlaskForm):
    rating = RadioField('Do you like this Pitch',choices=[('upvote', 'upvote'),('downvote', 'downvote')],validators=[Required()])
