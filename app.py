from flask import Flask, flash, redirect, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Transaction, UserTransaction
from forms import UserForm, TransactionForm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///budgetapp')
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
toolbar = DebugToolbarExtension(app)

@app.route('/')
def show_homepage():
    """ display main landing page """
    return render_template('homepage.html')

# Register, login and logout routes are to be implemented after
# all of the main functionality is built
@app.route('/register', methods=['GET','POST'])
def user_registration():
    """ Register a user and log them in """
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.username.password
        try:
            new_user = User.register(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
        except:
            flash('Username already exists!')
            return redirect('/register')
        session['username'] = username
        flash(f'Welcome, {username}!')
        return redirect('/transactions')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def user_login():
    """ Login page if you are registered """
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.username.password
        try:
            user = User.authenticate(username=username, password=password)
            db.session.add(user)
            db.session.commit()
        except:
            flash('Something went wrong. Are you registered?')
            return redirect('/login')
        session['username'] = username
        flash(f'Welcome back, {username}')
        return redirect('/transactions')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    """ log out a user and redirect to the home page """

@app.route('/transactions')
def show_user_transactions():
    """ Query the API and show all of a user's transactions """
    pass

@app.route('/transactions/new', methods=['GET','POST'])
def add_new_transaction():
    """ render new transaction form """
    form = TransactionForm()
    if form.validate_on_submit():
        pass
    else:
        return render_template('new_transaction.html', form=form)


@app.route('/transactions/<int:transaction_id>')
def show_transaction_detail(transaction_id):
    """ show specifics of a user's transaction """
    pass


