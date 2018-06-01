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
    def test_a_loginMD5_success(self, value):
        """正常账号登录  成功 接口/controller/app/login/loginMD5"""
        url = value["_api"]
        params = value["_params"][0]
        # log.info("url: "+url+"  params: "+ str(params))
        configHttp.set_url(url)
        configHttp.set_data(params)
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.info("loginMD5 接口返回数据：" + result)
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
        self.assertEqual(int(response.status_code), 200, "不一致")
        self.assertEqual(re_json["return_context"]["return_message"], "账号或密码错误", "不一致")

    @data(*get_data("test_login"))
    def test_c_getUserInf_success(self,value):
        """获取用户信息 正常 接口/controller/app/netease/getUserInfo"""
        json_re = json.loads(value["_response"])
        apiToken = json_re["return_context"]["apiToken"]
        userId = json_re["return_context"]["results"][0]["userid"]
        channelId = json_re["return_context"]["channelId"]

        configHttp.set_url("/controller/app/netease/getUserInfo")
        params = {
            "apiToken": apiToken, "channelId": channelId, "uid": userId, "imgUid": "15269803060001", "client": "iOS",
            "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi"}
        configHttp.set_data(params)
        response = configHttp.post()
        result = response.content.decode("utf-8")
        log.info("getUserInfo 接口返回数据：" + result)
        ExcelUtils.api_write_data("test", 2, 4, json.dumps({"_params": params}))
        ExcelUtils.api_write_data("test", 2, 5, json.dumps({"_response": result}))
        re_json = json.loads(result)
        self.assertEqual(re_json["code"],200)

    @data(*get_data("test_login"))
    def test_d_gethomepageCatagory_success(self,value):
        """获取首页信息  成功 接口/controller/app/goods/gethomepageCatagory"""
        json_re = json.loads(value["_response"])
        apiToken = json_re["return_context"]["apiToken"]
        userId = json_re["return_context"]["results"][0]["userid"]
        channelId = json_re["return_context"]["channelId"]

        configHttp.set_url("/controller/app/goods/gethomepageCatagory")
        params = "apiToken=" + apiToken + "&channelId=" + channelId + "&client=iOS&clientVersion=1.2&d_model=iPhone&networkType=WiFi&osVersion=11.0.3&uid=" + userId
        configHttp.set_params(params)
        response = configHttp.get()
        result = response.content.decode("utf-8")
        log.info("gethomepageCatagory 接口返回数据：" + result)
        ExcelUtils.api_write_data("test", 3, 4, json.dumps({"_params": params}))
        ExcelUtils.api_write_data("test", 3, 5, json.dumps({"_response": result}))
        re_json = json.loads(result)
        self.assertEqual(re_json["error"], 0, "error返回值不一致")
        self.assertEqual(re_json["status"], 0, "status返回值不一致")
        self.assertIsNotNone(re_json["results"], "results内容为空")

    @data(*get_data("test_login"))
    def test_e_getChannels_success(self,value):
        """获取首页频道  成功 接口/controller/app/channel/getChannels"""
        json_re = json.loads(value["_response"])
        apiToken = json_re["return_context"]["apiToken"]
        userId = json_re["return_context"]["results"][0]["userid"]
        channelId = json_re["return_context"]["channelId"]
        configHttp.set_url("/controller/app/channel/getChannels")
        params = {
            "apiToken": apiToken, "channelId": channelId, "uid": userId, "imgUid": "15269803060001", "client": "iOS",
            "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi"}
        configHttp.set_data(params)
        response = configHttp.post()
        result = response.content.decode("utf-8")
        log.info("getChannels 接口返回数据：" + result)
        ExcelUtils.api_write_data("test", 4, 4, json.dumps({"_params": params}))
        ExcelUtils.api_write_data("test", 4, 5, json.dumps({"_response": result}))
        re_json = json.loads(result)
        self.assertEqual(re_json["return_code"], "SUCCESS", msg="失败")
        self.assertIsNotNone(re_json["return_context"], msg="return_context数据为空")

    @data(*get_data("test_login"))
    def test_f_getClassitfyProductlist_success(self,value):
        """获取首页商品  成功 接口/controller/app/goods/v41/getClassitfyProductlist"""
        json_re = json.loads(value["_response"])
        apiToken = json_re["return_context"]["apiToken"]
        userId = json_re["return_context"]["results"][0]["userid"]
        channelId = json_re["return_context"]["channelId"]
        configHttp.set_url("/controller/app/goods/v41/getClassitfyProductlist")
        params = {
            "apiToken": apiToken, "channelId": channelId, "uid": userId, "imgUid": "15269803060001", "client": "iOS",
            "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi","pageCount":1,"sortType":1,"ifRecommend":2}
        configHttp.set_data(params)
        response = configHttp.post()
        result = response.content.decode("utf-8")
        log.info("getClassitfyProductlist 接口返回数据：" + result)
        ExcelUtils.api_write_data("test", 5, 4, json.dumps({"_params": params}))
        ExcelUtils.api_write_data("test", 5, 5, json.dumps({"_response": result}))
        re_json = json.loads(result)
        self.assertEqual(re_json["return_code"], "SUCCESS", msg="失败")
        self.assertIsNotNone(re_json["return_context"],msg="return_context数据为空")

    @data(*get_data("test_login"))
    def test_g_getTicketCpp_success(self,value):
        """获取首页弹框接口  成功 接口/controller/app/ticket/v3/getTicketCpp"""
        json_re = json.loads(value["_response"])
        apiToken = json_re["return_context"]["apiToken"]
        userId = json_re["return_context"]["results"][0]["userid"]
        channelId = json_re["return_context"]["channelId"]
        configHttp.set_url("/controller/app/ticket/v3/getTicketCpp")
        params = {
            "apiToken": apiToken, "channelId": channelId, "uid": userId, "imgUid": "15269803060001", "client": "iOS",
            "clientVersion": "1.2", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi"}
        configHttp.set_data(params)
        response = configHttp.post()
        result = response.content.decode("utf-8")
        log.info("getTicketCpp 接口返回数据：" + result)
        ExcelUtils.api_write_data("test", 6, 4, json.dumps({"_params": params}))
        ExcelUtils.api_write_data("test", 6, 5, json.dumps({"_response": result}))
        re_json = json.loads(result)
        self.assertEqual(re_json["return_code"],"SUCCESS",msg="失败")
