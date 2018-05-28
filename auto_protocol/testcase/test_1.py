# coding = utf-8
import unittest
import requests
from auto_protocol.config_data import ConfigData
from core.common import Common
from core.sq_unittest import SHTestCase


class AutoPro(SHTestCase):

    @classmethod
    def setUpClass(cls):
        """主要是用来创建多个用户，和登录操作后存储参数登录令牌，以便后续用例默认传入

        """
        cls.excel_data =ConfigData.excel_data
        cls.temp_data.clear()   # 一个模块系统开始前清空临时字典，防止2个系统间的值产生冲突等等
        for num, n in enumerate(cls.excel_data['test_config']['_users']):
            setattr(cls, n, requests.Session())
            _user = getattr(cls, n)
            cls.ip = cls.excel_data['test_config']['ip']
            result = _user.post('{}{}'.format(cls.ip, cls.excel_data['test_config']['_api']), cls.excel_data['test_config']['_param'][num])
            _user.params = {'token': Common.get_token(result)}      # 存储token


if __name__ == '_main_':
    unittest.main()
