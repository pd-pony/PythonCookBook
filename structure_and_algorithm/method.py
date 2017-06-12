#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : method.py
# @Software: PyCharm

# 函数
# # 1.1 可接受任意数量参数的函数
# # 为了能让一个函数接受任意数量的位置参数，可以使用一个* 参数
# def avg(first, *rest):
#     return (first + sum(rest))/(1 + len(rest))
#
# print(avg(1, 2))  # 1.5
# print(avg(1, 2, 3, 4)) # 2.5
#
# # 为了接受任意数量的关键字参数，使用一个以** 开头的参数
# import html
# def make_element(name, value, **attrs):
#     keyvals = [' %s="%s"' % item for item in attrs.items()]
#     attr_str = ''.join(keyvals)
#     element = '<{name}{attrs}>{value}</{name}>'.format(
#         name=name,
#         attrs=attr_str,
#         value=html.escape(value))
#     return element
# # 实例
# print(make_element('item', 'Albatross', size='large', quantity=6))
# print(make_element('p', '<spam>'))
# # 一个* 参数只能出现在函数定义中最后一个位置参数后面，而**参数只能出现在
# # 最后一个参数。有一点要注意的是，在* 参数后面仍然可以定义其他参数。

# # 1.2 定义匿名或内联函数
# # 使用lambda 表达式
# add = lambda x, y : x+y
# print(add(2, 3))
# print(add('hello', 'python'))
# # lambda 表达式典型的使用场景是排序或数据reduce 等：
# names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
# print(sorted(names, key=lambda name: name.split()[-1].lower()))

# # 1.3 匿名函数捕获变量值
# x = 10
# a = lambda y : x+y
# x = 20
# b = lambda y : x+y
# print(a(10)) # 30
# print(b(10)) # 30
# #  lambda 表达式中的x 是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的
# # 如果你想让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数
# # 即可，就像下面这样：
# x = 10
# a = lambda y, x=x: x + y
# x = 20
# b = lambda y, x=x: x+y
# print(a(10))
# print(a(20))
# # 迭代注意
# funcs = [lambda x, n=n: x+n for n in range(5)]
# for f in funcs:
#     print(f(0))

