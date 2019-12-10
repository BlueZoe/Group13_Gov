from app.api import bp
from flask import jsonify
from flask import request
from app import global_info as gl
from SQL_models import User
from app import db

def get_user_info(username):
    info_list = {}
    check_user = db.session.query(User).filter_by(username=username).first()
    if check_user:
        info_list['username'] = check_user.username
        info_list['real_name'] = check_user.real_name
        info_list['gender'] = check_user.gender
        info_list['email'] = check_user.email
        info_list['telephone'] = check_user.phone
        info_list['department'] = check_user.department
        info_list['worktime'] = check_user.worktime
        return info_list
    else:
        return "message wrong!"


def change_pw(username, pw_old, pw_new):
    check_user = db.session.query(User).filter_by(username=username).first()
    if check_user:
        if check_user.password == pw_old:
            check_user.password = pw_new
            db.session.commit()
            return jsonify(1)
        else:
            return jsonify(0)
    else:
        return jsonify(0)


def change_user_info(phone, email, department):
    username = gl.get_value_user('username')
    check_user = db.session.query(User).filter_by(username=username).first()
    if check_user:
        check_user.email = email
        check_user.phone = phone
        check_user.department = department
        db.session.commit()
    else:
        print("change user_info error")


@bp.route('/user_info', methods=['GET'])
def get_userInfo():
    user = gl.get_value_user('username')
    return jsonify(get_user_info(user))


@bp.route('/user_info_change', methods=['POST'])
def change_userInfo():
    user_info = request.json
    print(user_info)
    phone = user_info['userinfo']['telephone']
    department = user_info['userinfo']['department']
    email = user_info['userinfo']['email']
    change_user_info(phone, email, department)
    return 'right'


@bp.route('/change_password', methods=['POST'])
def change_password():
    old_pw = request.json['oldpass']
    new_pw = request.json['newpass']
    username = gl.get_value_user('username')
    return change_pw(username, old_pw, new_pw)
