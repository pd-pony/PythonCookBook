#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : time_and_date.py
# @Software: PyCharm

# 数字日期和时间

# # 1.1 数字的四舍五入
# # 简单的舍入运算，使用内置的round(value, ndigits) 函数即可
# print(round(1.23, 1))
# print(round(1.27, 1))
# print(round(1.25361, 3))
# print(round(1.25, 1))
# # 格式化数据
# x = 1.23456
# # 保留两位小数
# print(format(x, '0.2f'))
# # 保留三位小数
# print(format(x, '0.3f'))
# print('value is {:0.3f}'.format(x))

# # 1.2 执行精确的浮点数运算
# a = 2.1
# b = 4.2
# print((a + b) == 6.3)  # false
# # 如果你想更加精确(并能容忍一定的性能损耗)，你可以使用decimal 模块
# from decimal import Decimal
# a = Decimal('4.2')
# b = Decimal('2.1')
# print(a + b)
# print((a + b) == Decimal('6.3'))

# # 1.3 数字的格式化输出
# # 格式化输出单个数字的时候，可以使用内置的format()函数
# x = 1234.56789
# # 保留两位小数
# print(format(x, '0.2f'))
# # 保留10个字节数，右对齐，保留一位小数
# print(format(x, '>10.1f'))
# # 保留10个字节数，左对齐，保留一位小数
# print(format(x, '<10.1f'))
# # 保留10个字节数，居中，保留一位小数
# print(format(x, '^10.1f'))
# # 加上千字分隔符
# print(format(x, ','))
# # 科学计数法
# print(format(x, 'e'))
# # 科学计数法，保留2为小数
# print(format(x, '0.2E'))
# print('The value is {:0,.2f}'.format(x))

# # 二八十六进制整数
# # 为了将整数转换为二进制、八进制或十六进制的文本串，可以分别使用bin() ,oct() 或hex() 函数
# x = 1234
# # 二进制
# print(bin(x))
# # 八进制
# print(oct(x))
# # 十六进制
# print(hex(x))
# # 不想输出0b , 0o 或者0x 的前缀的话，可以使用format() 函数。
# # 二进制
# print(format(x, 'b'))
# # 八进制
# print(format(x, 'o'))
# # 十六进制
# print(format(x, 'x'))

# # 1.5 复数的数学运算
# # 复数可以用使用函数complex(real, imag) 或者是带有后缀j 的浮点数来指定。
# a = complex(2, 4)
# print(a)
# b = 3 -5j
# print(b)
# print(a + b)
# # 获取实部
# print(a.real)
# # 获取虚部
# print(b.imag)
# # 获取共轭
# print(a.conjugate())
# # 要执行其他的复数函数比如正弦、余弦或平方根，使用cmath 模块
# import cmath
# # 正弦
# print(cmath.sin(a))
# # 余弦
# print(cmath.cos(a))
# # 平方根
# print(cmath.exp(a))

# # 1.6 无穷大与NaN
# # 创建或测试正无穷、负无穷或NaN(非数字) 的浮点数。
# # Python 并没有特殊的语法来表示这些特殊的浮点值，但是可以使用float() 来创建它们
# a = float('inf')
# b = float('-inf')
# c = float('nan')
# print(a, b, c)
# # 为了测试这些值的存在，使用math.isinf() 和math.isnan() 函数
# import math
# print(math.isinf(a))
# print(math.isnan(c))

# # 1.7 分数运算
# # fractions 模块可以被用来执行包含分数的数学运算
# from fractions import Fraction
# a = Fraction(5, 4)
# b = Fraction(7, 16)
# print(a, b)
# # 分子
# print(a.numerator)
# # 分母
# print(a.denominator)
# # 转换成浮点小数
# print(float(a))
# x = 3.75
# # 将小数转换成分数
# y = Fraction(*x.as_integer_ratio())
# print(y)

# # 1.8 矩阵与线性代数运算
# # 执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组
# import numpy as np
# m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
# print(m)
# # 矩阵转置
# print(m.T)
# # 逆矩阵
# print(m.I)
# # 矩阵乘法
# v = np.matrix([[2], [3], [4]])
# print(m*v)

# # 1.9 随机选择
# # 从一个序列中随机抽取若干元素，或者想生成几个随机数。
# # random 模块有大量的函数用来产生随机数和随机选择元素。比如，要想从一个序
# # 列中随机的抽取一个元素，可以使用random.choice()
# import random
# values = [1, 2, 3, 4, 5, 6]
# print(random.choice(values))
# print(random.choice(values))
# print(random.choice(values))
# # 为了提取出N 个不同元素的样本用来做进一步的操作，可以使用random.sample()
# print(random.sample(values, 2))
# print(random.sample(values, 2))
# print(random.sample(values, 2))
# print(random.sample(values, 3))
# # 如果你仅仅只是想打乱序列中元素的顺序，可以使用random.shuffle()
# print(values)
# random.shuffle(values)
# print(values)
# # 生成随机整数，请使用random.randint()
# print(random.randint(0, 10))
# print(random.randint(0, 10))
# print(random.randint(0, 10))
# # 为了生成0 到1 范围内均匀分布的浮点数，使用random.random()
# print(random.random())
# print(random.random())
# print(random.random())
# # 如果要获取N 位随机位(二进制) 的整数，使用random.getrandbits()
# print(random.getrandbits(200))

# # 1.10 基本的日期与时间转换
# # 执行简单的时间转换，比如天到秒，小时到分钟等的转换
# # 为了执行不同时间单位的转换和计算，请使用datetime 模块
# from datetime import timedelta
# a = timedelta(days=2, hours=6)
# b = timedelta(hours=4.5)
# c = a + b
# print(c)
# print(c.days)
# print(c.seconds)
# print(c.total_seconds())
# # 如果你想表示指定的日期和时间，先创建一个datetime 实例然后使用标准的数学运算来操作它们f
# from datetime import datetime
# a = datetime(2012, 9,23)
# print(a)
# print(a + timedelta(days=10))
# # 获取当前日期及时间
# now = datetime.today()
# print(now)
# print(now + timedelta(minutes=10))

# # 1.11 计算最后一个周五的日期
# # 查找星期中某一天最后出现的日期，比如星期五
# # Python 的datetime 模块中有工具函数和类可以帮助你执行这样的计算
# from datetime import datetime, timedelta
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# def get_previous_byday(dayname, start_date = None):
#     if start_date is None:
#         start_date = datetime.today()
#     day_num = start_date.weekday()
#     day_num_target = weekdays.index(dayname)
#     days_ago = (7 + day_num - day_num_target)%7
#     if days_ago == 0:
#         days_ago = 7
#     target_date = start_date - timedelta(days=days_ago)
#     return target_date
# # 获取当前时间日期
# print(datetime.today())
# # 获取当前日期之前的周一日期
# print(get_previous_byday('Monday'))
# # 获取当前日期之前的周二日期
# print(get_previous_byday('Tuesday'))
# # 获取指定日期之前的周日
# print(get_previous_byday('Sunday', datetime(2012, 12, 21)))


# # 1.12 计算当前月份的日期范围
# # 代码需要在当前月份中循环每一天，想找到一个计算这个日期范围的高效方法。
# # 在这样的日期上循环并需要事先构造一个包含所有日期的列表。你可以先计算出开
# # 始日期和结束日期，然后在你步进的时候使用datetime.timedelta 对象递增这个日
# # 期变量即可
# from datetime import datetime, date, timedelta
# import calendar
#
# def get_month_range(start_date = None):
#     if start_date is None:
#         start_date = date.today().replace(day=1)
#     _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
#     end_date = start_date + timedelta(days=days_in_month)
#     return (start_date, end_date)
#
# a_day = timedelta(days=1)
# first_day, last_day = get_month_range()
# while first_day < last_day:
#     print(first_day)
#     first_day += a_day
# #
# # 上面的代码先计算出一个对应月份第一天的日期。一个快速的方法就是使用date
# # 或datetime 对象的replace() 方法简单的将days 属性设置成1 即可。replace()
# # 方法一个好处就是它会创建和你开始传入对象类型相同的对象。所以，如果输入参数
# # 是一个date 实例，那么结果也是一个date 实例。同样的，如果输入是一个datetime
# # 实例，那么你得到的就是一个datetime 实例。
# # 然后，使用calendar.monthrange() 函数来找出该月的总天数。任何时候只要你
# # 想获得日历信息，那么calendar 模块就非常有用了。monthrange() 函数会返回包含
# # 星期和该月天数的元组。

# 1.13 字符串转换成日期
# 使用Python 的标准模块datetime 可以很容易的解决这个问题
from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)
z = datetime.now()
diff = z - y;
print(diff)

# 1.14 结合时区的日期操作
