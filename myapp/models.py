from myapp.ext import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True)
    userID = db.Column(db.INTEGER, unique=True)
    Alipay_account = db.Column(db.String(80), nullable=False)
    balance=db.Column(db.FLOAT)

class Recharge(db.Model):
    __tablename = 'recharge'
    id = db.Column(db.INTEGER, primary_key=True)
    userID = db.Column(db.INTEGER,unique=True)
    recharge_account = db.Column(db.String(80),nullable=False)
    recharge_amount = db.Column(db.FLOAT)
    user = db.Column(db.ForeignKey('user.id'))