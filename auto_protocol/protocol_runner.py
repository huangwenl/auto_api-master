#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
UI自动化执行入口
"""
import unittest

from auto_protocol.config_data import ConfigData
from auto_protocol.testcase.test_1 import AutoPro
from core.TestRunner import CommonRunner

test_suite = unittest.TestSuite()


def set_case():
    for name in ConfigData.excel_data['_name'][1:]:     # 提取所有的用例名字
        def func(self, names=name):
            self.case_logic(self.excel_data[names])

        name = 'test_{:03d}_{}'.format(ConfigData.num, name)
        ConfigData.num += 1
        setattr(AutoPro, name, func)    # 设置子用例到AutoPro模块中
        test_suite.addTest(AutoPro(name))   # 添加子用例


set_case()

runner = CommonRunner('接口')
runner.run_test(test_suite)
