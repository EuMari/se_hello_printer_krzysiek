from hello_world import app
from formater import get_formatted
from formater import SUPPORTED, PLAIN
from flask import request, render_template
from hello_world.forms import LoginForm


moje_imie = "Krzysiek"
msg = "Aplikacja testowa!"


@app.route('/')
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


@app.route('/index')
def index():
    user = {'username': 'Bolek'}
    return render_template('index.html', title='Projekt', user=user)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Logowanie', form=form)
