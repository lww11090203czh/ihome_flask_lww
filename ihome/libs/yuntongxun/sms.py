#coding=utf-8

from ihome.libs.yuntongxun.CCPRestSDK import REST


#主帐号
accountSid= '8aaf0708701ea9ab01704d0abb031364'

#主帐号Token
accountToken= '50f16b204ed14fafa2329138e4026434'

#应用Id
appId='8aaf0708701ea9ab01704d0abb69136b'

#请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com'

#请求端口 
serverPort='8883'

#REST版本号
softVersion='2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
  # @param $tempId 模板Id


class CCP(object):
    """自己封装的发送短信辅助类"""
    # 用来保存对象的类属性
    instance = None

    def __new__(cls):
        # 判断CCP这个类有没有已经创建好的对象，如果没有，创建一个对象，并且保存
        if cls.instance is None:
            obj = super(CCP,cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance
        # 如果有，则将保存的对象直接返回


    def send_template_sms(self, to, datas, temp_id):
        """"""
        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        # for k, v in result.items():
        #
        #     if k == 'templateSMS':
        #         for k, s in v.items():
        #             print('%s:%s' % (k, s))
        #     else:
        #         print('%s:%s' % (k, v))

        # statusCode: 000000
        # smsMessageSid: 875c2d9c549e445b8d889a0767a18475
        # dateCreated: 20200216190041
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示发送短信成功
            return 0
        else:
            # 发送失败
            return -1



   
#sendTemplateSMS(手机号码,内容数据,模板Id)


if __name__ == '__main__':
    ccp = CCP()
    ret = ccp.send_template_sms("18301008056",["1234","5"],1)
    print(ret)