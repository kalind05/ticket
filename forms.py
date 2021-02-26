from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL

class LoginForm(FlaskForm):
    email = StringField("Enter Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    name = StringField("Enter Name", validators=[DataRequired()])
    phone = StringField("Enter Phone Number", validators=[DataRequired()])
    email = StringField("Enter Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
