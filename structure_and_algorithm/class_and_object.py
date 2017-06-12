#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : class_and_object.py
# @Software: PyCharm

# 类与对象
# # 1.1 改变对象的字符串显示
# # 要改变一个实例的字符串表示，可重新定义它的str () 和repr () 方法
# class Pair:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return 'Pair({0.x!r},{0.y!r})'.format(self)
#
#     def __str__(self):
#         return '({0.x!s},{0.y!s})'.format(self)
# # repr () 方法返回一个实例的代码表示形式，通常用来重新构造这个实例。内
# # 置的repr() 函数返回这个字符串，跟我们使用交互式解释器显示的值是一样的。
# # str () 方法将实例转换为一个字符串，使用str() 或print() 函数会输出这个字符串
# p = Pair(3, 4)
# print(p)
# print('p is {0!r}'.format(p))
# print('p is {0}'.format(p))
# # 上面的format() 方法的使用看上去很有趣，格式化代码f0.xg 对应的是第1 个参
# # 数的x 属性,作为这种实现的一个替代，你也可以使用% 操作符
# def __repr__(self):
#     return 'Pair(%r,%r)'%(self.x, self.y)

# 1.2 自定义字符串的格式化
# 通过format() 函数和字符串方法使得一个对象能支持自定义的格式化，需要在类上面定义
# format () 方法
_formats = {
   'ymd': '{d.year}-{d.month}-{d.day}',
   'mdy': '{d.month}/{d.day}/{d.year}',
   'dmy': '{d.day}/{d.month}/{d.year}'
}
class Date:
    def __init__(self, year, month, day):