from flask import render_template, url_for, flash, redirect, request
from .forms import RegisterationForm, LoginForm
from . import app, bcrypt, db
from .models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print(hashed_pwd)
        user = User(username = form.username.data, email = form.email.data, password = hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created for {form.username.data}!. Please Log In', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next', 'index')
            flash(f'You have been successfully logged in!', 'success')
            return redirect(url_for(next_page))
        flash(f'Login unsuccessfull. Please check your email and password', 'danger')
    return render_template('auth/login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/account')
@login_required
def account():
    return render_template('profile.html')