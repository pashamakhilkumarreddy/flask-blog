from dotenv import load_dotenv
import os
load_dotenv()

DEBUG = bool(os.getenv('DEBUG', 0))

SECRET_KEY = os.getenv('SECREY_KEY')
