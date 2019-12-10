from flask import jsonify
from app.api import bp
from flask import request
from app import db
from SQL_models import Event
import datetime
from app.General import statistics_today
from app import global_info as gl


def find_event_state(date_begin: str, date_end: str):
    """
    示例一：
    :param date_begin:
    :param date_end:
    :return:
    """
    # 将字符串转化为 datetime格式，当未选择时默认今日2018-10-30
    if not date_begin:
        date_begin = '2018-10-30'
        date_end = '2018-10-30'
    date1 = datetime.datetime.strptime(date_begin, "%Y-%m-%d").date()
    date2 = datetime.datetime.strptime(date_end, "%Y-%m-%d").date()
    date_today = datetime.datetime.strptime('2018-10-30', "%Y-%m-%d").date()
    datas = db.session.query(Event).all()
    statistics = {}
    value1 = 0
    value2 = 0
    value3 = 0
    for data in datas:
        # 将字符串转化为 datetime 格式
        date = datetime.datetime.strptime(data.CREATE_TIME[:10], "%Y-%m-%d").date()
        if date1.__le__(date) & date2.__ge__(date) & date.__ne__(date_today):
            if data.CREATE_TIME[:10] == '2018-10-30':
                value1 = value1 + 1
                if statistics.get("待结办") is None:
                    statistics["待结办"] = {}
                    statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                else:
                    if statistics["待结办"].get(eval('data' + '.' + 'EVENT_TYPE_NAME')) is None:
                        statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                    else:
                        statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = \
                            int(statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')]) + 1
            elif "1" == data.OVERTIME_ARCHIVE_NUM:
                if '2018-10-30' != data.CREATE_TIME[:10]:
                    value2 = value2 + 1
                    if statistics.get("超期结办") is None:
                        statistics["超期结办"] = {}
                        statistics["超期结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                    else:
                        if statistics["超期结办"].get(eval('data' + '.' + 'EVENT_TYPE_NAME')) is None:
                            statistics["超期结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                        else:
                            statistics["超期结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = \
                                int(statistics["超期结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')]) + 1
            else:
                if "1" == data.INTIME_ARCHIVE_NUM:
                    if data.CREATE_TIME[:10] != '2018-10-30':
                        value3 = value3 + 1
                        if statistics.get("按期结办") is None:
                            statistics["按期结办"] = {}
                            statistics["按期结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                        else:
                            if statistics["按期结办"].get(eval('data' + '.' + 'EVENT_TYPE_NAME')) is None:
                                statistics["按期结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                            else:
                                statistics["按期结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = \
                                    int(statistics["按期结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')]) + 1

    try:
        if date2.__eq__(date_today):
            id = gl.get_today_data_index()
            for i in range(id):
                data = statistics_today[i]
                if data.CREATE_TIME[:10] == '2018-10-30':
                    value1 = value1 + 1
                    if statistics.get("待结办") is None:
                        statistics["待结办"] = {}
                        statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                    else:
                        if statistics["待结办"].get(eval('data' + '.' + 'EVENT_TYPE_NAME')) is None:
                            statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                        else:
                            statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = \
                                int(statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')]) + 1
    except StopIteration:
        for data in statistics_today:
            if data.CREATE_TIME[:10] == '2018-10-30':
                value1 = value1 + 1
                if statistics.get("待结办") is None:
                    statistics["待结办"] = {}
                    statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                else:
                    if statistics["待结办"].get(eval('data' + '.' + 'EVENT_TYPE_NAME')) is None:
                        statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = 1
                    else:
                        statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')] = \
                            int(statistics["待结办"][eval('data' + '.' + 'EVENT_TYPE_NAME')]) + 1

    json_output = []
    if statistics:
        temp_data = []
        temp1 = {'value': value1, 'name': '待结办'}
        temp3 = {'value': value3, 'name': '按期结办'}
        temp2 = {'value': value2, 'name': '超期结办'}
        temp_data.append(temp1)
        temp_data.append(temp3)
        temp_data.append(temp2)
        json_output.append(temp_data)
        temp_data1 = []
        temp_data2 = []
        temp_data3 = []
        for state in statistics:
            if state is "待结办":
                for key, value in statistics[state].items():
                    temp = {'value': value, 'name': key}
                    temp_data1.append(temp)
            elif state is '按期结办':
                for key, value in statistics[state].items():
                    temp = {'value': value, 'name': key}
                    temp_data3.append(temp)
            else:
                for key, value in statistics[state].items():
                    temp = {'value': value, 'name': key}
                    temp_data2.append(temp)

        json_output.append(temp_data1)
        json_output.append(temp_data3)
        json_output.append(temp_data2)
        return json_output
    else:
        return []


@bp.route('/getdata_chart4', methods=['GET'])
def chart4_data():
    date_begin = request.args['day1']
    date_end = request.args['day2']
    return jsonify(find_event_state(date_begin, date_end))
