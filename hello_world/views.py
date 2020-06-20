# -*- coding: utf-8 -*-
from hello_world import app, db
from formater import get_formatted, SUPPORTED, PLAIN
from flask import request, render_template, flash, redirect, url_for
from hello_world.forms import LoginForm, RegistrationForm, EditProfileForm
from hello_world.forms import PostForm, EmptyForm
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
        flash(u'Twój post został opublikowany.')
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, app.config['POST_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Hej!', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


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
            flash(u'Nieprawidłowy login lub hasło.')
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
        flash(u'Zostałeś zarejestrowany. Teraz możesz się zalogować.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Rejestracja', form=form)


# profil
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POST_PER_PAGE'], False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url, form=form)


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
                           form=form)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(u'Nie znaleziono użytkownika: {} '.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash(u'Nie możesz śledzić samego siebie.')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash(u'Obserwujesz użytkownika {}'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))


@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash(u'Nie znaleziono użytkownika: {} '.format(username))
            return redirect(url_for('index'))
        if user == current_user:
            flash(u'Nie możesz przestać śledzić samego siebie.')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash(u'Nie obserwujesz użytkownika {}.'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('index'))


@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POST_PER_PAGE'], False)
    next_url = url_for('explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Odkrywaj!', posts=posts.items,
                           next_url=next_url, prev_url=prev_url)
