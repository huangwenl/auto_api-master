# -*- coding: UTF-8 -*-
import os
import unittest
import HTMLTestReportCN
from huilongbang_Api_test import readConfig
from datetime import datetime
# from huilongbang_Api_test.common.Log import Log
from log.mode.color import ColorLogger
log = ColorLogger()


class AllTest(object):
    def __init__(self):
        self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
        self.caseList = []
        self.resultPath = os.path.join(readConfig.proDir, "result")
        self.report_File = os.path.join(self.resultPath, str(datetime.now().strftime("%Y%m%d")))
        self.caseFile = os.path.join(readConfig.proDir, "testCase")

    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            # log.logger.info("读取caselist列表数据：" + data)
            log.info("读取caselist列表数据：" + data)
            if data != "" and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            log.logger.info(case_name + ".py")
            self.caseFile = self.caseFile + "/" + case.split("/")[0]
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + ".py", top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                log.info("**********开始测试***********")
                report_name = self.report_File + "\interface_test.html"
                fb = open(report_name, "wb")
                runner = HTMLTestReportCN.HTMLTestRunner(stream=fb, title="接口测试报告", description='详细测试用例结果',
                                                         tester='黄文亮')
                runner.run(suit)
            else:
                log.error("没有可执行的case测试")
        except Exception as ex:
            log.error(str(ex))
        finally:
            log.info("*********测试结束*********")


if __name__ == "__main__":
    obj = AllTest()
    # obj.set_case_suite()
    obj.run()
