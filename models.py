from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """ User model """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

class Transaction(db.Model):
    """ Transaction model """
    """ One user can have many transactions """

    __tabelname__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Datetime, default=datetime.now())



