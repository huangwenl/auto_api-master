#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
from log.log_level import LogLevel
import os
import logging.handlers
from colorama import Fore, Style
from huilongbang_Api_test import readConfig
from datetime import datetime

class ColorLogger(object):
    logger = logging.getLogger('sg_color_logger')
    # logger.setLevel(logging.info)
    # logger_handler = logging.StreamHandler(sys.stdout)
    # logger_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    # logger.addHandler(logger_handler)

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
    # self.logger = logging.getLogger()
    # 定义日志级别
    logger.setLevel(logging.INFO)
    # defined handler
    logger_handler = logging.FileHandler(os.path.join(logPath, str(datetime.now().strftime("%Y%m%d"))+".log"))
    # defined formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # defined formatter
    logger_handler.setFormatter(formatter)
    # add handler
    logger.addHandler(logger_handler)

    @classmethod
    def debug(cls, msg):
        cls.logger.debug("DEBUG " + str(msg))

    @classmethod
    def info(cls, msg):
        cls.logger.info("INFO " + str(msg))

    @classmethod
    def error(cls, msg):
        cls.logger.error(Fore.RED + "ERROR " + str(msg) + Style.RESET_ALL)

    @classmethod
    def warn(cls, msg):
        cls.logger.warning(Fore.YELLOW + "WARNING " + str(msg) + Style.RESET_ALL)

    @classmethod
    def set_level(cls, level):
        if level not in LogLevel.__dict__.values():
            raise Exception("使用了不存在的日志级别")
        cls.logger.setLevel(level)

# c=ColorLogger()
# c.warn("lalla")