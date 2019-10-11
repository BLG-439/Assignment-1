from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignInForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Sign in')