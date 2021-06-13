from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SelectField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import DateField

category_options = ['Shopping', 'Groceries', 'Dining Out', 'Coffee', 'Rent/Mortgage', 'Utilities', 'Entertainment', 'Car Expenses', 'Health']

class UserForm(FlaskForm):
    """ simple user form for login or registration """
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class TransactionForm(FlaskForm):
    """ simple form to allow the creating of a new budget transaction """
    location = StringField('Location', validators=[InputRequired()])
    amount = FloatField('Amount', validators=[InputRequired()])
    date = DateField('Date', format="%Y-%m-%d")
    category = SelectField('Category', choices=[(cat,cat) for cat in category_options], validators=[InputRequired()])
    details = StringField('Expense Details')