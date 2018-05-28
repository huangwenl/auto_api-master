# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"

import unittest, json

from huilongbang_Api_test.common.configHttp import ConfigHttp
from huilongbang_Api_test.common.Log import Log

configHttp = ConfigHttp()
log = Log()


class Login(unittest.TestCase):
    """IOS端"""

    def setUp(self):
        configHttp.set_headers(
            {"Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": "HLB/1.0 (iPhone; iOS 11.0.3; Scale/2.00)"})
        configHttp.set_url("/controller/app/users/loginMD5")

    def test_loginMD5_loginphoneIsNull(self):
        """手机号为空"""
        configHttp.set_data({
            "login": '{"loginphone" : "","appType" : "1","loginpassword" : "14e1b600b1fd579f47433b88e8d85291","appVersion" : "1.0"}'
            , "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone", "osVersion": "11.0.3"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        self.assertEqual(re_json["return_message"], "您还未注册")
        self.assertEqual(int(re_json["status"]), 6)

    def test_loginMD5_sueccess(self):
        """登录成功"""
        configHttp.set_data({
            "login": '{"loginphone" : "13926175078","appType" : "1","loginpassword" : "14e1b600b1fd579f47433b88e8d85291","appVersion" : "1.0"}'
            , "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone", "osVersion": "11.0.3"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        self.assertEqual(re_json["return_message"], "成功")
        self.assertEqual(int(re_json["status"]), 0)

    def test_loginMD5_passwordError(self):
        """密码错误"""
        configHttp.set_data({
            "login": '{"loginphone" : "13602813099","appType" : "1","loginpassword" : "c63e189ddc8b0741201f8b0abbd6d3b7","appVersion" : "1.0"}'
            , "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone", "osVersion": "11.0.3"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        self.assertEqual(re_json["return_message"], "账号或密码错误")
        self.assertEqual(int(re_json["status"]), 1)

    def test_loginMD5_passwordIsNull(self):
        """密码错误为空"""
        configHttp.set_data({
            "login": '{"loginphone" : "13602813099","appType" : "1","loginpassword" : "","appVersion" : "1.0"}'
            , "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone", "osVersion": "11.0.3"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        self.assertEqual(re_json["return_message"], "账号或密码错误")
        self.assertEqual(int(re_json["status"]), 1)

    def test_sqe(self):
        str = "abcdefghijklmnopqrstuvwxyz"
        i = -1
        for i in range(len(str),0, -1):
            print(str[:i])

        for i in range(-1, -len(str), -1):
            print(str[:i])
