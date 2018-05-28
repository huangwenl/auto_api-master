# -*- coding: UTF-8 -*-

import configparser
import os
import codecs

proDir = os.path.split(os.path.realpath(__file__))[0]
# D:\PyCharm_WorkSpace\auto_api-master\huilongbang_Api_test
configPath = os.path.join(proDir, "config.ini")


class ReadConfig(object):
    def __init__(self):
        fd = open(configPath)
        self.data = fd.read()
        #  remove BOM
        if self.data[:3] == codecs.BOM_UTF8:
            data = self.data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_http(self, name):
        value = self.cf.get("APPSERVER", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

# conf = ReadConfig()
# http_value = conf.get_http("baseurl")
# print(http_value)
