from models import db, User, Transaction, UserTransaction
from app import app

db.drop_all()
db.create_all()

