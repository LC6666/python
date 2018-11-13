# -*- coding:utf-8 -*-
__author__ = '豆豆嗯嗯'

if __name__ =='__main__':
    tuple_1 = (1,2,3,4,5,6,7,8,9,0)
    print("遍历元组，并打印出来：")
    for t in tuple_1:
        print(t)

     #  for列表遍历
    list_1 = ['DeepTest', '深度测试', '快学Python3']
    print("遍历列表，并打印出来： ")
    for text in list_1:
        print(text)
    print("\n-----------------------------")
    #  for字典遍历
    dict_1 = {"开源优测": "DeepTest", u"python": "快学Python3"}
    print("\n-----------------------------")
    print("遍历字典方式一，并打印出来： ")
    for (key, value) in dict_1.items():
        print("%s : %s " % (key, value))

    print("\n-----------------------------")

    print("遍历字典方式二，并打印出来： ")
    for key in dict_1:
        print("%s : %s " % (key, dict_1[key]))

    print("\n-----------------------------")
    print("range for循环实例")
    # 使用默认参数生成序列进行遍历
    for i in range(5):
        print(i, end=',')

        # 换行
    print('')

    # 指定范围生成序列进行遍历
    print("指定范围生成序列进行遍历")
    for i in range(0, 10):
        print(i, end=',')

        # 换行
    print('')

    # 带步长方式生成序列进行遍历
    print("带步长方式生成序列进行遍历")
    for i in range(0, 10, 2):
        print(i, end=',')

    print("\n-----------------------------")
    print("嵌套循环")
    print("九九乘法表：")
    for i in range(1, 10):
        for j in range(i, 10):
            print("%d * %d = %2d" % (i, j, i * j), end="  ")

        print("")

    print("\n-----------------------------")
    print("while循环")
    print("计算0-100间所有偶数和")

    n = 100
    index = 0
    sum = 0
    while index <= n:
        sum = sum + index
        index = index + 2

    print("0-100间偶数和= %d " % sum)
    print("\n-----------------------------")

    print("while和for综合使用：")
    print("九九乘法表实例：")
    n = 1

    while n <= 9:
        for m in range(n, 10):
            print(u"%d * %d = %2d" % (n, m, n * m), end="  ")

        print("")
        n = n + 1

