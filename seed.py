from models import db, User, Transaction, UserTransaction
from datetime import date
from app import app

db.drop_all()
db.create_all()

# User model creates a user
u1 = User.register(username='test_user', password='test')

db.session.add(u1)
db.session.commit()

# Transaction model creates a transaction
t1 = Transaction(location='mcdonalds', amount=7.63, date=date.today(), category='Dining Out', details='quick bite driving home')
t2 = Transaction(location='foot locker', amount=65.00, date=date.today(), category='Shopping')
t3 = Transaction(location='gym', amount=20.00, date=date.today(), category='Health', details='monthly fee')
t4 = Transaction(location='Esso', amount=26.81, date=date.today(), category='Car Expenses')
t5 = Transaction(location='shoppers', amount=9.99, date=date.today(), category='Health', details='cough medicine')
t6 = Transaction(location='amazon', amount=100.15, date=date.today(), category='Shopping')
db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.add(t4)
db.session.add(t5)
db.session.add(t6)
db.session.commit()

# UserTransaction model associates a particular transaction with a particular user
ut1 = UserTransaction(user_id=u1.id, transaction_id=t1.id)
ut2 = UserTransaction(user_id=u1.id, transaction_id=t2.id)
ut3 = UserTransaction(user_id=u1.id, transaction_id=t3.id)
ut4 = UserTransaction(user_id=u1.id, transaction_id=t4.id)
ut5 = UserTransaction(user_id=u1.id, transaction_id=t5.id)
ut6 = UserTransaction(user_id=u1.id, transaction_id=t6.id)

db.session.add(ut1)
db.session.add(ut2)
db.session.add(ut3)
db.session.add(ut4)
db.session.add(ut5)
db.session.add(ut6)
db.session.commit()
