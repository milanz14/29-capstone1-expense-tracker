from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Transaction, UserTransaction
from forms import UserForm, TransactionForm
import flask_sqlalchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///budgetapp').replace("://", "ql://", 1)
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
        password = form.password.data
        try:
            new_user = User.register(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            flash(f'Welcome, {username}!')
            return redirect(f'/users/{new_user.id}/transactions')
        except:
            flash('Username already exists!')
            return redirect('/register') 
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def user_login():
    """ Login page if you are registered """
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.authenticate(username=username, password=password)
        if user:
            session['username'] = username
            flash(f'Welcome back, {username}')
            return redirect(f'/users/{user.id}/transactions')
        else:
            form.username.errors= ['Bad password or Incorrect Username']
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    """ log out a user and redirect to the home page """
    session.pop('username')
    flash('Successfully logged out!')
    return redirect('/')

@app.route('/users/<int:user_id>/transactions')
def show_user_homepage(user_id):
    """ show user their home page """
    if 'username' not in session:
        flash('You must be logged in to view this')
        return redirect('/login')
    
    user = User.query.get_or_404(user_id)
    # TODO - find the user's transactions and limit the query to 5 most recent
    return render_template('user_transactions.html', user=user)


@app.route('/users/<int:user_id>/transactions/new', methods=['GET','POST'])
def add_new_transaction_for_user(user_id):
    """ render new transaction form """
    form = TransactionForm()
    user = User.query.get_or_404(user_id)
    if form.validate_on_submit():
        location = form.location.data
        amount = form.amount.data
        date = form.date.data
        category = form.category.data
        details = form.details.data
        new_transaction = Transaction(location=location, amount=amount, date=date, category=category, details=details)
        db.session.add(new_transaction)
        db.session.commit()
        new_user_transaction = UserTransaction(user_id=user_id, transaction_id=new_transaction.id)
        db.session.add(new_user_transaction)
        db.session.commit()
        flash('Added!')
        return redirect(f'/users/{user_id}/transactions')
    else:
        return render_template('new_transaction.html', form=form, user=user)


@app.route('/users/<int:user_id>/transactions/<int:transaction_id>')
def show_transaction_detail(user_id, transaction_id):
    """ show specifics of a user's transaction """
    transaction = Transaction.query.get_or_404(transaction_id)
    user = User.query.get_or_404(user_id)
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = Transaction.query.get_or_404(transaction_id)
        transaction.location = form.location.data
        transaction.amount = form.amount.data
        transaction.date = form.date.data
        transaction.category = form.category.data
        db.session.commit()
        return redirect(f'/users/{user_id}/transactions')
    return render_template('edit_transaction.html', user=user,transaction=transaction, form=form)

@app.route('/api/<int:user_id>/transactions')
def show_user_transaction(user_id):
    """ api route to show all user's transaction """
    user = User.query.get(user_id)
    user_transactions = user.transactions
    user_trans_serialized = [transaction.serialize() for transaction in user_transactions]
    # transactions_limit = user_trans_serialized.order_by(desc('transactions.date')).limit(5)
    return jsonify(transactions=user_trans_serialized)

@app.route('/api/transactions/<int:trans_id>')
def show_specific_transaction(trans_id):
    """ show the details of a specific transaction """
    transaction = Transaction.query.get_or_404(trans_id)
    serialized = transaction.serialize()
    return jsonify(transaction=serialized)

@app.route('/api/<int:user_id>/transactions', methods=['POST'])
def post_transactions(user_id):
    """ add a new transaction for a specific user """
    form = TransactionForm()
    location = form.location.data
    amount = form.amount.data
    date = form.date.data
    category = form.category.data
    details = form.details.data
    new_transaction = Transaction(location=location, amount=amount, date=date, category=category, details=details)
    db.session.add(new_transaction)
    db.session.commit()
    new_user_transaction = UserTransaction(user_id=user_id, transaction_id=new_transaction.id)
    db.session.add(new_user_transaction)
    db.session.commit()
    # return (jsonify(transaction=new_transaction.serialize()), 201)
    return redirect(f'/users/{user_id}/transactions')

@app.route('/api/<int:user_id>/transactions/<int:transaction_id>', methods=['PATCH','POST'])
def update_transaction(user_id, transaction_id):
    """ update a specific transaction """
    form = TransactionForm(form)
    transaction = Transaction.query.get_or_404(transaction_id)
    transaction.location = form.location.data
    transaction.amount = form.amount.data
    transaction.date = form.date.data
    transaction.category = form.category.data
    transaction.details = form.details.data
    db.session.commit()
    # return jsonify(transaction=transaction.serialize())
    return redirect(f'/users/{user_id}/transactions') 

@app.route('/api/<int:user_id>/transactions/<int:transaction_id>/delete', methods=['POST','DELETE'])
def delete_transaction(user_id, transaction_id):
    """ Delete a transaction by id number """
    deleted = Transaction.query.get_or_404(transaction_id)
    try:
        db.session.delete(deleted)
        db.session.commit()
        return redirect(f'/users/{user_id}/transactions')
    except:
        return "There was a problem"
    # return jsonify(message='Removed')
    



