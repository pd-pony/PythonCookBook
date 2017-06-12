#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : iter_and_generate.py
# @Software: PyCharm

# 迭代器与生成器

# 1.1 手动遍历迭代器
# 使用next() 函数并在代码中捕获StopIteration 异常
items = [1, 2, 3, 4]
# 获取迭代
it = iter(items)
print(next(it)) #1
print(next(it)) # 2
print(next(it)) # 3
print(next(it)) # 4

# 1.2 代理迭代
# 问题：你构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。你想直
# 接在你的这个新容器对象上执行迭代操作。
# 解决：定义一个iter () 方法，将迭代操作代理到容器内部的对象上去。
class Node:
    def __init__(self, value):
        self.value = value
        self._children = []

    def __repr__(self):
        return 'Node{!r}'.format(self.value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# 使用实例
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # 迭代遍历
    for ch in root:
        print(ch)

# 1.3 使用生成器创建新的迭代模式
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
for n in frange(0, 4, 0.5):
    print(n)
print(list(frange(0, 4, 0.5)))
# 生成器智能用于迭代操作，一个生成器函数主要特征是它只会回应在迭代中使用到的next 操作。一旦生成器
# 函数返回退出，迭代终止。
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = countdown(3)
print(c)
print(next(c)) # 3
print(next(c)) # 2
print(next(c)) # 1
print(next(c)) # Done

# 1.4 实现迭代器协议
# 在一个对象上实现迭代最简单的方式是使用一个生成器函数
class Node:
    def __init__(self, value):
        self.value = value
        self._children = []

    def __repr__(self):
        return 'Node{!r}'.format(self.value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

# 实例
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)

# 1.4 反向迭代
# 使用内置的reversed()函数
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)
# 反向迭代仅仅当对象的大小可预先确定或者对象实现了reversed () 的特殊方
# 法时才能生效。如果两者都不符合，那你必须先将对象转换为一个列表才行
f = open('someFile')
for line in reversed(list(f)):
    print(line, end='')
在自定义类上实现__reversed__()方法来实现反向迭代
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1
for rr in Countdown(30):
    print(rr)

# 1.5 迭代器切片
# 函数itertools.islice() 正好适用于在迭代器和生成器上做切片操作
def count(n):
    while True:
        yield n # 生成器
        n += 1
c = count(0)

import itertools
for x in itertools.islice(c, 10, 20):
    print(x, end=' ')
# 迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并
# 且也没有实现索引)。函数islice() 返回一个可以生成指定元素的迭代器，它通过遍
# 历并丢弃直到切片开始索引位置的所有元素。然后才开始一个个的返回元素，并直到
# 切片结束索引位置。
# 这里要着重强调的一点是islice() 会消耗掉传入的迭代器中的数据。必须考虑到
# 迭代器是不可逆的这个事实。所以如果你需要之后再次访问这个迭代器的话，那你就
# 得先将它里面的数据放入一个列表中。

# 1.6 排列组合的迭代
# 迭代遍历一个集合中元素的所有可能的排列或组合
# itertools 模块提供了三个函数来解决这类问题。其中一个是
# itertools.permutations() ， 它接受一个集合并产生一个元组序列， 每个元组
# 由集合中所有元素的一个可能排列组成
items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)
# 如果你想得到指定长度的所有排列，你可以传递一个可选的长度参数
for p in permutations(items, 2):
    print(p)
# 使用itertools.combinations() 可得到输入集合中元素的所有的组合
from itertools import combinations
for c in combinations(items, 3):
    print(c)
for c in combinations(items, 2):
    print(c)
for c in combinations(items, 1):
    print(c)
# 在计算组合的时候， 一旦元素被选取就会从候选中剔除掉(比如
# 如果元素’a’ 已经被选取了， 那么接下来就不会再考虑它了)。而函数
# itertools.combinations with replacement() 允许同一个元素被选择多次
for c in combinations_with_replacement(items, 3): # 命令有问题
    print(c)

# 1.7 序列上索引值迭代
# 问题：想在迭代一个序列的同时跟踪正在被处理的元素索引
# 解决：内置的enumerate() 函数可以很好的解决这个问题
my_list = ['a', 'b', 'c', 'd']
for idx, val in enumerate(my_list):
    print(idx, val, end=' ') # 0 a 1 b 2 c 3 d
# 为了按传统行号输出(行号从1 开始)，你可以传递一个开始参数
for idx, val in enumerate(my_list, 1):
    print(idx, val, end=' ') # 1 a 2 b 3 c 4 d

# 1.8 同时迭代多个序列
# 同时迭代多个序列，每次分别从一个序列中取一个元素
# 解决：同时迭代多个序列，使用zip() 函数
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99, 100, 123]
for x, y in zip(xpts, ypts):
    print(x, y)
# 迭代长度与参数中最短序列长度一致
# 如果这个不是你想要的效果，那么还可以使用itertools.zip longest() 函数来代替
from  itertools import zip_longest
for i in zip_longest(xpts, ypts):
    print(i, end=' ')
# 成对处理数据的时候zip() 函数是很有用的
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
# 使用zip() 可以让你将它们打包并生成一个字典
s = dict(zip(headers,values))
print(s)
# 成对输出
for name, val in zip(headers, values):
    print(name, '=', val)
# 多组数同时输出
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x','y','z']
for i in zip(a, b, c):
    print(i)
# zip() 会创建一个迭代器来作为结果返回。如果你需要将结对的值存储在列表中，要使用list() 函数

# 1.9 不同集合上元素的迭代
# 你想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不
# 失可读性的情况下避免写重复的循环。
# itertools.chain() 方法可以用来简化这个任务
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

# 1.10 展开嵌套的序列
from collections import Iterable
def flatten(items, ingore_types = (str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ingore_types):
            yield from flatten(x)
        else:
            yield x
items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x, end=' ') # 1 2 3 4 5 6 7 8
# 在上面代码中， isinstance(x, Iterable) 检查某个元素是否是可迭代的。如果是的话
# ， yield from 就会返回所有子例程的值
# 额外的参数ignore types 和检测语句isinstance(x, ignore types) 用来将字符
# 串和字节排除在可迭代对象外，防止将它们再展开成单个的字符
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)

# # 1.11 顺序迭代合并后的排序迭代对象
# # 问题：你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历。
# # 解决：heapq.merge() 函数可以帮你解决这个问题
# import heapq
# a = [1, 4, 7, 10]
# b = [2, 5, 10, 13]
# for c in heapq.merge(a, b):
#     print(c)


