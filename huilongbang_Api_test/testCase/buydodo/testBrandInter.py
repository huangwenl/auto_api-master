# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"

import unittest, json
from log.mode.color import ColorLogger
from huilongbang_Api_test.common.configHttp import ConfigHttp
from huilongbang_Api_test.common.excelutils import ExcelUtils
from ddt import ddt

configHttp = ConfigHttp()
log = ColorLogger()



"""App品牌接口"""
@ddt
class BrandInters(unittest.TestCase):

    def setUp(self):
        configHttp.set_headers(
            {"Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": "buydodo/1.2 (iPhone; iOS 11.0.3; Scale/2.00)"})

    def tearDown(self):
        pass
