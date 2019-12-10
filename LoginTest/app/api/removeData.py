from app.api import bp
from flask import jsonify
from flask import request
from app import global_info as gl


@bp.route('/removeData', methods=['POST'])
def remove_topdata():
    username = gl.get_value_user('username')
    usertype = username[0]
    data_remove = request.json
    if usertype == 'm':
        gl.del_value_topData(data_remove)
        gl.del_value_beforeData(data_remove)
        return jsonify({'code': '0'})
    else:
        return jsonify({'code': '1'})
