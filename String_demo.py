# -*- coding:utf-8 -*-

__author__ = '豆豆嗯嗯'

if __name__ == "__main__":
    t = ('1', '2', '3', '4', '5', 'a', 'b', "efg")

    # 用 - 将t中元素合并成一个新的字符串
    str_demo1 = '-'.join(t)
    print(str_demo1)

    # 将str_demo以-进行切割
    str_set = str_demo1.split('-')
    print(str_set)

    # 将t中元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)

    source_str = "it's my book, please show it, wa ka ka, yo yo yo!"

    # 从左往右查找yo
    print("从左往右查找 yo")
    print(source_str.find("yo"))
    print(source_str.index("yo"))

    # 从右往左查找yo
    print("从右往左查找 yo")
    print(source_str.rfind("yo"))
    print(source_str.rindex("yo"))

    # 替换所有的 yo
    des_str = source_str.replace("yo", "ha")
    print(des_str)

    # 替换两次 yo
    des_str = source_str.replace("yo", "ha", 2)
    print(des_str)

    # 去字符串空格示例
    demo_str3 = "  我的前  后 和 中 间  都有空格  "
    print(demo_str3)

    # 去除前面的空格
    lstr = demo_str3.lstrip()
    print(lstr)

    # 去除后面的空格
    rstr = demo_str3.rstrip()
    print(rstr)

    # 去除前后的空格
    str = demo_str3.strip()
    print(str)