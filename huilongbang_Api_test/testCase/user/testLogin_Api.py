# -*- coding: UTF-8 -*-

import unittest, json

from huilongbang_Api_test.common.configHttp import ConfigHttp

configHttp = ConfigHttp()


class Login_api_test(unittest.TestCase):
    def setUp(self):
        configHttp.set_headers(
            {"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "HUAWEI G7-TL00/Android4.4.2"})
        # configHttp.set_data({
        # "osVersion": "Android4.4.2", "networkType": "WIFI", "screen": "720*1280", "clientVersion": "1.0",
        #     "d_brand": "HUAWEI", "d_model": "HUAWEI G7-TL00"
        # })

    def tearDown(self):
        pass

    def test_getUserByLoginphone_success(self):
        """登录成功"""
        configHttp.set_url("/controller/app/users/getUserByLoginphone")
        configHttp.set_data({"loginphone": "13602813099"})
        response = configHttp.post()
        print(response.url)

    def test_loginMD5_unregisterNum(self):
        """未注册登录"""
        configHttp.set_url("/controller/app/users/loginMD5")
        configHttp.set_data({
            "login": '{"loginphone":"13926175077","appVersion":"1","appType":"2","loginpassword":"14e1b600b1fd579f47433b88e8d85291"}'
            , "osVersion": "Android4.4.2", "networkType": "WIFI", "screen": "720*1280", "clientVersion": "1.0",
            "d_brand": "HUAWEI", "d_model": "HUAWEI G7-TL00"
        })
        response = configHttp.post()
        self.assertEqual(int(response.status_code), 200, "不一致")
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        self.assertEqual(re_json["return_message"], "您还未注册")
        self.assertEqual(int(re_json["status"]), 6)

    def test_loginMD5_badNum(self):
        """错误手机号码登录"""
        configHttp.set_url("/controller/app/users/loginMD5")
        configHttp.set_data({
            "login": '{"loginphone":"11133366658","appVersion":"1","appType":"2","loginpassword":"14e1b600b1fd579f47433b88e8d85291"}'
            , "osVersion": "Android4.4.2", "networkType": "WIFI", "screen": "720*1280", "clientVersion": "1.0",
            "d_brand": "HUAWEI", "d_model": "HUAWEI G7-TL00"
        })
        response = configHttp.post()
        self.assertEqual(int(response.status_code), 200, "不一致")
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        self.assertEqual(re_json["return_message"], "您还未注册")
        self.assertEqual(int(re_json["status"]), 6)

    def test_loginMD5_oldUser(self):
        """存量用户登录"""
        configHttp.set_url("/controller/app/users/loginMD5")
        configHttp.set_data({
            "login": '{"loginphone":"13926175078","appVersion":"1","appType":"2","loginpassword":"14e1b600b1fd579f47433b88e8d85291"}'
            , "osVersion": "Android4.4.2", "networkType": "WIFI", "screen": "720*1280", "clientVersion": "1.0",
            "d_brand": "HUAWEI", "d_model": "HUAWEI G7-TL00"
        })
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        self.assertEqual(int(response.status_code), 200, "不一致")
        self.assertEqual(re_json["return_message"], "请先完善您的注册文本资料！")
        self.assertEqual(int(re_json["status"]), 11)
