from celery import Celery
from ihome.tasks import config


# 定义celery对象
app = Celery("ihome")

# 引入配置信息
app.config_from_object(config)

# 自动搜寻异步任务
app.autodiscover_tasks(["ihome.tasks.sms"])