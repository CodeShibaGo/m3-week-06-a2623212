from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required
from sqlalchemy import text

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from urllib.parse import urlsplit


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'Kenny'},
            'body': "Japan's SAKURA is beautiful!"
        },
        {
            'author': {'username': 'Mandy'},
            'body': "My baby is quite, right?"
        }
    ]
    return render_template(template_name_or_list='index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    print(form.password.data)
    if form.validate_on_submit():
        input_name = form.username.data
        sql_fine_user = text(f'SELECT * FROM users WHERE username = "{input_name}"')
        user = db.session.execute(sql_fine_user)
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect username or password')
            return redirect(url_for('index'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template(template_name_or_list='login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜，你現在是一名註冊使用者！')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
