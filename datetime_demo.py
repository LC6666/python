# -*-coding:utf-8 -*-

__author__ = '豆豆嗯嗯'

from datetime import date
from datetime import time
from datetime import datetime

if __name__ =="__main__":
    today = date.today()
    print("今天是:%s" %today)
    print("今天是：%s %s %s" %(today.year,today.month,today.day))

    weekdays_num = today.weekday()
    print("今天是星期%s" % weekdays_num)

    # 输出可读性更好的星期几
    weekdays = ("星期一", "星期二", "星期三",
                "星期四", "星期五", "星期六", "星期天")
    print("今天是%s" % weekdays[weekdays_num])

    # 看看现在的时间
    today_now = datetime.now()
    print("现在是 %s" % today_now)

    # 用time来构造个时间出来
    t = time(hour=12, minute=20, second=30, microsecond=200)
    print("我们自己造的时间是 %s" % t)

    # 再造个日期时间出来试试
    d = datetime(year=2008, month=8, day=8, hour=8, minute=8, second=8)
    print("我们自己造是日期时间 %s" % d)

    print("\n----------------------------------------------------------")
    print("格式化日期时间：strftime函数")
    #        % y    两位数的年份表示（00 - 99）
    #        % Y    四位数的年份表示（000 - 9999）
    #        % m    月份（01 - 12）
    #        % d    月内中的一天（0 - 31）
    #        % H    24小时制小时数（0 - 23）
    #        % I    12    小时制小时数（01 - 12）
    #        % M    分钟数（00 = 59）
    #        % S    秒（00 - 59）
    #        % a    简写的星期名称
    #        % A    完整星期名称
    #        % b    简写的月份名称
    #        % B    完整的月份名称
    #        % c    相应的日期表示和时间表示
    #        % j    年内的一天（001 - 366）
    #        % p    A.M.或P.M.的等价符
    #        % U    一年中的星期数（00 - 53）星期天为星期的开始
    #        % w    星期（0 - 6），星期天为星期的开始
    #        % W    一年中的星期数（00 - 53）星期一为星期的开始
    #        % x    相应的日期表示
    #        % X    相应的时间表示
    #        % z    当前时区的名称
    #        % % % 号本身

    # time.strftime(format[, t])

    # 先看下当前默认格式化的时间
    import time
    localtime = time.asctime(time.localtime())
    print("当前默认日期时间格式: %s" % localtime)

    # 格式化为： 年-月-日 时:分:秒 星期几
    print("24小时制全格式：", time.strftime("%Y-%m-%d %H:%M:%S %A",
                                     time.localtime()))
    print("12小时制缩写格式：", time.strftime("%Y-%m-%d %I:%M:%S %a",
                                      time.localtime()))

    # 带a.m. 或 p.m. 标识时间格式  %p
    print("带a.m或p.m 24小时制全格式：",
          time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))

    # 把时区也带上看看 %z
    print("带时区的全格式：",
          time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))

    # 格式乱排下试试
    print("随意排格式：",
          time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))

