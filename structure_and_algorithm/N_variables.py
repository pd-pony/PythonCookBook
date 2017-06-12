#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Peidong
# @Site    : 
# @File    : N_variables.py
# @Software: PyCharm

# 解压序列赋值给多个变量

# 1.1 问题：现在有一个包含N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N 个变量？
# 解答：任何的序列(或者是可迭代对象) 可以通过一个简单的赋值语句解压并赋值给多个变量。唯一的前提就是变量的数量必须跟序列元素的
# 数量是一样的。
p = (4,5)
x,y = p
print(x,y)
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)
name, shares, price, (year, mon, day) = data
print(name, shares, price, (year, mon, day))

# 这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。
# 包括字符串，文件对象，迭代器和生成器。
s = 'Hello'
a, b, c, d, e = s
print(a)

# 部分解析
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ =data
print(shares)

# 1.2 问题：如果一个可迭代对象的元素个数超过变量个数时，会抛出一个ValueError 。那么
# 怎样才能从这个可迭代对象中解压出N 个元素出来？
# 解决：Python 的星号表达式可以用来解决这个问题

# eg:统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)

# 星号表达式也能用在列表的开始部分
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing,   current)

# 星号表达式在迭代元素为可变长元组的序列
records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# 1.3 问题： 保留最后N个元素
# 解决： 使用collections.deque
# 使用deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并
# 且这个队列已满的时候，最老的元素会自动被移除掉
from collections import deque
q = deque(maxlen= 3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
q.append(5)
print(q)

# deque 类可以被用在任何你只需要一个简单队列数据结构的场合。如
# 果你不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的两端执
# 行添加和弹出元素的操作

p = deque()
p.append(1)
p.append(2)
p.append(3)
print(p)
# 在队列左边添加元素
p.appendleft(4)
print(p)
# 弹出左边元素
print(p.popleft())
print(p)

# 1.4 查找最大或最小的N个元素
# 问题: 怎么从一个集合中获得最大或最小的N个元素列表
# 解决：heapq 模块有两个函数：nlargest() 和nsmallest() 可以完美解决这个问
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # 最大的三个
print(heapq.nsmallest(3, nums)) # 最小的三个
# 更复杂的数据结构
portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# price为关键字查找
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)

# 堆数据结构最重要的特征是heap[0] 永远是最小的元素。并且剩余的元素可以很
# 容易的通过调用heapq.heappop() 方法得到，该方法会先将第一个元素弹出来，然后
# 用下一个最小的元素来取代被弹出元素(这种操作时间复杂度仅仅是O(log N)，N 是
# 堆大小)

# 当要查找的元素个数相对比较小的时候，函数nlargest() 和nsmallest() 是很
# 合适的。如果你仅仅想查找唯一的最小或最大(N=1) 的元素的话，那么使用min() 和
# max() 函数会更快些。类似的，如果N 的大小和集合大小接近的时候，通常先排序这
# 个集合然后再使用切片操作会更快点( sorted(items)[:N] 或者是sorted(items)[-
# N:] )。需要在正确场合使用函数nlargest() 和nsmallest() 才能发挥它们的优势(如果
# N 快接近集合大小了，那么使用排序操作会更好些)。

# 1.5 字典中的键映射多个值
# 问题：怎样实现一个键对应多个值的字典(也叫multidict )？
# 解决：一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你
# 就需要将这多个值放到另外的容器中，比如列表或者集合里面
d = { 'a': [1, 2, 3], 'b': [2, 3, 4, 5] }
print(d)
# 解决2：使用collections 模块中的defaultdict 来构造这样的字典
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(d)

# 1.6 字典排序
# 问题：创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
# 解决：为了能控制一个字典中元素的顺序， 可以使用collections 模块中的
# OrderedDict 类。在迭代操作的时候它会保持元素被插入时的顺序
from collections import OrderedDict
def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])
ordered_dict()

# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元
# 素插入进来的时候，它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会
# 改变键的顺序。


# 1.7 字典的运算
# 问题：怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)？
# 解决：通常需要使用zip() 函数先将键和值反转过来
prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
# 可以使用zip() 和sorted() 函数来排列字典数据
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
#执行这些计算的时候，需要注意的是zip() 函数创建的是一个只能访问一次的迭代器

# 1.8 序列中出现次数最多的元素
# 问题：怎样找出一个序列中出现次数最多的元素？
# 解决：collections.Counter 类就是专门为这类问题而设计的，它甚至有一个有用的
# most common() 方法直接给了答案
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的3 个单词
top_three = word_counts.most_common(3)
print(top_three)
# 作为输入， Counter 对象可以接受任意的hashable 序列对象。在底层实现上，一
# 个Counter 对象就是一个字典，将元素映射到它出现的次数上。

# 1.9 通过某个关键字排序一个字典列表
# 根据某个或某几个字典字段来排序这个列表
# 使用operator 模块的itemgetter 函数，可以非常容易的排序这样的数据结构。
rows = [
   {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
   {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
   {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
   {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
# 根据名称排序
rows_by_fname = sorted(rows, key=itemgetter('fname'))
# 根据id排序
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
# 根据多个关键字排序
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

# 1.10 通过某个字段将记录分组
# 问题: 某个特定的字段比如date 来分组迭代访问
# 解决：itertools.groupby() 函数对于这样的数据分组操作非常实用
rows = [
   {'address': '5412 N CLARK', 'date': '07/01/2012'},
   {'address': '5148 N CLARK', 'date': '07/04/2012'},
   {'address': '5800 E 58TH', 'date': '07/02/2012'},
   {'address': '2122 N CLARK', 'date': '07/03/2012'},
   {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
   {'address': '1060 W ADDISON', 'date': '07/02/2012'},
   {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
   {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter
from itertools import groupby
# 先按日期进行排序
rows.sort(key=itemgetter('date'))
# Iterate in groups 然后根据日期分组
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
# groupby() 函数扫描整个序列并且查找连续相同值(或者根据指定key 函数返回值
# 相同) 的元素序列。在每次迭代的时候，它会返回一个值和一个迭代器对象，这个迭代
# 器对象可以生成元素值全部等于上面那个值的组中所有对象。
# 一个非常重要的准备步骤是要根据指定的字段将数据排序。因为groupby() 仅仅
# 检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。

# 1.11 从字典中提取子集
prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)