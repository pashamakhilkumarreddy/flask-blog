# export FLASK_DEBUG=1
# export FLASK_APP=app.py
from app import app
from app.settings import DEBUG

if __name__ == '__main__':
    app.run(debug=DEBUG)
