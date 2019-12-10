# 数据库建立以及初始化文件
from app import db
from xml.dom.minidom import parse
import xml.dom.minidom
import datetime
import time


class User(db.Model):
    # __bind_key__ = 'user_db'
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(16))
    real_name = db.Column(db.String(16))
    gender = db.Column(db.String(16))
    email = db.Column(db.String(16))
    phone = db.Column(db.String(16))
    department = db.Column(db.String(16))
    worktime = db.Column(db.String(16))
    def __repr__(self):
        return 'name: %s' % self.username


class Event(db.Model):
    # 建立只读数据库连接
    __bind_key__ = 'government_db'
    # 表名
    __tablename__ = 'events'
    # 表示一个字段
    id = db.Column(db.Integer, primary_key=True)
    REPORT_NUM = db.Column(db.Integer)
    EVENT_PROPERTY_NAME = db.Column(db.String)
    EVENT_TYPE_ID = db.Column(db.Integer)
    EVENT_TYPE_NAME = db.Column(db.String)
    EVENT_SRC_NAME = db.Column(db.String)
    DISTRICT_ID = db.Column(db.Integer)
    DISTRICT_NAME = db.Column(db.String)
    COMMUNITY_ID = db.Column(db.String)
    REC_ID = db.Column(db.String)
    STREET_ID = db.Column(db.String)
    OVERTIME_ARCHIVE_NUM = db.Column(db.String)
    OPERATE_NUM = db.Column(db.String)
    DISPOSE_UNIT_ID = db.Column(db.String)
    STREET_NAME = db.Column(db.String)
    CREATE_TIME = db.Column(db.String)
    EVENT_SRC_ID = db.Column(db.String)
    INTIME_TO_ARCHIVE_NUM = db.Column(db.String)
    SUB_TYPE_NAME = db.Column(db.String)
    EVENT_PROPERTY_ID = db.Column(db.String)
    OCCUR_PLACE = db.Column(db.String)
    COMMUNITY_NAME = db.Column(db.String)
    DISPOSE_UNIT_NAME = db.Column(db.String)
    MAIN_TYPE_NAME = db.Column(db.String)
    MAIN_TYPE_ID = db.Column(db.String)
    INTIME_ARCHIVE_NUM = db.Column(db.String)


'''数据库初始添加数据'''

# db.drop_all(bind=None)
# db.create_all(bind=None)
# u1 = User(username='u123', password='123', real_name='张一', gender='男', email='12345678@qq.com',
#           phone='19000133331', department='税务部', worktime='2012-10-6')
# u2 = User(username='m4321', password='4321', real_name='李红', gender='女', email='87654321@qq.com',
#           phone='13331444567', department='人事处', worktime='2006-12-10')
# db.session.add_all([u1, u2])
# db.session.commit()

# db.drop_all(bind='government_db')
# db.create_all(bind='government_db')
#
# dom_tree = xml.dom.minidom.parse('2019 Project Data/坪山区-民生诉求数据_完整版.xml')
# print(dom_tree)
# collection = dom_tree.documentElement
# events_1 = collection.getElementsByTagName('REPORT_NUM')
# events_2 = collection.getElementsByTagName('EVENT_PROPERTY_NAME')
# events_3 = collection.getElementsByTagName('EVENT_TYPE_ID')
# events_4 = collection.getElementsByTagName('EVENT_TYPE_NAME')
# events_5 = collection.getElementsByTagName('EVENT_SRC_NAME')
# events_6 = collection.getElementsByTagName('DISTRICT_ID')
# events_7 = collection.getElementsByTagName('DISTRICT_NAME')
# events_8 = collection.getElementsByTagName('COMMUNITY_ID')
# events_9 = collection.getElementsByTagName('REC_ID')
# events_10 = collection.getElementsByTagName('STREET_ID')
# events_11 = collection.getElementsByTagName('OVERTIME_ARCHIVE_NUM')
# events_12 = collection.getElementsByTagName('OPERATE_NUM')
# events_13 = collection.getElementsByTagName('DISPOSE_UNIT_ID')
# events_14 = collection.getElementsByTagName('STREET_NAME')
# events_15 = collection.getElementsByTagName('CREATE_TIME')
# events_16 = collection.getElementsByTagName('EVENT_SRC_ID')
# events_17 = collection.getElementsByTagName('INTIME_TO_ARCHIVE_NUM')
# events_18 = collection.getElementsByTagName('SUB_TYPE_NAME')
# events_19 = collection.getElementsByTagName('EVENT_PROPERTY_ID')
# events_20 = collection.getElementsByTagName('OCCUR_PLACE')
# events_21 = collection.getElementsByTagName('COMMUNITY_NAME')
# events_22 = collection.getElementsByTagName('DISPOSE_UNIT_NAME')
# events_23 = collection.getElementsByTagName('MAIN_TYPE_NAME')
# events_24 = collection.getElementsByTagName('MAIN_TYPE_ID')
# events_25 = collection.getElementsByTagName('INTIME_ARCHIVE_NUM')
#
# i = 1
# print(events_1[0].childNodes[0].data)
# for i in range(len(events_1)):
#     # if '2018-10-30' not in events_15[i].childNodes[0].data:
#     event_to_add = Event(REPORT_NUM=int(events_1[i].childNodes[0].data),
#                          EVENT_PROPERTY_NAME=(events_2[i].childNodes[0].data),
#                          EVENT_TYPE_ID=(events_3[i].childNodes[0].data),
#                          EVENT_TYPE_NAME=(events_4[i].childNodes[0].data),
#                          EVENT_SRC_NAME=(events_5[i].childNodes[0].data),
#                          DISTRICT_ID=(events_6[i].childNodes[0].data),
#                          DISTRICT_NAME=(events_7[i].childNodes[0].data),
#                          COMMUNITY_ID=(events_8[i].childNodes[0].data),
#                          REC_ID=(events_9[i].childNodes[0].data),
#                          STREET_ID=(events_10[i].childNodes[0].data),
#                          OVERTIME_ARCHIVE_NUM=(events_11[i].childNodes[0].data),
#                          OPERATE_NUM=(events_12[i].childNodes[0].data),
#                          DISPOSE_UNIT_ID=(events_13[i].childNodes[0].data),
#                          STREET_NAME=events_14[i].childNodes[0].data,
#                          CREATE_TIME=(events_15[i].childNodes[0].data),
#                          EVENT_SRC_ID=(events_16[i].childNodes[0].data),
#                          INTIME_TO_ARCHIVE_NUM=(events_17[i].childNodes[0].data),
#                          SUB_TYPE_NAME=(events_18[i].childNodes[0].data),
#                          EVENT_PROPERTY_ID=(events_19[i].childNodes[0].data),
#                          OCCUR_PLACE=(events_20[i].childNodes[0].data),
#                          COMMUNITY_NAME=(events_21[i].childNodes[0].data),
#                          DISPOSE_UNIT_NAME=(events_22[i].childNodes[0].data),
#                          MAIN_TYPE_NAME=(events_23[i].childNodes[0].data),
#                          MAIN_TYPE_ID=(events_24[i].childNodes[0].data),
#                          INTIME_ARCHIVE_NUM=(events_25[i].childNodes[0].data)
#                          )
#     db.session.add(event_to_add)
# db.session.commit()
#
# today = datetime.datetime.strptime('2018-10-30', "%Y-%m-%d").date()
# datas = db.session.query(Event).all()
#
# for data in datas:
#     date = datetime.datetime.strptime(data.CREATE_TIME[:10], "%Y-%m-%d").date()
#     if today.__lt__(date):
#         db.session.delete(data)
#
# def Refresh_Input():
#     for i in range(len(events_1)):
#         if '2018-10-30' in events_15[i].childNodes[0].data:
#             event_to_add = Event(REPORT_NUM=int(events_1[i].childNodes[0].data),
#                                  EVENT_PROPERTY_NAME=(events_2[i].childNodes[0].data),
#                                  EVENT_TYPE_ID=(events_3[i].childNodes[0].data),
#                                  EVENT_TYPE_NAME=(events_4[i].childNodes[0].data),
#                                  EVENT_SRC_NAME=(events_5[i].childNodes[0].data),
#                                  DISTRICT_ID=(events_6[i].childNodes[0].data),
#                                  DISTRICT_NAME=(events_7[i].childNodes[0].data),
#                                  COMMUNITY_ID=(events_8[i].childNodes[0].data),
#                                  REC_ID=(events_9[i].childNodes[0].data),
#                                  STREET_ID=(events_10[i].childNodes[0].data),
#                                  OVERTIME_ARCHIVE_NUM=(events_11[i].childNodes[0].data),
#                                  OPERATE_NUM=(events_12[i].childNodes[0].data),
#                                  DISPOSE_UNIT_ID=(events_13[i].childNodes[0].data),
#                                  STREET_NAME=(events_14[i].childNodes[0].data),
#                                  CREATE_TIME=(events_15[i].childNodes[0].data),
#                                  EVENT_SRC_ID=(events_16[i].childNodes[0].data),
#                                  INTIME_TO_ARCHIVE_NUM=(events_17[i].childNodes[0].data),
#                                  SUB_TYPE_NAME=(events_18[i].childNodes[0].data),
#                                  EVENT_PROPERTY_ID=(events_19[i].childNodes[0].data),
#                                  OCCUR_PLACE=(events_20[i].childNodes[0].data),
#                                  COMMUNITY_NAME=(events_21[i].childNodes[0].data),
#                                  DISPOSE_UNIT_NAME=(events_22[i].childNodes[0].data),
#                                  MAIN_TYPE_NAME=(events_23[i].childNodes[0].data),
#                                  MAIN_TYPE_ID=(events_24[i].childNodes[0].data)
#                                  )
#             db.session.add(event_to_add)
#             db.session.commit()
#             print('import 10-30')
#             yield
#         else:
#             pass
