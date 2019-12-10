from flask import jsonify
from app.api import bp
from flask import request
from app import db
from SQL_models import Event
import datetime
from app.General import statistics_today
from app import global_info as gl

def plusOneCounter():
    """
    从1开始递增1计数器
    """
    i = -1
    while True:
        if i == 79:
            return 79
        i += 1
        yield i


it = plusOneCounter()


# 可视化功能2
def find_event_in_community(date_begin: str, date_end: str):
    '''
    这个函数用于展示不同时间范围内的各街道民生事件
    示例一：按月份展示即选择find_event_in_community('2018-10-1','2018-10-30')
    示例二：按季度展示即选择find_event_in_community('2018-06-01','2018-08-30')
    示例三：按当天展示即选择find_event_in_community('2018-10-1','2018-10-1')
    :param date_end:
    :param date_begin:
    :param date:
    :return:
    '''
    statistics = {}
    # 将字符串转化为 datetime格式，当未选择时默认今日2018-10-30
    if not date_begin:
        date_begin = '2018-10-30'
        date_end = '2018-10-30'
    date1 = datetime.datetime.strptime(date_begin, "%Y-%m-%d").date()
    date2 = datetime.datetime.strptime(date_end, "%Y-%m-%d").date()
    date_today = datetime.datetime.strptime('2018-10-30', "%Y-%m-%d").date()
    datas = db.session.query(Event).all()

    for data in datas:
        # 将字符串转化为 datetime 格式
        date = datetime.datetime.strptime(data.CREATE_TIME[:10], "%Y-%m-%d").date()
        if date1.__le__(date) & date2.__ge__(date) & date.__ne__(date_today):
            if statistics.get(eval('data' + '.' + 'EVENT_TYPE_NAME')) is None:
                statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')] = {}
                statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')] = 1
            else:
                if statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')].get(eval('data.STREET_NAME')) is None:
                    statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')] = 1
                else:
                    statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')] = \
                        int(statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')]) + 1
        else:
            continue
    try:
        if date2.__eq__(date_today):
            id = gl.get_today_data_index()
            for i in range(id):
                data = statistics_today[i]
                if statistics.get(eval('data' + '.' + 'EVENT_TYPE_NAME')) is None:
                    statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')] = {}
                    statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')] = 1
                else:
                    if statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')].get(eval('data.STREET_NAME')) is None:
                        statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')] = 1
                    else:
                        statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')] = \
                            int(statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')]) + 1
    except StopIteration:
        for data in statistics_today:
            if statistics.get(eval('data' + '.' + 'EVENT_TYPE_NAME')) is None:
                statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')] = {}
                statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')] = 1
            else:
                if statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')].get(eval('data.STREET_NAME')) is None:
                    statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')] = 1
                else:
                    statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')] = \
                        int(statistics[eval('data' + '.' + 'EVENT_TYPE_NAME')][eval('data.STREET_NAME')]) + 1

    json_output = []
    if statistics:
        if statistics.get('-', False):
            del statistics['-']
            for event in statistics:
                temp = {'name': event, 'type': 'bar', 'stack': 'xx', 'barWidth': 55, 'data': [0, 0, 0, 0, 0, 0]}
                for key, value in statistics[event].items():
                    if key == '坪山街道':
                        temp['data'][0] = value
                    else:
                        if key == '碧岭街道':
                            temp['data'][1] = value
                        else:
                            if key == '龙田街道':
                                temp['data'][2] = value
                            else:
                                if key == '坑梓街道':
                                    temp['data'][3] = value
                                else:
                                    if key == '马峦街道':
                                        temp['data'][4] = value
                                    else:
                                        if key == '石井街道':
                                            temp['data'][5] = value
                json_output.append(temp)
                return json_output
        else:
            for event in statistics:
                temp = {'name': event, 'type': 'bar', 'stack': 'xx', 'barWidth': 55, 'data': [0, 0, 0, 0, 0, 0]}
                for key, value in statistics[event].items():
                    if key == '坪山街道':
                        temp['data'][0] = value
                    else:
                        if key == '碧岭街道':
                            temp['data'][1] = value
                        else:
                            if key == '龙田街道':
                                temp['data'][2] = value
                            else:
                                if key == '坑梓街道':
                                    temp['data'][3] = value
                                else:
                                    if key == '马峦街道':
                                        temp['data'][4] = value
                                    else:
                                        if key == '石井街道':
                                            temp['data'][5] = value
                json_output.append(temp)
            return json_output
    else:
        return []


@bp.route('/getdata_chart2', methods=['GET'])
def chart2_data():
    date_begin = request.args['day1']
    date_end = request.args['day2']
    return jsonify(find_event_in_community(date_begin, date_end))
