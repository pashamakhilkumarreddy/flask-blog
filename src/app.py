from flask import Flask, render_template, url_for
from forms import RegisterationForm, LoginForm
from settings import DEBUG, SECRET_KEY

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

# export FLASK_DEBUG=1
# export FLASK_APP=app.py

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', posts = [])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    form = RegisterationForm()
    return render_template('auth/register.html', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form = form)

if __name__ == '__main__':
    app.run(debug=DEBUG)
