# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import pymysql
import random

if __name__=="__main__":
    print("PyMysql基本示例")

    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        db="zhys_yd_new",
        charset="utf8"
    )

    try:

        cursor = conn.cursor()
        sql = "insert into t values(%s, %s, %s)"

        '''
        sql_data = []
        for index in range(0, 10):
            email = "%.10f@126.com" % random.random()
            password = random.random()
            sql_data.append((email, password)) 
        '''

        sql_data = [(0,'肢体、关节疼痛', '胃炎')]
        #print(type(sql_data))
        cursor.executemany(sql, sql_data)
        conn.commit()

        sql2 = "select * from pageinfo limit 5"
        cursor.execute(sql2)

        all_data = cursor.fetchall()
        print("取所有查询到的数据")
        for data in all_data:
            print(data[1],data[2],data[3])

        one_data = cursor.fetchone()
        print("取1条数据")
        print(data[1],data[2],data[3])

    finally:
        conn.close()

