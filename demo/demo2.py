#!/usr/bin/python3
import pymysql


def func1():
    print('=================')


# 打开数据库连接
db = pymysql.connect(host="", port=33307, user="",
                     password="", database="")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
print(cursor.fetchone())

db.close()
