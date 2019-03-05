class Config:
    # 公共的配置
    DEBUG = False
    Test = False
    Online = False
    SECRET_KEY = "djhsdfjkashkwn"
    # SESSION_TYPE = "redis"
    SESSION_KEY_PREFIX = "myapp:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DebugConofig(Config):
    DEBUG = True
    # SESSION_REDIS = StrictRedis(host="127.0.0.1", db=5)

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 数据库配置
    DATABASE = {
        "engine": "pymysql",
        "backend": "mysql",
        'user': 'root',
        'pwd': 'root',
        "host": "127.0.0.1",
        "port": 3306,
        "db": 'test'
    }

    # SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

conf = {
    "debug": DebugConofig,
    # "test": TestConfig,
    # "online": OnlineConfig
}

# SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
#     DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
# )
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 5