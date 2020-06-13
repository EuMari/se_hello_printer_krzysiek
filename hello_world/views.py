# -*- coding: utf-8 -*-
from hello_world import app, db
from formater import get_formatted, SUPPORTED, PLAIN
from flask import request, render_template, flash, redirect, url_for
from hello_world.forms import LoginForm, RegistrationForm, EditProfileForm
from hello_world.forms import PostForm
from flask_login import current_user, login_user, logout_user, login_required
from hello_world.models import User, Post
from werkzeug.urls import url_parse
from datetime import datetime


moje_imie = "Krzysiek"
msg = "Aplikacja testowa!"


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(u'Twój post został opublikowany')
        return redirect(url_for('index'))
    posts = current_user.followed_post().all()
    return render_template('index.html', title='Hej!', form=form, posts=posts)


@app.route('/formaty')
def formaty():
    output = request.args.get('output')
    name = request.args.get('name')
    if not output:
        output = PLAIN
    if not name:
        name = moje_imie
    return get_formatted(msg, name,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(u'Nieprawidłowy login lub hasło')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Logowanie', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


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
        flash(u'Zostałes zarejestrowany. Teraz możesz się zalogowac')
        return redirect(url_for('login'))
        return render_template('register.html', title='Rejestracja', form=form)


# profil
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.aboutme = form.aboutme.data
        db.session.commit()
        flash('Zmiany zapisane')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.aboutme.data = current_user.aboutme
    return render_template('edit_profile.html', title="Edytuj profil",
                            form=form) # noqa


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
