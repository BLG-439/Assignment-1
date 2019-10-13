from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignInForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Sign in')


class SendEmailForm(FlaskForm):
    to=StringField('To', validators=[DataRequired()])
    subject=StringField('Subject', validators=[DataRequired()])
    body=StringField('Body', validators=[DataRequired()])
    submit=SubmitField('Submit')


class ReadFolderForm(FlaskForm):
    folder=StringField('Folder Name', validators=[DataRequired()])
    submit=SubmitField('Read')