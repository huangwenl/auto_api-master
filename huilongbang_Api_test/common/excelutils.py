#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import json,os
import re
import xlrd
import xlsxwriter
from xlutils.copy import copy

class ExcelUtils(object):
    proDir = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
    data_address = proDir + "\\api_data.xls"

    @staticmethod
    def api_read_data(page_name, data_address=data_address):
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
    def api_write_data(page_name,row,col,write_data,data_address=data_address):
        old_excel = xlrd.open_workbook(data_address,formatting_info=True)
        new_excel = copy(old_excel)
        newWs = new_excel.get_sheet(1)
        newWs.write(row,col,write_data)
        new_excel.save(data_address)


if __name__ == '__main__':

    cc = ExcelUtils.api_read_data('test')
    print(cc)
#     print("apiToken:"+cc["test_getUserInfo"]["_response"]["return_context"]["apiToken"])
#     print("results:" + cc["test_getUserInfo"]["_response"]["return_context"]["results"][0]["userid"])
#     print("channelId:" + cc["test_getUserInfo"]["_response"]["return_context"]["channelId"])
#     data = str({"_response":{"return_code":"SUCCESS","return_context":{"status":0,"results":[{"type":"1","userid":"15269803060001","storeName":"啛啛喳喳错"}],"channelId":"11510000000000","replenishShopInfo":0,"apiToken":"d78f490d-2a45-484d-9267-3ab2164ace1f","expire":"2018-05-29 22:45:37"},"return_date":"2018-05-29 10:45:37","return_msg":"成功"}})
#
#     w = ExcelUtils.api_write_data('test',2,5,data)
