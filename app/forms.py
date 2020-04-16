from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User

class RegisterationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators = [DataRequired(), Email(), Length(min=5, max=50)])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different username')

    def validate_email(self, email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('That email is taken. Please choose a different email')

    
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email(), Length(min=5, max=50)])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')
    