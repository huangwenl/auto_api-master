# -*- coding: UTF-8 -*-
__Author__ = "Sky Huang"

import pymysql

connection = pymysql.connect(host='127.0.0.1',user='root',password='',db='test',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

