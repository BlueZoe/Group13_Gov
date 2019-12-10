from flask import jsonify
from app.api import bp
from app.General import general_data


def nowData_need():
    """
    找到所有尚未结伴事件，即10.30事件
    :param info: 待加进all_data的民生信息
    :param datas: 从数据库中取出的所有尚未结办事件信息
    :return: all_data: 数组类型，每个元素是一个整理所需数据后的民生信息字典
    """
    all_datas = []
    for data in general_data:
        info = {}
        info['统计时间'] = data['统计时间']
        info['所属街道'] = data['所属街道']
        info['所属社区'] = data['所属社区']
        info['问题来源'] = data['问题来源']
        info['问题类型'] = data['问题类型']
        info['问题性质名称'] = data['问题性质名称']
        info['处置部门'] = data['处置部门']
        info['小类名称'] = data['小类名称']
        all_datas.append(info)
    return all_datas


info = nowData_need()
count = len(info)


def plusOneCounter():
    """
    从1开始递增1计数器
    """
    i = -1
    while True:
        if i == 79:
            i = -1
        i += 1
        yield i


it = plusOneCounter()
it_e = plusOneCounter()

Emergency_List=['雨水井盖','校园周边安全隐患','校园内安全隐患','危险用电','危险山塘、水库','易燃易爆危险品',
                '施工安全隐患','道路和公路交通安全','下水井盖','道路破损']

'''
动态展示消息，前端定时发出请求获取下一条信息

json格式数据如下
    nowdata = {
        'code': 0,
        'msg': '',
        'data': [{
            '统计时间': 'yyyy-mm-dd hh:mm:ss',
            '所属街道': 'xx街道',
            '所属社区': 'xx社区',
            '问题来源': 'xx来源',
            '问题类型': 'xx类型',
            '问题性质名称': 'xx性质',
            '处置部门': 'xx部门'
        }]
    }
'''
@bp.route('/nowData', methods=['GET'])
def dynamicData():
    id = next(it)
    nowdata = {
        'code': 0,
        'msg': 'OK',
        'data': [{
            '统计时间': '',
            '所属街道': '',
            '所属社区': '',
            '问题来源': '',
            '问题类型': '',
            '问题性质名称': '',
            '处置部门': ''
        }]
    }
    nowdata['data'][0]['统计时间'] = info[id]['统计时间']
    nowdata['data'][0]['所属街道'] = info[id]['所属街道']
    nowdata['data'][0]['所属社区'] = info[id]['所属社区']
    nowdata['data'][0]['问题来源'] = info[id]['问题来源']
    nowdata['data'][0]['问题类型'] = info[id]['问题类型']
    nowdata['data'][0]['问题性质名称'] = info[id]['问题性质名称']
    nowdata['data'][0]['处置部门'] = info[id]['处置部门']

    return jsonify(nowdata)


@bp.route('/getEmergency', methods=['GET'])
def emergency_info():
    id = next(it_e)
    emergency_data = {
        'code': 0,
        'data': [{
            '所属街道': '',
            '所属社区': '',
            '小类名称': '',
            '处置部门': ''
        }]
    }
    print(info[id]['小类名称'])
    if info[id]['小类名称'] in Emergency_List:
        emergency_data['code'] = 0
        emergency_data['data'][0]['所属街道'] = info[id]['所属街道']
        emergency_data['data'][0]['所属社区'] = info[id]['所属社区']
        emergency_data['data'][0]['小类名称'] = info[id]['小类名称']
        emergency_data['data'][0]['处置部门'] = info[id]['处置部门']
    else:
        emergency_data['code'] = 200
    return jsonify(emergency_data)
