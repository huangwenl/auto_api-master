# -*- coding: UTF-8 -*-
Author = "Sky Huang"

import requests
import json
from huilongbang_Api_test import readConfig as readConfig
# from huilongbang_Api_test.common.Log import Log
from log.mode.color import ColorLogger

localReadConfig = readConfig.ReadConfig()
# log = Log()
log = ColorLogger()


class ConfigHttp(object):
    def __init__(self):
        self.host = localReadConfig.get_http("baseurl")
        # self.port = localReadConfig.get_http("port")
        self.timeout = localReadConfig.get_http("timeout")
        # self.logger = log.logger
        self.headers = {}
        self.params = ""
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = self.host + url  # + self.port
        log.info("接口地址：" + self.url)

    def set_headers(self, header):
        self.headers = header
        log.info("请求头信息：" + json.dumps(self.headers))

    def set_params(self, param):
        self.params = param
        if isinstance(param,dict):
            log.info("参数：" + json.dumps(self.param))
        else:
            log.info("参数：" + param)

    def set_data(self, data):
        self.data = data
        log.info("参数：" + json.dumps(self.data))

    def set_files(self, file):
        self.files = file
        log.info("文件：" + json.dumps(self.files))

    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(self.timeout))
            return response
        except Exception as e:
            log.error("接口访问错误，Time out!")
            return None

    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(self.timeout))
            return response
        except Exception as e:
            log.error("接口访问错误，Time out!", str(e))
            return None
