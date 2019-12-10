from flask import jsonify
from app.api import bp
from app import db
from SQL_models import Event
from flask import request
from app.api.getManyData import repeated_data_detail


'''
json数据格式如下
    show_data = {
        'code': 0,
        'msg': 'OK',
        'data': {
            'data': [{
                '统计时间': 'yyyy-mm-dd hh:mm:ss',
                '所属区域': 'xx区',
                '所属社区': 'xx社区',
                '问题来源': 'xx来源',
                '处置部门': 'xx部门'
            },...,{}],     # 数组元素不断增加
            'len': 1       # 信息数量
        }
    }
'''
@bp.route('/getMonyDataInfo', methods=['GET', 'POST'])
def show_repeated_data():
    detail_result = {
        'code': 0,
        'msg': 'OK',
        'data': []
    }
    get_data = request.json
    print(get_data)
    if get_data:
        data_index = get_data['所属街道'] + get_data['所属社区'] + get_data['问题类型']\
                     + get_data['问题性质']+get_data['小类名称']
        detail_result['data'] = repeated_data_detail['data']['data_detail'][data_index]
    else:
        detail_result['code'] = 200
        detail_result['msg'] = '信息有误'
    return jsonify(detail_result)
