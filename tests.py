from unittest import TestCase

from app import app
from models import db, User, Transaction, UserTransaction

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///budgetapp-test';
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

db.drop_all()
db.create_all()

