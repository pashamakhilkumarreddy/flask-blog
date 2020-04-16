from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators = [DataRequired(), Email(), Length(min=5, max=50)])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email(), Length(min=5, max=50)])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')
    