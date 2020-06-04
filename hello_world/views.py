from hello_world import app, db
from formater import get_formatted
from formater import SUPPORTED, PLAIN
from flask import request, render_template, flash, redirect, url_for
from hello_world.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from hello_world.models import User
from werkzeug.urls import url_parse


moje_imie = "Krzysiek"
msg = "Aplikacja testowa!"


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Projekt')


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
            flash('Nieprawidlowy login lub haslo')
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
        flash('Zostales zarejestrowany. Teraz mozesz sie zalogowac')
        return redirect(url_for('login'))
    return render_template('register.html', title='Rejestracja', form=form)


# profil 
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)
