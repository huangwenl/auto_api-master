# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"

import unittest, json
from log.mode.color import ColorLogger
from huilongbang_Api_test.common.configHttp import ConfigHttp

configHttp = ConfigHttp()
log = ColorLogger()


class Buydodo_Api_Test(unittest.TestCase):
    def setUp(self):
        configHttp.set_headers(
            {"Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": "buydodo/1.2 (iPhone; iOS 11.0.3; Scale/2.00)"})
        self.channelId = "11510000000000"
        self.userId = "15269803060001"

    def tearDown(self):
        pass

    def test_a_loginMD5_success(self):
        """正常账号登录  成功"""
        configHttp.set_url("/controller/app/users/loginMD5")
        configHttp.set_data({
            "login": '{"loginphone" : "13926175076","appType" : "1","loginpassword" : "e1b5146bb46325d63acc1f2959caacbe","appVersion" : "2.0"}'
            , "client": "iOS", "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.info("接口返回数据：" + result)
        self.apiToken = re_json["apiToken"]
        self.assertEqual(int(response.status_code), 200, "不一致")
        self.assertEqual(re_json["status"], 0, "不一致")

    def test_b_loginMD5_errorPwd(self):
        """账号或密码错误"""
        configHttp.set_url("/controller/app/users/loginMD5")
        configHttp.set_data({
            "login": '{"loginphone" : "13926175076","appType" : "1","loginpassword" : "14e1b600b1fd579f47433b88e8d85291","appVersion" : "2.0"}'
            , "client": "iOS", "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        log.info("loginMD5 接口返回数据：" + result)
        re_json = json.loads(result)
        self.assertEqual(int(response.status_code), 200, "不一致")
        self.assertEqual(re_json["return_message"], "账号或密码错误", "不一致")

    def test_c_getUserInf_success(self):
        """获取用户信息 正常"""
        configHttp.set_url("/controller/app/netease/getUserInf")
        configHttp.set_data({
             "apiToken":self.apiToken,"channelId":self.channelId,"uid":self.userId, "imgUid":"15269803060001","client": "iOS", "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        log.info("getUserInf 接口返回数据：" + result)
        re_json = json.loads(result)
        self.assertIsNotNone(re_json["name"],"name没有值")

    def test_d_gethomepageCatagory_success(self):
        """获取首页信息  成功"""
        configHttp.set_url("/controller/app/goods/gethomepageCatagory")
        configHttp.set_params("apiToken="+self.apiToken +"&channelId=11510000000000&client=iOS&clientVersion=1.2&d_model=iPhone&networkType=WiFi&osVersion=11.0.3&uid=15269803060001")
        response = configHttp.post()
        result = response.content.decode("utf-8")
        log.info("gethomepageCatagory 接口返回数据：" + result)
        re_json = json.loads(result)
        self.assertEqual(re_json["error"],0,"error返回值不一致")
        self.assertEqual(re_json["status"], 0, "status返回值不一致")
        self.assertIsNotNone(re_json["results"],"results内容为空")