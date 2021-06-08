from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """ User model """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    transactions = db.relationship('Transaction', secondary='users_transactions', backref='user')

    @classmethod
    def register(cls, username, password):
        """ Register a user with hashed password and return the user """
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode('utf8')
        return cls(username=username, password=hashed_utf8)

    @classmethod
    def authenticate(cls, username, password):
        """ check if the user requesting authentication is valid... 
        Return user if valid, else return false """
        user = User.query.filter_by(username=username).first()
        # if the user exists and the password hash check passes:
        # compare database password and hash result of passed in password
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

class Transaction(db.Model):
    """ Transaction model """
    """ One user can have many transactions """
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    category = db.Column(db.Text, nullable=False)

    def serialize(self):
        """ serialize the transaction """
        return {
            'id': self.id,
            'location': self.location,
            'amount': self.amount,
            'date': self.date,
            'category': self.category
        }

class UserTransaction(db.Model):
    """ all of a User's transactions """
    __tablename__ = 'users_transactions'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), primary_key=True)

# class UserCategory(db.Model):
#     """ A specific user's categories """
#     __tablename__ = 'users_categories'
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
#     category = db.Column(db.Integer, db.ForeignKey('transactions.category'), primary_key=True)



