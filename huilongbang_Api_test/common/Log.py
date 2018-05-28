# -*- coding: UTF-8 -*-
import os

from huilongbang_Api_test import readConfig

import logging

from datetime import datetime

Author = "Sky Huang"


class Log(object):

    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        # 如果不存在文件夹创建文件夹
        if not os.path.exists(resultPath):
            os.makedirs(resultPath)
        # 以时间格式命名运行结果文件名
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d")))
        # 创建保持日志文件夹
        if not os.path.exists(logPath):
            os.makedirs(logPath)

        # 定义日志
        self.logger = logging.getLogger()
        # 定义日志级别
        self.logger.setLevel(logging.INFO)
        # defined handler
        handler = logging.FileHandler(os.path.join(logPath, str(datetime.now().strftime("%Y%m%d"))+".log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        handler.setFormatter(formatter)
        # add handler
        self.logger.addHandler(handler)

