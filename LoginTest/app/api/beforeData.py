from flask import jsonify
from app.api import bp
from app.General import general_data
from flask import request
from app import global_info as gl

def beforeData_need():
    '''
    :param info: 待加进all_data的民生信息
    :param datas: 从数据库中取出的所有尚未结办事件信息
    :return: all_data: 数组类型，每个元素是一个整理所需数据后的民生信息字典
    :return: count: 事件数目
    '''
    all_datas = []
    count = 0
    for data in general_data:
        info = {}
        info['统计时间'] = data['统计时间']
        info['所属社区'] = data['所属社区']
        info['问题来源'] = data['问题来源']
        info['小类名称'] = data['小类名称']
        info['处置部门'] = data['处置部门']
        # 其余不显示信息
        info['所属街道'] = data['所属街道']
        info['问题类型'] = data['问题类型']
        info['问题性质名称'] = data['问题性质名称']
        all_datas.append(info)
        count += 1
    return all_datas, count

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
show_data_none = {
    'code': 200,
    'msg': '暂无数据',
    'data': {
        'data': [],
        'len': 0
    }
}
show_data = {
    'code': 0,
    'msg': 'OK',
    'data': {
        'data': [],
        'len': 1
    }
}
show_data['data']['data'], show_data['data']['len'] = beforeData_need()
gl._init_beforeData(show_data['data']['data'])


@bp.route('/beforeData', methods=['GET'])
def showBeforedata():
    limit = int(request.args['limit'])
    offset = int(request.args['offset'])
    final_show_data = {
        'code': 0,
        'msg': 'OK',
        'data': {
            'data': [],
            'len': 0
        }
    }
    start_id = offset
    end_id = start_id + limit
    show_data['data']['data'] = gl.get_value_beforeData()
    final_show_data['data']['len'] = len(show_data['data']['data'])
    final_show_data['data']['data'] = show_data['data']['data'][start_id:end_id]
    if final_show_data['data']['data']:
        return jsonify(final_show_data)
    else:
        return jsonify(show_data_none)
