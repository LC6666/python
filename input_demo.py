# -*- coding:utf-8 -*-

__author__='豆豆嗯嗯'
if __name__=="__main__":
    # 读取键盘任意输入
    data = input("请输入一串任意字符：")
    print("你输入了：%s"%data)
    # 读取键盘任意输入
    data2 = input("请输入一串任意的字符：")
    # 以空格切割输入的字符串
    list_data = data2.split(" ")
    # 打印列表数据
    print(list_data)