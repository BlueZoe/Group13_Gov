import os
# from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))


'''数据库配置'''
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_sql_demo.sqlite')  # 默认数据库引擎
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 连接到只读数据库
SQLALCHEMY_BINDS = {
    # 'user_db': 'sqlite:///' + os.path.join(basedir, 'flask_sql_demo.sqlite'),
    'government_db': 'sqlite:///' + os.path.join(basedir, 'test1.db')
}


'''配置后端响应的json格式支持中文显示'''
JSON_AS_ASCII = False


class Config(object):
    pass
