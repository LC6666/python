# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

if __name__ == "__main__":

    # 字典基本示例
    dict_demo = {"DeepTest":"深度测试","Study":"快学Python3"}
    # 计算字典的长度
    print(len(dict_demo))

    # 以字符方式输出字典,即将字典转换成字符串
    str_d = str(dict_demo)
    print(str_d)
    print(dict_demo)
    # 判断类型
    print(type(dict_demo))
    print(type(str_d))

    print("字典方法应用示例")
    #dict_demo = {"DeepTest:深度测试", "Study:快学Python3"}
    list1 = [1,2,3,4]

    # copy复制字典
    dict_cp = dict_demo.copy()
    print(dict_demo)
    print(dict_cp)

    # fromkeys创建字典
    #以序列作为kye创建一个新字典，value为所有键对应的初始值
    dict_new = dict.fromkeys(list1,"value")
    print(dict_new)

    # get获取指定key的value
    #返回指定key的value，如果key不存在，则返回默认值
    value1 = dict_demo.get("DeepTest","我是默认值")
    value2 = dict_demo.get("Python3","我是默认值")
    print(value1)
    print(value2)

    # in, 判断key是否存在
    keyb = "DeepTest"
    result1 = keyb in dict_demo
    result2 = keyb in dict_new
    print(result1)
    print(result2)

    # items, 以元组形式返回字典所有的(key, value)
    items = dict_demo.items()
    print(items)

    # keys 以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)

    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    set_result1 = dict_demo.setdefault("DeepTest", "设置值")
    set_result2 = dict_demo.setdefault("我是key", "我是value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)

    # update, 更新字典
    dict_demo.update(dict_new)
    print(dict_demo)

    # values,返回字典中所有的value
    values = dict_demo.values()
    print(values)

    print("字典遍历、修改、删除示例")
    # 遍历 方法1
    for (key, value) in dict_demo.items():
        print("%s : %s" % (key, value))

        # 遍历 方法2
    for key in dict_demo.keys():
        print("%s : %s" % (key, dict_demo[key]))

        # 修改
    dict_demo["Study"] = "修改后的值"
    print(dict_demo)

    # 删除指定元素
    del dict_demo["Study"]
    print(dict_demo)

    # 清空字典
    dict_demo.clear()
    print(dict_demo)