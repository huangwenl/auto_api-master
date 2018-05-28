#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import time
import log
from core.BSTestRunner import BSTestRunner


class TestRunner(object):
    def __init__(self):
        self.default_runner = BSTestRunner
        self.suite = None


class CommonRunner(TestRunner):
    def __init__(self, name):
        self.name = name
        super(CommonRunner).__init__()

    def run_test(self, suite):
        if not os.path.exists('report'):  # 判断是否存在文件路径，若无则创建路径
            os.makedirs('report')

        report_name = "report\{}-{}.html".format("report",
                                                 time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))

        with open(report_name, "wb") as f:
            runner = BSTestRunner(stream=f, title='{}自动化测试报告'.format(self.name))
            runner.run(suite)

        log.info("{}自动化测试完成，请查看报告".format(self.name))
        os.system("start {}".format(report_name))

