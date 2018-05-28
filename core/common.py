#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import re
import xlrd


class Common(object):

    @staticmethod
    def api_read_data1(page_name, data_address):
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
                result_parameter = json.loads(result_parameter)
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


# if __name__ == '_main_':
# cc=Common.api_read_data1('test',r'D:\PyCharm_WorkSpace\auto_api-master\auto_protocol\api_config\testcase_data.xlsx')
# print(cc)