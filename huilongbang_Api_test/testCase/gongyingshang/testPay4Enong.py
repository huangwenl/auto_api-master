# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"

import unittest, json

from huilongbang_Api_test.common.configHttp import ConfigHttp
from huilongbang_Api_test.common.Log import Log

configHttp = ConfigHttp()
log = Log()


class Pay4Enong(unittest.TestCase):
    def setUp(self):
        configHttp.set_headers(
            {"Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": "HLB/1.0 (iPhone; iOS 11.0.3; Scale/2.00)"})
        configHttp.set_url("/controller/app/users/loginMD5")

    def loginMD5(self, loginphone):
        """登录成功"""
        configHttp.set_data({
            "login": '{"loginphone" : ' + loginphone + ',"appType" : "1","loginpassword" : "14e1b600b1fd579f47433b88e8d85291","appVersion" : "1.0"}'
            , "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone", "osVersion": "11.0.3"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        uid = re_json['results'][0]['userid']
        channelId = re_json['channelId']
        log.logger.info("uid:" + uid+"channelId:" + channelId)
        return uid, channelId

    def test_pay_withNoEnong(self):
        # 未开通e农支付
        # 接口地址 GET /controller/app/order/findPayStatus
        loginphone = "13926175073"
        uid, chanelId = self.loginMD5(loginphone=loginphone)
        configHttp.set_url("/controller/app/order/findPayStatus")
        data = "?channelId =" + chanelId + " &client=iOS&clientVersion=1.0&d_model=iPhone&networkType=wifi&osVersion=11.0.3&sourceId=234354393900646401&uid=" + uid
        configHttp.set_params(data)
        response = configHttp.get()
        result = response.content.decode("utf-8")
        log.logger.info("接口返回数据：" + result)
        re_json = json.loads(result)
        self.assertEqual(re_json["return_context"][0]["promptMessage"], "您尚未开通E农商贷服务，请选择其他支付方式")

    def test_pay_withEnong(self):
        uid, chanelId = self.loginMD5()
        # 开通e农支付并且额度足够、与供应商有从属关系
        pass

    def test_pay_withNoSupportEnong(self):
        uid, chanelId = self.loginMD5()
        # 不支持e农商贷商品
        pass

    def test_pay_EnongWithNoRelation(self):
        uid, chanelId = self.loginMD5()
        # 开通e农支付并且额度足够、与供应商无从属关系
        pass

    def test_pay_withEnongMoneyLimit(self):
        uid, chanelId = self.loginMD5()
        # 零售商开通e农支付并且额度不够、与供应商有从属关系
        pass

    def test_pay_withEnongSupplierLimit(self):
        uid, chanelId = self.loginMD5()
        # 零售商开通e农支付并且额度够、与供应商有从属关系、供应商可用额度不足
        pass
