from models import db, User, Transaction, UserTransaction
from datetime import datetime
from app import app

db.drop_all()
db.create_all()

# User model creates a user
u1 = User(username='test', password='test')

db.session.add(u1)
db.session.commit()

# Transaction model creates a transaction
t1 = Transaction(location='mcdonalds', amount='7.63', date=datetime.now(), category='dinner')
db.session.add(t1)
db.session.commit()

# UserTransaction model associates a particular transaction with a particular user
ut1 = UserTransaction(user_id=u1.id, transaction_id=t1.id)

db.session.add(ut1)
db.session.commit()
