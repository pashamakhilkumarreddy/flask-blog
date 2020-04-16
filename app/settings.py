from dotenv import load_dotenv
import os
load_dotenv()

DEBUG = bool(os.getenv('DEBUG', 0))

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
