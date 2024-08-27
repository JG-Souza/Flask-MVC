from flask import render_template, flash, redirect, url_for
from app import app, db, lm
from flask_login import login_user, logout_user, current_user
from app.models.tables import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember_me.data)
            flash('Logged in successfully.')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
    return render_template('form_login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))
