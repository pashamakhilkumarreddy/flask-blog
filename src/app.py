from flask import Flask

app = Flask(__name__)

# export FLASK_DEBUG=1
# export FLASK_APP=app.py

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return '<h1>Home</h1>'

if __name__ == '__main__':
    app.run(debug=True)