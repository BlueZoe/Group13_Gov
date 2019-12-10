from flask import Blueprint

bp = Blueprint('api', __name__)

# 写在最后是为了防止循环导入，login.py等文件也会导入 bp
from app.api import login
from app.api import nowData
from app.api import getTopData
from app.api import getManyData
from app.api import getMonyDataInfo
from app.api import beforeData
from app.api import topData
from app.api import removeData
from app.api import getdata_chart1
from app.api import getdata_chart2
from app.api import getdata_chart3
from app.api import getdata_chart4
from app.api import user_info
