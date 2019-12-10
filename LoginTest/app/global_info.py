def _init_user():
    global _global_dict_user
    _global_dict_user = {}


def set_value_user(name, value):
    _global_dict_user[name] = value


def get_value_user(name, defValue = None):
    try:
        return _global_dict_user[name]
    except KeyError:
        return defValue


def _init_topData():
    global _global_list_topData
    _global_list_topData = []


def set_value_topData(value):
    _global_list_topData.append(value)


def get_value_topData(defValue = None):
    try:
        return _global_list_topData
    except KeyError:
        return defValue


def del_value_topData(value):
    try:
        _global_list_topData.remove(value)
    except ValueError:
        print("topData has been delete")


def value_existed(value):
    if value in _global_list_topData:
        return True
    else:
        return False

def _init_beforeData(list):
    global _global_list_beforeData
    _global_list_beforeData = list


def get_value_beforeData(defValue = None):
    try:
        return _global_list_beforeData
    except KeyError:
        return defValue


def del_value_beforeData(value):
    try:
        _global_list_beforeData.remove(value)
    except ValueError:
        print("beforeData has been delete")


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


def get_today_data_index():
    id = next(it)
    return id