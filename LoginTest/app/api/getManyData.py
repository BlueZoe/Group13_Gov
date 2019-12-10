from flask import jsonify
from app.api import bp
from app.General import general_data
from flask import request
from app import db
from SQL_models import Event


def ele_num(data):
    return data['num'] > 50


def manyData_need():
    '''
    :param info: 待加进all_data的民生信息
    :param datas: 从数据库中取出的所有尚未结办事件信息
    :return: all_data: 数组类型，每个元素是一个整理所需数据后的民生信息字典
    :return: count: 事件数目
    '''
    all_datas = {}
    # 存储多人投诉信息对应的详情
    info_detail = {}
    count = 0
    datas = db.session.query(Event).all()
    for data in datas:
        info = {}
        data_detail = {}
        info["所属街道"] = data.STREET_NAME
        info["所属社区"] = data.COMMUNITY_NAME
        info["问题性质"] = data.EVENT_PROPERTY_NAME
        info['问题类型'] = data.EVENT_TYPE_NAME
        info['小类名称'] = data.SUB_TYPE_NAME
        # 以5个字符串组合为索引
        info_index = info["所属街道"] + info["所属社区"] + info['问题类型'] + info["问题性质"]+info['小类名称']
        data_detail['小类名称'] = data.SUB_TYPE_NAME
        data_detail['统计时间'] = data.CREATE_TIME
        data_detail['问题来源'] = data.EVENT_SRC_NAME
        data_detail['处置部门'] = data.DISPOSE_UNIT_NAME
        if info_detail.get(info_index) is None:
            count += 1
            info['num'] = 1
            all_datas[info_index] = info
            info_detail[info_index] = []
            info_detail[info_index].append(data_detail)
        else:
            all_datas[info_index]['num'] += 1
            info_detail[info_index].append(data_detail)
    # 字典值转化为列表
    all_datas = list(all_datas.values())
    all_datas = list(filter(ele_num, all_datas))    # 筛选出数量大于50的事件总数
    return all_datas, len(all_datas), info_detail


'''
json数据格式如下
    show_data = {
        'code': 0,
        'msg': 'OK',
        'data': {
            'data': [{
                '所属街道': 'xx街道',
                '所属社区': 'xx社区',
                '问题性质': 'xx性质',
                '事件数量': x
            },...,{}],     # 数组元素不断增加
            'len': 1       # 总的信息数量
        }
    }
'''
repeated_data_none = {
    'code': 200,
    'msg': 'None',
    'data': {
        'data': [],
        'len': 0
    }
}
repeated_data_detail = {
    'code': 0,
    'msg': 'OK',
    'data': {
        'data': [],
        'data_detail': [],
        'len': 0
    }
}
repeated_data_detail['data']['data'], repeated_data_detail['data']['len'],\
    repeated_data_detail['data']['data_detail'] = manyData_need()


@bp.route('/getManyData', methods=['GET', 'POST'])
def find_repeated_data():
    # 获取关于分页的相关信息 limit即每页显示信息数量
    limit = int(request.args['limit'])
    offset = int(request.args['offset'])
    repeated_data_show = {
        'code': 0,
        'msg': 'OK',
        'data': {
            'data': [],
            'len': 0
        }
    }
    start_id = offset
    end_id = start_id + limit
    repeated_data_show['data']['len'] = repeated_data_detail['data']['len']
    repeated_data_show['data']['data'] = repeated_data_detail['data']['data'][start_id:end_id]
    if repeated_data_show['data']['data']:
        return jsonify(repeated_data_show)
    else:
        return jsonify(repeated_data_none)

