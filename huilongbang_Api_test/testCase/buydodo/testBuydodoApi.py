# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"

import unittest, json
from log.mode.color import ColorLogger
from huilongbang_Api_test.common.configHttp import ConfigHttp
from huilongbang_Api_test.common.excelutils import ExcelUtils
from ddt import ddt, data, unpack

configHttp = ConfigHttp()
log = ColorLogger()


def get_data(numName):
    datas = ExcelUtils.api_read_data('test')
    list_json = []
    d = datas[numName]
    list_json.append(d)
    return list_json


@ddt
class Buydodo_Api_Test(unittest.TestCase):
    def setUp(self):
        configHttp.set_headers(
            {"Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": "buydodo/1.2 (iPhone; iOS 11.0.3; Scale/2.00)"})

    def tearDown(self):
        pass

    @data(*get_data("test_login"))
    def test_a_login(self, value):
        url = value["_api"]
        params = value["_params"][0]
        log.info("url: "+url+"  params: "+ str(params))
        configHttp.set_url(url)
        configHttp.set_data(params)
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.info("test_a_login 接口返回数据：" + result)
        ExcelUtils.api_write_data("test", 1, 5, json.dumps({"_response": result}))
        self.assertEqual(int(response.status_code), 200, "不一致")
        self.assertEqual(re_json["return_context"]["status"], 0, "不一致")

    def test_a_loginMD5_success(self):
        """正常账号登录  成功 接口/controller/app/login/loginMD5"""
        # data = json.loads(value)
        data = ExcelUtils.api_read_data("test")
        log.info("读取参数：" + str(data))
        url = data["test_login"]["_api"]
        params = data["test_login"]["_params"][0]
        configHttp.set_url(url)
        configHttp.set_data(params)
        # configHttp.set_data({
        #     "login": '{"loginphone" : "13926175076","appType" : "1","loginpassword" : "e1b5146bb46325d63acc1f2959caacbe","appVersion" : "2.0"}'
        #     , "client": "iOS", "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
        #     "networkType": "wifi"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.info("接口返回数据：" + result)
        ExcelUtils.api_write_data("test", 1, 5, json.dumps({"_response": result}))
        self.assertEqual(int(response.status_code), 200, "不一致")
        self.assertEqual(re_json["return_context"]["status"], 0, "不一致")

    def test_b_loginMD5_errorPwd(self):
        """账号或密码错误 接口/controller/app/login/loginMD5"""
        configHttp.set_url("/controller/app/login/loginMD5")
        configHttp.set_data({
            "login": '{"loginphone" : "13926175076","appType" : "1","loginpassword" : "14e1b600b1fd579f47433b88e8d85291","appVersion" : "2.0"}'
            , "client": "iOS", "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.info("loginMD5 接口返回数据：" + result)
        # ExcelUtils.api_write_data("test", 4, 5, str(re_json))
        self.assertEqual(int(response.status_code), 200, "不一致")
        self.assertEqual(re_json["return_context"]["return_message"], "账号或密码错误", "不一致")

    def test_c_getUserInf_success(self):
        """获取用户信息 正常 接口/controller/app/netease/getUserInfo"""
        excel_data = ExcelUtils.api_read_data('test')
        apiToken = excel_data["test_getUserInfo"]["_response"]["return_context"]["apiToken"]
        userId = excel_data["test_getUserInfo"]["_response"]["return_context"]["results"][0]["userid"]
        channelId = excel_data["test_getUserInfo"]["_response"]["return_context"]["channelId"]
        configHttp.set_url("/controller/app/netease/getUserInfo")
        configHttp.set_data({
            "apiToken": apiToken, "channelId": channelId, "uid": userId, "imgUid": "15269803060001", "client": "iOS",
            "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        log.info("getUserInfo 接口返回数据：" + result)
        re_json = json.loads(result)
        self.assertIsNotNone(re_json["name"], "name没有值")

    def test_d_gethomepageCatagory_success(self):
        """获取首页信息  成功 接口/controller/app/goods/gethomepageCatagory"""
        excel_data = ExcelUtils.api_read_data('test')
        apiToken = excel_data["test_getUserInfo"]["_response"]["return_context"]["apiToken"]
        userId = excel_data["test_getUserInfo"]["_response"]["return_context"]["results"][0]["userid"]
        channelId = excel_data["test_getUserInfo"]["_response"]["return_context"]["channelId"]

        configHttp.set_url("/controller/app/goods/gethomepageCatagory")
        configHttp.set_params(
            "apiToken=" + apiToken + "&channelId=" + channelId + "&client=iOS&clientVersion=1.2&d_model=iPhone&networkType=WiFi&osVersion=11.0.3&uid=" + userId)
        response = configHttp.get()
        result = response.content.decode("utf-8")
        log.info("gethomepageCatagory 接口返回数据：" + result)
        re_json = json.loads(result)
        self.assertEqual(re_json["error"], 0, "error返回值不一致")
        self.assertEqual(re_json["status"], 0, "status返回值不一致")
        self.assertIsNotNone(re_json["results"], "results内容为空")

    def test_e_getChannels_success(self):
        """获取首页频道  成功 接口/controller/app/channel/getChannels"""
        pass

    def test_f_getClassitfyProductlist_success(self):
        """获取首页商品  成功 接口/controller/app/goods/v41/getClassitfyProductlist"""
        pass

    def test_g_getTicketCpp_success(self):
        """获取首页弹框接口  成功 接口/controller/app/ticket/v3/getTicketCpp"""
        pass
