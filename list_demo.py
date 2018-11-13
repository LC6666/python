# -*- coding:utf-8 -*-

__author__ = "豆豆嗯嗯"

if __name__ =="__main__":
    list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    print("内置函数处理list示例： ")

    # 计算list_demo中元素个数
    print(len(list_demo))

    # 返回list_demo中最大值的元素
    print(max(list_demo))

    # 返回list_demo中最小值的元素
    print(min(list_demo))

    # 将list转换成元组
    tuple_demo = (1, 2, 3, 4, 5, 6)
    list1 = list(tuple_demo)

    # 打印转换后的列表
    print(list1)

    print("list方法代码示例：")
    list2 = [1,1,2,2,3,3,4,5,6]
    list3 = [7,8,9,0,10,11]

    # append，追加一个元素
    list2.append(17)
    print(list2)

    # count, 统计1出现的次数
    count = list2.count(1)
    print(count)

    # extend, 将list2追加到list1中
    list2.extend(list3)
    print(list2)

    # index, 返回第一个2的索引
    index = list2.index(2)
    print(index)

    # insert, 在列表第一个位置插入30
    list2.insert(0,30)
    print(list2)

    # pop, 删除最后一个元素
    list2.pop()
    print(list2)

    # reverse, 把列表反向一下
    list2.reverse()
    print(list2)

    # sort,对列表进行排序
    list2.sort()
    print(list2)

    # copy，列表拷贝
    list4 = list2.copy()
    print(list2)
    print(list4)

    # clear 清空列表
    list2.clear()
    print(list2)
    print(list4)

    print("列表切片操作示例：")

    data_demo = ["DeepTest","appium","testinguniom.com","hello","python3"]

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

    print("列表更新操作示例：")
    data_demo[3] = "hello,豆豆"
    print(data_demo)


    MyList = [1, 2, 4, 5]
    for i in MyList:
        if i % 2 == 0:
            print(i)
            MyList.remove(i)

    print(MyList)
