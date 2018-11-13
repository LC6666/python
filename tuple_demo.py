# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

if __name__ == "__main__":

    tuple_demo = (1,2,3,4,5,6,7,8,9,0)
    # 计算tuple_demo中元素个数
    print(len(tuple_demo))

    # 返回tuple_demo中最大值的元素
    print(max(tuple_demo))

    # 返回tuple_demo中最小值的元素
    print(min(tuple_demo))

    # 将list转换成元组
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple1 = tuple(list_demo)

    # 打印转换后的元组
    print(tuple1)

    print(u"元组切片操作示例!")

    data_demo = ("DeepTest", "appium", "testingunion.com", "hello", "python3")

    # 读取第二个元素appium, 注意索引下标从0开始
    e = data_demo[1]
    print(e)

    # 读取倒数第二个hello
    e = data_demo[-2]
    print(e)

    # 切片，截取从第2个元素开始后的所有元素
    e = data_demo[1:]
    print(e)

    # 切片，截取第2-4个元素
    e = data_demo[1:4]
    print(e)

    print("元组合并或连接操作示例!")
    tup1 = ("DeepTest", "appium")
    tup2 = ("testingunion.com", "hello", "python3")

    # 合并成新的元组
    tup3 = tup1 + tup2

    # 打印看看效果
    print(tup1)
    print(tup2)
    print(tup3)

    print("元组合并或连接操作示例!")
    tup4 = ("DeepTest", "appium")
    print(tup4)

    # 删除元组
    del tup4
   # print(tup4)


    print("元组运算示例")
    tup5 = ("DeepTest", "开源优测")
    tup6 = (1, 2, 3, 4)

    # 计算元组长度
    print(len(tup5))

    #  元组连接
    tup7 = tup5 + tup6
    print(tup7)

    # 元组复制
    tup8 = tup5 * 2
    print(tup8)

    # 判断元素是否在元组中, 是则返回True, 否则返回
    result = 5 in tup6
    print(result)

    # 遍历元组
    for t in tup6:
        print(t)


    # 将list转换成元组
    print(" 将list转换成元组")
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple9 = tuple(list_demo)

    # 打印转换后的元组
    print(tuple9)