from app.api import bp
from flask import jsonify
from app import global_info as gl

top_data_show = {
    'code': 0,
    'msg': 'OK',
    'data': []
}

@bp.route('/getTopData', methods=['GET'])
def showTopData():
    top_data_show['data'] = gl.get_value_topData()
    return jsonify(top_data_show)
