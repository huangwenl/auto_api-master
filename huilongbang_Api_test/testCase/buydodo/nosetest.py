# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"

from ddt import ddt,data,unpack,file_data
import unittest,json
from huilongbang_Api_test.common.excelutils import ExcelUtils


def get_data(numName):
    datas = ExcelUtils.api_read_data('test')
    # api_url = datas[numName]["_api"]
    # api_params = datas[numName]["_params"]
    # api_response = datas[numName]["_response"]
    list_json = []
    # list_json.append(api_url)
    # list_json.append(api_params)
    # list_json.append(api_response)
    d = datas[numName]
    list_json.append(d)
    return list_json

@ddt
class MyTestCase(unittest.TestCase):

    #下面的1,2,3代表我们传入的参数,每次传入一个值
    @data(1,2,3)
    #定义一个value用于接收我们传入的参数
    def test_oneValue(self,value):
        #对于传入的参数与2进行对比,相等就通过,否则就是不同过
        self.assertEqual(value, 2)

    # 下面的(1,2)(2,3)代表我们传入的参数,每次传入两个值
    @data((1, 2), (2, 3))
    # 告诉我们的测试用例传入的是两个以上的值
    @unpack
    # 定义两个参数value用于接收我们传入的参数
    def test_twoValue(self, value1, value2):
        print(value1, value2)
        # 对于传入的第一个参数+1与第二个参数进行对比,相等就通过,否则就是不通过
        self.assertEqual(value2, value1 + 1)

    @data(*get_data("test_login"))
    def test_file_data_json(self, value):
       print(value["_response"])
       print(value["_api"])
       print(value["_params"][0])


if __name__ == '__main__':
    unittest.main()
