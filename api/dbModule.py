# coding: utf-8
import MySQLdb


def db_connect():
    return MySQLdb.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           db='first_schema',
                           passwd='seok0604',
                           charset='utf8')
