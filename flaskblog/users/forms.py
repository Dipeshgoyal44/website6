#Imports                    
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email,EqualTo, ValidationError
from flaskblog.models import User



#Registration Form
class RegistrationForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email= StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username Taken! Please try again.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is Taken! Please try again.')

#Login Form
class LoginForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password= PasswordField('Password', validators=[DataRequired()])
    remember= BooleanField('Remember Me')
    submit=SubmitField('Login')

#UpdateAccountForm 
class UpdateAccountForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email= StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username Taken! Please try again.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email is Taken! Please try again.')

class RequestResetForm(FlaskForm):
    email= StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
                raise ValidationError('There is no account with that email!. You must register first.')

class ResetPasswordForm(FlaskForm):
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
