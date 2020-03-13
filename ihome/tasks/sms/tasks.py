from ihome.tasks.main import app
from ihome.libs.yuntongxun.sms import CCP



@app.task
def send_template_sms(to, datas, temp_id):
    """发送短信的异步任务"""
    ccp = CCP()
    ret = ccp.send_template_sms(to, datas, temp_id)
    return ret





