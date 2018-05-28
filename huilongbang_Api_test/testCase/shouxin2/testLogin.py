# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"

import unittest, json

from huilongbang_Api_test.common.configHttp import ConfigHttp
from huilongbang_Api_test.common.Log import Log

configHttp = ConfigHttp()
log = Log()


class Login(unittest.TestCase):
    """IOS端"""
    userid = None
    channelId = None

    def setUp(self):
        configHttp.set_headers(
            {"Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": "HLB/2.0 (iPhone; iOS 11.0.3; Scale/2.00)"})

    def test_loginMD5_sueccess(self):
        """登录成功"""
        configHttp.set_url("/controller/app/users/loginMD5")
        configHttp.set_data({
            "login": '{"loginphone" : "18888888886","appType" : "1","loginpassword" : "14e1b600b1fd579f47433b88e8d85291","appVersion" : "2.0"}'
            , "client": "iOS", "clientVersion": "1.0", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi"})
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        # userid = re_json["results"][0]["userid"]
        # channelId = re_json["channelId"]
        # print(re_json)

    def test_shouxin2(self):
        """零售商反向邀请供应商提交授信资料"""
        configHttp.set_url("/controller/app/ecredit/shopkeeperapply")
        userid = "11522291484717"
        channelId = "11510000000000"
        applyData = {"storeCityId": 64,
                     "idCardHandheld": "https://image.hlb.ltd/shop/201804111009391169493840.png",
                     "emergencyContactPhone": "",  # 紧急联系人手机
                     "emergencyContact": "皇上",  # 紧急联系人姓名
                     "storeAreaId": 575,
                     "businessLicense": "https://image.hlb.ltd/shop/201804111008451441586523.png",
                     "idCardPositive": "https://image.hlb.ltd/shop/201804111008341358618777.png",
                     "applyType": 0,#紧急联系人关系
                     "identityCard": "",#身份证号码
                     "houseAddressDetail": "故宫博物院",
                     "serviceLife": "10",
                     "storeGoodsTotalValue": "2580528",
                     "houseCityId": 64,
                     "ecreditShopkeeperRecommends": [
                         {
                             "supplierUserName": "黄煌",
                             "supplierCompanyName": "惠龙邦测试2.0",
                             "supplierMobile": "18888888884"
                         }
                     ],
                     "houseAreaId": 575,
                     "name": "黄雯",
                     "idCardOpposite": "https://image.hlb.ltd/shop/20180411100522544227685.png",
                     "annualSales": "100250",
                     "emergencyContactRelation": 0,
                     "businessLicenseId": "456777ggh",
                     "phone": "18888888886",
                     "houseProvinceId": 1,
                     "storeProvinceId": 1,
                     "storeAddressDetail": "11号文得路"}

        configHttp.set_data({
            "apply": '{"storeCityId":64,"idCardHandheld":"https:\/\/image.hlb.ltd\/shop\/201804111009391169493840.png",'
                     '"emergencyContactPhone":"14712345679","emergencyContact":"皇上","storeAreaId":575,'
                     '"businessLicense":"https:\/\/image.hlb.ltd\/shop\/201804111008451441586523.png",'
                     '"idCardPositive":"https:\/\/image.hlb.ltd\/shop\/201804111008341358618777.png",'
                     '"applyType":0,"identityCard":"360428199011250612","houseAddressDetail":"故宫博物院",'
                     '"serviceLife":"10","storeGoodsTotalValue":"2580528","houseCityId":64,'
                     '"ecreditShopkeeperRecommends":[{"supplierUserName":"黄煌",'
                     '"supplierCompanyName":"惠龙邦测试2.0",'
                     '"supplierMobile":"18888888889"},{"supplierUserName":"黄煌0417",'
                     '"supplierCompanyName":"惠龙邦测试3.0",'
                     '"supplierMobile":"18888888879"}],"houseAreaId":575,"name":"黄雯",'
                     '"idCardOpposite":"https:\/\/image.hlb.ltd\/shop\/20180411100522544227685.png",'
                     '"annualSales":"100250","emergencyContactRelation":0,"businessLicenseId":"456777ggh",'
                     '"phone":"13926175077","houseProvinceId":1,"storeProvinceId":1,'
                     '"storeAddressDetail":"11号文得路"}', "client": "iOS",
            "clientVersion": "2.0", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi", "channelId": channelId, "uid": userid})

        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        print(re_json)

    def test_shouxin21(self):
        """零售商填写邀请码提交授信资料"""
        configHttp.set_url("/controller/app/ecredit/shopkeeperapply")
        userid = "11522291484717"
        channelId = "11510000000000"
        configHttp.set_data({
            "apply": '{"storeCityId":64,'
                     '"idCardHandheld":"https:\/\/image.hlb.ltd\/shop\/20180411143747468169647.png",'
                     '"emergencyContactPhone":"15870883144",'
                     '"emergencyContact":"紧急联系人名字","storeAreaId":575,'
                     '"businessLicense":"https:\/\/image.hlb.ltd\/shop\/20180411143731157580224.png",'
                     '"supplierCooperationDuration":"25",'
                     '"idCardPositive":"https:\/\/image.hlb.ltd\/shop\/2018041114374463196427.png",'
                     '"applyType":1,"identityCard":"360428199911250675",'
                     '"weddingPhotos":"https:\/\/image.hlb.ltd\/shop\/20180411143747468169647.png",'
                     '"houseAddressDetail":"体育西路11号","serviceLife":"12",'
                     '"houseCityId":64,"storeGoodsTotalValue":"250000","houseAreaId":575,'
                     '"name":"0417测试",'
                     '"idCardOpposite":"https:\/\/image.hlb.ltd\/shop\/2018041114374463196427.png",'
                     '"annualSales":"12345","emergencyContactRelation":1,'
                     '"businessLicenseId":"在于他们","phone":"13926175078",'
                     '"supplierInvitationCode":"10001","houseProvinceId":1,"storeProvinceId":1,'
                     '"storeAddressDetail":"黄埔大道198号","supplierBusinessAmount":"123456"}',
            "client": "iOS",
            "clientVersion": "2.0", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi", "channelId": channelId, "uid": userid})

        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        print(re_json)

    def test_getMyEcreditAuditInfo(self):
        """查询授信状态"""
        configHttp.set_url("/controller/app/ecredit/myEcreditAuditInfo")
        userid = "11519872994249"
        channelId = "11510000000000"
        configHttp.set_data({
            "client": "iOS", "clientVersion": "2.0", "d_model": "iPhone", "osVersion": "11.0.3",
            "networkType": "wifi", "channelId": channelId, "uid": userid, "type": 1
        })
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        print(re_json)


    def test_suppliershouxin(self):
        """供应商提交授信资料"""
        configHttp.set_url("/controller/app/ecredit/supplierapply")
        userid = "11515574192857"
        channelId = "11510000000000"
        configHttp.set_data({
                        "apply":'{"houseAddressDetail":"体育西路189号",'
                                     '"businessLicense":"https:\/\/image.hlb.ltd\/shop\/201804111458441213601964.png",'
                                     '"personalCreditReportJson":["https:\/\/image.hlb.ltd\/shop\/201804111459041797877530.png",'
                                     '"https:\/\/image.hlb.ltd\/shop\/20180411145906811429510.png",'
                                     '"https:\/\/image.hlb.ltd\/shop\/201804111459081211199473.png",'
                                     '"https:\/\/image.hlb.ltd\/shop\/20180411145910625353878.png",'
                                     '"https:\/\/image.hlb.ltd\/shop\/20180411145911512229266.png"],'
                                     '"phone":"18888888884","supplierAddressDetail":"体育西路189号","houseAreaId":2260,'
                                     '"saleAmount":"1236547","channelName":"农业","identityCard":"360428199011250614",'
                                     '"houseProvinceId":19,"houseCityId":260,"introducerPhone":"18888888885",'
                                     '"idCardPositive":"https:\/\/image.hlb.ltd\/shop\/201804111458541070922984.png",'
                                     '"idCardOpposite":"https:\/\/image.hlb.ltd\/shop\/201804111458541070922984.png",'
                                     '"name":"黄煌","idCardHandheld":"https:\/\/image.hlb.ltd\/shop\/201804111458541070922984.png"}',
                        "client": "iOS", "clientVersion": "2.0", "d_model": "iPhone", "osVersion": "11.0.3",
                        "networkType": "wifi", "channelId": channelId, "uid": userid
                            })
        response = configHttp.post()
        result = response.content.decode("utf-8")
        re_json = json.loads(result)
        log.logger.info("接口返回数据：" + result)
        print(re_json)