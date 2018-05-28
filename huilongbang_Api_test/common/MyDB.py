# -*- coding: UTF-8 -*-
from huilongbang_Api_test import readConfig
from huilongbang_Api_test.common.Log import Log

Author = "Sky Huang"

import pymysql

localReadConfig = readConfig.ReadConfig()
log = Log()


class MyDB(object):
    global host, username, password, port, database
    host = localReadConfig.get_db("host")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = int(localReadConfig.get_db("port"))
    database = localReadConfig.get_db("database")

    # config = {"host": str(host), "username": username, "password": password, "port": int(port), "db": database}

    def __init__(self):
        # self.logger = log.logger
        # self.connection = None
        # self.cursor = None
        try:
            self.connection = pymysql.connect(host=host, port=port, user=username, password=password, db=database,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.connection.cursor()
            log.logger.info("Connect DB successfully!")
        except ConnectionError as ex:
            log.logger.error(str(ex))

    # def connectDB(self):
    #     try:
    #         self.connection = pymysql.connect(host=host, port=port, user=username, password=password, db=database,
    #                                           charset='utf8mb4',
    #                                           cursorclass=pymysql.cursors.DictCursor)
    #         self.cursor = self.connection.cursor()
    #         log.logger.info("Connect DB successfully!")
    #     except ConnectionError as ex:
    #         log.logger.error(str(ex))

    def executeSQL(self, sql, params):
        # self.connectDB()
        self.cursor.execute(sql, params)
        self.connection.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.connection.close()
        log.logger.info("Database closed!")


# db = MyDB()
# sql = "SELECT * from t_users WHERE loginphone=%s"
# cursor = db.executeSQL(sql=sql, params="15615615600")
# result = db.get_one(cursor=cursor)
# log.logger.info(result)
