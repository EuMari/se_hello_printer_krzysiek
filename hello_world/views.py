from hello_world import app
from formater import get_formatted
from formater import SUPPORTED, PLAIN
from flask import request, render_template, flash, redirect, url_for
from hello_world.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from hello_world.models import User


moje_imie = "Krzysiek"
msg = "Aplikacja testowa!"


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bolek'}
    return render_template('index.html', title='Projekt', user=user)


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
        return redirect(url_for('index'))
    return render_template('login.html', title='Logowanie', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
