from flask import Flask
from myapp import settings
from myapp.views import init_blue
from myapp.ext import init_ext

def create_app(env_name):

    # 实例化app
    app = Flask(__name__)

    #配置
    app.config.from_object(settings.conf.get(env_name,'debug'))

    #实例化第三方
    init_ext(app)

    # 实例化蓝图
    init_blue(app)

    return app