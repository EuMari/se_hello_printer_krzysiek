from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, \
TextAreaField # noqa
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
Length # noqa
from hello_world.models import User


class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Haslo', validators=[DataRequired()])
    remember_me = BooleanField('Pamietaj mnie')
    submit = SubmitField('Zaloguj')


class RegistrationForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Haslo', validators=[DataRequired()])
    password2 = PasswordField(
        'Powtorz haslo', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Uzyj innego loginu')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Uzyj innego adresu email')


class EditProfileForm(FlaskForm):
    aboutme = TextAreaField('O mnie', validators=[Length(min=0, max=140)])
    submit = SubmitField('Zapisz')
