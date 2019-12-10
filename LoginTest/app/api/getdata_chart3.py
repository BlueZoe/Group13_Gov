from flask import jsonify
from app.api import bp
from flask import request
from app import db
import datetime
from app import db
from SQL_models import Event
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


# 可视化功能3
def Hot_community_by_date(date_begin: str, date_end: str):
    '''
    这个函数用于展示不同时间段的热点社区（返回排名前六的事件最多的社区）
    示例一：
    示例二：
    :param date_begin:
    :param date_end:
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
            if statistics.get(eval('data.COMMUNITY_NAME')) is None:
                statistics[eval('data.COMMUNITY_NAME')] = 1
            else:
                statistics[eval('data.COMMUNITY_NAME')] = int(statistics[eval('data.COMMUNITY_NAME')]) + 1

    try:
        if date2.__eq__(date_today):
            id = gl.get_today_data_index()
            for i in range(id):
                data = statistics_today[i]
                if statistics.get(eval('data.COMMUNITY_NAME')) is None:
                    statistics[eval('data.COMMUNITY_NAME')] = 1
                else:
                    statistics[eval('data.COMMUNITY_NAME')] = int(statistics[eval('data.COMMUNITY_NAME')]) + 1
    except StopIteration:
        for data in statistics_today:
            if statistics.get(eval('data.COMMUNITY_NAME')) is None:
                statistics[eval('data.COMMUNITY_NAME')] = 1
            else:
                statistics[eval('data.COMMUNITY_NAME')] = int(statistics[eval('data.COMMUNITY_NAME')]) + 1

    final_output = sorted(statistics.items(), key=lambda x: x[1])
    print(final_output)
    for i in final_output:
        if i[1] == '-':
            final_output.remove(i)
        elif i[0] == '-':
            final_output.remove(i)

    if len(final_output) != 0:
        json_output = []
        for each in final_output:
            temp = {'value': each[1], 'name': each[0]}
            json_output.append(temp)
        return json_output
    else:
        return []


@bp.route('/getdata_chart3', methods=['GET'])
def chart3_data():
    date_begin = request.args['day1']
    date_end = request.args['day2']
    return jsonify(Hot_community_by_date(date_begin, date_end))
