from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateField

class UserForm(FlaskForm):
    """ simple user form for login or registration """
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class TransactionForm(FlaskForm):
    """ simple form to allow the creating of a new budget transaction """
    location = StringField('Location', validators=[InputRequired()])
    amount = FloatField('Amount', validators=[InputRequired()])
    date = DateField('Date', format="%Y-%m-%d")
    category = StringField('Category', validators=[InputRequired()])