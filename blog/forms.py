from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from blog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[
                           DataRequired(), Length(min=4, max=20)])
    email = StringField('email', validators=[DataRequired(), Email(
        message='Please enter correct email address')])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[
                                     DataRequired(), EqualTo('password', message='password must be match')])
    

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('this username already exists')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('this email already exists')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[
                           DataRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
