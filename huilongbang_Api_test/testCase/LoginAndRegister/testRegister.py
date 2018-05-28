# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"
import unittest, json

from huilongbang_Api_test.common.configHttp import ConfigHttp
from huilongbang_Api_test.common.Log import Log

configHttp = ConfigHttp()
log = Log()


class Register(unittest.TestCase):
    def setUp(self):
        configHttp.set_headers(
            {"Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": "HLB/1.0 (iPhone; iOS 11.0.3; Scale/2.00)"})

    def test_checkIfRegist_unregist(self):
        configHttp.set_url("/controller/app/users/checkIfRegist")
        configHttp.set_data({"loginphone": "15622338930", "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone",
                             "osVersion": "11.0.3"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        self.assertEqual(re_json["return_message"], "用户未注册")

    def test_checkIfRegist_regist(self):
        configHttp.set_url("/controller/app/users/checkIfRegist")
        configHttp.set_data({"loginphone": "13926175077", "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone",
                             "osVersion": "11.0.3"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        self.assertEqual(re_json["return_msg"], "用户已注册")

    def test_registuserMD5_olduser(self):
        configHttp.set_url("/controller/app/users/v3/regisuserMD5")
        configHttp.set_data(
            {
                "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone", "osVersion": "11.0.3",
                "regis": '{"loginphone" : "13926175077","areaId" : 2257,"loginpassword" : "14e1b600b1fd579f47433b88e8d85291","channelId" : "11510000000000","matchcode" : "8682","shopInfo" : "{\n  \"shopSize\" : \"100-200平米\",\n  \"shopType\" : \"综合店\",\n  \"mainBrand\" : \"8682\",\n  \"yearTurnover\" : \"100-300万\",\n  \"shopArea\" : \"一般商业区\"\n}","addressDetail" : "狗狗你呢13公斤","userName" : "狗狗名功能mino","registerSource" : "1","provinceId" : 19,"storeName" : "国家级风景名胜区后给您","cityId" : 260}'
            }
        )
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        self.assertEqual(re_json["return_msg"], "失败")

    def test_registuserMD5_newuser(self):
        configHttp.set_url("/controller/app/users/v3/regisuserMD5")
        configHttp.set_data(
            {
                "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone", "osVersion": "11.0.3",
                "regis": '{"loginphone" : "15622338930","areaId" : 2257,"loginpassword" : "14e1b600b1fd579f47433b88e8d85291","channelId" : "11510000000000","matchcode" : "1234","shopInfo" : "{\n  \"shopSize\" : \"100-200平米\",\n  \"shopType\" : \"综合店\",\n  \"mainBrand\" : \"8682\",\n  \"yearTurnover\" : \"100-300万\",\n  \"shopArea\" : \"一般商业区\"\n}","addressDetail" : "狗狗你呢13公斤","userName" : "狗狗名功能mino","registerSource" : "1","provinceId" : 19,"storeName" : "","cityId" : 260}'
            }
        )
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        self.assertEqual(re_json["return_msg"], "1")

