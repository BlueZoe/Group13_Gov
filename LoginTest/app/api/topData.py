from app.api import bp
from flask import jsonify
from flask import request
from app import global_info as gl

gl._init_topData()


@bp.route('/topData', methods=['POST'])
def judge_user():
    username = gl.get_value_user('username')
    # password = gl.get_value_user('password')
    top_data = request.json
    usertype = username[0]
    if usertype == 'm':
        if gl.value_existed(top_data):
            pass
        else:
            gl.set_value_topData(top_data)
        return jsonify({'code': '0'})
    else:
        return jsonify({'code': '1'})
