from app import db
from SQL_models import Event
import datetime


def find_uncompleted():
    '''
    找到所有尚未结伴事件，即10.30事件
    :param info: 待加进all_data的民生信息
    :param datas: 从数据库中取出的所有尚未结办事件信息
    :return: all_data: 数组类型，每个元素是一个民生信息字典
    :return: count: 事件数目
    '''
    all_datas = []
    count = 0
    datas = db.session.query(Event).all()
    for data in datas:
        if data.CREATE_TIME[:10] == '2018-10-30':
            info = {}
            info['统计时间'] = data.CREATE_TIME
            info['所属社区'] = data.COMMUNITY_NAME
            info['问题来源'] = data.EVENT_SRC_NAME
            info['小类名称'] = data.SUB_TYPE_NAME
            info['处置部门'] = data.DISPOSE_UNIT_NAME
            info["所属街道"] = data.STREET_NAME
            info["问题性质"] = data.EVENT_PROPERTY_NAME
            info['问题类型'] = data.EVENT_TYPE_NAME
            info['问题性质名称'] = data.EVENT_PROPERTY_NAME
            all_datas.append(info)
            count += 1
        else:
            pass
    return all_datas, count

def show_type_today():
    today_data = []
    # 将字符串转化为 datetime格式，当未选择时默认今日2018-10-30
    date_today = datetime.datetime.strptime('2018-10-30', "%Y-%m-%d").date()
    datas = db.session.query(Event).all()
    for data in datas:
        # 将字符串转化为 datetime 格式
        date = datetime.datetime.strptime(data.CREATE_TIME[:10], "%Y-%m-%d").date()
        if date.__eq__(date_today):
            today_data.append(data)
    return today_data


statistics_today = show_type_today()

general_data, general_count = find_uncompleted()

