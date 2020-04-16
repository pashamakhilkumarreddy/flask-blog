from flask import render_template, url_for, flash, redirect
from .forms import RegisterationForm, LoginForm
from . import app

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', posts = [])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account successfully created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('auth/register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been successfully logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Login unsuccessfull. Please check your username and password', 'danger')
    return render_template('auth/login.html', form = form)