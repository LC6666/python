# -*-coding:utf-8 -*-
__author__='豆豆嗯嗯'


# 求和函数
def sum(a, b):
    c = a + b
    return c

# 九九乘法表
def multi():
    data = []
    for i in range(1,10):
        line = []
        for j in range(i,10):
            line.append("%d * %d = %2d" %(i,j,i*j))
        data.append(line)
    return data

# 元组传递
def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum +s
    return sum

# 字符串连接函数
def str_join(str1, str2, str3):
    return str1 + str2 + str3

if __name__ == '__main__':
   print("函数定义，求和")
   c = sum(3,6)
   print(c)

   data = multi()
   for d in data:
        print(d)

   print("\n-----------------------------")
   print("元组传参，求和实例：")
   tuple_1 = (1, 9, 10, 2, 2, 39, 0, 11, 20)
   print(tuple_1)
   sum = sum_tuple(tuple_1)
   print(u"和为： %d" % sum)

   print("\n-----------------------------")
   print("字符串连接实例：")
   str1 = "明天，"
   str2 = "你好"
   str3 = "！"

   str_j = str_join(str1,str2,str3)
   print(str_j)

