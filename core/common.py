#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import re
import xlrd
import xlsxwriter
from xlutils.copy import copy

class Common(object):

    @staticmethod
    def api_read_data(page_name, data_address):
        """ 获取excel数据，并转化成dict

        """
        excel_data = {}
        _name = []
        book = xlrd.open_workbook(data_address)
        sheet = book.sheet_by_name(page_name)
        num = sheet.nrows
        for row in range(1, num):
            test_name = sheet.cell(row, 0).value
            _name.append(test_name)
            re_way = sheet.cell(row, 2).value
            address_data = sheet.cell(row, 3).value
            parameter_data = sheet.cell(row, 4).value
            result_parameter = sheet.cell(row, 5).value
            draw_parameter = sheet.cell(row, 6).value
            result_data = sheet.cell(row, 7).value
            col = 1
            try:
                re_way = json.loads(re_way)
                col += 1
                address_data = json.loads(address_data)
                col += 1
                parameter_data = json.loads(parameter_data)
                col += 1
                result_parameter = json.loads(result_parameter.replace("'","\""))
                col += 1
                draw_parameter = json.loads(draw_parameter)
                col += 1
                result_data = json.loads(result_data)
                col += 1
            except Exception as e:
                print('excel第{}行,第{}列，json数据解析失败'.format(row+1, col))
                raise e
            result_data.update(re_way)
            result_data.update(address_data)
            result_data.update(result_parameter)
            result_data.update(draw_parameter)
            result_data.update(parameter_data)
            excel_data[test_name] = result_data
        excel_data['_name'] = _name
        return excel_data

    @staticmethod
    def api_write_data(page_name, data_address,row,col,write_data):
        old_excel = xlrd.open_workbook(data_address,formatting_info=True)
        new_excel = copy(old_excel)
        newWs = new_excel.get_sheet(1)
        newWs.write(row,col,write_data)
        new_excel.save(data_address)

    @staticmethod
    def _token(result):
        """ 递归字典数据，查找出深层中键为token的值

        """
        if isinstance(result, list):
            for n in result:
                return Common._token(n)
        else:
            for n in result:
                if n == 'token':
                    return result[n]
                else:
                    if isinstance(result[n], list):
                        for n1 in result[n]:
                            if not Common._token(n1):
                                continue
                            else:
                                return Common._token(n1)
                    elif isinstance(result[n], dict):
                        if not Common._token(result[n]):
                            continue
                        else:
                            return Common._token(result[n])

    @staticmethod
    def get_token(result):
        """ 两种方式获取token，第一种返回数据没有的话，就从cookies.items中获取

        """
        one = Common._token(result.json())
        if one:
            return one
        else:
            for n in result.cookies.items():
                if isinstance(n, tuple):
                    n = list(n)
                    for n1 in n:
                        if n1.find('token') != -1:
                            return re.findall(r'\w+\.?\w', n1.split('token:')[1])[0]
                        else:
                            assert '两种方式都获取不到token'



if __name__ == '__main__':

    cc = Common.api_read_data('test',r'D:\PyCharm_WorkSpace\auto_api-master\auto_protocol\api_config\testcase_data.xls')
    print(cc)
    print("apiToken:"+cc["test_getUserInfo"]["_response"]["return_context"]["apiToken"])
    print("results:" + cc["test_getUserInfo"]["_response"]["return_context"]["results"][0]["userid"])
    print("channelId:" + cc["test_getUserInfo"]["_response"]["return_context"]["channelId"])
    # data = str({"_response":{"return_code":"SUCCESS","return_context":{"status":0,"results":[{"type":"1","userid":"15269803060001","storeName":"啛啛喳喳错"}],"channelId":"11510000000000","replenishShopInfo":0,"apiToken":"d78f490d-2a45-484d-9267-3ab2164ace1f","expire":"2018-05-29 22:45:37"},"return_date":"2018-05-29 10:45:37","return_msg":"成功"}})
    #
    # w = Common.api_write_data('test',r'D:\PyCharm_WorkSpace\auto_api-master\auto_protocol\api_config\testcase_data.xls'
    #                           ,2,5,data)
