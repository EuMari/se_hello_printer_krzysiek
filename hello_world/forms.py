# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms.validators import Length
from hello_world.models import User


class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField(u'Hasło', validators=[DataRequired()])
    remember_me = BooleanField(u'Pamiętaj mnie')
    submit = SubmitField('Zaloguj')


class RegistrationForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(u'Hasło', validators=[DataRequired()])
    password2 = PasswordField(
        u'Powtórz hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(u'Użyj innego loginu')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(u'Użyj innego adresu email')


class EditProfileForm(FlaskForm):
    aboutme = TextAreaField('O mnie', validators=[Length(min=0, max=140)])
    submit = SubmitField('Zapisz')


class PostForm(FlaskForm):
    post = TextAreaField('Co u Ciebie?', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(u'Podziel się')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
