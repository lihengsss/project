from flask import Blueprint ,render_template
from myapp.ext import db
from myapp.models import User
from myapp.models import Recharge

index=Blueprint('index',__name__)

@index.route('/init_tables')
def init_tables():
    try:
        db.create_all()
    except  Exception as e:
        print(e)
    return 'init_table successful!'

@index.route('/user_table')
def user_table():
    try:
        users=User.query.filter_by()
        # print(users.userID,users.Alipay_account,users.balance)
    except  Exception as e:
        print(e)
    return render_template('user_data.html',users=users)

@index.route('/pay_table')
def pay_table():
    try:
        payDatas=Recharge.query.filter()
    except  Exception as e:
        print(e)
    return render_template('pay_data.html',payDatas=payDatas)

