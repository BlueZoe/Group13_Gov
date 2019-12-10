from flask import jsonify
from app.api import bp
from flask import request, make_response
from app import db
from SQL_models import User
from app import global_info as gl

import sys
gu = set()
'''定义用户信息全局变量'''
gl._init_user()


@bp.route('/login', methods=['POST', 'GET'])
def getuser():
    # 分别定义登陆成功、用户名错误、密码错误三个场景对应返回的json数据
    right = {
        'code': 0,
        'msg': '登陆成功',
        'data': {
            'token': 'asdfghjk'
        }
    }
    wrong = {
        'code': 200,
        'msg': '用户名或密码错误',
        'data': {
            'token': ''
        }
    }
    log_out = {
        'code': 401,
        'msg': '退出登陆',
        'data': {
            'token': ''
        }
    }
    if request.method == 'POST':
        # 获取前端页面传入的数据
        user_info = request.json
        username = user_info.get('username')
        password = user_info.get('password')
        gl.set_value_user('username', username)
        gl.set_value_user('password', password)
        # 查询该用户是否在数据库中
        real_user = db.session.query(User).filter_by(username=username).first()
        # 若在则继续判断密码是否正确
        if real_user:
            # 密码正确
            if real_user.password == password:
                return jsonify(right)
            # 密码错误，告知前端错误
            else:
                return jsonify(wrong)
        # 若用户不在数据库中则告知前端错误
        else:
            return jsonify(wrong)

    if request.method == 'GET':
        reponse = make_response(jsonify(log_out), 401)
        return reponse


@bp.route('/title', methods=['GET'])
def set_title():
    usertype = gl.get_value_user('username')[0]
    if usertype == 'm':
        return jsonify("亲爱的管理员，欢迎来到坪山区大数据分析平台")
    else:
        return jsonify("亲爱的用户，欢迎来到坪山区大数据分析平台")
