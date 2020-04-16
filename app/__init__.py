from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .settings import DEBUG, SECRET_KEY, SQLALCHEMY_DATABASE_URI
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI or 'sqlite:///blog.db'
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

from . import routes